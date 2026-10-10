# 10b. Gate RF-21 y feature set versionado

Rama `e75/gate-rf21`. **Estado: sin mergear y sin pushear.** Falta una decisión del autor sobre la huella D1 (ver §2a).

## 1. Qué se trajo
- **Gate** (`bfa1e8a`, de `bae86d2` de x5): `metricas_service.py` (`evaluar_gate`, `comparar_y_promover(id, respaldo)`), `history_store.py`, `main.py` (sin `bootstrap_metricas_vigentes`), `reentrenamiento_scheduler.py`, migración `010`, `conftest.py`, `test_deploy_flags.py`, `test_reentrenamiento_backup.py`, `test_gate_promocion.py` (11 tests). El bundle `gate_rf21.bundle` no existe en esta PC; la fuente fue x5.
- **Feature set** (commit siguiente, de `05eb9a4` de x5), solo 10 archivos, 252 inserciones / 48 borrados: `features.py`, `hybrid_service.py`, `isoforest_service.py`, `lstm_service.py`, `explainability.py`, `drift_service.py`, `personal_baseline_service.py`, `redis_state.py` (solo `n_share_events` y deserializado genérico), `routes.py` (solo import y `feature_dict_desde(..., feature_set_de(...))`), `test_paridad_features_v2.py`. Aplicó limpio con `--3way`. No se tocó `artifacts.py`, `main.py`, scripts, notebooks ni artefactos.
- Sin `feature_set` en el config, todo es v1.

## 2. Equivalencia con v1
**a. Replay de 800 eventos.** El script del D1 no está en el repo (se perdió con el scratchpad del informe 10), así que lo reconstruí (2 uids de `clean_valid_001` por orden de aparición, 400 eventos, fechas corridas en días enteros, `POST /eventos` por TestClient). Salida: `risk_score_hibrido`, `nivel_sugerido`, `accion_id`, `cobertura`, `explicacion`.

| Árbol | MD5 | cobertura | niveles | score |
|---|---|---|---|---|
| base `e75/entrega` (`git archive`) | `cfccf513` | 687 completa / 113 parcial | bajo 19, medio 546, alto 215, crítico 20 | 8,99 a 91,54 |
| nuevo | `cfccf513` | igual | igual | igual |

Base y nuevo son idénticos byte a byte. **No coincide con `ac31d306` del D1**: cobertura (687/113), bajo (19), crítico (20) y rango (9,0 a 91,5) sí; medio/alto difieren (546/215 contra 538/223). La causa es que mi reconstrucción no es el script original (selección de eventos/mapeo de campos), no el código: el árbol base da lo mismo que el nuevo. Probé orden por tiempo, rol sin filtrar y país; el resultado no cambió. **Por regla del autor frené acá.**

**b. `ensayo_demo_pep.py`**: rc=0. Primer alto #15 (71,91), primer crítico #44 (90,03), máximo 91,14 (#46). Idéntico a `14_ensayo.md` §2.

**c. Suites** (entorno aislado):
- API completa: 350 passed.
- API como CI (`data/feature` renombrado, 4 `--ignore`): 326 passed, 15 skipped.
- Agente: 177 passed.
- Frontend: `oxlint` limpio, `tsc -b` rc=0, `npm run build` ok.
- `cobertura_local.ps1` exit 0: API 92 % de líneas (`metricas_service.py` 98,8 %), agente 88 %.

## 3. Humo del gate (`gate_promocion.py`, vigente copiado al scratchpad)
- **Vigente contra sí mismo: PROMUEVE.** ROC-AUC media 0,7726 (S2_k2 0,7408, S2_k5 0,7778, S2_k10 0,7811, S3 0,7906), FPR ≥ alto 0,0557, n_neg 6127, 62 víctimas. 332 s.
- **`artifacts_v2` contra vigente: RECHAZA por FPR.** AUC 0,8395 (ok), FPR 0,0734 contra máximo 0,0657 (NO). 353 s.

Salida del vigente: `"pasa": true, "motivo": "promueve: (a) AUC media primarios sin pais 0.7726 vs vigente 0.7726 (minimo 0.7526): ok; (b) FPR >=alto negativos DEV 0.0557 vs vigente 0.0557 (maximo 0.0657): ok"`.
Salida de v2: `"pasa": false, "motivo": "rechaza: (a) ... 0.8395 vs vigente 0.7726 (minimo 0.7526): ok; (b) FPR >=alto negativos DEV 0.0734 vs vigente 0.0557 (maximo 0.0657): NO"`.

## 4. Tesis §9.2.4 contra el código
| Condición de la tesis | Código | Estado |
|---|---|---|
| (a) AUC media en S2 k=2,5,10 y S3 sin país ≥ vigente − 0,02 | `PRIMARIOS`, `pais == "sin_pais"`, `MARGEN_AUC = 0.02`, `>=` | Coincide |
| (b) FPR en nivel ≥ alto sobre días limpios de DEV ≤ vigente + 0,01 | `NIVELES_ALTO = {alto, critico}`, negativos = `world_id == -1` de víctimas DEV, `MARGEN_FPR = 0.01`, `<=` | Coincide |
| HOLDOUT nunca participa | `puntuar.py` bloquea las 57 víctimas sin `--holdout` | Coincide |
| No promueve y registra el motivo si faltan escenarios | `precondicion`: falta `mundos.parquet`/`escenarios.parquet` | Coincide |
| ... si el corte no es el 2 de agosto de 2021 | primer día de test ≠ 2021-08-03 | Coincide |
| ... si el puntuado falla | `except` y `ok == False` | Coincide, y también si las métricas levantan |
| "unos 7,5 minutos" | medido 332 s y 353 s (5,5 y 5,9 min) | **Difiere**: x5 dice 7,4 min; en esta PC son ~5,7 min |

Otras notas: los márgenes no tienen calibración propia (lo dice el código). El gate puntúa el candidato contra el respaldo del scheduler, no contra un valor guardado. El log de `puntuar` muestra `chequeo ISO vs Fase6 ... max|diff| decision_function=2.18e-01`; es un chequeo informativo que ya existía.

## 5. Migración 010
Solo es aditiva y relajante: `ALTER COLUMN metrica_valor DROP NOT NULL`, `ALTER COLUMN cantidad_muestras DROP NOT NULL` y `ADD COLUMN IF NOT EXISTS rol/metricas/motivo`. Sin DROP de tabla ni columna, sin cambio de tipo, sin datos nuevos. Idempotente.

**El código viejo de la EC2 sigue funcionando después de correrla:**
- `write_metrica_modelo(modelo, valor, n, es_vigente)` inserta 4 columnas; las nuevas quedan en NULL.
- `get_metrica_vigente` y `marcar_metrica_no_vigente` filtran por `modelo` `'iso'`/`'lstm'`, así que no ven las filas `benchmark_dev`.
- `DROP NOT NULL` solo permite NULL; no rompe inserts que mandan valores.
- Sin correrla, el código nuevo falla best-effort al registrar (queda en el log) pero el gate decide igual.

Comando (no ejecutado):
```
psql "$SUPABASE_DB_URL" -f api/app/scoring/sql/010_metricas_modelo_gate_benchmark.sql
```

## 6. Merge y push
**No hechos.** Pendiente por §2a. `origin/e75/entrega` tiene 2 commits de docs adelante; el rebase sería limpio.