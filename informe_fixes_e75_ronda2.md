# Informe de correcciones E75, ronda 2

Fecha: 2026-10-20. Rama `fix/e75-limitaciones-menores` (sobre `f4111a4`). Partes A y B1–B3 hechas; B4 (push), C y D no autorizadas todavía.

## 1. Commits nuevos

| Commit | Mensaje |
|---|---|
| `b01b538` | fix(scheduler): registrar como fallido el reentrenamiento cuando falla la comparación del modelo |
| `580511a` | refactor(agente): quitar el mapeo de respaldo nivel→acción que la API nunca activa |
| `d8d0edd` | test(agente): con el circuit breaker abierto el cierre de sesión se bufferiza y vence con la vigencia de 3 horas |
| (este) | docs: informe de la ronda 2 |

`git log --format=%B f4111a4..HEAD`: cero coincidencias de `Co-Authored-By`, "Generated with" o "Claude". Ninguna atribución.

## 2. Parte A

**A1 (hecho).** `reentrenamiento_scheduler.py`: la llamada a `comparar_y_promover` ahora va en un `try/except` que llama `_registrar_fallo("excepción en la comparación …")` y relanza. Mismo mecanismo de la ronda 1 (prefijo `fallido: ` en `variacion_metrica`, sin tocar el esquema). Prueba nueva `test_excepcion_en_la_comparacion_registra_fallido_restaura_y_respeta_la_periodicidad` (`api/tests/test_reentrenamiento_backup.py`): pipeline simulado exitoso + excepción en la comparación → fila `fallido: excepción…`, artefactos restaurados (hashes iguales), y el `_tick` siguiente no dispara otro intento. Falló antes del cambio (fila quedaba "pipeline en curso"); pasa después. Los artefactos ya se restauraban por el `finally`.

**A2 (hecho, eliminado).** El mapeo de respaldo vivía en `agent/enforcement.py` (`NIVEL_ORDEN`, `NIVEL_TERMINAR_PROCESO`, `NIVEL_DENEGAR_CARPETA`, `_alcanza`, `_apply_nivel`) y se usaba solo si la respuesta no traía `accion_id` (`apply()` y `main.py`). La API siempre asigna `accion_id` en `POST /eventos` (`hybrid_service.py:403`; si falta mapeo cae a `alertar`). Ningún script importa esas constantes (los `NIVEL_ORDEN` de `scripts/` son definiciones propias; `generar_word_agente_pep.py` solo cita el código en texto). La única prueba que lo tocaba usaba un enforcer falso (`test_main_loop.py`) y se reescribió. Ahora, sin `accion_id` (solo `nivel`) no se ejecuta nada; `main.py` retorna si `accion_id is None`. Pruebas nuevas en `agent/tests/test_confirmacion_estado.py` con el `Enforcer` real: `apply(nivel)` y `apply(nivel, None)` → `[]` para `bajo/alto/critico/extremo` (fallaban en `alto` y `critico`: terminaban un proceso y denegaban la carpeta), y `apply("critico", "formatear_disco")` → `[]` con log "desconocida". Se actualizaron CLAUDE.md y el glosario (riesgo residual del fallback). Los snapshots en `docs/agente/` quedan como están (históricos).

**A3 (confirmado, sin cambio de código).** Prueba `test_breaker_abierto_session_ended_se_bufferiza_y_vence_con_la_vigencia_de_3_horas`: con el breaker abierto, `SESSION_ENDED` va al buffer sin HTTP; a 2,9 h se reenvía y a 3,1 h `flush_pending` lo descarta por TTL vencido (3 h por defecto), igual que cualquier otro evento. Frase para el documento: *con el circuit breaker abierto el evento de cierre de sesión se bufferiza como cualquier otro y se pierde si la API no vuelve dentro de las 3 horas de vigencia, parte de la limitación ya declarada de RNF-05.*

## 3. Parte B

**B1. Pruebas omitidas en la configuración de CI.** Árbol limpio de `HEAD` (`git archive`, sin artefactos), mismos comandos y 4 archivos ignorados del job `api`: **445 pasadas, 23 omitidas, 0 fallidas** (468 recogidas).

| Motivo | Omitidas |
|---|---|
| Requieren los modelos entrenados (artefactos no versionados) | 16 |
| Verifican la paridad de features con la segunda versión del modelo (sin `artifacts_v2/` ni `data/processed/`) | 3 |
| Otras: salidas del benchmark controlado (`data/benchmark/controlado`) | 3 |
| Otras: salidas de Fase 6 | 1 |
| **Total** | **23** |

(16 = `test_cu04_aprendizaje` 5, `test_iam_eventos` 4, `test_e2e_pdp_pep` 2, `test_score_confirmacion` 2, `test_config_auth_y_validacion` 1, `test_config_umbrales_put` 1, `test_eventos_recientes_explicacion` 1.)

**B2. Archivos de prueba.** Criterio: `test_*.py` dentro de `api/tests` y `agent/tests`, recursivo, sin `conftest.py` ni `__init__.py`. **API 44, agente 15** (la tabla 10.II dice 39 y 14: desactualizada; con cualquier `*.py` que no sea `conftest`/`__init__` serían 60 en total).

**B3. Números finales** (`scripts/cobertura_local.ps1`, con artefactos, Windows):

| | API | Agente | Total |
|---|---|---|---|
| Pruebas | 477 aprobadas, 0 omitidas, 0 fallidas | 190 aprobadas, 0 omitidas, 0 fallidas | 667 |
| Sentencias | 2808 | 1107 | 3915 |
| No cubiertas | 147 | 91 | 238 |
| Cobertura de líneas | 94,76 % | 91,78 % | 93,92 % |
| Líneas y ramas | 93,51 % | 91,09 % | 92,81 % |

Total = suma aritmética de ambos componentes (el script no lo emite). Meta ≥ 85 % de líneas cumplida en ambos.

Configuración de CI (árbol limpio, sin artefactos, alcance `--include` del workflow): 2808 sentencias, 323 no cubiertas, **88,50 % de líneas, 87,11 % combinado**; `coverage report --fail-under=85` aprobado. El job `agent-windows` corre las 190 del agente (aprobadas localmente).

**B4. GitHub Actions.** Verificado: ningún commit nuevo con atribución; `ci.yml` se dispara con `push:` sin filtro de ramas. **Push no autorizado todavía**: resultado de los 4 trabajos pendiente.

## 4. Parte C

No autorizada (no se pidió). Sin capturas ni borrado de uids.

## 5. Parte D

No autorizada.

## 6. Efectos colaterales

- CLAUDE.md y `docs/general/glosario_dominio.md` editados (riesgo residual del fallback del agente).
- Un test nuevo del agente (`apply("critico")` sobre `Enforcer` real) llama a `icacls` en un directorio temporal de pytest durante su ejecución en rojo; ya no ocurre tras el cambio.
- Árbol temporal `ci_tree` en `%TEMP%` (copia de `HEAD` para B1) y `reports/cobertura/` regenerado (gitignorado). Nada en Redis, Supabase ni artefactos de modelo.
