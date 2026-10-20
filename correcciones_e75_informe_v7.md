# Informe de la tanda 7 (LaTeX) — correcciones E75

Rama `correcciones-e75-revision`. Dos commits, en español, sin trailers de coautoría, sin push:

- `9c757f8` — bloque T (texto).
- `150c5c1` — bloque D (diagramas).

## Paquetes usados

No se tocó el preámbulo ni se agregó ningún paquete. El cuerpo sigue sin cargar TikZ.

Los diagramas nuevos son archivos `standalone` aparte, en `images/diagramas/Cargar/`. Se compilan con `pdflatex` y cargan `estilos_uml.tex`, el mismo archivo de estilos de los originales (TikZ con las librerías que ya cargaba: `shapes.multipart`, `arrows.meta`, `positioning`, `fit`, `backgrounds`, `calc`). El documento principal solo incluye los PDF con `\includegraphics`, a través de `adjustbox` (cargado en `config/symbols.tex`) y `pdfpages`/`graphicx` del preámbulo. El preámbulo carga graphicx, pdflscape, titlesec, cmap, inputenc, fontenc, lmodern, biblatex, xurl, xcolor, framed, placeins, microtype, anyfontsize, enumitem, lastpage, titleps, textcase, pdfpages, vmargin, todonotes, etoolbox, pdfcomment, babel, csquotes, indentfirst, multicol, multirow, array, longtable, mathptmx, amsmath, amsfonts, amssymb, amsthm, cancel, ulem, setspace, tocloft, hyperref y adjustbox.

## Bloque T

- **T1** (9.2.7, `chapters/producto.tex`): se reemplazó la oración por el texto indicado, con `\ref{sec:estado-despliegue}`. La fila de la tabla "Clave de administración aceptada en el nivel de agente" ya decía "Corregido en el código; pendiente de publicar en la instancia", así que no hubo contradicción y no se tocó.
- **T2** (después de la tabla 8.II, `chapters/datos.tex`): se agregó el párrafo. Se verificó contra la sección 2 (C1) de `informe_fixes_e75.md`: el 0,1180 solo se carga para el chequeo de `/health`, y la regla de producción es `lstm_risk_user > 95`, donde `lstm_risk_user` es el percentil de la media de error del usuario contra la referencia de entrenamiento. **Ajuste de redacción:** donde el prompt decía "riesgo acumulado del usuario" escribí "error medio de reconstrucción del usuario, expresado como percentil respecto de la distribución de referencia del entrenamiento", que es lo que dice el informe. Los `\ref` apuntan a `sec:metricas-no-supervisadas` (10.5.1) y `sec:benchmark-controlado` (10.7.6). La fila "Criterio de detección" de la tabla 8.II, 10.5.1 y 10.7.6 no se modificaron: 10.7.6 ya habla de "un riesgo mayor que 95 para el LSTM" y 10.5.1 describe el umbral como percentil 95 del entrenamiento, consistente con la nueva oración.
- **T3** (10.2.3, `chapters/pruebas.tex`): "En la última corrida registrada, el *pipeline* finaliza con los cuatro trabajos aprobados."

## Bloque D: vistas de diseño

Texto efectivo en página = tamaño de fuente del PDF × escala con la que entra en el cuerpo (ancho `\textwidth` y alto máximo `0.8\textheight`). Los valores están medidos sobre el `main.pdf` compilado (fuente más chica de cada página con diagrama).

| Fig. | Archivo nuevo (`images/diagramas/uml/`) | Texto mínimo efectivo | Clases / nodos incluidos | Omitidos |
|---|---|---|---|---|
| 6.1 | `01v_flujo_informacion_diseno.pdf` | **7,1 pt** | 6 carriles (contingencia, agente, API, persistencia, externos, dashboard) y banda de reentrenamiento offline; 31 cajas, una frase corta cada una | Se quitaron los rótulos de protocolo de las flechas internas. Quedan HTTPS, "sí" y "misma respuesta". No están las flechas `push_recent_event`, `save_state`, las lecturas del dashboard a Redis/Postgres ni el hot-swap de artefactos |
| 6.2 | `02v_componentes_protocolos_diseno.pdf` | **7,05 pt** | Analista SOC, Endpoint Windows (agente), EC2 (Caddy, dashboard estático, API, Keycloak), Redis/Upstash, PostgreSQL/Supabase, Gmail SMTP, Google Gemini, Microsoft Entra ID, SSM Parameter Store, S3, estación de desarrollo (pipeline offline); solo protocolos en las flechas | Usuario monitoreado, DEMO_ROOT, SO Windows, artefactos de modelo, `manage_agent_key`, `iam_mock`, API local |
| 6.3 | `03v_clases_agente_pep_diseno.pdf` | **7,16 pt** | AgentConfig, main, ScoringClient, event_buffer, colectores (los cuatro nombres), Debouncer, EventFactory, Enforcer, Signal, EnforcementPolicy | `config`, `api_client`, `_FileState`, `collectors`, `process_filter`, `enforcement`, `RevertOutcome`, `requests.Session`, `psutil`, `icacls.exe` |
| 6.5 | `04av_clases_api_estado_diseno.pdf` | 9,4 pt | UserScoringState, ContinuityState, LstmState, IsoDayState, HybridAnchorState, PersonalBaselineState, WelfordStat, redis_state, Redis | `_InMemoryRedis`, `_InMemoryPipeline` (dobles de prueba) |
| 6.6 | `04bv_clases_api_scoring_diseno.pdf` | 8,4 pt | hybrid_service, isoforest_service, lstm_service, coverage, explainability, Artifacts, artifacts | `personal_baseline_service`, `drift_service`, `features` y las clases de resultado |
| 6.7 | `04cv_clases_api_iam_auth_diseno.pdf` | 7,6 pt | iam_service, IAMProvider, Mock/Keycloak/Entra/ChainIAMProvider, iam_providers, auth | `_KcCfg`, `_EntraCfg`, `dedup_service`, `notifications` |
| 6.8 | `04dv_clases_api_persistencia_config_diseno.pdf` | 7,4 pt | main, routes, reentrenamiento_scheduler, config_store, history_store, metricas_service | `paths`, SQLAlchemy y las tablas de Postgres |
| 6.9 | `04ev_clases_api_schemas_diseno.pdf` | 7,4 pt | EventoIn, EventoScoreOut, FeatureContribucion, ConfirmarAccionIn/Out, EventosRecientesOut, EventoRecienteItem, UsuariosListOut, UsuarioResumen | las otras 30 clases de esquemas (historial, umbrales y configuración, auditoría, reentrenamiento, deriva, salud, login, IAM) |

- Las relaciones entre las clases que quedaron se conservan con la misma semántica: composiciones con multiplicidad, «usa», «crea», realización y agregación del compuesto IAM. En 6.3, la creación de Debouncer, EventFactory y Enforcer por `main`, que el original solo mostraba en una nota, ahora es una flecha «crea». En 6.7 las cuatro realizaciones comparten un solo triángulo hacia `IAMProvider`.
- Cada clase tiene como máximo 3 miembros, sin tipos, valores, constantes ni rutas.
- **6.4 (vista de paquetes) no se tocó.**
- Se mantuvieron los `\label` de las figuras del cuerpo. En el Anexo H las figuras de la versión completa conservan sus labels `fig:anexo-*` (de 6.1, 6.2, 6.3 y 6.5) y se agregaron `fig:anexo-clases-{scoring,iam,persistencia,schemas}-{izq,der}` para 6.6 a 6.9.
- Los epígrafes del cuerpo terminan en "(vista de diseño)". Cada párrafo de figura termina con "La versión completa, con todos los atributos y operaciones, se presenta en el Anexo H." Se agregó la frase en 6.6 a 6.9, que no tenían ninguna mención al Anexo H.
- Consistencia con el texto: se verificó una por una la presencia de las clases que nombra el párrafo de cada figura.
  - 6.3: AgentConfig, los cuatro colectores, Debouncer, EventFactory, ScoringClient (el *circuit breaker* es `breaker_open`), el *buffer* local (`event_buffer`) y Enforcer, que revierte con `revert()`.
  - 6.5: UserScoringState y las cinco partes, más Welford.
  - 6.6: los servicios de Isolation Forest y del LSTM, la combinación híbrida, la cobertura, la explicación y los artefactos.
  - 6.7: IAMProvider con Mock, Keycloak y Entra, y las clases de autenticación (`auth`).
  - 6.8: rutas, `history_store`, `config_store` y el planificador con `metricas_service`.
  - 6.9: EventoIn, EventoScoreOut y ConfirmarAccionIn/Out.
  - 6.1: en la caja de la API agregué "valida el esquema" para que el párrafo se cumpla.
- Se actualizaron el párrafo de apertura de la sección 6, la introducción del Anexo H ("versiones completas… de las que el cuerpo muestra una vista de diseño") y la mención en 1.5.

## Anexo H

Pasó de 4 a 8 diagramas, 16 páginas (+8). Las versiones completas de 6.6 a 6.9 usan los PDF originales sin modificar, cortados por la mitad con `trim` (anchos: 04b 1599,41 pt; 04c 1287,26; 04d 1341,94; 04e 1493,56). Los epígrafes tienen la forma "…, versión completa (mitad izquierda/derecha)".

Las mitades del anexo siguen con texto chico, porque el original fue dibujado a gran escala. Con el criterio "como ahora", queda en unos 3 a 6 pt. La versión vectorial permite ampliarlas. El texto legible está en las vistas de diseño.

## Verificación

- `latexmk -C` y `latexmk -pdf main.tex` desde cero; `main.dvi` restaurado con `git checkout`. Sin "Rerun" y sin referencias o citas indefinidas en `main.log`. Quedan los avisos de siempre (`h` → `ht`, `usenames`, `microtype`).
- 283 páginas (antes 273): 281 con numeración, y el pie "Página X de N" muestra N=281 en todas. Esa diferencia de 2 con el total existe también en la versión anterior (252 páginas, N=250).
- Índice, listas de figuras y de tablas: las entradas de la sección 6 (6.1 a 6.9) y del Anexo H (H.1 a H.16) apuntan a las páginas correctas. Las advertencias del script de comprobación (índice 5, figuras 15, tablas 2) son falsos positivos de coincidencia de texto: títulos de las imágenes de la encuesta (el texto está en la imagen), guiones largos `---`, `\%`, la ligadura "Bibliograf' a", "Anexo".
- Imágenes de revisión en `revision_diagramas/` (páginas 96 a 104 del PDF, a 100 dpi; **sin commitear**).

## Puntos a revisar por el autor

1. **Página de 6.1.** La vista es vertical y de página completa. Como no entra debajo del título y el párrafo de la sección, se pasa a la página siguiente y la página con el título queda con la mitad de abajo vacía. Se puede mover el párrafo o forzar un salto si molesta.
2. **Texto en las vistas.** Las vistas quedan entre 7,05 y 9,4 pt. 6.2 y 6.1 son las más ajustadas.
3. **Párrafos de 6.6 a 6.9.** Los párrafos aparecen antes que las figuras porque las figuras ocupan una página y flotan.
4. El informe `informe_fixes_e75_ronda2.md` aparece sin seguimiento en el repo. No lo toqué.
5. Este informe quedó sin commitear.
