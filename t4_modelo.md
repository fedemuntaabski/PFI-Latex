# T4b, T4c y T4f. Cambios de modelo: qué se cambió primero

Decisión del autor (16/11): **medir y promover**. El criterio se escribió en `plan.md` antes de medir y las mediciones se hicieron en sandbox. Un cambio pasa al default solo si cumple el criterio, y después hay una sola corrida en HOLDOUT (T4f).

Todas las cifras son de CLUE DEV: 63 usuarios, 6.132 usuario-días reales posteriores al corte del 2021-08-02.

Con qué se calcula cada métrica:
- **FPR ≥ alto y p90 semanal:** las mismas funciones del gate (`metricas_service.metricas_benchmark` y `decidir`).
- **Etiquetas:** las congeladas y provisionales de `docs/etiquetado/` (17 usuario-días `merece_revision`, 14 de ellos con alerta del default anterior).
- **Puntuación:** `scripts/benchmark/puntuar.py`, deduplicado por `id` (ver T1).
- **Tabla:** `scripts/evidencia/t4_resumen.py`.

**Aviso de sobreajuste.** Las etiquetas se hicieron sobre DEV, así que elegir con ellas es optimista. Eso se compensa en parte con la corrida única en HOLDOUT (T4f).

## T4b. Detección de novedad

`scripts/evidencia/novedad_opciones.py`. Las opciones 1 y 2 parchean `novedad_service.actualizar` solo dentro del proceso de medición.

| Opción | FPR ≥ alto | p90 semanal | Alertas | Solo novedad | Merecían revisión con alerta (de 14) |
|---|---|---|---|---|---|
| 0. Vigente (cuantil móvil, FPR 0,05, eleva a alto) | 2,66 % | 4,95 % | 163 | 58 | 14 |
| 1. No cuenta lo que el usuario crea (`file_created`) | 2,89 % | 5,83 % | 177 | 72 | 14 |
| 2. Solo carpetas que ya existían en la población | 3,05 % | 5,83 % | 187 | 82 | 14 |
| 3. Cuantil con FPR 0,01 | 2,04 % | 4,81 % | 125 | 20 | 14 |
| **4. Informativa (sin elevar el nivel)** | **1,71 %** | **4,65 %** | **105** | **0** | **14** |

FPR ≥ crítico: 0,08 % en las cinco opciones.

**Lectura.**
- Las 14 alertas que merecían revisión vienen todas de ISO, así que ninguna opción de novedad las pierde.
- Las opciones 1 y 2 suben las alertas en vez de bajarlas. Al contar menos recursos "nuevos" por día, baja el cuantil móvil poblacional con el que se comparan, y más días lo superan. El umbral es relativo a la población, y sacar ruido del numerador también lo saca del umbral.

**Decisión, con la regla fijada antes de medir:**
1. Ninguna opción pierde alertas que merecían revisión.
2. La de menor FPR es la 4 (1,71 %), que le saca a la 3 (2,04 %) más que el umbral de empate de 0,002.
3. No es mayor que la vigente.

**Se promueve la opción 4.** En el camino por defecto (`iso`), `SCORING_DETECTOR_NOVEDAD` vacío pasa a valer `1`: la novedad sigue en la explicación y en la cola, pero no sube el nivel. El camino `markov` conserva `nivel` y v1 conserva `0`. Para volver al comportamiento anterior: `SCORING_DETECTOR_NOVEDAD=nivel`.

**Efecto en el dominio del agente:** ninguno medido. En la EC2 (Upstash), el cuantil de novedad tenía 7 de las 50 muestras mínimas y nunca elevó un nivel (devolución de los puntos 3 y 5).

## T4c. País fuera del modelo y regla explícita de ubicación

**Modelo.** `scripts/evidencia/iso_sin_pais.py` repite las celdas de Fase 4: features escaladas de Fase 3, corte fijo, 200 árboles, contamination 0,02 y random_state 42. La única diferencia es que en train `n_distinct_countries` se reemplaza por su moda (98,83 % de los días: en train la variable tiene 2 valores).

Un árbol de aislamiento nunca corta por una variable constante. En inferencia el modelo no la usa, sea cual sea el valor que llegue. El script lo verifica: multiplicar la variable por 7 en test no mueve ningún `decision_function`.

Con esto el scaler, las 8 columnas de la API y el contrato del evento no cambian. Cambian solo los artefactos del IF:
- `isolation_forest.joblib`, `isoforest_test_results.parquet`, `iso_train_reference.pkl` e `iso_calibracion.json`, regenerados con `fase6_sin_lstm.py`, `export_train_references.py --solo-iso` y `export_iso_calibracion.py`;
- `markov_reference.json` y `isoforest_risk_full.parquet`, que dependen del riesgo ISO.

**Control de la réplica:** el mismo script con la columna real (`--con-pais`) reproduce el modelo vigente con una diferencia de 0,0 en el `decision_function` de los 61.284 días.

**Regla** (`api/app/scoring/ubicacion_service.py`, camino `iso`):
- **Cuándo dispara:** con un país conocido que el usuario no usó en 90 días, si tiene al menos 3 días de historia o si ya tenía otro país conocido en la ventana (enmienda, ver `plan.md`).
- **Efecto:** fija el nivel mínimo `SCORING_PAIS_NUEVO_NIVEL` (default `critico`; `0` la apaga) por el resto del día.
- **Cómo se ve:** "ubicación nueva: XX" en la explicación y "Nivel minimo … por ubicacion nueva (XX), regla de ubicacion" en el motivo.
- **XAI:** la explicación deja afuera las variables que ningún árbol usa (`explainability.columnas_usadas`), así que el país ya no aparece como "variable desviada".
- **Simulación:** `puntuar.py` simula la misma regla, de modo que el gate la evalúa.

| Configuración (novedad informativa en todas) | FPR ≥ alto | p90 semanal | FPR crítico | Alertas | Merecían revisión con alerta |
|---|---|---|---|---|---|
| Vigente: IF con país, sin regla | 1,71 % | 4,65 % | 0,08 % | 105 | 14 de 14 |
| IF sin país, sin regla | 1,81 % | 5,19 % | 0,10 % | 111 | 14 de 14 |
| **IF sin país + regla (`critico`)** | **1,81 %** | **5,19 %** | **0,10 %** | **111** | **14 de 14** |

Entre el vigente y el candidato, 103 alertas coinciden, 2 quedan solo en el vigente y 8 solo en el candidato. La regla dispara en 36 usuario-días de DEV, todos anteriores al corte, y en ninguno de los evaluados. Es 0 %, debajo del 1 % fijado, así que el nivel mínimo queda en `critico`.

**Gate** (FPR ≤ vigente + 0,01 y p90 ≤ vigente + 0,01): 1,81 % ≤ 2,71 % y 5,19 % ≤ 5,65 %. **Pasa y se promueve.** Los artefactos anteriores quedan respaldados en `data/sandbox/20261116/respaldo_vigente/`. Cambiaron exactamente los 5 artefactos del IF y la referencia de Markov (SHA-256 antes y después en `data/sandbox/20261116/hash_*.txt`), más `isoforest_risk_full.parquet`.

**Demo.** Con el IF sin país, la exfiltración sola llega a ~57, medio (`demo/ensayos.md` §0). El crítico de la demo con VPN sale ahora de la regla, con el motivo visible en el panel, y no del modelo. La historia sembrada de Lucía manda `AR` (hace 38 a 52 días), así que solo dispara el `RU` del ataque. `test_e2e_pdp_pep.py` (guion de un solo día, AR y después RU) pasa con la regla enmendada.

**Reversión:** restaurar los archivos de `respaldo_vigente/` y poner `SCORING_PAIS_NUEVO_NIVEL=0`.

## T4f. Evaluación única del camino por defecto en HOLDOUT

Una sola corrida, sin iterar, del default final (IF sin país, regla de ubicación en `critico` y novedad informativa): `puntuar.py --holdout`, tag `t4f_final`. El uso quedó registrado en `data/benchmark/ampliado/manifest.json["holdout_usos"]` con el SHA-256 de la salida.

| Partición | Usuarios | Usuario-días | FPR ≥ alto | p90 semanal | FPR crítico | Alertas |
|---|---|---|---|---|---|---|
| DEV | 63 | 6.132 | 1,81 % | 5,19 % | 0,10 % | 111 |
| HOLDOUT | 60 | 5.912 | **1,05 %** | **2,48 %** | 0,03 % | 62 |

Criterio: si HOLDOUT superaba a DEV por más de 0,02, se declaraba como limitación. HOLDOUT queda por debajo de DEV, así que no hay limitación por sobreajuste a DEV.

Salvedad: la corrida es de la regla antes de la enmienda. En DEV, la enmienda no cambió nada.

Referencia histórica: v1 en HOLDOUT (08/10) daba FPR ≥ alto de 4 % en negativos.

## Resumen para la memoria (qué cambiaron primero)

1. La novedad pasó a ser informativa: −0,95 puntos de FPR ≥ alto en DEV, sin perder ninguna alerta que mereciera revisión.
2. El país salió del modelo y quedó como regla explícita y configurable: +0,10 puntos de FPR dentro del margen, con el crítico de la demo explicado.

Resultado: el camino por defecto pasa de 2,66 % a 1,81 % de FPR ≥ alto en DEV y da 1,05 % en HOLDOUT.

Siguen como trabajo futuro la variable de compartición (T4d) y el piloto de host (T4e).
