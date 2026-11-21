# Plan: devolución de la entrega del 90 % (código)

Fecha: 2026-11-16. Rama: `entrega/limpieza` (desde `f74fed8`). Fuente: `correcciones_devolucion_90_codigo.md` (raíz).

## Contexto: leer antes de empezar

- `correcciones_devolucion_90_codigo.md`: tareas T1–T8.
- `devolucion_puntos_3_y_5.md`: estado del 15/11 (548 pruebas, 95,29 % API, p95 13,40 ms).
- `docs/etiquetado/resultado_provisional.md` y `cruce.md`: etiquetas congeladas (`228b98c`).
- `api/app/scoring/metricas_service.py`: criterio de promoción (`decidir`, `precondicion`).
- `scripts/run_regression_test.py`, `scripts/fase6_sin_lstm.py`, `scripts/_score_common.py`.
- `LIMITACIONES_Y_ESTADO.md` §0.3 (CI) y `METRICAS_SISTEMA.md`.

## Decisiones del autor (16/11, antes de empezar)

1. T4b/T4c: **medir y promover**. Se fija el criterio por escrito (abajo), se mide en `data/sandbox/20261116/`, se cambia el default solo si pasa, y después hay **una** corrida en HOLDOUT (T4f).
2. T4a: la planilla del analista no volvió, así que se cita como **provisional**.
3. T7 (EC2): al llegar a ese punto se le pide al autor `! aws login`. Se prende la instancia, se verifica y se apaga con `apagar.ps1`.
4. T8: la herramienta de seguimiento fue **solo git**.

## Reglas duras

- Commit y push después de cada avance importante, sin trailers ni menciones de Claude.
- No se usa HOLDOUT para elegir. El criterio se escribe antes de medir. Ninguna métrica sale de datos sintéticos o inyectados.
- SHA-256 de los artefactos de producción (`models/`, `scripts/models/`, `artifacts_v2/`) antes y después de cada experimento. Solo una promoción decidida puede cambiarlos.
- No se tocan las etiquetas congeladas.
- Toda instancia EC2 que se prenda se apaga al terminar.
- Si aparecen diferencias en una prueba, se busca y se corrige la causa; nunca se ajusta la tolerancia para que pase.
- Timer de revisión cada 20 min hasta el cierre.

## Criterios fijados antes de medir

**T1(b), regresión del camino por defecto.** Mismo historial de tres usuarios con `SCORING_TERCER_MODELO` sin setear y `W_PERSONAL_MAX=0`. Para cada usuario-día cerrado: 0 diferencias de nivel y |Δpuntaje| ≤ 0,5 frente a la simulación fuera de línea del camino por defecto.

**T1(a), regresión v1.** Con el oráculo regenerado: 0 diferencias con la tolerancia que ya tiene el script. Si queda alguna, tiene que tener una causa escrita.

**T4b, novedad.** Se miden en DEV las opciones 0 (actual) a 4: FPR ≥ alto, días al cierre, alertas de solo-novedad y cuántas de las 14 alertas que merecían revisión se conservan.
Regla de elección:
1. Descartar las opciones que pierdan alguna de las alertas que merecían revisión respecto de la opción 0.
2. Entre las que quedan, elegir la de menor FPR ≥ alto.
3. Ante un empate (diferencia < 0,002), elegir la de menos código, en este orden: 4, 3, 1, 2.
4. Solo se promueve si la FPR ≥ alto no es mayor que la de la opción 0.

Aviso: las etiquetas se hicieron sobre DEV, así que la elección es optimista y se declara así.

**T4c, país.** IF reentrenado sin `n_distinct_countries` (pipeline de Fase 4, corte fijo 2021-08-02). Se promueve si la FPR ≥ alto en DEV es como mucho 0,01 mayor que la vigente (la parte de no inferioridad del criterio de promoción). La parte de AUC del criterio usa escenarios inyectados y no se usa (regla de datos reales).
Además hacen falta dos cosas: la regla de ubicación probada y la demo llegando a crítico por un motivo explicado.

**T4c, regla de ubicación** (agregado el 16/11, antes de medirla). Se dispara con un país conocido (no `unknown`) que el usuario no usó en los últimos 90 días, solo si el usuario ya tiene al menos 3 días de historia. El nivel mínimo se configura con `SCORING_PAIS_NUEVO_NIVEL`.
- Default: `critico`, que es lo que hoy produce el modelo en la demo, pero ahora explícito y explicado.
- Si en DEV la regla se dispara en más del 1 % de los usuario-días post-corte, el default pasa a `alto`.
- La variable de país sale de la explicación (XAI) cuando el modelo no la usa.

**Enmienda a la regla (16/11, después de medir y de la corrida en HOLDOUT).** La regla con la condición "≥ 3 días de historia" pasó el gate, pero no cumplió el "hecho cuando" de la demo: `test_e2e_pdp_pep` es un guion de un solo día (AR y después RU) y no llegó a crítico. Se amplió a "≥ 3 días de historia **o** otro país conocido en la ventana" (cambio de país), y el primer país de un uid nuevo sigue sin disparar. DEV vuelto a medir: idéntico (36 usuario-días, 0 post-corte, FPR 1,81 %). HOLDOUT no se volvió a correr: su cifra corresponde a la regla anterior, y así se declara.

Corrección al criterio de T4c: el gate vigente (`metricas_service.decidir`) no usa AUC. Usa la FPR ≥ alto y su p90 semanal, cada una con un margen de 0,01, y se aplican los dos.

**T4f, HOLDOUT.** Una sola corrida del default final; se reporta la FPR ≥ alto y los días al cierre. Si la FPR de HOLDOUT supera a la de DEV en más de 0,02, se declara como limitación. No se itera.

## Orden

| Paso | Tarea | Salida |
|---|---|---|
| 1 | T6: diagnóstico del CI (`hello.yml` en una rama aparte, políticas de actions, la corrida en cola) | `docs/devolucion_90/t6_ci.md` |
| 2 | T1 (a) y (b) | `reports/regresion/`, `docs/devolucion_90/t1_regresion.md` |
| 3 | T2: vitest en el frontend | `frontend/src/**/*.test.ts(x)`, ci.yml |
| 4 | T3: `icacls` real | `agent/tests/test_enforcement_icacls_real.py` |
| 5 | T5: tabla de datasets y perfilado | `docs/data/relevamiento_datasets.md`, `reports/perfilado_clue/` |
| 6 | T4b y T4c, luego T4f | `docs/devolucion_90/t4_modelo.md` |
| 7 | T4a (decisión provisional), T4e (protocolo del piloto), T4d (trabajo futuro) | `docs/devolucion_90/t4_*.md` |
| 8 | T7: conteos de pruebas omitidas, cobertura, latencia y EC2 | `docs/devolucion_90/t7_cifras.md` |
| 9 | T8: cronograma a partir de git | `docs/devolucion_90/t8_metodologia.md` |
| 10 | Cierre: `METRICAS_SISTEMA.md`, `LIMITACIONES_Y_ESTADO.md`, devolución para el LaTeX | `docs/devolucion_90/devolucion_latex.md` |

## Avance

| Tarea | Estado | Dónde |
|---|---|---|
| T1 | `iso` y `lstm`: 0 diferencias con la configuración final | `t1_regresion.md` |
| T2 | 35 pruebas, 34,92 % de líneas, job de CI | `frontend/src/**/*.test.*` |
| T3 | 3 pruebas con `icacls` real, en verde en esta PC (sin elevar: `/remove:d`) | `agent/tests/test_enforcement_icacls_real.py` |
| T4a | Se cita como provisional | `t4ade_etiquetado_y_piloto.md` |
| T4b | Opción 4 (informativa) promovida | `t4_modelo.md` |
| T4c | IF sin país + regla de ubicación, promovidos (enmienda documentada) | `t4_modelo.md` |
| T4d | Trabajo futuro | `t4ade_etiquetado_y_piloto.md` |
| T4e | Protocolo del piloto escrito | `t4ade_etiquetado_y_piloto.md` |
| T4f | HOLDOUT 1,05 % (una corrida) | `t4_modelo.md` |
| T5 | Tabla y perfilado | `docs/data/relevamiento_datasets.md`, `reports/perfilado_clue/` |
| T6 | Diagnóstico: falla de cuenta o repo, pendiente del autor | `t6_ci.md` |
| T7 | Omitidas, cobertura, archivos, latencia (p95 13,51 ms) y EC2 (release 20261116 verificada, apagada) | `devolucion_latex.md` |
| T8 | Cronograma desde git | `t8_metodologia.md` |
| Cierre | `docs/contexto/{estado_modelos,limitaciones,testing}.md` actualizados (sucesores de METRICAS_SISTEMA y LIMITACIONES_Y_ESTADO) | — |
