# Informe de correcciones E75 (limitaciones menores)

Fecha: 2026-10-20. Parte A completa; Parte B no se hizo (no se pidió en el chat).

## 1. Ramas y commits

- Rama de partida: `analysis/metricas-clasificacion` (HEAD `7dc88a6`, árbol limpio, la rama de trabajo más reciente).
- Rama nueva: `fix/e75-limitaciones-menores`. Sin push.

| Commit | Mensaje |
|---|---|
| `f9f5632` | fix(auth): rechazar la clave de administración en los endpoints del agente en modo estricto |
| `040ddf7` | fix(agente): informar como parcial la suspensión sin registro recuperable |
| `871fd76` | fix(agente): con el circuit breaker abierto, bufferizar los eventos nuevos sin enviarlos |
| `613529f` | fix(agente): con el buffer lleno descartar los eventos más antiguos |
| `f647106` | fix(scheduler): registrar como fallido el reentrenamiento que falla, lanza excepción o excede el tiempo máximo |
| `e989cd4` | fix(dashboard): volver a /login cuando la API responde 401 por sesión vencida |
| (este) | docs: informe de correcciones E75 |

Ningún commit quedó revertido.

## 2. C1: umbral vigente del LSTM (solo lectura)

Carga con `artifacts._build_artifacts()` desde un `python -c` fuera del repo.

| Valor | Archivo / clave | ¿Decide algo en vivo? |
|---|---|---|
| **0,1180463821693793** | `scripts/models/lstm_threshold.pkl` → `Artifacts.lstm_threshold` (`api/app/scoring/artifacts.py:88-89`) | **No.** Solo se carga para el chequeo de presencia de `/health` (comentario en `artifacts.py:81-87`). |
| **95,0** (percentil) | `LSTM_USER_PERCENTIL_PISO`, constante en `api/app/scoring/lstm_service.py:20`, usada en `:80` | **Sí, este prevalece.** `is_anomaly_lstm_user = lstm_risk_user > 95`, donde `lstm_risk_user` es el percentil de la media de error del usuario contra `models/score_hibrido/lstm_user_mean_error_train_reference.pkl` (163 valores; mín. 0,0019, mediana 0,1287, p95 17,41, máx. 1167). |
| 0,0874 | No aparece en el repo (búsqueda en `.md`, `.ipynb`, `.py`, `.json`). | — Probablemente sale de artefactos anteriores. El diagrama de objetos está desactualizado. |

Conclusión para el documento: el p95 del error de entrenamiento es 0,1180, y ese es el valor del artefacto. Pero la regla de anomalía LSTM en producción no lo usa: usa el percentil 95 de la referencia por usuario. El 0,0874 debería salir del diagrama.

SHA-256 antes y después de la carga (todos iguales):

| Artefacto | SHA-256 |
|---|---|
| isolation_forest | `8de938982e309557522aa7fe6594b81124494bb7818942a17626371673dac470` |
| lstm_autoencoder | `d5f12c899e0eee4890b1cfdb38965a997480170c8446d99f9e556156b1bae4d2` |
| scaler_isoforest | `631698514d3fcc73a898d56e01fe4d8bdede7c6dd64f2d35dca51276e60a7607` |
| scaler_lstm | `51b7f52e44c83b86e105204e191f7f720212dea564c8547f3ce1cda677efb2b8` |
| type_encoding | `c88416d5d7f505fd03c864518b22983013a4daf7ef5c0c0cd048922e30af1141` |
| lstm_threshold | `15bb00ffc4b7a4ac178697d8ccc4d01a6cc42fe307a62eea1a4b4da1e37fc7d9` |
| config_score_hibrido | `ddd6e60e705114a5548b365acd4eae72bf911be4b40e7ae65555e066ea687f0e` |
| iso_train_reference | `95d41f5700268a7e943284e87797403c2a3fa68aa9c3bdd5f29398fe671a90de` |
| lstm_user_mean_error_train_reference | `3bab9693a0d0a32e514ff75b4616e0604b10d178aa32859407e586e3270de484` |

## 3. Correcciones C2 a C7

Cada una siguió el mismo orden: primero la prueba nueva fallando, después el cambio, después la prueba en verde.

### C2. Clave de administración en los endpoints del agente — aplicada

**Diagnóstico de llamadores** (antes del cambio). Mandan eventos o confirmaciones con `SCORING_ADMIN_KEY`:
- Scripts de demo: `caso_bajo_riesgo.py`, `caso_app_no_monitoreada.py`, `caso_conexion_red.py`, `catalogo_acciones.py`, `demo_exfil.py`, `ensayo_demo_pep.py`, `simulator.py`, `simulate_day_pass.py`.
- Ensayos: `ensayo_carga_pool_hash_chain.py`, `ensayo_concurrencia_redis.py`.
- Latencia: `scripts/analysis/bench_rnf01_latencia.py`.
- Generadores de informes: `generar_word_*` (agente_pep, auth_reset, corrida_integracion, demo_pep_hora, revision_demo_sistema).
- El agente con `--allow-admin-key` (solo con la API en loopback).
- Unas 12 pruebas de `api/tests`.

`run_regression_test.py`, `replay_equivalencia_v1.py`, `validacion_escenarios.py`, `verificar_decaimiento.py` y `contar_viajes_process_event.py` usan `TestClient` con las keys vacías (fail-open), no la admin key. `bench_aws_latencia.py`, el único que apunta a la nube, usa una agent key para `/eventos` y la admin key solo para el reset. El `.env` local no define `SCORING_STRICT_AUTH`, así que ninguno de los llamadores locales se ve afectado.

**Modo estricto**: ya existía y está definido. Es `SCORING_STRICT_AUTH=1` (`auth.strict_auth_enabled()`), y lo fija la EC2 (`infra/user_data.sh.tftpl:105`).

**Cambio**: en `api/app/scoring/auth.py`, `require_agent_key` ahora devuelve 403 ante la admin key cuando el modo es estricto. Fuera del modo estricto, sigue igual que antes.

**Archivos**: `api/app/scoring/auth.py`, `api/tests/test_auth_agente.py`, `CLAUDE.md`.

**Pruebas nuevas** (`test_auth_agente.py`):
- `test_estricto_admin_key_da_403_en_eventos`
- `test_estricto_admin_key_da_403_en_confirmar_accion`
- `test_estricto_agent_key_ligada_al_uid_pasa`
- `test_estricto_agent_key_con_uid_ajeno_sigue_dando_403`

Fuera del modo estricto lo cubren las pruebas que ya existían: `test_confirmar_accion_sigue_aceptando_key_de_admin` y `test_confirmar_accion_de_uid_ajeno_con_admin_pasa`. Resultado: 92/92 en los 3 archivos de auth.

El 200 de la agent key en modo estricto se verificó en `confirmar-accion`. Un 200 de `POST /eventos` necesita los artefactos y el lifespan; la parte de autorización es la misma dependencia.

### C3. Suspensión fallida informada como éxito — aplicada

**Defecto real** (M7 de `00_resumen.md`): los errores de `proc.suspend()` ya iban a `ultimos_fallos`. Lo que se informaba como `ejecutado` era la falla al guardar el estado de suspensión, porque la advertencia iba a la lista de acciones.

**Cambio**: esa advertencia ahora va a `ultimos_fallos`. Si los procesos quedaron suspendidos pero sin registro para reanudarlos, la confirmación sale `parcial`, con `FALLO: ...` en el detalle.

**Archivos**: `agent/enforcement.py`, `agent/tests/test_confirmacion_estado.py`, `agent/tests/test_enforcement_revert.py`.

**Pruebas nuevas**:
- `test_suspender_proceso_ok_es_ejecutado`
- `test_suspender_con_error_de_psutil_es_fallido`
- `test_suspender_con_fallo_al_guardar_estado_no_es_ejecutado` (la que reproducía el defecto)

**Prueba modificada**: `test_suspend_marca_advertencia_si_save_falla` ahora busca la advertencia en `ultimos_fallos` en vez de en las acciones.

### C4. Breaker abierto: eventos nuevos sin HTTP — aplicada

**Cambio** en `agent/main.py::handle_signal`: con `client.breaker_open`, el evento va directo a `append_event` y no se hace ningún POST. Lo reenvía el sondeo de `flush_pending`, que ya existía (cada `breaker_poll_interval_sec`, 300 s). No se tocó `post_event`, porque el mismo sondeo lo usa.

**Archivos**: `agent/main.py`, `agent/tests/test_main_loop.py`, `CLAUDE.md`.

**Prueba nueva**: `test_breaker_abierto_evento_nuevo_va_al_buffer_sin_http`.

**Prueba modificada**: `test_run_envia_inicio_eventos_de_archivo_y_cierre_y_espacia_el_flush_con_breaker_abierto` fijaba el comportamiento anterior: con el breaker abierto esperaba que `FILE_CREATED` y `SESSION_ENDED` se enviaran. Ahora verifica que van al buffer.

### C5. Buffer lleno: se conserva lo reciente — aplicada

**Cambio** en `agent/event_buffer.py::append_event`: al llegar al tope, se descartan las líneas más antiguas (con log de cuántas) y se conserva el evento nuevo. El TTL de 3 h no cambió.

**Archivos**: `agent/event_buffer.py`, `agent/tests/test_event_buffer_tope.py` (nuevo), `CLAUDE.md`.

**Pruebas nuevas**:
- `test_buffer_lleno_descarta_el_mas_antiguo_y_conserva_el_nuevo`
- `test_buffer_por_encima_del_tope_vuelve_al_tope`

### C6. Planificador: fallido, excepción y tiempo máximo — aplicada

**Cambio** en `api/app/scoring/reentrenamiento_scheduler.py::correr_reentrenamiento`:
- La fila de `historial_reentrenamientos` se inserta **antes** del pipeline. Con eso, una excepción queda registrada y `_tick` respeta `periodo_dias`, en vez de reintentar a los 5 minutos.
- Un paso fallido, una excepción o un corte por tiempo dejan `variacion_metrica = "fallido: <motivo>"`.
- El pipeline corre bajo `asyncio.wait_for` con `SCORING_REENTRENAMIENTO_TIMEOUT_SEC` (default 14400 s = 4 h). Al vencer, la cancelación mata el subproceso con el `except CancelledError` que ya existía, y se restaura el respaldo.

**Restricción**: `historial_reentrenamientos` no tiene columna de estado, y la regla 2 prohíbe tocar el schema. Por eso "fallido" es un prefijo de texto en `variacion_metrica`, no un campo.

**Archivos**: `api/app/scoring/reentrenamiento_scheduler.py`, `api/tests/test_reentrenamiento_backup.py`, `CLAUDE.md`.

**Pruebas nuevas** (todas verifican además la restauración, comparando el SHA-256 de los artefactos falsos):
- `test_paso_fallido_registra_fallido_con_motivo`
- `test_excepcion_registra_fallido_antes_de_relanzar`
- `test_excepcion_respeta_la_periodicidad_configurada`: dos `_tick` seguidos y una sola corrida.
- `test_tiempo_maximo_corta_registra_fallido_y_restaura`: tiempo máximo de 0,2 s; la prueba comprueba que el pipeline se cancela.
- `test_tiempo_maximo_por_defecto_es_4_horas`

Las pruebas de restauración que ya existían (rechazo, fallo, excepción, cancelación) siguen en verde. No se ejecutó ningún reentrenamiento real.

**Prueba modificada**: el fixture `repo` suma `update_variacion_metrica` a su `history_store` falso.

### C7. Dashboard: 401 lleva a /login — aplicada

**Cambio**: hay un único punto, `verificarSesion()` en `frontend/src/api/client.ts`, invocado desde `request()` y `del()`. Ante un 401 en una solicitud que llevaba token:
- borra la sesión local (`marcarSesionVencida`, en `lib/dashboardAuth.ts`);
- hace `window.location.replace('/login')`, lo que además descarta la caché de React Query.

`LoginPage` muestra "La sesión venció; volvé a iniciar sesión." una sola vez. El 401 del login, que va sin token, sigue mostrándose como "Usuario o contraseña inválidos".

**Archivos**: `frontend/src/api/client.ts`, `frontend/src/lib/dashboardAuth.ts`, `frontend/src/pages/LoginPage.tsx`.

**Verificación automática**: `tsc -b` 0 errores, `oxlint` 0 avisos, `npm run build` OK (solo el aviso de chunk grande de `recharts`, que ya existía).

**Prueba manual** con Playwright (`playwright-core` instalado solo en el scratchpad, con el Chromium que ya estaba), contra una API local **aislada**: `SCORING_FAKE_REDIS=1`, sin Supabase, scheduler apagado y contraseñas de prueba propias. No se tocaron Redis ni Supabase gestionados, y no se usó la instancia. Pasos:
1. Login como admin: entra al dashboard y queda el token en `sessionStorage`.
2. Simulación de la otra pestaña: `POST /auth/logout` con ese mismo token desde fuera de la página → 204.
3. En el siguiente poll (2 s), el panel redirige a `/login`, muestra el aviso y la sesión local queda borrada.
4. Al recargar `/login`, el aviso ya no aparece.
5. Un login con la contraseña equivocada se queda en `/login` y muestra "Usuario o contraseña inválidos".

Los 5 pasos dieron el resultado esperado.

## 4. Números nuevos (medidos al final, HEAD `e989cd4`)

### Pruebas

Suites completas como se corren en el proyecto: `scripts/cobertura_local.ps1`, con la API con artefactos reales y el agente en Windows.

| Suite | Aprobadas | Omitidas | Fallidas |
|---|---|---|---|
| API (con artefactos) | 476 | 0 | 0 |
| Agente (Windows) | 183 | 0 | 0 |
| **Total** | **659** | 0 | 0 |

El documento dice 623 = 446 + 177. La rama de partida ya tenía 467 pruebas de API (las 21 de más vienen de la evaluación controlada y de pruebas anteriores a esta sesión). Esta sesión suma 9 pruebas de API y 6 del agente.

### Cobertura

Sale de `reports/cobertura/*/coverage.json`, generado por `cobertura_local.ps1`.

| Componente | Líneas | Líneas + ramas | Antes |
|---|---|---|---|
| API | **94,76 %** (2657/2804) | **93,50 %** | 94,7 / 93,5 |
| Agente | **90,20 %** (1012/1122) | **89,12 %** | 89,3 / 88,1 |
| Combinada (suma de ambos) | **93,45 %** | **92,21 %** | 93,2 / 91,9 |

Las dos cumplen el mínimo de 85 % de líneas. El script terminó con código de salida 0.

### Integración continua

Se reprodujo localmente el job `api` de `.github/workflows/ci.yml`:
- en un worktree limpio, sin artefactos de modelo ni `.env`;
- con `SCORING_FAKE_REDIS=1` y los mismos 4 `--ignore`;
- con `coverage report --fail-under=85` sobre el mismo `--include`.

Resultados:
- **444 aprobadas, 23 omitidas, 0 fallidas.**
- Cobertura **87,10 % combinada** (antes 87,03 %), 88,48 % de líneas.
- Umbral superado (código de salida 0).
- Los 4 archivos del agente de ese job: 28/28.

El job `frontend` equivale a lint y build, los dos OK. El job `agent-windows` corresponde a la suite completa del agente, en verde y con 90,20 % de líneas. El job `infra` no se tocó.

**El pipeline de GitHub Actions no se ejecutó, porque no hubo push.** Se corrió con Python 3.12 local; CI usa 3.11.

## 5. Qué no está en la release desplegada (`b499fa3`)

Ninguna de las correcciones C2 a C7 está desplegada en la EC2: no hubo despliegue en esta sesión. En particular, la instancia (`SCORING_STRICT_AUTH=1`) **sigue aceptando la admin key** en `POST /eventos` y en `confirmar-accion` hasta el próximo despliegue. El dashboard que sirve la instancia tampoco redirige ante un token vencido.

## 6. Efectos colaterales

- **Pruebas modificadas** (las tres reflejan el comportamiento nuevo, no lo esconden):
  - `test_suspend_marca_advertencia_si_save_falla` (C3)
  - `test_run_envia_inicio_..._con_breaker_abierto` (C4)
  - el fixture `repo` de `test_reentrenamiento_backup.py` (C6)
- **Scripts**: ninguno local deja de funcionar, porque el modo estricto no está activo en local. Hacia la nube:
  - después de un despliegue, todo lo que mande eventos a la EC2 con la admin key va a recibir 403;
  - `bench_aws_latencia.py` no se ve afectado, porque usa agent key;
  - el agente con `--allow-admin-key` ya estaba limitado a loopback.
- **C6**: una excepción dentro de `comparar_y_promover` (después de un pipeline exitoso) sigue dejando la fila como "pipeline en curso"; quedó fuera del alcance pedido. Si Postgres está caído al insertar la fila (`write_reentrenamiento_log` devuelve `None`), no hay fila que actualizar y la periodicidad no se puede respetar, igual que antes.
- **C4**: con el breaker abierto, el evento de cierre de sesión (`SESSION_ENDED`) también va al buffer y se pierde si el agente no vuelve a arrancar antes del TTL. Antes se intentaba un POST, que de todos modos fallaba con la key muerta.
- **CLAUDE.md**: se actualizaron los bullets de tier agente (C2), circuit breaker (C4), buffer (C5) y backup del reentrenamiento (C6), y las cifras de pruebas y cobertura.
- **Archivos temporales**: el worktree de CI, `playwright-core` y los logs quedaron fuera del repo (scratchpad / `%TEMP%`) y se borraron, o están en el scratchpad. `reports/cobertura/` está en gitignore.
