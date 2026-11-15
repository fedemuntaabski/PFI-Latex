# Respuestas para la memoria LaTeX

Relevamiento sobre el repositorio de código `G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad`, rama `entrega/limpieza`, *commit* `0f53d62` ("testing.md: cobertura y conteos re-medidos (2026-11-14)"). Fecha: 15/11/2026.

Condiciones comunes de las corridas locales: Windows 10 Pro, Python 3.12.3 (`.venv`), entorno aislado igual al de `scripts/cobertura_local.ps1` (sin Postgres, Redis en memoria `SCORING_FAKE_REDIS=1`, sin SMTP, sin servicio externo de redacción, `IAM_PROVIDER=none`). La integración continua usa Python 3.11 (`.github/workflows/ci.yml:49`).

---

## A. Pruebas y cobertura (`chapters/pruebas.tex`, 10.2)

### P1

- **Dato:** API: 547 pruebas en 54 archivos `test_*.py`. Agente: 200 pruebas en 16 archivos `test_*.py`. Las 547 y 200 de la memoria **coinciden**; los 44 y 15 archivos **no**: son 54 y 16.
- **Fuente:** `python -m pytest --collect-only -q -p no:cacheprovider api/tests` → "547 tests collected"; ídem `agent/tests` → "200 tests collected" (15/11/2026 07:52). Archivos: conteo de `test_*.py` en `api/tests` y `agent/tests` y de archivos distintos en la salida de `--collect-only` (54 y 16, todos con al menos una prueba).
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.2 (inventario de suites).
- **Estado:** OBTENIDO.
- **Texto sugerido:** La suite de la API reúne 547 pruebas en 54 archivos y la del agente, 200 pruebas en 16 archivos.

### P2

- **Dato:** Columna "Sentencias": API **3 287**, agente **1 124**, total **4 411** (la memoria dice 2 808, 1 107 y 3 915: no coinciden). Porcentajes sin cambio respecto de la referencia:

  | Componente | Sentencias | Sin cubrir | Ramas | % líneas | % líneas + ramas |
  |---|---|---|---|---|---|
  | API | 3 287 | 156 | 768 | 95,25 | 93,86 |
  | Agente | 1 124 | 91 | 296 | 91,90 | 91,20 |
  | Total | 4 411 | 247 | 1 064 | 94,40 | 93,17 |

  Resultado de las suites en esa corrida: API 547 aprobadas; agente 200 aprobadas; 0 omitidas, 0 fallidas.
- **Fuente:** `powershell -ExecutionPolicy Bypass -File scripts/cobertura_local.ps1` (15/11/2026 07:51–07:53, salida 0); `reports/cobertura/{api,agente}/coverage.json` → `totals` (`num_statements`, `missing_lines`, `num_branches`, `covered_branches`). Total = suma de ambos JSON: líneas (4 411 − 247) / 4 411 = 94,40 %; combinado (4 164 + 937) / (4 411 + 1 064) = 93,17 %.
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.2, tabla de cobertura.
- **Estado:** OBTENIDO.

### P3

- **Dato:** Configuración de integración continua emulada (copia limpia de `HEAD` sin artefactos de modelo, mismos cuatro `--ignore` del *workflow*): **508 aprobadas, 30 omitidas, 0 fallidas**. Desglose de las 30 omitidas:

  | Cant. | Motivo (texto del `skip`) | Archivos |
  |---|---|---|
  | 14 | faltan artefactos de modelo no versionados (`ARTIFACT_PATHS`) | `test_cu04_aprendizaje.py` (5), `test_iam_eventos.py` (4), `test_e2e_pdp_pep.py` (2), `test_score_confirmacion.py` (2), `test_eventos_recientes_explicacion.py` (1) |
  | 9 | sin artefactos de modelo | `test_markov_service.py` (3), `test_novedad_service.py` (3), `test_umbral_movil_service.py` (2), `test_sin_lstm.py` (1) |
  | 2 | ejercita *scoring* real (`POST /eventos`): necesita artefactos de modelo | `test_config_auth_y_validacion.py` (1), `test_config_umbrales_put.py` (1) |
  | 3 | sin `artifacts_v2/` o `data/processed/` | `test_paridad_features_v2.py` (3) |
  | 2 | sin `markov_reference.json` de *sandbox* (`export_markov_reference.py`) | `test_markov_service.py` (2) |

  Agrupado con el criterio de la memoria: **25 requieren los modelos entrenados** (14 + 9 + 2), **3 requieren los datos procesados de la versión 2** (`artifacts_v2/` o `data/processed/`) y **2 requieren la referencia de Markov de una corrida en *sandbox***. Los cuatro archivos excluidos con `--ignore` no cuentan como omitidos.
- **Fuente:** en `git archive HEAD` extraído fuera del repo: `SCORING_FAKE_REDIS=1 python -m pytest api/tests -q -rs --tb=short -p no:cacheprovider --ignore=api/tests/test_health_ready.py --ignore=api/tests/test_historial_scores_explicacion.py --ignore=api/tests/test_hybrid_service_backdated.py --ignore=api/tests/test_reload_artifacts_endpoint.py --cov --cov-report=` (15/11/2026 07:55) → "508 passed, 30 skipped, 15 warnings in 46.60s". Comando igual al de `.github/workflows/ci.yml:74-82` más `-q -rs`.
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.2 (párrafo de la configuración de integración continua).
- **Estado:** OBTENIDO.
- **Texto sugerido:** De las 30 pruebas omitidas, 25 requieren los modelos entrenados, 3 los datos procesados de la versión 2 y 2 la referencia de Markov de una corrida en *sandbox*.

### P4

- **Dato:** Cobertura de la API en la configuración de integración continua (sin artefactos): **87,65 % de líneas** (3 287 sentencias, 406 sin cubrir) y **85,70 % combinada** (líneas + ramas; 768 ramas, 594 cubiertas). El umbral del *workflow* es 85 % combinado (`coverage report --fail-under=85`). Medido con Python 3.12; el CI usa 3.11 y el propio *workflow* prevé una diferencia de hasta 2 puntos (`ci.yml:72-73`).
- **Fuente:** misma corrida que P3; `python -m coverage json --include="api/app/*,scripts/_score_common.py,scripts/_audit_common.py"` → `totals.percent_statements_covered` = 87,65; `totals.percent_covered` = 85,70 (15/11/2026).
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.2.
- **Estado:** OBTENIDO (local; la cifra del CI real queda en P5).
- **Texto sugerido:** Sin los artefactos de modelo, la cobertura de la API baja a 87,65 % de líneas y 85,70 % combinada, por encima del umbral de 85 % que aplica la integración continua.

### P5

- **Dato:**
  - **Últimas corridas por rama** (`gh run list --limit 40`, 15/11/2026): `entrega/limpieza` — 5 corridas por *push* entre 15/11/2026 01:03 y 01:32 UTC, todas `startup_failure` (la última: 43663580828, *commit* `0f53d62`); `pre-limpieza-entrega` — 1 corrida, 15/11/2026 00:35 UTC, `startup_failure`; `analysis/etiquetado-clue` — 24 corridas del 11/11 al 14/11/2026, todas `startup_failure`; `demo/aws-video3` — 3 corridas el 09/11/2026, `startup_failure`; `analysis/datos-reales` — 3 corridas el 08/11/2026 (desde `5c36b9d`), `startup_failure`.
  - **Última corrida exitosa:** 41839628959, rama `analysis/datos-reales`, *commit* `9cc967a`, **04/11/2026 13:36 UTC**, con los cuatro trabajos en `success` (`frontend`, `api`, `agent-windows`, `infra`). URL: https://github.com/fedemuntaabski/Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad/actions/runs/41839628959. La primera falla es del 08/11/2026 20:58 UTC (42522781777).
  - **Error exacto de `startup_failure`:** `gh run view 43663580828` informa "This run likely failed because of a workflow file issue." La API de GitHub devuelve para esa corrida `"conclusion":"startup_failure"`, `"path":"BuildFailed"`, `"name":""` y **0 trabajos** (no llegó a crearse ningún *job*); ninguna *check run* asociada al *commit*.
  - **Causa: no es el archivo.** (a) `git diff 9cc967a 0f53d62 -- .github/` no muestra cambios: el `ci.yml` es el mismo que corrió bien el 04/11; (b) la falla aparece a la vez en cinco ramas con contenidos distintos; (c) re-ejecución autorizada por el autor: `gh run rerun 43663580828` → "This workflow run cannot be retried"; luego `gh workflow run ci.yml --ref entrega/limpieza` (15/11/2026 10:55:40 UTC) → corrida **43706419315**, que GitHub sí interpreta (`"name":"CI"`, `"path":".github/workflows/ci.yml"`) y aun así termina en `startup_failure` con **0 trabajos**. URL: https://github.com/fedemuntaabski/Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad/actions/runs/43706419315.
  - **Configuración verificada:** Actions habilitado en el repositorio (`"enabled":true,"allowed_actions":"all"`); el repositorio es **privado**; los permisos del *workflow* son `contents: read` (`ci.yml:13-14`) y no cambiaron. Con un repositorio privado, un trabajo que no llega a arrancar en todas las ramas a la vez apunta a la cuenta (minutos incluidos agotados, límite de gasto o pago pendiente).
  - **Facturación de Actions: descartada como causa.** Con el token ampliado por el autor (`gh auth refresh -s user`, 15/11/2026), `gh api users/<usuario>/settings/billing/usage/summary` da: **septiembre** 36 min Linux; **octubre** 1 117 min Linux + 242 min Windows (1 601 minutos equivalentes con el multiplicador 2 de Windows, por debajo de los 2 000 incluidos por mes); **noviembre** 4 min Linux + 1 min Windows (de la corrida exitosa del 04/11) y 33,65 GB-hora de almacenamiento. Todo con `netAmount = 0`: no hay cargos ni consumo excedido. El endpoint de presupuestos (`settings/billing/budgets`) responde 404.
  - **Causa: no identificada.** Quedan descartados el archivo (sin cambios), los permisos del repositorio (Actions habilitado, todas las *actions* permitidas) y la cuota de minutos. La API solo informa `startup_failure` con 0 trabajos y ningún mensaje; la anotación que explica el fallo solo se ve en la interfaz web (sin navegador conectado en esta sesión).
  - **Aislar si es la cuenta o el repositorio: no se puede.** Ningún otro repositorio de la cuenta tiene corridas recientes con las que comparar: el único con historial es `Quest`, con la última del 11/05/2026 (`gh api repos/<cuenta>/<repo>/actions/runs`, 15/11/2026).
  - **Resultado de los cuatro trabajos tras re-ejecutar:** no hay. La corrida 43706419315 terminó en `startup_failure` con 0 trabajos. El autor la re-ejecutó desde la interfaz web el 15/11/2026 a las 11:44:59 UTC; a las 12:13 UTC seguía `queued`, con **0 trabajos creados** (`gh api …/runs/43706419315/jobs` → `total_count: 0`). La página web solo lista los cuatro nombres del `ci.yml` (`agent-windows`, `api`, `frontend`, `infra`) sin ejecución. GitHub no llega a asignar trabajos a este repositorio: es el mismo síntoma que el `startup_failure`.- **Fuente:** `gh run list`, `gh run view 43663580828`, `gh api repos/<repo>/actions/runs/{43663580828,43706419315,41839628959}` y `/jobs`, `gh api repos/<repo>/actions/permissions`, `gh api repos/<repo>/commits/0f53d62/check-suites` (15/11/2026 10:50–10:57 UTC).
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.2 (integración continua).
- **Estado:** PARCIAL. La falla está confirmada y quedan descartados el archivo, los permisos y la facturación. La causa no está identificada: GitHub no la informa ni por la API ni en la interfaz web. El autor la consulta con el soporte de GitHub (decisión del autor, 15/11/2026). Mientras tanto, la memoria puede citar como evidencia de la integración continua la última corrida completa (04/11/2026, cuatro trabajos aprobados).
- **Texto sugerido:** La última corrida completa de la integración continua, del 4 de noviembre de 2026, aprobó los cuatro trabajos. Desde el 8 de noviembre las corridas no llegan a iniciar trabajos en ninguna rama, sin cambios en el *workflow* ni consumo excedido.

### P6

- **Dato:** El guion sigue teniendo **46 eventos: 9 de calentamiento** (1 `session_started` + 4 × (`file_written`, `process_started`)), **31 de exfiltración** (1 `process_started` que arranca `demo_exfil` + 5 ciclos × 6 tipos) y **6 desde un país simulado** (1 ciclo × 6 tipos, país `RU`, IP no local). La prueba exige `len(res.filas) == 46`.
  - **Modelo que produce el puntaje en la prueba automatizada:** `api/tests/conftest.py:17` fija `SCORING_TERCER_MODELO=lstm` para toda la suite y `test_e2e_pdp_pep.py` no lo cambia: la prueba corre el **camino de la versión 1** (Isolation Forest + LSTM). Con 46 eventos no se completa una ventana del LSTM (límite 50, `scripts/ensayo_demo_pep.py:70`), así que el puntaje es Isolation Forest puro.
  - **Con el camino por defecto** (`CAMINO_DEFAULT = "iso"`, `api/app/scoring/markov_service.py:46`: Isolation Forest + novedad de recurso, sin Markov ni LSTM) el mismo guion da **el mismo resultado**: primer `alto` en el evento 15, primer `critico` en el 44 (puntaje 90,03; acción `terminar_y_denegar`, efectos `terminar` + `denegar`), 3 confirmaciones del agente, la última `terminar_y_denegar / ejecutado`. Con `lstm` se obtuvieron los mismos hitos y puntajes.
- **Fuente:** `scripts/ensayo_demo_pep.py:67-69,139-148,160-161`; `api/tests/test_e2e_pdp_pep.py:55-61`; `api/tests/conftest.py:6-8,17`. Corridas: `python scripts/ensayo_demo_pep.py` en entorno aislado con `SCORING_TERCER_MODELO=iso` y con `=lstm` (15/11/2026 07:57) → "OK: captura -> decision -> accion -> confirmacion (ciclo PDP->PEP cerrado)" en ambos.
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.3.
- **Estado:** OBTENIDO.
- **Texto sugerido:** La prueba automatizada recorre 46 eventos (9 de calentamiento, 31 de exfiltración y 6 desde un país simulado). Se ejecuta con el camino de la versión 1, pero como no alcanza una ventana completa del LSTM el puntaje lo produce el Isolation Forest; con el camino por defecto el guion llega al nivel crítico en el mismo evento, el 44.

---

## B. Rendimiento y despliegue (`chapters/pruebas.tex`, 10.4)

### P7

- **Dato:** RNF-01 con el camino por defecto (`iso`), mismo *script* y procedimiento (1 000 eventos medidos, 50 de calentamiento, 5 usuarios, semilla 42, Redis en memoria, sin base de datos, HTTP real a 127.0.0.1):

  | Métrica | Camino por defecto (15/11/2026) | Versión 1, referencia (`bench_rnf01_resultado.json`) |
  |---|---|---|
  | Media | 12,83 ms | 16,96 ms |
  | Mediana | 12,59 ms | 13,35 ms |
  | p95 | 13,71 ms | 14,91 ms |
  | p99 | 18,24 ms | 148,87 ms |
  | Máximo | 55,28 ms | 880,26 ms |
  | Mínimo | 11,67 ms | 12,22 ms |
  | Errores | 0 de 1 000 | 0 de 1 000 |
  | Eventos por segundo | 78 | 59 |
  | Tiempo interno de la API (últimas 100) | 10,21 ms media, 10,64 ms p95 | 18,2 ms media, 16,09 ms p95 |

  **Colas altas:** el *health* de la corrida muestra que no se carga ni el LSTM ni su *scaler* (`detalle` solo con `isolation_forest`, `scaler_isoforest`, `type_encoding`, `config_score_hibrido`, `train_references`). Los cinco eventos más lentos (55,3; 30,6; 25,8; 20,9 y 20,7 ms) son aislados, de tipos distintos (`file_written`, `app_disabled`, `logout_occured`) y no forman rachas; en la versión 1 aparecían en grupos consecutivos (eventos 446 a 448, de 168 a 177 ms) y un pico de 880 ms. El *script* no desglosa el tiempo por componente, así que **no hay una causa identificable** de los picos actuales; la que se atribuía al LSTM ya no aplica porque el modelo no se carga.
- **Fuente:** `python scripts/evidencia/bench_rnf01_latencia.py --n 1000 --warmup 50 --uids 5 --out <temporal>` en entorno aislado con `SCORING_TERCER_MODELO=iso` (15/11/2026 07:57:20–07:57:37, salida 0). Referencia: `scripts/evidencia/bench_rnf01_resultado.json` (versionado, *commit* `60350b5` del 14/11/2026). Condiciones: Windows 10 Pro, Python 3.12.3, Intel 12 núcleos lógicos, 15,9 GB.
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.4 (RNF-01).
- **Estado:** OBTENIDO.
- **Texto sugerido:** Con el camino por defecto, la latencia media de `POST /eventos` en local es de 12,83 ms, con p95 de 13,71 ms y p99 de 18,24 ms, sin errores en 1 000 eventos. Sin el LSTM desaparecen las rachas de más de 100 ms que se observaban en la versión 1.

### P8

- **Dato:** Release vigente en la instancia (`i-0b2a6179e41985b60`, `us-east-2`): **`20261114-221354-3634c38`**, *commit* **`3634c38cc2fe584c5cc7ec93fe7f7a0bff6cd238`** ("GET /usuarios: SCAN con count=1000 y estados en un solo MGET"), empaquetada el 15/11/2026 01:13:55 UTC (14/11/2026 22:13 ART). Es la misma que registra `demo/README.md:5`. La anterior instalada es `20261108-175917-5c36b9d`. Verificaciones de 10.4.3 sobre esa release (15/11/2026, autorizadas por el autor):

  | Verificación | Resultado |
  |---|---|
  | Versión de Python | **3.11.16** (`/opt/scoring/venv/bin/python --version`) |
  | Camino de *scoring* | `SCORING_TERCER_MODELO` no definida en `/etc/scoring/{config,api,keycloak}.env` → `iso` (Isolation Forest + novedad de recurso) |
  | Artefactos que carga el camino por defecto | `isolation_forest`, `scaler_isoforest`, `type_encoding`, `config_score_hibrido`, `train_references` (`GET /health` → `detalle`); el LSTM y su *scaler* viajan en la release pero no se cargan |
  | SHA-256 contra el local | **Coinciden los 6** del camino por defecto: `scripts/models/isolation_forest.joblib` `8de93898…dac470`, `data/feature/scaler_isoforest.pkl` `63169851…0a7607`, `data/feature/type_encoding.pkl` `c88416d5…af1141`, `models/score_hibrido/config_score_hibrido.json` `ddd6e60e…ea687f0e`, `iso_calibracion.json` `3c45f0e2…b6bd08`*, `iso_train_reference.pkl` `95d41f57…671a90de`. También coinciden los del LSTM (`lstm_autoencoder.keras`, `lstm_threshold.pkl`, `scaler_lstm.pkl`, `lstm_user_mean_error_train_reference.pkl`) |
  | Certificado TLS | Válido, Let's Encrypt (emisor `CN=YE2`), sujeto `CN=3-147-149-208.sslip.io`, vigente del 06/10/2026 al 04/01/2027, TLS 1.2 desde el cliente Windows |
  | Redirección HTTP→HTTPS | `GET http://3-147-149-208.sslip.io/` → **308**, `Location: https://3-147-149-208.sslip.io/` |
  | Documentación interactiva | **Deshabilitada** en la release: `SCORING_DISABLE_DOCS=1` en el entorno del servicio; `GET /api/docs` → **404**, `/api/openapi.json` → **404**; por *loopback* `/docs`, `/openapi.json` y `/redoc` → **404**. (`https://…/docs` devuelve 200 pero es el `index.html` del *dashboard*, por el `try_files` de Caddy) |
  | `POST /api/eventos` sin clave | **401** |
  | Con clave falsa | **401** |
  | Con clave de agente válida | **200** (puntaje 43,32, nivel medio) |
  | Modo de autenticación | `SCORING_STRICT_AUTH=1` |
  | Recuperación tras detener y arrancar | `apagar.ps1` (08:19:36 ART, confirmado `stopped`) → `prender.ps1` (08:20:23): `running`, SSM `Online` y `/health/ready` por HTTPS **200 en 41 s**; `GET /health` con `artefactos_cargados: true`, `redis_ok: true`, `postgres_ok: true`, 0 errores; misma IP elástica |
  | Agente real hasta el nivel crítico | Estado preparado con `demo/preparar_estado.ps1 -SoloLucia` (todo en bajo), agente real en la PC (`demo/iniciar_agente.ps1`) contra la API de la EC2 y `demo/atacar.ps1` a las 08:17:28 ART: bajo → medio (44,8) → alto (89,9) → **crítico 93,25** a los **~36 s** del ataque (08:18:04, `monitor.ps1`). Acción **`terminar_y_denegar`**: el agente terminó el proceso del ataque (`powershell.exe`) y denegó el acceso a la carpeta `Sueldos 2026`; confirmación `terminar_y_denegar / ejecutado` en `GET /usuarios/{uid}/score`. Correo al administrador enviado a las 11:18:14 UTC (con el texto de respaldo mecánico, porque el servicio externo que redacta el correo no respondió a tiempo: `ReadTimeout`). Reversión con `demo/revertir.ps1`: carpeta disponible, ACL restaurada |
  | Suite de la release en la instancia | Copia de la release en `/tmp` (borrada al terminar), Python 3.11.16 del *venv* de producción, entorno aislado (Redis en memoria, sin Postgres, sin SMTP ni servicio externo de redacción): **496 aprobadas, 4 omitidas, 7 con error**; cobertura de la API **91,38 % de líneas** y **89,63 % combinada** (3 307 sentencias). Los 7 errores no son fallas del código: la release no incluye los *scripts* *offline* que importan cinco archivos de prueba (`test_clasificacion_benchmark.py`, `test_export_clue_filtro.py`, `test_hash_chain_verificacion.py`, `test_manage_agent_key.py`, `test_markov_service.py`: `ModuleNotFoundError`) ni el agente (`test_e2e_pdp_pep.py`, 2 pruebas: `FileNotFoundError`). Las 4 omitidas: 3 de `test_paridad_features_v2.py` (sin `artifacts_v2/`) y 1 de `test_sin_lstm.py` |

  \* Hash completo de `iso_calibracion.json`: `3c45f0e279ff38b1c647471a1c5e4f1cc9054202b8c9fc4d9c24ade719b6bd08`. El `manifest.json` de la release registra los mismos SHA-256.
  - **Incidente durante la verificación:** al encender, la API no llegaba a Postgres (`FATAL: (ENOTFOUND) tenant/user postgres.<proyecto> not found`, `postgres_ok: false`): el proyecto de Supabase estaba pausado. Con Postgres caído, `DELETE /usuarios/{uid}` devolvía 500 y no se podía preparar el estado de la demo; la primera prueba del agente (desde el estado previo, nivel medio) llegó igual a crítico 92,12 con la misma acción. El autor reactivó el proyecto y las verificaciones con base de datos (preparación del estado, prueba limpia del agente y recuperación) se repitieron con `postgres_ok: true`. Se dejó una consulta de actividad (15/11/2026 11:28 UTC); no se automatizó un mantenimiento por decisión del autor, así que el proyecto se vuelve a pausar tras unos 7 días sin uso.
- **Fuente:** `infra/deploy/prender.ps1`, `apagar.ps1`, `estado.ps1`; comandos por SSM (`readlink -f /opt/scoring/current`, `sha256sum`, `systemctl cat scoring-api`, `curl http://127.0.0.1:8001/health`, `journalctl -u scoring-api`, `cat manifest.json`); `Invoke-WebRequest` y `SslStream` desde la PC; `demo/preparar_estado.ps1`, `iniciar_agente.ps1`, `atacar.ps1`, `monitor.ps1`, `revertir.ps1` (15/11/2026 08:00–08:21 ART). Instancia apagada al terminar (confirmado `stopped`, 08:21:38 ART).
- **Dónde va en la memoria:** `chapters/pruebas.tex`, 10.4 (10.4.3, verificaciones en la nube).
- **Estado:** OBTENIDO.
- **Texto sugerido:** La release vigente, `20261114-221354-3634c38`, corre con Python 3.11.16 y carga solo los artefactos del camino por defecto, cuyos SHA-256 coinciden con los locales. Se verifica el certificado TLS, la redirección 308 a HTTPS, la documentación interactiva deshabilitada (404), el rechazo de eventos sin clave o con clave falsa (401), la recuperación tras detener y arrancar la instancia (41 s) y el ciclo con el agente real, que llega a crítico (93,25) a los 36 s y ejecuta `terminar_y_denegar`.

---

## C. Modelos y reentrenamiento (`chapters/producto.tex` 9.2.5; `chapters/datos.tex`)

### P9

- **Dato:** Los artefactos del Isolation Forest que usa hoy el camino por defecto provienen de la **corrida manual de reentrenamiento del 02/09/2026** (actor `manual-corrida-real`, fila 17 de `historial_reentrenamientos`, 92 eventos crudos). Se confirma lo que dice la memoria, con dos precisiones:
  1. **La regla anterior la rechazó**: `variacion_metrica` = "iso: 0.007928 -> 0.008091 (rechazado, empeora); lstm: 0.115535 -> 0.122532 (rechazado, empeora)". Aun así sus artefactos quedaron en disco porque el respaldo y la restauración ante un rechazo (`respaldar_artefactos` / `restaurar_artefactos`, `api/app/scoring/reentrenamiento_scheduler.py:96-124`) se agregaron después, el 28/09/2026 (*commit* `2a46653`, "Fixes de la auditoria v7: … backup de modelos"). El comentario del módulo lo describe: "Sin esto, un modelo rechazado quedaba en disco y el proximo reinicio de la API lo cargaba" (`reentrenamiento_scheduler.py:18-19`).
  2. **No todo el juego es de esa corrida**: `isolation_forest.joblib`, `isoforest_test_results.parquet`, `scaler_isoforest.pkl`, `type_encoding.pkl` y `config_score_hibrido.json` tienen fecha 02/09/2026 11:11–11:38 ART (= 14:11–14:38 UTC, inmediatamente antes de la fila 17, creada a las 14:39 UTC). `iso_train_reference.pkl` se regeneró el **06/10/2026 15:11** (`export_train_references.py`; el *snapshot* `scripts/models_snapshot_20261006/` tiene el mismo `isolation_forest.joblib`, SHA-256 `8de93898…`) e `iso_calibracion.json` se generó el **31/10/2026 12:57** (`scripts/export_iso_calibracion.py`, sobre ese mismo Isolation Forest).
  - Las corridas en *sandbox* de octubre (`data/sandbox/20261023`, `20261028`, `20261029`, `20261031`) produjeron otros `isolation_forest.joblib` (hashes distintos) y **ninguna se promovió** al repositorio. El respaldo `scripts/models_backup_pre_corrida_20260901/` guarda el modelo anterior a la corrida manual (otro hash, `514ec48f…`).
  - Otras filas de `historial_reentrenamientos`: 15 (25/08/2026, `scheduler-automatico`, rechazada por el lado LSTM), 16 (02/09/2026 03:31 UTC, `scheduler-automatico`, quedó en "pipeline en curso"), 18 y 19 (filas de prueba: actor vacío y `test-rev75 no usar`).
- **Fuente:** consulta de solo lectura `select * from historial_reentrenamientos order by created_at` (Supabase, 15/11/2026); fechas de modificación y SHA-256 de `scripts/models/`, `data/feature/`, `models/score_hibrido/`, `scripts/models_snapshot_20261006/`, `scripts/models_backup_pre_corrida_20260901/` y `data/sandbox/*/`; `git log -S "def restaurar_artefactos"`.
- **Dónde va en la memoria:** `chapters/producto.tex`, 9.2.5.
- **Estado:** OBTENIDO.
- **Texto sugerido:** El Isolation Forest vigente proviene de la corrida manual de reentrenamiento del 2 de septiembre de 2026. La regla de promoción de entonces lo rechazó, pero sus artefactos quedaron cargados porque la restauración automática ante un rechazo se incorporó después; las referencias de percentil y la calibración se regeneraron sobre ese mismo modelo en octubre.

### P10

- **Dato:** Cadena del reentrenamiento (`construir_comandos_pipeline`, `api/app/scoring/reentrenamiento_scheduler.py:249-293`):
  - **Camino por defecto (`iso`, sin LSTM), 9 pasos:** (1) `scripts/export_clue_combinado.py`; (2–5) `Fase1_analisis`, `Fase2_limpieza`, `Fase3_engineering`, `Fase4_forest` (notebooks, `nbconvert --execute`); (6) `scripts/fase6_sin_lstm.py` (reemplaza Fase 5, Auditoría 2 y Fase 6); (7) `scripts/export_train_references.py --solo-iso`; (8) `scripts/export_iso_calibracion.py`; (9) `scripts/export_markov_reference.py`.
  - **Camino `lstm` (versión 1), 10 pasos:** `export_clue_combinado.py`; `Fase1` a `Fase5_autoencoders`; `Auditoria2_cobertura_cruzada`; `Fase6_score_hibrido`; `export_train_references.py`; `export_markov_reference.py`.
  - Las "seis fases" de la memoria son los notebooks `Fase1`–`Fase6`; el camino por defecto ejecuta **cuatro** (Fase 1 a 4) y sustituye Fase 6 por `fase6_sin_lstm.py`: omite el LSTM (Fase 5) y la combinación híbrida.
  - **Auditorías:** en el repo hay `Auditoria1_usuarios_faltantes`, `Auditoria2_cobertura_cruzada`, `Auditoria3_normalizacion_scores` y `Auditoria4_train_val_loss` (`scripts/`); la documentación menciona además Auditoría 5 y 6, que no están en el repo. **La única bloqueante es la Auditoría 2**: produce `tabla_cobertura.csv`, contra la que `Fase6` hace un `assert` (`docs/scripts/arquitectura_scripts.md:129-136`; `reentrenamiento_scheduler.py:52`). Las demás son de solo lectura y no bloquean nada. En el reentrenamiento solo corre la Auditoría 2, y solo en el camino `lstm`.
  - Después del *pipeline* corre el gate de promoción (P12), que no es una fase del *pipeline* sino `metricas_service.comparar_y_promover()`.
- **Fuente:** `api/app/scoring/reentrenamiento_scheduler.py:46-55, 249-293`; `docs/scripts/arquitectura_scripts.md:116-150`; listado de `scripts/*.ipynb`.
- **Dónde va en la memoria:** `chapters/producto.tex`, 9.2.5.
- **Estado:** OBTENIDO.
- **Texto sugerido:** En el camino por defecto, el reentrenamiento ejecuta las fases 1 a 4 y reemplaza la fase 6 por una variante sin LSTM; la única auditoría bloqueante, la de cobertura cruzada, solo corre en el camino de la versión 1.

### P11

- **Dato:** Ninguna de estas columnas tiene restricción `CHECK` en las migraciones: los valores se fijan por convención en el código. Valores admitidos hoy:

  | Columna | Comentario de la migración | Lo que escribe el código hoy | Valores presentes en la base (15/11/2026) |
  |---|---|---|---|
  | `metricas_modelo.modelo` | `'iso' \| 'lstm'` (`006_create_metricas_modelo.sql:23`); `010` agrega `'benchmark_dev'` (`010_metricas_modelo_gate_benchmark.sql:5`) | **solo `benchmark_dev`** (`metricas_service.py:44, 154, 157`) | `iso` (4 filas) y `lstm` (4), del 22/08 al 02/09/2026; ninguna `benchmark_dev` |
  | `metricas_modelo.rol` | `'candidato' \| 'vigente'`, NULL en filas viejas (`010…sql:24`) | `candidato`, `vigente` (`metricas_service.py:152, 157`) | NULL en las 8 filas |
  | `drift_alerts.lado` | `'iso' \| 'lstm'` (`004_create_drift_alerts.sql:18`) | `iso`, `lstm` (`drift_service.py:80-81`); el *drift* compara ambas líneas de base personales en cualquier camino | `lstm` (2 filas, la última del 28/08/2026) |
  | `historial_politicas.form` | `'umbrales' \| 'acciones' \| 'reentrenamiento'` (`002_create_historial_politicas.sql:13`, desactualizado) | `umbrales`, `acciones`, `notificaciones`, `reentrenamiento`, `aprendizaje`, `iam` (`routes.py:479-692`, llamadas a `_auditar`) | los seis: `acciones` 11, `aprendizaje` 9, `iam` 5, `notificaciones` 24, `reentrenamiento` 14, `umbrales` 20 |

  Para la nota de la figura ER: `metricas_modelo.modelo` = `iso | lstm | benchmark_dev` es correcto como conjunto histórico (las dos primeras ya no se escriben); `drift_alerts.lado` = `iso | lstm` es correcto; `historial_politicas.form` admite seis valores.
- **Fuente:** `api/app/scoring/sql/002`, `004`, `006`, `010`; `api/app/scoring/metricas_service.py`, `drift_service.py`, `routes.py`; consultas de solo lectura `select modelo, rol, count(*) … from metricas_modelo group by 1,2`, `select lado, count(*) from drift_alerts group by 1`, `select form, count(*) from historial_politicas group by 1` (Supabase, 15/11/2026).
- **Dónde va en la memoria:** `chapters/datos.tex`, notas de las figuras ER.
- **Estado:** OBTENIDO.

### P12

- **Dato:** Con el criterio nuevo (gate de no inferioridad sobre los días reales post-corte de los usuarios DEV), cada reentrenamiento registra:
  - En **`metricas_modelo`**, **dos filas** con `modelo = 'benchmark_dev'`: una `rol = 'candidato'` y otra `rol = 'vigente'`, cada una con `metrica_valor` = FPR de nivel ≥ alto, `cantidad_muestras` = días negativos evaluados (`n_neg`), `es_vigente` (verdadero en la que queda cargada), `motivo` (texto de la decisión) y `metricas` (JSONB) con `fpr_alto`, `fpr_alto_semana_p90`, `n_semanas`, `n_neg`, `n_usuarios` y `sha256` de cada artefacto (`isolation_forest`, *scalers*, referencias, `markov_reference`, `iso_calibracion`). Si el gate cae en *fail-safe* sin puntuar, una sola fila `candidato` con el motivo y sin métricas (`metricas_service.py:150-157`).
  - En **`historial_reentrenamientos`**: `fecha`, `cantidad_eventos`, `actor` y `variacion_metrica` = motivo del gate + duración ("promueve: (1) FPR >=alto … ; (2) p90 FPR semanal … [gate N s]"), o "fallido: …" si el *pipeline* falla (`reentrenamiento_scheduler.py:143-160`; `metricas_service.py:158-160`).
  - **Ya no se registran "las métricas de ambos modelos"** (Isolation Forest y LSTM por separado): se registran las del **candidato y del vigente**, medidas sobre el camino que esté activo (`camino`: `iso`, `markov` o `v1`), y se promueve si FPR ≥ alto y su p90 semanal del candidato no superan las del vigente en más de 0,01 (`MARGEN_FPR`, `metricas_service.py:43, 83-91`).
  - En la base de Supabase no hay todavía filas `benchmark_dev`: el gate nuevo solo corrió en *sandbox* (P9).
- **Fuente:** `api/app/scoring/metricas_service.py:1-161`; `api/app/scoring/sql/010_metricas_modelo_gate_benchmark.sql`; consulta de solo lectura a `metricas_modelo` (15/11/2026).
- **Dónde va en la memoria:** `chapters/producto.tex`, 9.2.5, último párrafo.
- **Estado:** OBTENIDO.
- **Texto sugerido:** Cada reentrenamiento registra las métricas del candidato y del modelo vigente (FPR de nivel alto o superior, su percentil 90 semanal, cantidad de días y de usuarios evaluados y el SHA-256 de cada artefacto) junto con el motivo de la decisión.

---

## D. Diseño y UML (`chapters/e50_uml.tex`, `chapters/e50_diseno_ux.tex`, `chapters/requerimientos.tex`)

### P13

- **Dato:** Paquete `api/app/scoring/`. Las piezas del cálculo del puntaje son módulos con funciones y *dataclasses*, no clases de servicio:

  | Pieza | Archivo | Elementos | Responsabilidad |
  |---|---|---|---|
  | Orquestación y combinación | `hybrid_service.py` | `process_event` (:246), `w_iso_efectivo` (:140), `construir_motivo` (:156) | Recorre un evento: agregado, modelos, novedad, nivel, acción, explicación y cierre de día; según el camino combina ISO + LSTM con `w_iso` (v1), toma el máximo calibrado de ISO y Markov (`markov`) o calibra solo ISO (`iso`, :401-408) |
  | Isolation Forest | `isoforest_service.py`, `features.py` | `update_daily_aggregate` (:50), `IsoForestResult` (:74), `score_isoforest` (:80); `DailyAggregateAccumulator` (`features.py`:157) | Agregado usuario-día incremental de 8 variables y puntaje del Isolation Forest |
  | Explicación | `explainability.py` | `FeatureContribucion` (:29), `explicar_features` | Variables del día que se desvían de la distribución de entrenamiento (z) |
  | Novedad de recurso | `novedad_service.py` | `detector_novedad` (:44), `novedad_al_nivel`, `ResultadoNovedad` (:59), `actualizar`, `umbral_nuevos` | "Primer acceso a" destino, proceso o carpeta en 90 días con ≥ 3 días de historia; en modo `nivel` (default del camino `iso`) eleva a la regla de piso si los recursos nuevos del día superan el cuantil móvil poblacional |
  | Markov | `markov_service.py` | `camino` (:49), `CAMINO_DEFAULT = "iso"` (:46), `MarkovReferencia` (:86), `ResultadoMarkov` (:105), `actualizar`, `congelar` | Perfil de Markov por usuario (camino `markov`); el módulo también decide el camino activo |
  | LSTM | `lstm_service.py` | `LstmChunkResult` (:24), `update_lstm_buffer` (:29), `LstmUserRisk` (:65), `compute_lstm_user_risk` | Ventanas de 50 eventos y riesgo LSTM por usuario (solo camino `lstm`) |
  | Regla de piso | `scripts/_score_common.py`, `hybrid_service.py` | `assign_nivel_con_piso` (`_score_common.py`:117), `regla_piso_aplicada` (`hybrid_service.py`:146) | Si hay anomalía (ISO, novedad en modo `nivel` o LSTM/Markov), el nivel no baja de `regla_piso.nivel_minimo` |
  | Calibración | `markov_service.py`, `scripts/_score_common.py` | `historia_iso` (:63), `cargar_nudos_iso` (:73), `markov_calibrar` (`_score_common.py`:233) | Mapea el percentil a la escala 0–100 con los nudos de `iso_calibracion.json`, solo con ≥ 3 días de historia en 90 |
  | Cola por cuenta | `cola_service.py` | `cola_activa` (:19), `clases`, `actualizar` | Clases de señal distintas por cuenta en 7 días (≥ 2); `SCORING_COLA_CUENTA=1`, apagada por defecto; no cambia nivel ni acción |
  | Umbral móvil | `umbral_movil_service.py` | `umbral_movil_activo` (:34), `parametros`, `registrar_dia`, `cuantil` | Cuantil (1 − FPR) de los días cerrados en 30 días; como umbral del puntaje es informativo y solo con `SCORING_UMBRAL_MOVIL=1`; la novedad usa su `cuantil` y `registrar_dia` para su propio umbral |
  | Apoyo | `artifacts.py` (`Artifacts`, :53), `coverage.py` (`determine_coverage`), `personal_baseline_service.py`, `drift_service.py` (`DriftFinding`, :31), `redis_state.py` (`UserScoringState`, :229) | — | Carga de artefactos, cobertura, línea base personal, *drift* y estado por usuario |

  **Diagramas:** no hay fuentes Mermaid ni PlantUML en el repo. Los diagramas de clases están en TikZ: `docs/diagramas/04_clases_api_paquetes.tex`, `04a_clases_api_estado.tex`, `04b_clases_api_scoring.tex`, `04c_clases_api_iam_auth.tex`, `04d_clases_api_persistencia_config.tex`, `04e_clases_api_schemas.tex` y `03_clases_agente_pep.tex`, con sus PDF. `04b_clases_api_scoring.tex` (última modificación: *commit* `2cbc10f`, 17/10/2026) **no incluye** novedad, Markov, calibración, cola por cuenta ni umbral móvil (búsqueda de esos nombres en 04a y 04b: 0 coincidencias).
- **Fuente:** `api/app/scoring/*.py` (líneas indicadas); `scripts/_score_common.py`; `docs/diagramas/`; búsqueda de `mermaid`, `@startuml` y `classDiagram` en el repo (0 resultados).
- **Dónde va en la memoria:** `chapters/e50_uml.tex` (diagrama de clases del *scoring*).
- **Estado:** OBTENIDO.

### P14

- **Dato:** `UserScoringState` (`api/app/scoring/redis_state.py:229-284`), un JSON por usuario en la clave `scoring:{uid}`. Campos actuales:

  | Campo | Tipo | Uso |
  |---|---|---|
  | `continuity` | `ContinuityState` (`last_time`, `last_country`, `last_type`) | todos los caminos |
  | `lstm` | `LstmState` (`buffer`, `chunks_completed`, `error_sum`) | **solo `lstm`**: en `iso` y `markov` no se actualiza (`hybrid_service.py:323-324`), aunque `chunks_completed` define la cobertura |
  | `iso_day` | `IsoDayState` (`date`, `n_events`, `distinct_types`, `distinct_countries`, `n_file_events`, `n_login_events`, `sum_hours`, `n_off_hours`, `type_counts`, `n_share_events`) | todos |
  | `hybrid_anchor` | `HybridAnchorState` (`date`, `score`) | todos (decaimiento) |
  | `personal_baseline` | `PersonalBaselineState` (`iso`, `lstm`, `anchor_iso`, `anchor_lstm`, `anchor_date`; Welford por variable) | todos; incluye las 8 variables del LSTM aun sin LSTM |
  | `total_events`, `last_day_score` | `int`, `float` | todos |
  | `last_risk_score_hibrido`, `last_nivel_sugerido`, `last_cobertura`, `last_accion_sugerida`, `last_accion_id`, `last_explicacion`, `last_motivo` | — | todos (último resultado y explicación para `historial_scores`) |
  | `last_role`, `last_department`, `last_iam_nivel` | `str` | todos (IAM) |
  | `last_event_epoch` | `float` | todos ("sin reportar") |
  | `last_confirmacion_accion_id`, `last_confirmacion_estado`, `last_confirmacion_timestamp`, `last_confirmacion_detalle` | — | todos (confirmación del agente, RF-11) |
  | **`markov`** (nuevo) | `dict \| None` | solo camino `markov` |
  | **`novedad`** (nuevo) | `dict \| None` (`vistos`, `dias`, `fecha`, `nuevos`, `distintos`, opcionales `decaida` e `info`) | camino `iso` (default) y `markov`; `None` con `lstm` |
  | **`iso_dias`** (nuevo, calibración) | `list[str]` | solo camino `iso`: últimos días activos, para calibrar solo con historia |
  | **`cola`** (nuevo) | `dict \| None` | solo con `SCORING_COLA_CUENTA=1` |

  `en_aprendizaje(umbral)` es un método derivado, no se persiste. El umbral móvil no vive en este estado: es una lista global en Redis (`scoring:umbral_movil:scores`, `umbral_movil_service.py`). El comentario de `novedad` en `redis_state.py:278` ("solo con SCORING_DETECTOR_NOVEDAD=1") está desactualizado: hoy el detector corre por defecto en el camino `iso` (`novedad_service.py:2-4, 40-42`).
- **Fuente:** `api/app/scoring/redis_state.py:149-294`; `hybrid_service.py:321-359, 433-490`; `novedad_service.py:1-50`.
- **Dónde va en la memoria:** `chapters/e50_uml.tex` (clase de estado por usuario).
- **Estado:** OBTENIDO.

### P15

- **Dato:**
  - **La nota «En calibración» sigue existiendo**, en la vista de explicación de un usuario (`frontend/src/pages/UserExplanationPage.tsx`, ruta de detalle "Por qué pasó esto"), en el recuadro informativo debajo de la explicación (:227-231). Texto (:23-25): "En calibración: todavía no hay eventos suficientes para el modelo de secuencias, así que el score usa solo el modelo de comportamiento del día." **Condición:** `data.cobertura === 'parcial'` (`AVISO_COBERTURA[data.cobertura]`).
  - La cobertura la calcula la API (`api/app/scoring/coverage.py:26-33`): `parcial` mientras `lstm.chunks_completed` sea 0. Como en el camino por defecto el LSTM no se actualiza (P14), **un usuario nuevo queda siempre en `parcial` y la nota aparece siempre**, aunque ya no hay un modelo de secuencias que calibrar. A la inversa, un usuario que acumuló ventanas LSTM antes del cambio de camino queda en `completa` y ve el texto que describe la combinación de dos modelos (:20-22): en la prueba de la EC2 (P8) `lucia.fernandez` llegó a crítico con `cobertura=completa`.
  - **Recurso de la novedad en la explicación:** la API agrega a `explicacion` una entrada con `feature = "primer acceso a <clase>:<recurso>"` (por ejemplo `primer acceso a proceso:rclone.exe`; `hybrid_service.py:436-442`) y, si eleva el nivel, el `motivo` agrega "Nivel elevado por primer acceso a …" (:477-478). El *frontend* no tiene texto propio para la novedad (0 coincidencias de "novedad" o "primer acceso" en `frontend/src`): la muestra con el fallback de `featureFrase` (`frontend/src/lib/featureLabels.ts:61-63`), que concatena el nombre recibido y "por encima de lo habitual". Es decir, **el recurso se ve**, con el formato técnico `clase:recurso` y una frase genérica; el `motivo` se muestra tal cual.
- **Fuente:** `frontend/src/pages/UserExplanationPage.tsx:18-27, 154-231`; `frontend/src/lib/featureLabels.ts:14-25, 61-63`; `api/app/scoring/coverage.py`; `api/app/scoring/hybrid_service.py:340, 433-442, 477-478`; `api/app/scoring/explainability.py:24` (`DIRECCION_ENCIMA = "por_encima"`).
- **Dónde va en la memoria:** `chapters/e50_diseno_ux.tex` (vista de explicación).
- **Estado:** OBTENIDO (por lectura de código; no se abrió el *dashboard*).

### P16

- **Dato:** **Sí, con una condición.** `historial_scores.explicacion` y `motivo` se escriben al cerrar el día con `state.last_explicacion` y `state.last_motivo` (`hybrid_service.py:299-310`; `history_store.py:60-85`): son la explicación y el motivo **del último evento del día**. La entrada "primer acceso a …" queda persistida solo si ese último evento fue un primer acceso, y el motivo de novedad solo si ese evento elevó el nivel.
  - Verificación local con el camino por defecto (guion de `test_novedad_service.py`, 4 días + 1 para cerrar, captura de `write_closed_day`): con el proceso nuevo en el **último** evento del día, la explicación persistida es `['type_entropy', 'n_distinct_types', 'primer acceso a proceso:rclone.exe']`; con el proceso nuevo en el **primero** de los tres eventos del día, la persistida es `['type_entropy', 'n_distinct_types']` (sin la novedad). En ambos casos el motivo fue "Score ISO calibrado. Usuario en período de aprendizaje (acción ablandada).", sin mención a la novedad (el usuario estaba en aprendizaje y no hubo elevación).
  - En la base de Supabase: 0 de 1 981 filas de `historial_scores` (última fecha 09/11/2026) tienen "primer acceso" en `explicacion` o en `motivo`; 60 filas tienen explicación.
- **Fuente:** `api/app/scoring/hybrid_service.py:294-310, 433-490`; `api/app/scoring/history_store.py:60-90`; corrida local en entorno aislado con `SCORING_TERCER_MODELO=iso` (15/11/2026 08:34); consulta de solo lectura `select count(*) filter (where explicacion::text like '%primer acceso%') … from historial_scores` (15/11/2026).
- **Dónde va en la memoria:** `chapters/requerimientos.tex` (RNF-11).
- **Estado:** OBTENIDO.
- **Texto sugerido:** La explicación persistida en `historial_scores` corresponde al último evento de cada día; incluye el primer acceso a un recurso cuando ese evento lo registró.

---

## E. Referencias bibliográficas (`biblio.bib`)

### P17

Búsqueda primero en el repo y después en la web, con autorización del autor (15/11/2026). Cada dato de la web lleva la página consultada.

- **Dato:**

  | Referencia | Autores | Título | Año | Editorial o evento | DOI / URL | Licencia |
  |---|---|---|---|---|---|---|
  | **Larroche (2026)** | Corentin Larroche | *On fair and realistic performance evaluations for graph-based lateral movement detectors* | 2026 (arXiv v1, 31/07/2026) | Aceptado en ANUBIS 2026 (2nd International Workshop on Assessment with New methodologies, Unified Benchmarks, and environments, of Intrusion detection and response Systems), junto a ESORICS 2026, Roma, 18/09/2026 | 10.48550/arXiv.2607.29390 · https://arxiv.org/abs/2607.29390 | CC BY 4.0 (del artículo) |
  | **LANL 2017** | Melissa J. M. Turcotte, Alexander D. Kent, Curtis Hash | *Unified Host and Network Data Set* | 2018 | Capítulo 1, pp. 1–22, en *Data Science for Cyber-Security*, World Scientific, nov. 2018 (preprint: arXiv 1708.07518, 2017) | 10.1142/9781786345646_001 · https://csr.lanl.gov/data/2017/ | Datos: CC0 1.0 |
  | **GUIDE** (Microsoft) | Scott Freitas, Jovan Kalajdjieski, Amir Gharib, Robert McCann | (título en arXiv; no se transcribe porque nombra un producto de asistencia automatizada) | 2024 (v1, 12/07/2024; v4, 26/11/2024) | Preprint arXiv, sin *journal-ref*; datos en Kaggle, "Microsoft Security Incident Prediction" | 10.48550/arXiv.2407.09017 · https://arxiv.org/abs/2407.09017 · https://www.kaggle.com/datasets/Microsoft/microsoft-security-incident-prediction | El artículo dice "permissive CDLA-2.0" (`research_notes/Datasets reales para matriz UEBA/host_insider.md:12`) |
  | **DARPA OpTC** | Rody Arantes, Carl Weir, Henry Hannon, Marisha Kulseng | *Operationally Transparent Cyber (OpTC)* | 2021 | IEEE Dataport | 10.21227/edq8-nk52 · https://ieee-dataport.org/open-access/operationally-transparent-cyber-optc · https://github.com/FiveDirections/OpTC-data | Dominio público (Distribution A, "as-is") |

  Precisiones:
  - **Larroche:** el resumen de arXiv habla de métodos de preprocesamiento y etiquetado en "two popular datasets" pero no los nombra. Que traten sobre LANL 2015 lo confirma una fuente secundaria: AuthBench (Mahamane Sani Adamou Mahamane, Zenodo, 27/10/2026, DOI 10.5281/zenodo.23687498, CC BY 4.0) dice que reproduce el conjunto de eventos del protocolo de Larroche (2026) sobre el registro de autenticación de LANL. **No se verificó en el texto completo** la afirmación de `docs/contexto/estado_modelos.md:3`: "una sola intrusión simulada, casi toda desde un host". AuthBench, por su parte, habla de 162 campañas de *red team*.
  - **LANL 2017:** la cita del capítulo es la que pide la página oficial del conjunto de datos. arXiv 1708.07518 es la versión previa (sin editorial).
  - **GUIDE:** ni arXiv ni la página de Kaggle mostraron un campo de licencia. La única fuente de "CDLA-2.0" es el texto del artículo; que sea **CDLA-Permissive-2.0** sigue sin confirmar.
  - **OpTC:** los datos vienen del repo (`Datasets reales complementarios a CLUE-LDS.md:92-99`, `DATASETS.md:10-13`). No se volvieron a consultar en la web.
- **Fuente:** https://arxiv.org/abs/2607.29390, https://zenodo.org/records/23687498, https://csr.lanl.gov/data/2017/, https://arxiv.org/abs/1708.07518, https://arxiv.org/abs/2407.09017, https://www.kaggle.com/datasets/Microsoft/microsoft-security-incident-prediction (consultadas el 15/11/2026); `DATASETS.md`; `research_notes/Datasets reales para matriz UEBA/host_insider.md`.
- **Dónde va en la memoria:** `biblio.bib`.
- **Estado:** OBTENIDO, con dos datos sin verificar: la licencia exacta de GUIDE (el artículo dice CDLA-2.0; Kaggle no muestra el campo) y el detalle sobre LANL 2015 que se atribuye a Larroche (solo confirmado por una fuente secundaria).

### P18

- **Dato:** El repo **no cita fuentes** para estos tres métodos: las decisiones se apoyan en evidencia propia (`docs/contexto/estado_modelos.md`; `api/app/scoring/umbral_movil_service.py:3-5`). Las referencias de abajo salen de la web (autorizada el 15/11/2026). Son **candidatas** que tratan el mismo método. El código no las usa ni las implementa tal cual; elegirlas es decisión del autor.

  | Tema | Referencia | Datos verificados |
  |---|---|---|
  | Novedad / primer acceso | Bowman, B.; Laprade, C.; Ji, Y.; Huang, H. H. *Detecting Lateral Movement in Enterprise Computer Networks with Unsupervised Graph AI* | 23rd International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2020), San Sebastián, oct. 2020, USENIX Association, pp. 257–268, ISBN 978-1-939133-18-2. https://www.usenix.org/conference/raid2020/presentation/bowman. Compara su detector con una línea base por reglas que marca toda autenticación por primera vez como anómala |
  | Novedad / primer acceso | Ho, G.; Dhiman, M.; Akhawe, D.; Paxson, V.; Savage, S.; Voelker, G. M.; Wagner, D. *Hopper: Modeling and Detecting Lateral Movement* | USENIX Security Symposium 2021; versión extendida en arXiv 2105.13442 (DOI 10.48550/arXiv.2105.13442). Trata los falsos positivos de los inicios de sesión legítimos por primera vez |
  | Markov en UEBA / amenaza interna | Kim, D.-W.; Hong, S.-S.; Han, M.-M. *A study on Classification of Insider threat using Markov Chain Model* | KSII Transactions on Internet and Information Systems, vol. 12, n.º 4, pp. 1887–1898, 2018. DOI 10.3837/tiis.2018.04.027 |
  | Markov en UEBA / amenaza interna | Rashid, T.; Agrafiotis, I.; Nurse, J. R. C. *A New Take on Detecting Insider Threats: Exploring the use of Hidden Markov Models* | MIST '16, 8th ACM CCS International Workshop on Managing Insider Security Threats, ACM, 2016, ISBN 978-1-4503-4571-2. DOI 10.1145/2995959.2995964. Usa cadenas ocultas de Markov, no la cadena de orden 2 del proyecto |
  | Umbral por cuantil o extremos en flujo | Siffer, A.; Fouque, P.-A.; Termier, A.; Largouët, C. *Anomaly Detection in Streams with Extreme Value Theory* | Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2017), ACM, pp. 1067–1075. DOI 10.1145/3097983.3098144. Umbral automático en flujo (SPOT/DSPOT); el proyecto usa un cuantil empírico móvil, más simple |

  No se encontró una fuente que use exactamente el esquema del proyecto: conteo de recursos nuevos del día contra un cuantil móvil poblacional.
- **Fuente:** páginas citadas en la tabla (USENIX, arXiv, itiis.org vía DOI, kar.kent.ac.uk/67482, bibtex.github.io/KDD-2017-SifferFTL.html), consultadas el 15/11/2026; búsqueda sin resultados en el repo (`docs/`, `research_notes/`, `README.md`, notebooks y código).
- **Dónde va en la memoria:** `biblio.bib`; estado del arte o justificación del diseño.
- **Estado:** OBTENIDO (referencias candidatas de la web; el repo no tiene ninguna). Los resúmenes de método salen de los resúmenes y metadatos, no de los textos completos.

---

## F. Decisiones que quedan para el autor

### P19

- **Dato:** **Sin criterio escrito: decisión del autor.** Ni `docs/contexto/` ni los registros de la revisión fijan una meta numérica de oscilación dentro del día. Lo único escrito son mediciones sin meta asociada: "Días con algún evento ≥ alto / al cierre del día, 51 usuarios | **2,66 % / 1,29 %** (antes 14,04 % / 4,95 %)" (`docs/contexto/estado_modelos.md:25`) y "El piso de Markov explicaba la oscilación (177 de 189 días transitorios); sacarlo del default bajó los días con algún evento ≥ alto de 14,04 % a 2,66 %" (`estado_modelos.md:62`). El único umbral numérico de estabilidad del código es el del gate de promoción (p90 semanal de la FPR ≥ alto del candidato ≤ vigente + 0,01, `api/app/scoring/metricas_service.py:43, 85`), que es una regla de no inferioridad entre modelos y no una meta de oscilación.
- **Fuente:** búsqueda de "oscila", "transitori", "días con algún evento", "estabilidad" en `docs/` (sin `docs/etiquetado/`), `informes_codigo_e75/` y los `.md` de `data/sandbox/`.
- **Dónde va en la memoria:** decisión del autor (capítulo de evaluación del modelo).
- **Estado:** OBTENIDO: no hay criterio escrito y la meta queda como decisión del autor, la respuesta que el plan prevé para este caso.

---

## Tabla resumen

| Ítem | Estado | Dato |
|---|---|---|
| P1 | OBTENIDO | API 547 pruebas en **54** archivos; agente 200 pruebas en **16** archivos (547 y 200 coinciden; 44 y 15 no) |
| P2 | OBTENIDO | Sentencias API **3 287**, agente **1 124**, total **4 411** (no 2 808 / 1 107 / 3 915); % sin cambio: 95,25 / 93,86; 91,90 / 91,20; 94,40 / 93,17 |
| P3 | OBTENIDO | 508 aprobadas, 30 omitidas: 25 requieren los modelos entrenados, 3 los datos procesados de la versión 2, 2 la referencia de Markov de *sandbox* |
| P4 | OBTENIDO | Sin artefactos: **87,65 %** de líneas y **85,70 %** combinada (Python 3.12 local) |
| P5 | PARCIAL | Última exitosa 04/11/2026 (4 trabajos OK); desde 08/11 `startup_failure` en todas las ramas con 0 trabajos y `ci.yml` sin cambios; re-ejecución 43706419315 falla y su reintento queda en cola sin crear trabajos; facturación descartada (consumo dentro de lo incluido, cargo 0); causa no identificada; en consulta con el soporte de GitHub |
| P6 | OBTENIDO | 46 eventos (9 + 31 + 6); la prueba corre con `lstm` (puntaje = Isolation Forest, < 50 eventos); con el camino por defecto, crítico en el evento 44 igual |
| P7 | OBTENIDO | Media 12,83 ms; mediana 12,59; p95 13,71; p99 18,24; máx. 55,28; 0 errores; 78 ev/s; sin LSTM, picos aislados sin causa identificable |
| P8 | OBTENIDO | Release `20261114-221354-3634c38` (`3634c38`), Python 3.11.16, 6 artefactos con SHA-256 igual, TLS válido, 308, docs 404, eventos 401/401/200, recuperación en 41 s, crítico 93,25 a ~36 s con `terminar_y_denegar`, suite 496/4/7 (91,38 % líneas) |
| P9 | OBTENIDO | Isolation Forest de la corrida manual del 02/09/2026, rechazada por la regla anterior pero conservada (la restauración se agregó el 28/09); referencias del 06/10 y calibración del 31/10 |
| P10 | OBTENIDO | Default: export + Fase 1–4 + `fase6_sin_lstm.py` + referencias `--solo-iso` + calibración + Markov; bloqueante: Auditoría 2 (solo en `lstm`) |
| P11 | OBTENIDO | Sin `CHECK`; `modelo`: hoy solo `benchmark_dev` (históricos `iso`, `lstm`); `rol`: `candidato \| vigente`; `lado`: `iso \| lstm`; `form`: 6 valores |
| P12 | OBTENIDO | Candidato y vigente: FPR ≥ alto, p90 semanal, n_semanas, n_neg, n_usuarios, SHA-256 y motivo; ya no "ambos modelos" |
| P13 | OBTENIDO | Módulos con su responsabilidad; diagramas en TikZ (`docs/diagramas/04*.tex`), sin Mermaid/PlantUML; 04b sin novedad, Markov, calibración, cola ni umbral móvil |
| P14 | OBTENIDO | Campos listados; nuevos `markov`, `novedad`, `iso_dias`, `cola`; `lstm` solo en camino `lstm` |
| P15 | OBTENIDO | Nota presente en la vista de explicación con `cobertura === 'parcial'`, siempre visible en el default para usuarios nuevos; el recurso de novedad se ve como `primer acceso a clase:recurso` con frase genérica |
| P16 | OBTENIDO | Sí, si el último evento del día fue el primer acceso (verificado en local); 0 casos en la base |
| P17 | OBTENIDO | Larroche 2026 (arXiv 2607.29390, ANUBIS 2026); LANL 2017 (Turcotte, Kent, Hash, World Scientific 2018, DOI 10.1142/9781786345646_001, CC0); GUIDE (Freitas et al., arXiv 2407.09017, "CDLA-2.0" según el artículo, sin confirmar en Kaggle); OpTC (DOI 10.21227/edq8-nk52, dominio público) |
| P18 | OBTENIDO | El repo no cita fuentes; candidatas de la web: Bowman et al. (RAID 2020) y Ho et al. (USENIX Security 2021) para novedad; Kim et al. (KSII 2018) y Rashid et al. (MIST 2016) para Markov; Siffer et al. (KDD 2017) para el umbral en flujo |
| P19 | OBTENIDO | Sin criterio escrito: decisión del autor (mediciones vigentes 2,66 % / 1,29 %, sin meta) |

Al cierre: `git status` del repo igual que al inicio (`?? goal_demo_aws.md`, `?? main.pdf`); `reports/cobertura/` restaurado con el reporte del 14/11/2026 22:28; instancia EC2 apagada (confirmado `stopped`).
