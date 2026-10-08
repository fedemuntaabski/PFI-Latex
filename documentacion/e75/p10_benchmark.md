# P10 E75 — Benchmark de detección, criterio de promoción y limitaciones

**Fuente:** `documentacion/informe_final_modelos.md` (en adelante, "el informe"), fechado 2026-10-08. El archivo está sin trackear y no se commitea en esta tanda.
**Rama:** `e75/paquete`. **Modelo en producción:** sin cambios (v1).
**Compilación de cada tanda** (pdflatex, biber, pdflatex ×2): 0 errores, 0 `Overfull \hbox`, 0 referencias indefinidas, 0 `??` en el PDF.

## Commits

| tanda | commit | archivos |
|---|---|---|
| T1 | `feb5aeb` P10 E75 T1 | pruebas.tex |
| T2 | `fa4d11a` P10 E75 T2 | pruebas.tex, producto.tex (label) |
| T3 | `914bdd1` P10 E75 T3 | producto.tex, requerimientos.tex, pruebas.tex |
| T4 (+T6a, T6b) | `14dd5a9` P10 E75 T4 | producto.tex, pruebas.tex, conclusiones.tex, arquitectura.tex |
| T5 | `02b73db` P10 E75 T5 | producto.tex |
| entregable | (este archivo) | documentacion/e75/p10_benchmark.md |

T6 no tiene un commit propio, porque cada punto entró en la tanda que tocaba ese texto: T6c en T3, T6d y T6e en T1, y T6a y T6b en T4.

## Cambios por tanda

### T1. Nueva sección 10.7 "Evaluación con escenarios etiquetados" (`\label{sec:benchmark}`)
- Se ubica entre 10.6 (validación por escenarios inyectados) y la evaluación de usabilidad, que pasa a ser 10.8. Por eso Decisiones pasa a 10.9, Limitaciones de las pruebas a 10.10 y Síntesis a 10.11.
- Subsecciones: Escenarios (`tab:bench-escenarios`), Partición y métricas, Resultados en HOLDOUT (`tab:bench-auc`, `tab:bench-recall`, `tab:bench-fpr`), Lectura de los resultados y Contraste con las metas.
- T6d: la lectura usa la versión corregida ("HOLDOUT es una estimación limpia del sistema vigente, porque no se adoptó nada de lo explorado en DEV").
- T6e: se usa "período de test de Isolation Forest".
- Criterios tomados por defecto:
  - El rango 12–30 % excluye S2 solo archivos (0,11), que se nombra aparte.
  - El rango 91–99 % con país se limita a la exfiltración (S2).
  - El contraste con las metas aclara que la meta de detección se mide en usuarios y el benchmark en usuario-días.
  - El corte se escribe "2 de agosto de 2021", como en el cap. 8.
  - Se omite el 99,8 % del informe para no contradecir el 99,946 % de 10.6.

### T2. 10.9 Decisiones
- Párrafos agregados después de `tab:decisiones-pruebas`: enlace, recalibración de umbrales, agregación del LSTM y combinación, decaimiento, modelos v2 y cierre.
- Coherencia:
  - La fila "No existen etiquetas…" ahora remite a sec:benchmark.
  - Se agrega una oración al final del párrafo de 10.5 que dice que no es posible calcular recall ni ROC, remitiendo a sec:benchmark.
  - Se agrega `\label{sec:reentrenamiento-producto}` en 9.2.4.

### T3. Criterio de promoción
- 9.2.4: se reemplaza la regla anterior y el marcador `[[CODIGO: regla de promoción vigente…]]`. El texto nuevo incluye:
  - el criterio de no inferioridad sobre DEV;
  - las causas de no promoción;
  - los 7,5 minutos que agrega al reentrenamiento;
  - el motivo del reemplazo;
  - el margen del orden de la variación entre semillas (T6c);
  - la demostración;
  - el respaldo completo y la exportación de referencias como último paso.
- Tabla de componentes (9.1): "comparación de métricas" pasa a "evaluación del candidato sobre escenarios de referencia".
- RF-21: el texto describe el criterio nuevo. El estado sigue en "Parcial: todavía no se observa la promoción real de un modelo mejor".
- Diferencias encontradas y corregidas:
  - **CU-03 paso 4:** "compara las métricas" pasa a "puntúa el modelo nuevo y el vigente sobre los mismos escenarios de referencia".
  - **CU-03 paso 5:** "iguala o mejora" pasa a "no es inferior según el criterio de promoción".
  - **CU-03 alt. 4a:** "empeora" pasa a "no cumple el criterio, faltan escenarios, el corte no coincide o el puntuado falla; se registra el motivo".
  - **HU-09 enunciado:** "solo se reemplace si mejora" pasa a "si no detecta peor que el vigente".
  - **HU-09 criterios 2 y 3:** "métricas iguales o mejores / peores" pasa a "cumple / no cumple el criterio de no inferioridad, o la evaluación está incompleta".
- Otras menciones del criterio anterior:
  - Fila de redondeo de 10.9: se quita "manteniendo el criterio…" y se aclara que ese criterio se reemplazó después.
  - Prueba E2E de reentrenamiento (10.3): se aclara que verifica el criterio anterior.
  - La tabla de metas de 10.5 usa la tasa de anomalías como métrica de evaluación, no como criterio de promoción, así que no cambia.

### T4. Limitaciones, interpretación y conclusiones
- 9.6, filas nuevas:
  - el país actúa como interruptor;
  - el LSTM no aprovecha el orden de los eventos;
  - horas en UTC;
  - calibración del híbrido sin datos independientes;
  - salto al cerrar la primera secuencia del LSTM;
  - fragilidad del corte temporal del criterio de promoción (T6a).
- 9.6, filas existentes que se fusionan:
  - "Sensibilidad baja…": suma la confirmación del benchmark, y el tratamiento pasa a "evaluación con datos etiquetados del dominio del agente".
  - "Explicación solo de Isolation Forest": el tratamiento suma la opción de reemplazar el LSTM por un modelo explicable.
- 10.10: seis ítems nuevos:
  - escenarios sintéticos;
  - día cerrado;
  - pocas víctimas;
  - LSTM in-sample;
  - falsos positivos ante cambios de ubicación legítimos no medidos (T6b);
  - brecha de dominio.
- 10.6.4: hay causas verificadas además del país desconocido:
  - el cambio de país domina el error del LSTM;
  - el LSTM no aprovecha el orden de los eventos;
  - el riesgo correlaciona −0,68 con el volumen de actividad.

  La granularidad diaria sigue como causa inferida. Sobre el decaimiento se agrega que el benchmark confirma que empeora el ordenamiento en ventanas cortas.
- 10.11 Síntesis: suma el resultado del benchmark y actualiza las causas que orientan el trabajo futuro.
- Capítulo 13:
  - **Resultados principales:** se agregan las cifras de HOLDOUT y se ajustan las causas.
  - **Objetivo 2:** la evidencia suma sec:benchmark; el estado sigue en "Parcial".
  - **Lecciones aprendidas:** se agrega la lección pedida.
  - **Trabajo futuro:**
    - el ítem 1 suma la regla de ubicación y la transición gradual;
    - "Explicabilidad del LSTM" se fusiona en "Rediseño del LSTM";
    - "Datos propios" suma los escenarios etiquetados del dominio del agente;
    - se agrega un ítem nuevo, "Benchmark con reproducción evento a evento", que incluye fijar el corte del criterio de promoción.
- Cap. 8: no afirma hora local (dice "día calendario en UTC") ni que el LSTM capte el orden, así que no cambia.
- Hallazgo en el cap. 7 (`arquitectura.tex`, fila de TensorFlow): decía que el LSTM "analiza el orden de los eventos". Se matizó a "elegido para analizar el orden… la evaluación muestra que el modelo entrenado no aprovecha ese orden".

### T5. Región de Upstash
- `tab:tratamiento-datos`: ahora dice que PostgreSQL (Supabase) y Redis (Upstash) están en la región de São Paulo, Brasil. La columna de la organización ya mencionaba Brasil, así que no cambia.

## Verificación de números contra el informe

| cifra en el documento | ubicación | sección del informe |
|---|---|---|
| 7 días, 0,3 / 0,7 (similitud), k = 2, 5, 10, 2 a 5 h Viena | tab:bench-escenarios | §4.1 |
| cuatro diferencias del método de los autores | 10.7.1 | §4.2 |
| 123 víctimas, 5 días, DEV 63 / HOLDOUT 60, 62 / 57 | 10.7.2 | §4.3 |
| 47 de 57 víctimas in-sample del LSTM | 10.7.2, 10.7.4 | §4.3, §5 lectura 5 |
| prevalencia 0,08–0,09 | 10.7.2 | §4.4 |
| umbrales 40/70/90; riesgo ≥ 70 y ≥ 90 | 10.7.2 | §4.4 |
| 1.000 remuestreos, IC 95 % | 10.7.2 | §4.5 |
| ROC-AUC HOLDOUT (21 valores con IC) | tab:bench-auc | Tabla 5.1, columnas HOLDOUT |
| recall del híbrido (28 valores) | tab:bench-recall | Tabla 5.2 |
| FPR (12 valores; 6.127 / 62, 5.894 / 57, 12.236 / 262) | tab:bench-fpr | Tabla 5.3 |
| sin decaimiento: 0,08 DEV, 0,05 HOLDOUT, 0,07 test | 10.7.3 | Tabla 5.3, última columna |
| IF 0,76–0,88 en S2, 0,90 en S3, 0,46–0,62 en S1 | 10.7.4 | §5 lectura 2 |
| 0,80 vs 0,90 (S3); 0,80 vs 0,88 (S2 k=10); 0,68 vs 0,62 | 10.7.4 | §5 lectura 3 |
| 4–5 % FPR alto; 12–30 %; 91–99 % | 10.7.4, 10.7.5, 10.10, 10.11, 9.6, cap. 13 | §5 lectura 4; §10.1–10.3 |
| 0,11 (S2 solo archivos, alto, sin país) | 10.7.4 | Tabla 5.2 |
| LSTM 0,56–0,63 sin país | 10.7.4 | §10.4 |
| 10 víctimas sin secuencia de 50 eventos | 10.7.4 | §5 lectura 5 |
| 27 víctimas (primera versión); 13 y 14 | 10.9 | §4.3, §6 |
| 50,1 / 71,9 / 81,8; 60 % → 32 % | 10.9 | §6.1 |
| −0,004 a −0,10 de AUC; 3 días | 10.9 | §6.3 |
| 0,02 y 0,01; corte 2021-08-02; 7,5 min | 9.2.4, RF-21 | §7 |
| 0,7726 / 0,0557; 0,0734 vs 0,0657 | 9.2.4 | §7, demostración |
| Spearman 0,989; 66,7 %; ~72 % | 9.6 | §2 (DIAG §D.6), §6.5 |
| −0,68 | 10.6.4 | §2 |
| ±0,05–0,10 de AUC; 62 DEV, 57 HOLDOUT | 10.10 | §8, validez interna |
| ~28 usuario-días posteriores a 2022 | 9.6 | §7, fragilidad del corte |

### Discrepancias registradas (sin corregir)
- **Usuario-días del período de test:** el informe da 12.236 y la tabla `tab:metricas-modelo` de 10.5 da 12\,235. Se usa 12.236 en la tabla nueva y 10.5 no se toca.
- **País desconocido:** el informe da 99,8 % y 10.6 da 99,946 %. Se omite el 99,8 % para no contradecir 10.6.
- **"cerca del 70 %"** no figura en el informe. En su lugar se usan el 66,7 % (muestra del diagnóstico) y cerca del 72 % (período de test).
- **Ruta de la fuente:** el pedido citaba `documentacion/e75/informe_modelos_20261008.md`, pero el archivo real es `documentacion/informe_final_modelos.md`.

## Marcadores `[[...]]` restantes (ninguno nuevo)
| archivo:línea | marcador |
|---|---|
| chapter01.tex:53 | `[[CODIGO: confirmar estado del despliegue]]`, `[[CODIGO: confirmar según el resultado del Prompt C]]` |
| chapter04.tex:437–438 | `[[COMPLETAR: fechas]]` |
| requerimientos.tex:224 | `[[ESTADO SEGÚN RNF-02]]` |
| producto.tex:136 | `[[ESTADO SEGÚN RNF-02]]` |
| producto.tex:165 | `[[CODIGO: cifrado TLS…; claves de agente ligadas a su identificador]]` |
| pruebas.tex:204–210 | `[[CPU MEDIA/P95/MÁX]]`, `[[RSS MEDIA/P95/MÁX]]`, `[[INTERPRETACIÓN DE RNF-02…]]` |
| conclusiones.tex:20 | `[[CODIGO: TLS y autenticación mutua]]`, `[[CODIGO: RNF-02]]`, `[[CODIGO]]` |
| conclusiones.tex:23 | `[[CODIGO: actualizar si se reentrena]]` |
| conclusiones.tex:35, 39–40 | `[[CODIGO: resultado de seguridad]]`, `[[CODIGO: cantidad de pruebas y cobertura]]`, `[[CODIGO]]` |
| conclusiones.tex:46 | `[[CODIGO: actualizar conteo con RNF-02, RNF-03 y RNF-13]]` |
| conclusiones.tex:71 | `[[CODIGO: actualizar si el reentrenamiento cambia los resultados.]]` |
| conclusiones.tex:121, 125 | `[[CODIGO: ajustar según el resultado de la cobertura]]`, `[[CODIGO: limitaciones de seguridad…]]` |

Resuelto en esta tanda: `[[CODIGO: regla de promoción vigente tras el cierre de los modelos]]` (producto.tex) y `[[VERIFICAR: región de Upstash]]` (producto.tex).
Los dos marcadores "actualizar si se reentrena" del cap. 13 siguen abiertos: el modelo no cambió, pero el autor decide si los da por cerrados.
