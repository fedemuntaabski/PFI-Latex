# Verificación de la evaluación controlada para LaTeX (2026-10-19)

Rama `analysis/metricas-clasificacion`, base a2a6f41. Subconjunto `sin_insample_v1` (32 víctimas DEV). Decimales con coma, listo para pegar en LaTeX.

## Comandos ejecutados

```
python scripts/benchmark/generar_controlados.py
python scripts/benchmark/puntuar.py --run controlado --tag vigente
python scripts/benchmark/clasificacion.py --run controlado
SUPABASE_DB_URL= python -m pytest api/tests/test_clasificacion_benchmark.py
```

## Verificaciones

- `integridad_vigente.json`: `iguales: true` (los 9 artefactos, SHA-256 antes = después).
- Reproducibilidad: `confusion_vigente.csv` sale byte a byte igual al re-correr (SHA-256 `7858a25311fca30f…ef17e415`, semilla 42, n_boot 300).
- pytest `test_clasificacion_benchmark.py`: 18 passed.
- Contra `evaluacion_controlada_latex_20261019.md`: TP/FP/TN/FN de ISO y híbrido coinciden con las filas verificadas (ISO TODOS 15/21/3572/639; híbrido TODOS 65/151/3442/589; híbrido S5 57/151/3442/291). Sin discrepancias en lo comparado.
- Chequeo ISO vs Fase6 (log de puntuar): 61284/61284 días cruzados; LSTM vs Fase5: 36 uids, diff relativa 0.

## Matriz de confusión y métricas (S4, S5, TODOS)

| Modelo | Unidad | Escenario | TP | FP | TN | FN | Precision | Recall | F1 | Especif. | Acc. | Bal. acc. | ROC-AUC [IC95%] | PR-AUC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IsolationForest | usuario-dia | TODOS | 15 | 21 | 3572 | 639 | 0,417 | 0,023 | 0,043 | 0,994 | 0,845 | 0,509 | 0,56 [0,50; 0,61] | 0,206 |
| IsolationForest | usuario-dia | S4\_secuencia | 1 | 21 | 3452 | 305 | 0,045 | 0,003 | 0,006 | 0,994 | 0,914 | 0,499 | 0,49 [0,43; 0,55] | 0,079 |
| IsolationForest | usuario-dia | S5\_pico\_corto | 14 | 21 | 3572 | 334 | 0,400 | 0,040 | 0,073 | 0,994 | 0,910 | 0,517 | 0,62 [0,56; 0,69] | 0,172 |
| LSTM (usuario-día) | usuario-dia | TODOS | 1 | 0 | 3593 | 653 | 1,000 | 0,002 | 0,003 | 1,000 | 0,846 | 0,501 | 0,54 [0,47; 0,60] | 0,184 |
| LSTM (usuario-día) | usuario-dia | S4\_secuencia | 0 | 0 | 3473 | 306 | n/d | 0,000 | 0,000 | 1,000 | 0,919 | 0,500 | 0,53 [0,45; 0,60] | 0,106 |
| LSTM (usuario-día) | usuario-dia | S5\_pico\_corto | 1 | 0 | 3593 | 347 | 1,000 | 0,003 | 0,006 | 1,000 | 0,912 | 0,501 | 0,55 [0,47; 0,62] | 0,117 |
| Híbrido | usuario-dia | TODOS | 65 | 151 | 3442 | 589 | 0,301 | 0,099 | 0,149 | 0,958 | 0,826 | 0,529 | 0,57 [0,52; 0,62] | 0,196 |
| Híbrido | usuario-dia | S4\_secuencia | 8 | 76 | 3397 | 298 | 0,095 | 0,026 | 0,041 | 0,978 | 0,901 | 0,502 | 0,52 [0,46; 0,57] | 0,088 |
| Híbrido | usuario-dia | S5\_pico\_corto | 57 | 151 | 3442 | 291 | 0,274 | 0,164 | 0,205 | 0,958 | 0,888 | 0,561 | 0,64 [0,58; 0,70] | 0,149 |
| Híbrido + decay | usuario-dia | TODOS | 46 | 121 | 3472 | 608 | 0,275 | 0,070 | 0,112 | 0,966 | 0,828 | 0,518 | 0,56 [0,51; 0,63] | 0,191 |
| Híbrido + decay | usuario-dia | S4\_secuencia | 2 | 36 | 3437 | 304 | 0,053 | 0,007 | 0,012 | 0,990 | 0,910 | 0,498 | 0,51 [0,46; 0,58] | 0,086 |
| Híbrido + decay | usuario-dia | S5\_pico\_corto | 44 | 121 | 3472 | 304 | 0,267 | 0,126 | 0,172 | 0,966 | 0,892 | 0,546 | 0,62 [0,56; 0,69] | 0,146 |
| LSTM (chunk, exploratorio) | chunk-50-eventos | TODOS | 74 | 319 | 12288 | 1659 | 0,188 | 0,043 | 0,070 | 0,975 | 0,862 | 0,509 | 0,68 [0,57; 0,77] | 0,180 |
| LSTM (chunk, exploratorio) | chunk-50-eventos | S4\_secuencia | 29 | 308 | 12238 | 806 | 0,086 | 0,035 | 0,049 | 0,975 | 0,917 | 0,505 | 0,62 [0,51; 0,76] | 0,083 |
| LSTM (chunk, exploratorio) | chunk-50-eventos | S5\_pico\_corto | 45 | 319 | 12288 | 853 | 0,124 | 0,050 | 0,071 | 0,975 | 0,913 | 0,512 | 0,73 [0,60; 0,81] | 0,119 |

IC bootstrap por víctima (300 réplicas) de las demás métricas: columnas `*_lo`/`*_hi` de `confusion_vigente.csv`. `lstm_seq` no es comparable con las matrices usuario-día.

## Controles negativos S6 (identidad) y S7 (benigno)

Sin positivos: solo FP/TN y especificidad.

| Modelo | Escenario | FP | TN | Especificidad |
|---|---|---|---|---|
| IsolationForest | S6\_control\_identidad | 1 | 347 | 0,997 |
| IsolationForest | S7\_control\_benigno | 2 | 356 | 0,994 |
| LSTM (usuario-día) | S6\_control\_identidad | 0 | 348 | 1,000 |
| LSTM (usuario-día) | S7\_control\_benigno | 0 | 358 | 1,000 |
| Híbrido | S6\_control\_identidad | 26 | 322 | 0,925 |
| Híbrido | S7\_control\_benigno | 29 | 329 | 0,919 |
| Híbrido + decay | S6\_control\_identidad | 22 | 326 | 0,937 |
| Híbrido + decay | S7\_control\_benigno | 19 | 339 | 0,947 |

## Avisos

- Los números de HOLDOUT del cap. 10 salen del run `ampliado`, no se regeneran acá.
- `data/benchmark/` está gitignorado.
