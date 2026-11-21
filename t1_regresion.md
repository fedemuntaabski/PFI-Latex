# T1. Regresión del puntaje (16/11)

## Qué estaba mal

`scripts/run_regression_test.py` probaba solo el camino v1 (forzaba `SCORING_TERCER_MODELO=lstm`) y fallaba con 6 diferencias, todas de `digital-harlequin-possum-procuratorfiscal` en días de cobertura parcial: de 0,055 a 4,47 puntos. Se reprodujo de nuevo el 16/11 con el script viejo: las mismas 6, en 25 min 39 s (`data/sandbox/20261116/t1/v1_antes.log`).

**Causa.** La falla no estaba en la API, estaba en el oráculo, y por dos motivos:
1. **Eventos duplicados en los datos procesados.** Hay 27 `id` repetidos entre archivos `clean_valid_*`: los 24 eventos de `digital-harlequin` (en `clean_valid_012` a `015` y otra vez en `017`) y 6 filas del primer día de `big-maroon-lynx-radiocontroller` (2017-07-07, en `001` y `017`). La API ve cada evento una vez; Fase 3 y Fase 6 los contaban dos veces. `scripts/benchmark/puntuar.py` tampoco deduplicaba por `id` al armar la población.
2. **Oráculo de otra época.** `ejemplos_decaimiento.csv` y `score_hibrido_final.csv` son del 02/09, de otros artefactos.

**Verificación de la causa.** Con los 24 eventos sin duplicar, el cálculo fuera de línea (ISO más decaimiento, con las funciones de producción) da exactamente lo que devuelve la API, por ejemplo 97.253711 y 9.213429. Duplicados, da otros valores.

## Qué se cambió

- `run_regression_test.py` se reescribió con `--camino iso|lstm`; `iso` es el default.
  - **Oráculo:** la simulación fuera de línea del mismo camino, `scripts/benchmark/puntuar.py`, la misma que da las métricas del benchmark y el gate, aplicada a los mismos eventos que recibe la API. Por día cerrado calcula el agregado, ISO (calibrado con historia en `iso`), el LSTM con la media acumulada de chunks (en `lstm`), el decaimiento, la novedad con el servicio real y la regla de ubicación.
  - **Online:** cada evento pasa por `POST /eventos`, con los tres usuarios intercalados en orden de tiempo, como en producción, porque el cuantil de novedad es poblacional. El último evento de cada día es el día cerrado.
  - **Mismos eventos:** se descartan los duplicados de contenido que `dedup_service` no procesa: 44 en `structural-teal` y 422 en `big-maroon`.
  - La línea base personal se apaga (`W_PERSONAL_MAX=0`), igual que antes, porque `puntuar.py` no la reproduce.
  - Compara cada usuario-día: puntaje y nivel. Salida en `reports/regresion/regresion_<camino>.csv` y `.json`.
- `puntuar.py` deduplica la población por `id`. Las métricas DEV no cambian: 2,66 % y 163 alertas con la configuración anterior. `digital-harlequin` no es de DEV, y el día duplicado de `big-maroon` (DEV) es de 2017, antes del corte, donde con una vida media de 3 días no influye en los días evaluados. Los artefactos de producción no se reentrenaron; el duplicado quedó en su train, que son 2 de 908 usuarios.
- Ya no se usan `ejemplos_decaimiento.csv` ni `score_hibrido_final.csv` como oráculo.

## Criterio (fijado antes de correr, `plan.md`)

0 diferencias de nivel y |Δ puntaje| ≤ 0,5 en `iso`, y ≤ 0,05 en `lstm`, en todos los usuario-días.

## Resultados

| Camino | Usuarios | Eventos | Usuario-días | Δ máx. | Diferencias de nivel | Resultado | Tiempo |
|---|---|---|---|---|---|---|---|
| `iso` (por defecto) | 3 | 67.066 | 1.923 | 0,0 | 0 | **pasa** | 22 min |
| `lstm` (v1) | 3 | 67.066 | 1.923 | 0,0 | 0 | **pasa** | 23 min |

Ambas corridas son del 16/11 con la configuración final (IF sin país, regla de ubicación y novedad informativa), después de la promoción de T4. `iso` también pasó con la configuración anterior, antes de promover. Salidas: `reports/regresion/regresion_{iso,lstm}.{csv,json}`; logs en `data/sandbox/20261116/t1/final_*.log`.

## Dónde corre

Corre en local, no en CI:
- necesita los artefactos de modelo, que no están versionados y el job `api` no tiene;
- tarda unos 22 minutos (`iso`) y 25 minutos (`lstm`), a unos 16–19 ms por evento con Redis en memoria.

Comando:

```bash
SCORING_API_KEY= SCORING_ADMIN_KEY= SUPABASE_DB_URL= python scripts/run_regression_test.py            # camino por defecto
SCORING_API_KEY= SCORING_ADMIN_KEY= SUPABASE_DB_URL= python scripts/run_regression_test.py --camino lstm
```

`SUPABASE_DB_URL=` vacía evita escribir en `eventos_crudos` real; cada evento deja un traceback de "SUPABASE_DB_URL no configurada" en el log, que es la escritura best-effort que se salta. Requisito previo: los eventos de los tres usuarios en `reports/score_hibrido/regresion_fase7/` (`scripts/extract_user_events.py`).

## Límite declarado

El oráculo comparte con la API las funciones de cálculo (agregado, `score_isoforest`, decaimiento, novedad). Esta regresión prueba la máquina de estados online contra el cálculo por lotes:
- el estado en Redis;
- el agregado parcial evento a evento;
- el anclaje del decaimiento;
- la historia de calibración;
- la deduplicación;
- el cuantil poblacional;
- la regla de ubicación.

No prueba esas funciones contra una implementación independiente. Eso lo cubre `puntuar.py` con su propio chequeo contra Fase 6 (`decision_function` por usuario-día: máx. |Δ| 7,3e-3 sobre todos los días, que viene de los días duplicados de 2017 a 2021; 5,6e-17 en los días DEV post-corte) y las pruebas de paridad de features.
