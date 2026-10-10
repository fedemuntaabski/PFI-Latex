21. Cifras finales de e75/entrega
Medidas el 2026-10-10 desde la raíz del repo, sobre e75/entrega en 4b1c218 (más este informe), con el entorno aislado de C0: SCORING_FAKE_REDIS=1, REDIS_URL=redis://127.0.0.1:1/0, SUPABASE_*/UPSTASH_*/SCORING_{API,ADMIN,AGENT}_KEY/SMTP_*/GEMINI_API_KEY vacías, IAM_PROVIDER=none, SCORING_DISABLE_SCHEDULER=1, -p no:cacheprovider -W ignore, .venv del repo.

1. Merge y push
e75/gate-rf21 rebaseada sobre origin/e75/entrega (sin commits nuevos del remoto desde el último push), merge fast-forward en e75/entrega y push de las dos ramas: d41faa5..4b1c218. Sin force.
Commits nuevos: 58fd902 (script de replay), 4b1c218 (test del reset + DEMO.md). Grep de "claude" en los mensajes = 0.
Decisión del autor: se acepta la equivalencia v1 por la prueba A/B.
2. Script de replay
scripts/analysis/replay_equivalencia_v1.py. Manda 800 eventos reales (2 uids de clean_valid_001, 400 c/u, por orden de aparición, fechas corridas en días enteros) por POST /eventos en proceso y calcula el MD5 de risk_score_hibrido, nivel_sugerido, accion_id, cobertura y explicacion. Se usa contra dos árboles de api/ (git archive <rev> api); --esperado compara el MD5.

Árbol	MD5	Salida
base 8b89e49 (sin feature set)	cfccf513	687 completa / 113 parcial; bajo 19, medio 546, alto 215, crítico 20; 8,99 a 91,54
e75/entrega actual	cfccf513	idéntica byte a byte (cmp)
El ac31d306 del informe 10 salió de otro script, perdido: no es comparable.

3. Reset: causa y arreglo
El código del reset no toca sesiones ni agent keys, así que no hubo nada que corregir.

POST /usuarios/{uid}/reset llama a reset_state(uid) (borra scoring:{uid}) y delete_notif_cooldown(uid). DELETE /usuarios/{uid} suma eventos recientes e historial del uid. No hay flushdb, KEYS ni borrado por patrón en api/app; list_uids (SCAN) solo lee y excluye session: y agent_key:.
Una sesión (scoring:session:{sha256(token)}) solo se borra con POST /auth/logout o al leerla vencida (8 h). La EC2 corre un solo worker.
Test nuevo api/tests/test_reset_conserva_sesion_y_agent_key.py (2 tests): login admin → agent key en Redis → uid con estado → reset (y, aparte, delete) con el token. Verifica que el uid desaparece, que las claves scoring:session:* y scoring:agent_key:* siguen idénticas, que GET /config/notificaciones con el mismo token da 200 y que require_agent_key sigue aceptando la agent key. Pasa.
Por qué falló el --no-notify del 18 (causa probable, no verificable sin los logs): en scripts/demo_exfil.py el reset (línea 121) y el PUT usan SCORING_ADMIN_KEY, pero el GET /config/notificaciones (línea 218) usa _api_key(), que prefiere SCORING_API_KEY. Una SCORING_API_KEY heredada de api/.env pisa el token de sesión y da 401. Un logout o un token vencido darían el mismo síntoma. Documentado en DEMO.md, con la receta (exportar ambas variables con la misma key o token vigente y desactivar notif_niveles desde el dashboard). demo_exfil.py no se tocó.
4. Tiempos del gate
Fuente	Tiempo
Medido en esta PC, vigente contra sí mismo	332 s (5,5 min)
Medido en esta PC, artifacts_v2 contra vigente	353 s (5,9 min)
Reportado por x5 (sesion_cierre_modelos_20261008.md)	7,4 min (dos corridas de puntuar.py de ~3,7 min)
Texto actual de la tesis	"unos 7,5 minutos"
Cada medición incluye las dos corridas de puntuar.py (candidato y vigente) más el cálculo de métricas. Texto sugerido: "entre 5,5 y 7,5 minutos, según la máquina".

5. Cifras finales (copiar a la tesis)
Suites
Suite	passed	skipped
API completa (con artefactos)	352	0
API como CI (data/feature renombrado, 4 --ignore de ci.yml)	328	15
Agente (agent/tests, Windows)	177	0
Archivos de test
Componente	Archivos
API (api/tests/test_*.py)	35
Agente (agent/tests/test_*.py)	14
Frontend (*.test.*)	0 (vitest no está en esta rama)
Cobertura (scripts/cobertura_local.ps1, exit 0, reports/cobertura/*/coverage.json)
Componente	Sentencias	Líneas cubiertas	% líneas	Ramas	Ramas cubiertas	% combinado
API (api/app, _score_common, _audit_common)	2465	2315	93,91	520	444	92,43
Agente	1116	997	89,34	300	251	88,14
TOTAL API + agente	3581	3312	92,49	820	695	91,05
Cuenta del total, a mano:

Sentencias: 2465 + 1116 = 3581. Líneas cubiertas: 2315 + 997 = 3312. % líneas = 3312 / 3581 = 92,49 %.
Ramas: 520 + 300 = 820. Ramas cubiertas: 444 + 251 = 695.
Combinado = (líneas cubiertas + ramas cubiertas) / (sentencias + ramas) = (3312 + 695) / (3581 + 820) = 4007 / 4401 = 91,05 %.
% líneas = líneas cubiertas / sentencias. % combinado es el que reporta coverage.py (percent_covered); la terminal del script imprime ese, por eso muestra 92 % y 88 %.
CI en GitHub
No se pudo consultar. gh no está instalado en esta PC y la API pública de GitHub responde 404 para este repo (privado). El estado de e75/entrega hay que mirarlo en la pestaña Actions o con gh run list --branch e75/entrega desde una máquina con gh autenticado. Se esperan los 3 jobs (frontend, api, infra) sobre 4b1c218; no se verificó. El job api corre con --cov-fail-under=85 y sin artefactos.

6. Migración 010
Corrida a pedido del autor el 2026-10-10 con el mismo archivo SQL vía psycopg2 (no hay psql en esta PC). Era un no-op: antes de correrla metricas_modelo ya tenía rol, metricas y motivo, y metrica_valor/cantidad_muestras ya eran nullable; el esquema quedó idéntico. 8 filas, todas con rol NULL (las del criterio viejo).