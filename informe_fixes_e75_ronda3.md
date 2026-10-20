# Informe ronda 3 — CI y capturas del dashboard (2026-10-20)

Rama `fix/e75-limitaciones-menores`. No se tocó código de producción, modelos, umbrales ni Postgres directamente.

## Parte 1 — Integración continua

- Trailers: `git log f4111a4..HEAD` sin `Co-Authored-By`, "Generated with" ni "Claude".
- Remoto `origin` = `fedemuntaabski/Agente-...-Identidad`. La rama ya existía en el remoto en `bf2d70d`; `git push` (autorizado) devolvió `Everything up-to-date`. `main` no se tocó.
- `gh` 2.102.0 instalado con winget y autenticado (cuenta SantiagoMo65).

| Commit | Corrida | frontend | api | agent-windows | infra |
|---|---|---|---|---|---|
| `bf2d70d` | [39465070290](https://github.com/fedemuntaabski/Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad/actions/runs/39465070290) | ✓ | ✓ | **✗** | ✓ |
| `605cca3` | [39476821123](https://github.com/fedemuntaabski/Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad/actions/runs/39476821123) | ✓ | ✓ | **✓** | ✓ |
| `388d43d` | 39456012013 | ✓ | ✓ | **✗** | ✓ |
| `f4111a4` | 39454516867 | ✓ (corrida verde completa) | | | |

**Causa de `agent-windows`**: falla en `actions/checkout` del runner Windows, antes de correr tests: `unable to create file ml_core/reports/auditoria_pre_score_hibrido/03_normalizacion_scores/scores_normalizados_isoforest.csv: Filename too long`. El commit `388d43d` (mensaje "."; 20/10) reincorporó 36 archivos bajo `ml_core/reports/`, carpeta que CLAUDE.md da por eliminada el 2026-10-17. Ninguna referencia en código; solo en docs.

**Arreglo** (elegido por el autor): commit local `605cca3` (`git rm -r ml_core`, mensaje en español sin trailers). Pusheado con autorización del autor (`bf2d70d..605cca3`): **los 4 trabajos pasan** en la corrida 39476821123.

## Parte 2 — Capturas

Entorno: API local `127.0.0.1:8001` (Redis Upstash y Supabase reales, `reentrenamiento_automatico=false`), dashboard Vite en `127.0.0.1:5173`. Las capturas se tomaron con Playwright (`playwright-core` en carpeta temporal, Chromium 1234), 1440×900, tema oscuro, entrando por `http://localhost:5173` (la API solo permite ese origen en CORS). Carpeta `capturas_e75/` en la raíz, **sin commitear** (no está en `.gitignore`: no usar `git add -A`).

### Estado vivo

Borrados con `DELETE /usuarios/{uid}` (204), confirmados por el autor: `197608`, `197609`, `agentid-verify-uid`, `catalogo-acciones-demo`, `demo-conexion-red`, `drift-fase2b-test`, `drift-fase2b-test-broken`, `smoketest-aprendizaje-1788116888`, `usuario-normal-demo`. Se conservaron `demo-pfi` y `FEDE-PC-FEDE` (el autor no los marcó para borrar).

Actividad generada con un script propio (scratchpad, `POST /eventos` con la admin key local, sin agente, por lo que no hubo enforcement): no se usaron `demo_exfil.py`/`caso_*` (lanzan el agente real). Usuarios resultantes:

| uid | Nivel | Score | Eventos | Aprendizaje |
|---|---|---|---|---|
| IT-PC-jrodriguez | Crítico | 98,5 | 17 | sí (17/21) |
| FINANZAS-PC-dsosa | Alto | 77,3 | 5 | sí (5/21) |
| RRHH-PC-acastro | Alto (regla piso) | 50,5 | 90 | no |
| VENTAS-PC-lperez | Medio | 45,5 | 64 | no |
| ADMIN-PC-mgarcia | Bajo | 37,8 | 24 | no |
| demo-pfi (previo) | Alto | 77,3 | 41 | no |
| FEDE-PC-FEDE (previo) | Alto | 48,2 | 17 | sí |

Notas: `lperez`, `mgarcia` y `acastro` tienen 3 días cerrados en `historial_scores` (`jrodriguez` 1). El crítico es un usuario nuevo (en aprendizaje): con historial previo el blend personal (hasta 70 %) lo mantenía en ~50. Umbral de aprendizaje cambiado 21→22→21 (dos entradas de auditoría, actor `sesion-admin-96474218`). Los usuarios nuevos **no se borraron**.

### Tabla de capturas

| Archivo | Pantalla | Qué muestra |
|---|---|---|
| `01_login.png` | `/login` | Formulario "Acceso a configuración" (usuario, contraseña, Entrar), vacío. |
| `02_usuarios.png` | `/` | Título "Usuarios (7)", "7 de 7 usuarios". Niveles: 1 Crítico, 4 Alto (FEDE, FINANZAS, RRHH, demo-pfi), 1 Medio, 1 Bajo. 3 en aprendizaje (jrodriguez 17/21, FEDE 17/21, dsosa 5/21). Badges "Sin reportar" en 5 usuarios (demo-pfi: hace 7121 min). Cobertura "Parcial" en todos. |
| `03_detalle.png` | `/usuarios/IT-PC-jrodriguez` | Crítico, score 98,5, "En aprendizaje (17/21)", Parcial. Histórico: "Todavía no hay días cerrados". Eventos recientes: 17 en total (se ven 3 completos y el cuarto cortado). Última acción confirmada: —. |
| `04_explicacion_arriba.png` | `/usuarios/IT-PC-jrodriguez/explicacion`, arriba | "En resumen" (Crítico, 98,5 de 100, nivel desde 90; acción solo alertar; 17 de 21 eventos), "Cómo evolucionó el riesgo" con gráfico de 17 eventos (de Alto 86,9 a Crítico 98,5). |
| `05_explicacion_senales.png` | misma vista, desplazada | Gráfico, "Señales que se desviaron" (3: países, fuera de horario, hora promedio), aviso de calibración (sin modelo de secuencias), sección "Acción": alertar. |
| `06_alertas.png` | `/alertas` | "Alertas (5)": jrodriguez Crítico; FEDE, FINANZAS, RRHH, demo-pfi Alto. Botón Reconocer en cada fila. |
| `07_umbrales_arriba.png` | `/umbrales`, arriba | Umbrales por nivel 0–40/40–60/60–90/90–100; Acción por nivel (Alertar ×3, Terminar y denegar en Crítico); Periodicidad 30 días, ventana 02:00-04:00; Umbral de aprendizaje 21. |
| `08_umbrales_abajo.png` | `/umbrales`, desplazada | Notificación por email (Medio activo, 2 emails de admin visibles), Proveedores de identidad ("Ninguno configurado", rige `IAM_PROVIDER` none), Log de reentrenamientos (formulario + primeras entradas: `test-rev75 no usar`, `x`). |
| `09_auditoria.png` | `/auditoria` | 50 entradas en total (8 visibles): 2 de umbral de aprendizaje (22→21, 21→22, 20/10), notificaciones, proveedores IAM (3 con texto `[object Object]`), periodicidad, acción por nivel. |
| `10_salud.png` | `/salud` | "Saludable"; Artefactos cargados Sí, Estado en vivo OK, Historial OK; 8 artefactos todos OK (isolation_forest, scaler_isoforest, lstm_autoencoder, scaler_lstm, type_encoding, lstm_threshold, config_score_hibrido, train_references). |
| `11_historial.png` | `/historial` | "Usuarios con historial (9)": ADMIN-PC-mgarcia, VENTAS-PC-lperez, RRHH-PC-acastro, demo-pfi y 5 uids de prueba/CLUE que están en Postgres (ver abajo). |

### Lo que el documento debe tener en cuenta

1. **Uids de prueba todavía visibles** en `11_historial.png`: `big-maroon-lynx-radiocontroller`, `digital-harlequin-possum-procuratorfiscal`, `structural-teal-starfish-homeeconomist`, `test-hu15-explicacion-uid`, `test-hybrid-backdated-uid`. Salen de Postgres (`historial_scores`), que esta ronda no podía tocar; borrar el estado vivo no los quita. Lo mismo con las entradas `test-rev75 no usar` y `x` del log de reentrenamientos (`08`) y los `[object Object]` de la auditoría (`09`, entradas del 15/10; defecto de visualización de la auditoría de IAM, no corregido).
2. `demo-pfi` y `FEDE-PC-FEDE` siguen en el listado, la lista de alertas y el estado; `FEDE-PC-FEDE` es un host real. Si no deben aparecer, hay que borrarlos y volver a capturar `02` y `06`.
3. `08` muestra dos correos reales de administradores.
4. En `02`, cinco filas muestran "Sin reportar hace N min" porque la actividad se generó por API sin agente; las capturas deben tomarse sin demora.
5. El usuario crítico está en aprendizaje (la acción mostrada es "alertar", ablandada); no hay un crítico maduro.
6. Postgres: los `POST /eventos` escribieron en `eventos_crudos` e `historial_scores` a través de la API (inevitable). `GET /usuarios` tarda ~5,4 s con Redis remoto; las capturas esperan a que desaparezca "Cargando".
7. Nada de esto se probó contra AWS: la instancia corre la release `20261015-143709-b499fa3` (anterior a las rondas 1–2), usa autenticación estricta y p95 ≈ 3 s por evento.
