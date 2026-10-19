# Evaluación controlada con casos sintéticos etiquetados (2026-10-19)

Rama `analysis/metricas-clasificacion`, base `a2a6f41`. Resumen para LaTeX (con HOLDOUT del 08/10): `evaluacion_controlada_latex_20261019.md`.

## 1. Objetivo y restricciones

Medir la capacidad de detección de IsolationForest y del LSTM autoencoder con casos sintéticos de etiqueta conocida, calculando matriz de confusión y métricas de clasificación. Los sintéticos **solo se usan para evaluar**: no entran al entrenamiento ni al reentrenamiento, y no se modificó ningún artefacto ni la lógica de producción.

## 2. Auditoría: qué había ya

`scripts/benchmark/` ya tenía el grueso de la metodología (escenarios S1 swap de cuenta, S2 exfiltración, S3 fuera de horario; DEV/HOLDOUT; puntuado offline con artefactos de solo lectura; ROC-AUC, PR-AUC, recall y FPR con IC bootstrap). Se extendió ese benchmark en vez de crear un pipeline paralelo.

Brechas encontradas:

| Faltaba | Estado tras este trabajo |
|---|---|
| Matriz de confusión y precision/F1/especificidad/accuracy por modelo | Agregado (`clasificacion.py`) |
| Reportes separados por modelo | Agregado (3 reportes) |
| Verificación de hash de artefactos | Agregado (`integridad_artefactos.py`) |
| Secuencia inusual, volumen en ventana corta, controles negativos | Agregado (S4 a S7) |
| IP o ubicación inusual | Solo país (`RU`, ya en `*_con_pais`); los datos no traen IP |
| Recurso/archivo inusual | **No representable**: los modelos solo leen `time`, `type` y `countryCode`; se cubre únicamente con tipos `file_*` (S2_archivos) |

Cómo deciden los modelos (leído del código):

- **ISO**: agregado diario de 8 features, `StandardScaler`, `predict == -1` (contamination 0,02).
- **LSTM**: chunks de 50 eventos, MSE de reconstrucción, riesgo de usuario = percentil de la media acumulada; anomalía si `risk > 95`. `lstm_threshold.pkl` se carga pero no decide.
- **Híbrido**: `w_iso = 0,5`, decay (`vida_media_dias = 3`), `regla_piso`, alerta = nivel ≥ alto.
- **LSTM por chunk** no tiene umbral de producción.

## 3. Lo realizado

Archivos nuevos:

- `scripts/benchmark/generar_controlados.py`: escenarios S4 a S7, determinista. Cada mundo usa `Random(f"{seed}|{victima}|{ventana}|{escenario}")`. Reutiliza las ventanas DEV del run `ampliado` sin modificar `generar_escenarios.py` (agregarle variantes habría cambiado el consumo de su RNG y los sha256 del HOLDOUT registrado). Escribe solo en `data/benchmark/controlado/`.
- `scripts/benchmark/clasificacion.py`: matriz de confusión, precision, recall, F1, especificidad, accuracy, balanced accuracy, ROC-AUC y PR-AUC, por modelo, escenario y subconjunto, con IC 95% por bootstrap sobre víctimas. Genera `reporte_iso.md`, `reporte_lstm.md`, `reporte_hibrido.md`, `predicciones_<modelo>.csv` (etiqueta, score, umbral, predicción y TP/FP/TN/FN por fila) y `confusion_vigente.csv`.
- `scripts/benchmark/integridad_artefactos.py`: SHA-256 de los 9 artefactos antes y después del puntuado; falla si alguno cambia.
- `api/tests/test_clasificacion_benchmark.py`: 18 pruebas (métricas contra cálculo manual, denominador cero → NaN, empates, bootstrap reproducible, detección de artefacto modificado, determinismo, propiedades de S4/S5/S7, ausencia de llamadas de entrenamiento, la etiqueta no viaja en las columnas de eventos, y con datos locales: regresión S6, cardinalidad, paridad ISO, coherencia predicciones/matriz).

Archivo modificado: `scripts/benchmark/puntuar.py` (unas pocas líneas: hashea antes de cargar y verifica al final, dejando `integridad_<tag>.json`).

### Escenarios nuevos (solo víctimas DEV, país habitual)

| ID | Etiqueta | Construcción | Mundos |
|---|---|---|---|
| S4_secuencia | 1 | Tipos de evento permutados dentro de cada día; horas, conteos y país intactos (ISO ciego por construcción) | 138 |
| S5_pico_corto | 1 | Por día activo, ráfaga de 5 × los eventos de archivo habituales en ≤ 5 min, tipos del perfil propio | 167 |
| S6_control_identidad | 0 | Ventana original sin modificar | 167 |
| S7_control_benigno | 0 | Ventana corrida +1 h y 10% de eventos duplicados (jitter 1 a 30 s) | 167 |

Se omitieron 29 mundos S4 porque ningún día tenía tipos distintos que permutar (un positivo sin eventos alterados no es un caso positivo); quedan en el manifest.

### Separación entrenamiento/evaluación

- Modelos cargados desde los artefactos existentes; sin `fit`, sin `Fase*`, sin `export_clue_combinado`. La prueba de aislamiento lo verifica sobre el código fuente.
- Los datos derivan de días posteriores al corte 2021-08-03 (ISO no los vio). Los mundos no pasan por `eventos_crudos`.
- **Resultado de integridad real**: los 9 artefactos tienen el mismo SHA-256 antes y después (`integridad_vigente.json`, `iguales: true`).
- Unidad de evaluación: usuario-día (ISO, LSTM, híbrido) y chunk de 50 eventos (`lstm_seq`). Los negativos son los días originales de las mismas víctimas; los controles S6 y S7 se reportan aparte para no contar dos veces los mismos días.

### Umbrales (los de producción, sin ajustar)

| Modelo | Regla de alerta |
|---|---|
| iso | `anom_iso` (`predict == -1`) |
| lstm | `risk_lstm > 95` con ≥ 1 chunk cerrado |
| hibrido | nivel ∈ {alto, crítico} (umbral 70 + regla_piso) |
| hibrido_decay | igual, con decay |
| lstm_seq | `err > lstm_threshold.pkl` (p95 de train). **Exploratorio**: no decide nada en producción |

## 4. Resultados

Corrida: `puntuar.py --run controlado` (131 s) y `clasificacion.py --run controlado`, n_boot 300, seed 42. Commit de partida `a2a6f41`. Los scores son percentiles de ranking, no probabilidades calibradas.

### 4.1 Subconjunto `sin_insample_v1` (principal: sin víctimas del train del LSTM v1)

| Modelo | Escenario | TP | FP | TN | FN | Precision | Recall | F1 | Especif. | Accuracy | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iso | TODOS | 15 | 21 | 3572 | 639 | 0,417 | 0,023 | 0,043 | 0,994 | 0,845 | 0,556 | 0,206 |
| iso | S4 | 1 | 21 | 3452 | 305 | 0,045 | 0,003 | 0,006 | 0,994 | 0,914 | 0,489 | 0,079 |
| iso | S5 | 14 | 21 | 3572 | 334 | 0,400 | 0,040 | 0,073 | 0,994 | 0,910 | 0,621 | 0,172 |
| lstm | TODOS | 1 | 0 | 3593 | 653 | 1,000 | 0,002 | 0,003 | 1,000 | 0,846 | 0,539 | 0,184 |
| lstm | S4 | 0 | 0 | 3473 | 306 | n/d | 0,000 | 0,000 | 1,000 | 0,919 | 0,527 | 0,106 |
| lstm | S5 | 1 | 0 | 3593 | 347 | 1,000 | 0,003 | 0,006 | 1,000 | 0,912 | 0,554 | 0,117 |
| hibrido | TODOS | 65 | 151 | 3442 | 589 | 0,301 | 0,099 | 0,149 | 0,958 | 0,826 | 0,573 | 0,196 |
| hibrido | S4 | 8 | 76 | 3397 | 298 | 0,095 | 0,026 | 0,041 | 0,978 | 0,901 | 0,515 | 0,088 |
| hibrido | S5 | 57 | 151 | 3442 | 291 | 0,274 | 0,164 | 0,205 | 0,958 | 0,888 | 0,637 | 0,149 |
| hibrido_decay | TODOS | 46 | 121 | 3472 | 608 | 0,275 | 0,070 | 0,112 | 0,966 | 0,828 | 0,562 | 0,191 |
| hibrido_decay | S4 | 2 | 36 | 3437 | 304 | 0,053 | 0,007 | 0,012 | 0,990 | 0,910 | 0,513 | 0,086 |
| hibrido_decay | S5 | 44 | 121 | 3472 | 304 | 0,267 | 0,126 | 0,172 | 0,966 | 0,892 | 0,618 | 0,146 |
| lstm_seq (chunk) | TODOS | 74 | 319 | 12288 | 1659 | 0,188 | 0,043 | 0,070 | 0,975 | 0,862 | 0,676 | 0,180 |
| lstm_seq (chunk) | S4 | 29 | 308 | 12238 | 806 | 0,086 | 0,035 | 0,049 | 0,975 | 0,917 | 0,622 | 0,083 |
| lstm_seq (chunk) | S5 | 45 | 319 | 12288 | 853 | 0,124 | 0,050 | 0,071 | 0,975 | 0,913 | 0,725 | 0,119 |

Víctimas: 32 (S4: 26). Los IC bootstrap están en `confusion_vigente.csv`.

### 4.2 Controles negativos (`sin_insample_v1`, solo FP/TN)

| Modelo | S6 FP / TN | S6 especif. | S7 FP / TN | S7 especif. |
|---|---|---|---|---|
| iso | 1 / 347 | 0,997 | 2 / 356 | 0,994 |
| lstm | 0 / 348 | 1,000 | 0 / 358 | 1,000 |
| hibrido | 26 / 322 | 0,925 | 29 / 329 | 0,919 |
| hibrido_decay | 22 / 326 | 0,937 | 19 / 339 | 0,947 |

### 4.3 Subconjunto `todas` (incluye víctimas en train del LSTM v1: **optimista para el LSTM**)

| Modelo | Escenario | TP | FP | TN | FN | Precision | Recall | F1 | Especif. | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| iso | TODOS | 34 | 80 | 6047 | 1225 | 0,298 | 0,027 | 0,050 | 0,987 | 0,571 | 0,217 |
| lstm | TODOS | 8 | 21 | 6106 | 1251 | 0,276 | 0,006 | 0,012 | 0,997 | 0,561 | 0,207 |
| hibrido | TODOS | 171 | 471 | 5656 | 1088 | 0,266 | 0,136 | 0,180 | 0,923 | 0,593 | 0,217 |
| hibrido_decay | TODOS | 113 | 341 | 5786 | 1146 | 0,249 | 0,090 | 0,132 | 0,944 | 0,580 | 0,206 |
| lstm_seq (chunk) | TODOS | 181 | 562 | 17121 | 2291 | 0,244 | 0,073 | 0,113 | 0,968 | 0,732 | 0,219 |

Detalle por escenario (S4, S5) en `data/benchmark/controlado/reporte_*.md`.

## 5. Lectura de los resultados

- Con el umbral de producción, el recall es bajo en ambos escenarios nuevos y para todos los modelos (híbrido 0,10; ISO 0,02; LSTM por día ≈ 0). Estos escenarios son difíciles para los modelos vigentes; no es un resultado a corregir ajustando umbrales sobre estos mismos casos.
- **S4 (secuencia)**: ISO no puede verlo por construcción (AUC 0,49, azar). El LSTM por día tampoco lo detecta. A nivel chunk el AUC es 0,62, algo por encima del azar pero con recall 0,035. Es coherente con la limitación ya documentada de que el LSTM v1 casi no usa el orden de la secuencia.
- **S5 (pico corto)**: detección débil (híbrido recall 0,16; ISO 0,04; AUC del híbrido 0,64). La causa no se investigó: queda por verificar si el ISO, que evalúa el agregado diario, diluye una ráfaga de minutos en el total del día.
- El híbrido es el único que alerta con alguna frecuencia, pero a costa de más falsos positivos: 4,2% en días originales y ≈ 8% en los controles S6/S7 (especificidad 0,92 a 0,95).
- **Discrepancia S6: resuelta, no es error del pipeline** (auditoria 2026-10-19). Las 685 filas S6 coinciden con los dias originales por (uid, date): 0 duplicados, 0 huerfanos, 0 diferencias en `n_events`, scores ISO/LSTM, `chunks_cum`, hibrido, decay, niveles y anomalias (test `test_regresion_s6_identico_a_dias_originales`). El 7,5% de FP (26/348) vs 3,9% en el resto de dias de las mismas victimas (125/3245) es diferencia de **poblacion comparada**. La hipotesis "ventanas mas activas" no se confirma (mediana de eventos 68 vs 83). Pesa el agrupamiento por usuario: 16 de los 26 FP vienen de 2 de 32 victimas; sin ellas S6 da 3,1% y los originales 2,3%.
- **Paridad ISO contra Fase6**: el `max|diff| = 0,218` corresponde a **1 dia de 61 284** (mediana 0, media 3,6e-6); 0 predicciones binarias distintas, sin efecto sobre alertas. Dia: `silent-gray-hawk-salesassistant` 2020-05-05 (pre-corte, fuera de la evaluacion), con un evento de `location_country = None`: Fase3 (pandas `nunique`) lo ignora (`n_distinct_countries` = 1) y `DailyAggregateAccumulator` lo cuenta aparte de `'unknown'` (= 2). Es un caso borde de datos limpios con pais nulo (1 en 3001 filas de ese archivo); no se cambio el pipeline.
- Auditoria de reproducibilidad: segunda corrida de `puntuar.py` (tag `auditoria`) bit-identica en scores y errores por chunk; 9 artefactos con SHA-256 iguales; `clasificacion.py` repetido con la misma semilla da `confusion_vigente.csv` byte a byte igual; `ampliado/` y los sha256 del HOLDOUT registrado sin cambios.
- Los IC bootstrap usan un RNG por celda (`rng_celda`) y `n_boot_validas` (300/300 en todas las celdas). `lstm_seq` tiene `unidad = chunk-50-eventos`: su matriz no es comparable con la de usuario-dia.

## 6. Limitaciones

- Detectar sintéticos no demuestra detectar anomalías reales desconocidas; es capacidad frente a los escenarios probados.
- Brecha de dominio: modelos entrenados con CLUE-LDS (colaboración cloud), no con telemetría del agente.
- País domina ISO y LSTM v1: los escenarios `*_con_pais` del benchmark previo son más fáciles por eso, y los nuevos se evalúan sin país a propósito.
- Evaluación a día cerrado, distinta del agregado parcial online; el blend personal no se reproduce.
- LSTM v1 es in-sample para parte de las víctimas: reportar siempre `sin_insample_v1` como cifra principal.
- Ventanas S6/S7 agrupadas por victima (2 victimas = 62% de los FP de S6): los IC por victima son anchos y de cobertura incierta con 32 victimas. Un chunk `lstm_seq` es positivo si contiene >= 1 evento modificado (en S5 incluye chunks mayormente benignos).
- Los escenarios nuevos son solo DEV y exploratorios. El HOLDOUT ya se usó una vez (08/10) y no se tocó.
- S7 usa un corrimiento fijo de +1 h (el plan decía ±1 h) para no mover eventos antes del inicio de la ventana.
- No se evaluó el sistema combinado más allá del híbrido real (sin blend personal).

## 7. Reproducir

```
python scripts/benchmark/generar_controlados.py            # data/benchmark/controlado/ (mundos, casos.csv, manifest.json)
python scripts/benchmark/puntuar.py --run controlado --tag vigente    # ~2 min, artefactos de solo lectura
python scripts/benchmark/clasificacion.py --run controlado            # reportes, predicciones, confusion_vigente.csv
SUPABASE_DB_URL= python -m pytest api/tests/test_clasificacion_benchmark.py
```

`data/benchmark/` está gitignorado (la reproducción requiere `data/processed/clean_*` y `data/benchmark/ampliado/` locales; `puntuar.py` sin `--tag` nuevo pisa `scores_vigente.parquet`). El manifest registra el sha256 de las salidas (`mundos.parquet`, `escenarios.parquet`, `casos.csv`) y el md5 de las entradas.

## 8. Pendiente

- Ninguno bloqueante. `lstm_seq` a nivel usuario-día queda sin implementar (requiere definir cómo asignar un chunk a un día).
