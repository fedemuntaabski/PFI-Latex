# Informe final de los modelos de detección

**Fecha:** 2026-10-08. **Alcance:** los dos detectores no supervisados del score de riesgo (IsolationForest y autoencoder LSTM), su combinación híbrida, la metodología con que se evaluaron y el criterio con que se promueve un reentrenamiento. Documento pensado como base de un capítulo de tesis.

**Convención de citas.** Cada cifra indica entre corchetes el documento de origen, todos en `docs/analysis/`:

| clave | documento |
|---|---|
| [DIAG] | `diagnostico_entrenamiento_modelos.md` |
| [HIG] | `sesion_higiene_pipeline_20261006.md` |
| [BENCH] | `benchmark_deteccion_baseline_20261006.md` |
| [CAND] | `candidatos_score_20261007.md` |
| [CONF] | `sesion_score_iso_piso_lstm_20261007.md` |
| [V2] | `modelos_v2_20261008.md` |
| [CIERRE] | `sesion_cierre_modelos_20261008.md` |
| [RMS] | `docs/general/diagnostico_rms_personal_risk_agregacion_20260903.md` (fuera de `docs/analysis/`) |
| [S6B] | `sesion_s6b_verificacion_20261008.md` |

**Nomenclatura.** Para hablar de las variantes de cálculo del score se usan descripciones en palabras. Donde los documentos de origen usan códigos, la correspondencia es: *agregación del LSTM* — media acumulada de todos los fragmentos cerrados (A0, la vigente), media de los fragmentos del día (A1), máximo de los fragmentos del día (A2); *combinación* — promedio ponderado 0,5 (B0, vigente), promedio 0,8/0,2 (B1), máximo (B2), solo IsolationForest con el LSTM como piso (B3); *suavizado temporal* — sin decaimiento (C0), decaimiento exponencial vigente (C1), decaimiento asimétrico que solo suaviza bajadas (C2); *ubicación* — sin cambios (D0), ubicación neutralizada en los modelos más una regla explícita de país nuevo (D1).

---

## 1. Problema y objetivo de detección

El sistema es una plataforma UEBA (*User and Entity Behavior Analytics*) que asigna a cada usuario un score de riesgo conductual en tiempo real y, según el nivel resultante (bajo, medio, alto, crítico), dispara acciones locales en el equipo. El score se calcula a partir de dos detectores entrenados sin etiquetas:

- **IsolationForest** sobre el agregado diario de cada usuario (8 variables: volumen de eventos, tipos distintos, países distintos, eventos de archivo, inicios de sesión, hora media, proporción fuera de horario y entropía de tipos) [DIAG §C.1].
- **Autoencoder LSTM** sobre secuencias de 50 eventos consecutivos (tipo de evento embebido, tiempo entre eventos, hora y día en forma cíclica, cambio de tipo y cambio de país) [DIAG §D.1].

Cada detector se lleva a un percentil 0-100 contra su distribución de entrenamiento; el score híbrido es el promedio de ambos (o solo IsolationForest mientras el usuario no cerró su primera secuencia de 50 eventos), con decaimiento exponencial de vida media 3 días y una regla de piso que lleva el nivel a "alto" si cualquiera de los dos modelos marca anomalía [DIAG §H].

El objetivo de detección, fijado durante este trabajo, es **la exfiltración o el uso indebido del puesto de trabajo**, en la medida en que el dataset lo permite representar [BENCH, encabezado]. El dataset de entrenamiento es CLUE-LDS (Landauer et al., 2022): ~50 millones de eventos reales de una plataforma de almacenamiento en la nube, seudonimizados, sin etiquetas ni ataques [DIAG §B.1-B.2].

## 2. Diagnóstico del entrenamiento original y hallazgos principales

La revisión del pipeline de entrenamiento concluyó que la arquitectura (dos detectores no supervisados de granularidad distinta, normalización por percentil y decaimiento) es defendible, pero **no existía ninguna medida de capacidad de detección** [DIAG §1]. Los hallazgos principales fueron:

| severidad | hallazgo | evidencia |
|---|---|---|
| crítica | El criterio de promoción de reentrenamientos comparaba la tasa de anomalías de IsolationForest y el error medio del LSTM con "nuevo ≤ vigente". Ninguna de las dos mide detección; con ese criterio, un modelo que no marque nada sería el mejor. | [DIAG §F.1] |
| crítica | Los dos rechazos reales de promoción se decidieron por diferencias del tamaño del ruido: ~2 filas de 12.236 en IsolationForest y ±5 % de error en el LSTM con el mismo split. | [DIAG §F.2] |
| crítica | El reentrenamiento no regeneraba las distribuciones de referencia de los percentiles; los artefactos en disco eran los de un modelo rechazado. | [DIAG §A.3, §G.3] |
| alta | En el LSTM, la variable binaria "cambio de país" (desvío 0,021, se escala a ~47) explica el 66,7 % del error de reconstrucción; permutar el orden de los 50 eventos casi no cambia el ranking (Spearman 0,989). | [DIAG §D.4, §D.6] |
| alta | El riesgo LSTM por usuario correlaciona −0,68 con el logaritmo del volumen de actividad del usuario. | [DIAG §D.7] |
| alta | La calibración del híbrido (peso 0,5, piso, umbrales 40/70/90) se hizo con un riesgo LSTM que usaba datos futuros y con "etiquetas" sacadas de los propios modelos. | [DIAG §H, §B.4] |
| media | Diferencias entre entrenamiento y producción: IsolationForest se evalúa online sobre el agregado parcial del día; las horas se toman en UTC aunque el dataset es de Viena y el agente corre en Argentina; el agente traduce telemetría de host a tipos de evento del dataset con otra semántica. | [DIAG §E.1, §E.3, §E.5] |

## 3. Correcciones de higiene aplicadas

Antes de medir se corrigieron los problemas que invalidaban cualquier comparación, sin rediseñar ni reentrenar modelos [HIG]:

1. **Set de modelo consistente.** Ningún respaldo tenía un conjunto completo (modelo, escaladores, codificación y referencias). Se adoptó el único set coherente disponible (el del 02/09) y se regeneraron sus referencias de percentil. La referencia de IsolationForest regenerada coincide exactamente con la función de decisión sobre las 49.048 filas de entrenamiento; el desvío de la referencia LSTM anterior quedó medido en +5,3 % de la media [HIG Paso 1].
2. **Reentrenamiento autocontenido.** La exportación de referencias pasó a ser el último paso del pipeline, y el respaldo previo al reentrenamiento pasó de 9 a 17 archivos, de modo que un rechazo restaura modelo, escaladores, codificación, referencias y salidas offline juntos [HIG Paso 2].
3. **Un solo productor de la configuración** (`config_score_hibrido.json`), eliminando constantes duplicadas a mano [HIG Paso 2c].
4. **Pipeline robusto ante usuarios nuevos** (aserciones de conteo fijas reemplazadas por chequeos de consistencia) y **filtro de datos de prueba** en la mezcla de eventos reales usada para reentrenar [HIG Paso 3].
5. **Aislamiento de la suite de tests** respecto de las bases reales [BENCH §0].

Las mismas sesiones confirmaron dos hechos que condicionan todo lo que sigue: la escena de la demo con VPN escala a crítico **solo por la ubicación**, en los dos modelos (con dos países en el día, el riesgo de IsolationForest pasa de 75 a 98,5; un único cambio de país lleva el riesgo LSTM de 8,0 a 85,9) [HIG Paso 4], y forzar dos países en todo el período de test de IsolationForest vuelve anómalos al 49,6 % de los días en IsolationForest [HIG Paso 5b].

## 4. Metodología de evaluación

### 4.1 Escenarios

Como CLUE-LDS no trae ataques, se construyeron escenarios con etiqueta conocida, siguiendo la propuesta de los propios autores del dataset para la sustitución de cuenta y agregando dos escenarios sintéticos propios [BENCH §1]:

| escenario | qué simula | construcción |
|---|---|---|
| S1 (similar / disímil) | toma de cuenta | Desde el instante T, los eventos de la víctima en una ventana de 7 días se reemplazan por los de otro usuario activo en la misma ventana: el más parecido o el menos parecido según la similitud de los autores (0,3 · cociente de eventos por día + 0,7 · Jaccard de tipos). |
| S2 (k = 2, 5, 10) | exfiltración | En cada día activo de la ventana se inyecta una ráfaga de eventos de archivo y de compartición, de tamaño k veces la mediana diaria de eventos de archivo de la víctima, a una hora habitual de ella. |
| S2_archivos (k = 2, 5, 10) | exfiltración sin compartir | Igual que S2 pero solo con eventos de archivo, para separar el efecto de la compartición [V2 §3]. |
| S3 | uso fuera de horario | Los eventos de cada día se reubican entre las 02:00 y las 05:00 hora de Viena, conservando el orden. |

Cada escenario existe **sin país** (ubicación original, desconocida en el 99,8 % de los eventos) y **con país** (los eventos modificados llevan un país atacante). La versión sin país es la que mide comportamiento; la versión con país mide el efecto del "interruptor de ubicación" de los modelos.

### 4.2 Método de los autores y diferencias

El swap de S1 reproduce la fórmula y los pesos de similitud de la herramienta de los autores (`ait-aecid/clue-lds`). Se aparta en cuatro puntos, todos documentados: se usan los extremos de similitud en vez de pares al azar, el swap es unidireccional, la etiqueta es por usuario-día dentro de la ventana, y los donantes se restringen a usuarios que el LSTM no vio en entrenamiento [BENCH §1.3].

### 4.3 Partición DEV / HOLDOUT

Se tomaron como víctimas los usuarios con al menos 5 días activos posteriores al corte temporal de IsolationForest (2021-08-02), 123 en total, repartidos 50/50 por estrato de actividad previa: **DEV 63 y HOLDOUT 60**; con alguna ventana válida quedan 62 y 57 [V2 §3]. Las 27 víctimas de la primera versión del benchmark, ya usadas para explorar candidatos, quedaron forzadas en DEV. Esa primera versión las separaba según el split por usuario del LSTM en 13 de validación y 14 de prueba; en este informe se las llama **DEV-val (13)** y **DEV-test (14)**, y son subconjuntos de DEV, no particiones independientes como HOLDOUT [BENCH §1.1; CAND §1]. Todos los experimentos se hicieron solo sobre DEV; los scripts bloquean HOLDOUT salvo un pedido explícito, y **HOLDOUT se usó una única vez**, para la evaluación final de la sección 5 [CIERRE §1].

IsolationForest se entrenó con un split temporal, por lo que sus resultados en HOLDOUT son limpios. El LSTM vigente se entrenó con un split aleatorio por usuario: 47 de las 57 víctimas HOLDOUT con escenarios forman parte de su entrenamiento, y sus cifras en HOLDOUT son, por lo tanto, optimistas [V2 §7].

### 4.4 Métricas

La unidad es el usuario-día. Positivos: los días de los mundos modificados. Negativos: los días limpios posteriores al corte de las mismas víctimas. Se reportan [BENCH §3]:

- ROC-AUC y PR-AUC (la prevalencia de positivos ronda 0,08-0,09, por lo que el PR-AUC de azar es ese valor);
- recall en nivel ≥ alto y en crítico, con los umbrales de producción (40/70/90 para el híbrido; riesgo ≥ 70 y ≥ 90 para cada componente solo);
- tasa de falsos positivos (FPR) en ≥ alto y en crítico, sobre los negativos de cada subconjunto y sobre todo el **período de test de IsolationForest** (los usuario-días posteriores al corte 2021-08-02: 12.236 usuario-días, 262 usuarios). "Test" se refiere siempre a ese período del split temporal de IsolationForest, no a una partición del benchmark.

### 4.5 Intervalos de confianza

Intervalos al 95 % por bootstrap con 1.000 remuestreos **sobre víctimas** (no sobre días), porque los días de una misma víctima están correlacionados. Para comparar dos variantes se usa el mismo remuestreo, lo que da intervalos pareados de la diferencia [CONF §1].

### 4.6 Qué no reproduce el benchmark

Trabaja con el día cerrado, sin el agregado parcial que usa la producción en cada evento, y sin el ajuste por línea base personal de cada usuario, porque reproducirlo exige reprocesar evento a evento [BENCH §2, §6]. Ambos efectos suben el score de usuarios nuevos o poco activos.

## 5. Resultados finales en HOLDOUT del sistema en producción, evaluado a día cerrado (sin línea base personal ni agregado parcial)

Sistema evaluado: modelos v1 vigentes, agregación LSTM por media acumulada, promedio 0,5, con decaimiento, umbrales 40/70/90. Como todo el benchmark, se evalúa con el día cerrado: no incluye el ajuste por línea base personal ni el agregado parcial que la producción usa en cada evento (§4.6). Se agregan como referencia cada componente solo y el híbrido sin decaimiento. Fuente de todas las cifras de esta sección: [CIERRE §2] (`data/benchmark/ampliado/metricas_v1_holdout.csv`, sha256 registrado en el manifest).

**Tabla 5.1. ROC-AUC [IC 95 %], escenarios sin país.**

| escenario | ISO DEV | ISO HOLDOUT | LSTM DEV | LSTM HOLDOUT | híbrido DEV | híbrido HOLDOUT |
|---|---|---|---|---|---|---|
| S1 similar | 0,53 [0,45–0,61] | 0,46 [0,37–0,55] | 0,52 [0,46–0,57] | 0,56 [0,51–0,61] | 0,58 [0,50–0,64] | 0,58 [0,52–0,65] |
| S1 disímil | 0,65 [0,57–0,73] | 0,62 [0,52–0,70] | 0,59 [0,53–0,64] | 0,62 [0,56–0,67] | 0,68 [0,60–0,75] | 0,68 [0,63–0,73] |
| S2 k=2 | 0,80 [0,75–0,86] | 0,76 [0,70–0,82] | 0,57 [0,52–0,60] | 0,57 [0,53–0,61] | 0,74 [0,68–0,80] | 0,75 [0,71–0,80] |
| S2 k=5 | 0,89 [0,85–0,93] | 0,85 [0,80–0,91] | 0,59 [0,53–0,63] | 0,61 [0,57–0,65] | 0,78 [0,73–0,83] | 0,79 [0,76–0,84] |
| S2 k=10 | 0,91 [0,87–0,94] | 0,88 [0,82–0,93] | 0,59 [0,54–0,64] | 0,62 [0,58–0,66] | 0,78 [0,73–0,83] | 0,80 [0,76–0,84] |
| S2 archivos k=10 | 0,65 [0,59–0,71] | 0,59 [0,53–0,65] | 0,60 [0,55–0,65] | 0,63 [0,59–0,67] | 0,66 [0,60–0,72] | 0,67 [0,63–0,72] |
| S3 | 0,93 [0,89–0,96] | 0,90 [0,85–0,95] | 0,54 [0,49–0,58] | 0,56 [0,51–0,60] | 0,79 [0,74–0,84] | 0,80 [0,77–0,84] |

**Tabla 5.1b. ROC-AUC [IC 95 %] del híbrido sin decaimiento, escenarios sin país** (referencia para la lectura 3; misma fuente, filas `modelo = hibrido`).

| escenario | híbrido sin decaimiento DEV | híbrido sin decaimiento HOLDOUT |
|---|---|---|
| S1 similar | 0,56 [0,49–0,64] | 0,56 [0,48–0,62] |
| S1 disímil | 0,68 [0,60–0,76] | 0,71 [0,65–0,76] |
| S2 k=2 | 0,79 [0,73–0,84] | 0,80 [0,76–0,84] |
| S2 k=5 | 0,85 [0,79–0,89] | 0,86 [0,82–0,89] |
| S2 k=10 | 0,85 [0,81–0,90] | 0,87 [0,83–0,91] |
| S2 archivos k=10 | 0,68 [0,61–0,74] | 0,68 [0,64–0,73] |
| S3 | 0,87 [0,83–0,91] | 0,88 [0,85–0,91] |

**Tabla 5.2. Detección operativa del híbrido en producción (nivel con piso), HOLDOUT.**

| escenario | recall ≥ alto sin país | recall ≥ alto con país | recall crítico sin país | recall crítico con país |
|---|---|---|---|---|
| S1 similar | 0,12 [0,06–0,19] | 0,12 [0,06–0,19] | 0,00 | 0,00 |
| S1 disímil | 0,18 [0,10–0,27] | 0,18 [0,10–0,27] | 0,00 | 0,00 |
| S2 k=2 | 0,19 [0,12–0,28] | 0,91 [0,87–0,94] | 0,01 | 0,12 [0,07–0,18] |
| S2 k=5 | 0,27 [0,18–0,37] | 0,99 [0,98–1,00] | 0,00 | 0,12 [0,07–0,18] |
| S2 k=10 | 0,30 [0,20–0,41] | 0,99 [0,98–1,00] | 0,01 | 0,10 [0,05–0,16] |
| S2 archivos k=10 | 0,11 [0,04–0,19] | 0,79 [0,71–0,86] | 0,00 | 0,10 [0,05–0,16] |
| S3 | 0,29 [0,20–0,41] | 0,30 [0,20–0,41] | 0,04 [0,01–0,07] | 0,04 [0,01–0,08] |

**Tabla 5.3. Falsos positivos sobre usuario-días limpios.**

| base | ISO ≥ 70 | LSTM ≥ 70 | híbrido ≥ alto | híbrido crítico | híbrido sin decaimiento ≥ alto |
|---|---|---|---|---|---|
| negativos DEV (6.127 días, 62 usuarios) | 0,23 [0,15–0,31] | 0,10 [0,04–0,18] | 0,06 [0,02–0,11] | 0,00 | 0,08 [0,04–0,13] |
| negativos HOLDOUT (5.894 días, 57 usuarios) | 0,31 [0,19–0,44] | 0,08 [0,03–0,14] | 0,04 [0,02–0,09] | 0,00 | 0,05 [0,02–0,10] |
| período de test de IsolationForest (12.236 días, 262 usuarios) | 0,26 [0,20–0,34] | 0,09 [0,05–0,14] | 0,05 [0,03–0,09] | 0,00 | 0,07 [0,04–0,10] |

**La FPR ante cambios de ubicación legítimos (viajes, VPN corporativa) no se midió:** los negativos no tienen país (CLUE-LDS no trae ubicación en el 99,8 % de los eventos), así que las tasas de la Tabla 5.3 no dicen nada sobre cuántas alertas generaría un usuario legítimo que cambia de país.

**Lectura.**

1. **HOLDOUT como estimación limpia del vigente.** De lo explorado en DEV no se adoptó nada: el sistema evaluado es el mismo que estaba en producción antes de los experimentos, así que no había selección sobre DEV que HOLDOUT pudiera desmentir. El valor de HOLDOUT es dar una estimación del vigente sobre víctimas nunca miradas. Las diferencias DEV–HOLDOUT del híbrido caen dentro de los intervalos.
2. **IsolationForest sostiene la detección por volumen y horario** (S2 0,76-0,88 y S3 0,90 en HOLDOUT, con split temporal limpio) y está cerca del azar en la toma de cuenta (S1 0,46-0,62).
3. **El híbrido ordena peor que IsolationForest solo en lo que este detecta** (S3: 0,80 contra 0,90; S2 k=10: 0,80 contra 0,88), y algo mejor en la toma de cuenta disímil (0,68 contra 0,62). Sin decaimiento, el híbrido ordena mejor en S2 y S3 (0,80-0,88 en HOLDOUT, Tabla 5.1b; 0,86-0,88 sin contar S2 k=2), igual que en las sesiones previas, con algo más de falsos positivos (5 % contra 4 % en HOLDOUT).
4. **Operativamente**, con una tasa de falsos positivos en alto del 4-5 % y prácticamente nula en crítico, el sistema detecta en nivel alto entre el 12 % y el 30 % de los días atacados sin país. Cuando el ataque introduce un país nuevo mezclado en el día, el piso de IsolationForest lleva la detección al 91-99 %. El nivel crítico casi no se alcanza sin país.
5. **LSTM in-sample.** Sobre las 10 víctimas HOLDOUT que no forman parte del entrenamiento del LSTM, los valores del LSTM no son interpretables como señal: esas víctimas tienen tan poca actividad que su historia no llega a cerrar una secuencia de 50 eventos, y las únicas secuencias aparecen por los eventos inyectados (los negativos valen 0). Por eso el LSTM marca 1,00 en S2 k=10 y 0,50 en S3 en ese subconjunto. Con solo 65 días negativos, sus intervalos son además muy amplios. El híbrido en ese subconjunto: S2 k=2-10 sin país 0,77-0,87, S3 0,96, FPR ≥ alto 0,09 [CIERRE §2.3]. La conclusión sobre el LSTM se apoya, entonces, en la evidencia de DEV fuera de muestra (32 víctimas fuera de su entrenamiento: entre 0,02 y 0,08 menos de AUC que con todas [V2 §4.3]) y en el diagnóstico.

**Fila informativa: IsolationForest v2 en HOLDOUT** (variables corregidas, sin país; ver §6.4). ROC-AUC sin país: S1 0,42/0,52, S2 0,98-0,99, S2_archivos 0,50-0,58, S3 0,94; FPR ≥ 70 en negativos HOLDOUT 0,38 [0,24–0,52] [CIERRE §2.4]. El salto en S2 se explica por la nueva variable de compartición, que es en parte circular con el escenario (§6.4), y la pérdida en S1 se repite. **No cambia la decisión de mantener v1.**

## 6. Experimentos realizados y por qué no se adoptaron

Los experimentos de esta sección se hicieron sobre la primera versión del benchmark (27 víctimas). Donde los documentos de origen dicen VAL y TEST, aquí se usa **DEV-val (13 víctimas)** y **DEV-test (14 víctimas)**: los dos son subconjuntos de DEV (§4.3). Sus cifras no son comparables con las de §5 y §7, que usan las 62 víctimas DEV del benchmark ampliado, con otras ventanas y otros negativos.

### 6.1 Recalibración de umbrales

Calibrar los umbrales por cuantiles sobre los usuario-días de entrenamiento (20 % medio, 5 % alto, 1 % crítico) da 50,1 / 71,9 / 81,8. Con ellos la FPR en alto del período de test de IsolationForest es 4,4 % y en crítico 1,3 %, el recall en alto queda parecido (DEV-val 0,18 contra 0,21; DEV-test 0,18 contra 0,19) y el nivel medio deja de marcar el 60 % de los días limpios para marcar el 32 % [CAND §2]. Se recomendó en su momento, pero la decisión final mantiene 40/70/90: la mejora es de reparto entre niveles, no de detección, y con los umbrales calibrados la escena de exfiltración de la demo cae a "bajo" al cerrar el primer fragmento LSTM [CONF §4]. Los umbrales son editables en tiempo de ejecución, por lo que la recalibración queda disponible sin tocar código.

### 6.2 Agregación del LSTM y combinación

Una selección por pasos sobre DEV-val eligió el máximo diario del LSTM (AUC del LSTM solo 0,62 contra 0,48 con la media acumulada), pero en DEV-test la ventaja desapareció (0,58 contra 0,59). El máximo diario activa el piso LSTM en el 2,9 % de los días limpios (contra 0,27 %), con lo que el piso consume casi todo el presupuesto de falsos positivos y el umbral de alto queda pegado al de crítico. El ganador formal del protocolo quedó por debajo del vigente en DEV-test (AUC primaria 0,78 contra 0,85; AUC de S1 0,53/0,58 contra 0,62/0,66) y cumplía 1 de 3 criterios de la demo [CAND, Resumen y §1-§3]. Resultado central: con tan pocas víctimas, la selección secuencial persiguió diferencias que DEV-test no confirmó.

**Por qué el vigente tiene AUC primaria 0,85 aquí y 0,77 en §5 y §7.** Es el mismo sistema medido sobre versiones distintas del benchmark: 0,85 (0,845) es la media de los cuatro primarios sin país en las 14 víctimas de DEV-test, con las ventanas y los negativos de la primera versión [CAND §3; CONF §1]; 0,77 (0,7726) es la misma media sobre las 62 víctimas DEV del benchmark ampliado [CIERRE §3.3], con el que se calcula el gate de §7. En DEV-val la misma métrica valía 0,68 [CAND §3]: la variación entre subconjuntos de pocas víctimas es mayor que cualquier diferencia entre variantes de esta sección.

Una prueba confirmatoria de "IsolationForest como score, con el LSTM solo como piso y decaimiento asimétrico", fijada de antemano, ganó en ordenamiento (AUC primaria +0,18 en DEV-val, +0,08 en DEV-test) pero perdió en recall operativo en DEV-val (0,127 contra 0,178) y en la toma de cuenta similar (0,40 contra 0,46), y en la demo la exfiltración sin VPN no llegaba nunca a alto. No pasó el criterio [CONF, Veredicto y §2].

### 6.3 Decaimiento temporal

El decaimiento empeora el ordenamiento en todos los escenarios de ventana corta (−0,004 a −0,10 de AUC) [BENCH §4], lo que vuelve a verse en HOLDOUT (§5, lectura 3). Quitarlo es la única mejora de ordenamiento que se sostuvo en DEV-val y DEV-test, pero no se tradujo en más recall en alto en DEV-test (0,158 contra 0,180) [CAND, post-hoc]. Se mantuvo porque es una constante de negocio de producción, con respaldo en la mediana real de intervalos de actividad (3 días), y su efecto operativo neto no es concluyente.

### 6.4 Modelos v2

Se entrenaron versiones corregidas de ambos modelos: sin variables de país, con split temporal también para el LSTM, hora local de Viena, escaladores ajustados solo con entrenamiento, conteo de archivos ampliado a los 7 tipos y una variable nueva de eventos de compartición [V2 §1]. En DEV:

| resultado | evidencia [V2] |
|---|---|
| IsolationForest v2 mejora mucho en S2 sin país (0,805 → 0,975) | §4.1 |
| pero toda esa mejora la explica la variable de compartición: en S2_archivos, sin compartición, v1 y v2 empatan (0,578 contra 0,575) | §4.1, §4.7 |
| IsolationForest v2 empeora en toma de cuenta (S1 disímil 0,654 → 0,570, IC de la diferencia [−0,12; −0,05]) | §4.1 |
| el LSTM v2 sigue en el azar sin país (0,52-0,58), y su variante por máximo diario varía entre semillas tanto como el intervalo de confianza | §4.2, §4.6 |
| v2 no depende del país (idéntico con y sin en S1 y S3), pero pierde todo lo que v1 detectaba por ubicación; la escena VPN de la demo ya no llega a crítico | §4.5, §5 |

v2 no se promueve: la ganancia es circular con el diseño del escenario S2, pierde en la toma de cuenta y, sin una regla explícita de ubicación en el motor de decisión, pierde la detección por país. El gate de promoción de la sección 7 lo rechaza también por falsos positivos (§7).

### 6.5 Aporte real de cada variable

| modelo | variable | aporte medido |
|---|---|---|
| IsolationForest | todas sobre el período de test | ablación por reemplazo con la mediana: Spearman del ranking entre 0,94 y 0,99, ninguna domina; las anomalías se reparten entre volumen (57 de 99) e inicios de sesión (50 de 99) [HIG 5b] |
| IsolationForest | países distintos | latente en el período de test (nunca > 1), decisiva cuando dispara: forzarla a 2 vuelve anómalo el 49,6 % de los días [HIG 5b] |
| IsolationForest | compartición (v2) | explica toda la mejora de v2 en S2 [V2 §4.7] |
| IsolationForest | archivos, 7 tipos (v2) | no aporta frente a 3 tipos [V2 §4.7] |
| LSTM | cambio de país | ~72 % del error medio en todo el período de test (66,7 % en la muestra del diagnóstico) [HIG 5a; DIAG §D.6] |
| LSTM | cambio de tipo / hora / tiempo entre eventos / embedding del tipo | 17,1 % / 8,9 % / 4,2 % / 3,0 % del error [DIAG §D.6] |
| LSTM | orden de los eventos | permutar los 50 pasos no cambia el ranking (Spearman 0,989), con y sin la variable de país [HIG 5a] |

## 7. Nuevo criterio de promoción del reentrenamiento

El criterio anterior (tasa de anomalías de IsolationForest y error medio del LSTM, "nuevo ≤ vigente") se reemplazó por un **gate de no-inferioridad sobre el benchmark DEV** [CIERRE §3]:

- **Candidato:** los artefactos recién entrenados. **Vigente:** el respaldo que el sistema ya hace antes de reentrenar. Ambos se puntúan sobre los mismos escenarios DEV; HOLDOUT nunca participa.
- **Se promueve solo si** (a) la ROC-AUC media del híbrido de producción en los cuatro escenarios primarios sin país (S2 k=2, 5, 10 y S3) es al menos la del vigente menos 0,02, **y** (b) la FPR en nivel ≥ alto sobre los días limpios DEV es como máximo la del vigente más 0,01. Los márgenes se fijaron de antemano, del orden de la variación entre semillas de entrenamiento observada [V2 §4.6].
- **No se promueve, con motivo registrado,** si faltan los escenarios, si el corte temporal del candidato no es el 2021-08-02 (con datos nuevos, días de evaluación podrían pasar a entrenamiento) o si el puntuado falla.
- Las métricas de ambos y el motivo se registran en la base (tabla `metricas_modelo`, extendida) y en el historial de reentrenamientos.

**Demostración** [CIERRE §3.3]:

| candidato | AUC media primarios | FPR ≥ alto DEV | decisión |
|---|---|---|---|
| vigente (contra sí mismo) | 0,7726 vs 0,7726 | 0,0557 vs 0,0557 | promueve |
| modelos v2 | 0,8395 vs 0,7726 (pasa a) | 0,0734 vs 0,0557, máximo 0,0657 (falla b) | rechaza |

El gate agrega unos 7,5 minutos al pipeline (dos puntuados de ~3,7 minutos) [CIERRE §3.3].

**Alcance del margen.** El margen de 0,02 de AUC es del orden del ruido entre semillas de entrenamiento [V2 §4.6], no un umbral de significación: un candidato equivalente al vigente puede quedar rechazado solo por la semilla con que se entrenó, y uno algo peor puede pasar. El gate protege contra regresiones grandes, no distingue diferencias chicas.

**Fragilidad del corte temporal.** El corte de IsolationForest v1 no está fijo: Fase4 lo calcula como el percentil 80 de las fechas de los usuario-días. Con los datos actuales sigue siendo 2021-08-02, pero bastan 28 usuario-días nuevos posteriores a 2022 (del orden de un mes de captura de un equipo) para correrlo a 2021-08-03, y desde ahí el gate rechaza por fail-safe cualquier reentrenamiento [S6B, A1]. Las alternativas (fijar el corte al reentrenar o evaluar sobre los días DEV posteriores al corte del candidato) quedan propuestas en ese documento.

**Desalineación con el requisito formal.** La letra de RF-21 en el documento de requerimientos ("promover el modelo nuevo solo si iguala o mejora las métricas del modelo vigente", y el paso 5 del CU-03) describe el criterio anterior. El gate de no-inferioridad acepta un candidato hasta 0,02 de AUC peor y hasta 0,01 de FPR mayor, así que el requisito formal debe actualizarse para reflejarlo.

## 8. Limitaciones y amenazas a la validez

**Validez de constructo.**
- Los escenarios son sintéticos: ráfagas uniformes (S2) y reubicación lineal (S3) son modelos simples de un ataque, y la ganancia en S2 premia a modelos que cuentan los mismos tipos de evento que se inyectan [BENCH §6; V2 §7].
- El país atacante es una inyección artificial; CLUE-LDS no tiene ubicación en el 99,8 % de los eventos [BENCH §6].
- **La FPR ante cambios de ubicación legítimos no se midió:** los negativos no tienen país, así que no hay estimación de cuántas alertas generan viajes o VPN corporativas de usuarios legítimos.
- **El país dentro de los modelos v1** actúa como interruptor: decide la detección operativa con país y el crítico de la demo, no el comportamiento [HIG Paso 4, 5b].

**Validez interna.**
- Pocas víctimas (62 DEV, 57 HOLDOUT): intervalos de ±0,05-0,10 de AUC; diferencias pequeñas entre variantes no son significativas.
- El LSTM v1 es in-sample para 47 de 57 víctimas HOLDOUT y 30 de 62 DEV; sus cifras son optimistas [V2 §3, §7].
- El LSTM no es determinista entre corridas y su variante por máximo diario varía entre semillas tanto como los intervalos [DIAG §G.1; V2 §4.6].
- El primer intento de cálculo de métricas sobre HOLDOUT falló por un error de código en una métrica auxiliar antes de escribir resultados; se corrigió y se repitió una vez, sin haber visto ninguna cifra [CIERRE §1.3].

**Validez externa.**
- **Brecha de dominio con el agente:** los modelos se entrenaron con logs de colaboración en la nube; producción recibe telemetría de host traducida a ese vocabulario con otra semántica. Ninguna cifra del benchmark se transfiere al agente sin más [DIAG §E.3].
- **Zona horaria:** v1 calcula horas en UTC, el dataset es de Viena y el agente corre en Argentina [DIAG §E.5].
- **Agregado parcial (E.1)** y **línea base personal:** producción evalúa IsolationForest en cada evento sobre el agregado parcial del día y ajusta el score con un baseline personal cuyo componente tiene un sesgo estructural hacia percentiles altos en usuarios con poca historia; el benchmark no reproduce ninguno de los dos [BENCH §6; RMS].
- **Salto al cerrar el primer fragmento LSTM:** el score pasa de 100 % IsolationForest a 50/50 de un evento al otro (en la demo, de 76,6 a 48,8) [BENCH §5].
- **LSTM sin señal secuencial:** el modelo no aprovecha el orden; sin país está cerca del azar [HIG 5a; §5].

## 9. Trabajo futuro

1. **Regla explícita de ubicación en el motor de decisión**, que reemplace a las variables de país dentro de los modelos, como requisito para cualquier modelo sin país [V2 §4.7].
2. **Reemplazar o rediseñar el LSTM**: un modelo no secuencial sobre la misma ventana probablemente rankee igual con menos complejidad y con explicabilidad [DIAG §D.9]; evaluar agregaciones que respondan a ventanas cortas sin inflar el piso.
3. **Transición gradual** al cerrar el primer fragmento, en vez del salto 100/0 → 50/50.
4. **Ablaciones pendientes**: la pérdida de IsolationForest v2 en toma de cuenta (hora local frente a escalador) y el efecto del logaritmo del tiempo entre eventos en el LSTM [V2 §7].
5. **Datos del dominio del agente** con escenarios etiquetados, para medir la brecha de dominio.
6. **Benchmark con replay evento a evento**, que incluya el agregado parcial y la línea base personal.
7. **Recalibración de umbrales en cada reentrenamiento** si se adopta la calibración por cuantiles [CAND §4.a].

## 10. Conclusiones

1. **Detección del sistema en producción, HOLDOUT, sin país** (Tablas 5.1-5.2): ROC-AUC del híbrido 0,75-0,80 en exfiltración (S2), 0,80 fuera de horario (S3) y 0,58-0,68 en toma de cuenta (S1). En nivel ≥ alto detecta entre el 12 % y el 30 % de los días atacados.
2. **Con país**, el piso de IsolationForest lleva el recall ≥ alto de S2 al 91-99 %: la detección operativa fuerte del sistema sale de la ubicación, no del comportamiento.
3. **Falsos positivos** en nivel ≥ alto: 4 % en los negativos HOLDOUT y 5 % en el período de test de IsolationForest; en crítico, prácticamente 0 (Tabla 5.3). No hay medida de FPR ante cambios de ubicación legítimos.
4. **Componentes:** IsolationForest solo ordena mejor que el híbrido donde detecta (S3 0,90, S2 k=10 0,88 en HOLDOUT); el LSTM queda cerca del azar sin país (0,56-0,63) y no usa el orden de los eventos.
5. **Nada de lo explorado se adoptó:** ni la recalibración de umbrales, ni otras agregaciones o combinaciones, ni quitar el decaimiento, ni los modelos v2 superaron al vigente de forma consistente sin romper la demo o la carga de alertas (§6).
6. **Reentrenamiento:** RF-21 pasa a un gate de no-inferioridad sobre DEV (AUC media primaria ≥ vigente − 0,02 y FPR ≥ alto ≤ vigente + 0,01). Demostrado con el vigente contra sí mismo (0,7726 / 0,0557, promueve) y contra v2 (rechaza por FPR 0,0734). Sigue sin ejercitarse con un modelo nuevo de Fase 1-6, y su precondición de corte temporal se rompe con ~28 usuario-días nuevos (§7).
