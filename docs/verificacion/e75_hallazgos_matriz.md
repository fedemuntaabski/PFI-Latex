# E75: correcciones de texto por hallazgos de la matriz de trazabilidad

Rama `e75/hallazgos-matriz` (desde `e75/cierre`). `e75/cap7-8-11-12` no toca requerimientos, producto, conclusiones ni el capítulo de la encuesta: no hubo conflicto.
Código leído (solo lectura) en rama `e75/matriz-trazabilidad`.

## Ítems aplicados (archivo:línea actual)

| Ítem | Archivo:línea | Resultado |
|---|---|---|
| 1a RF-19 | requerimientos.tex:159 | "…registrar los eventos crudos que recibe y, en cada reentrenamiento, exportar todos los acumulados (sin los de prueba y demostración) junto con el conjunto de datos original, como insumo del *pipeline* de reentrenamiento." |
| 1b CU-03 precondición | requerimientos.tex:340 | Se conservó "El reentrenamiento automático está habilitado y" y se reemplazó el resto: "…y hay eventos crudos registrados en la base; el planificador no comprueba que haya eventos nuevos desde el último entrenamiento." |
| 1c CU-03 paso 2 | requerimientos.tex:345 | "exporta los eventos crudos acumulados, junto con el conjunto de datos original, al formato…" |
| 1d 9.2.4 | producto.tex:93 | "exporta los eventos crudos acumulados, junto con el conjunto de datos original, y ejecuta…" |
| 2a RF-31 | requerimientos.tex:141 | "recibe el identificador del usuario, el puntaje, el nivel, las variables que lo explican y los eventos recientes de la alerta" |
| 2b, 2c 9.5 art. 12 | producto.tex:169 | columnas central y derecha según lo pedido |
| 3a, 3b 9.5 art. 9 | producto.tex:165 | "seis de las siete tablas… (`historial_scores` queda pendiente, sección~\ref{sec:modelo-datos})"; la sección del cap. 8 es `sec:modelo-datos` (datos.tex:193) |
| 4 CU-01 postcondición | requerimientos.tex:298 | según lo pedido |
| 5a RF-10 | requerimientos.tex:111 | lista: terminar_procesos, denegar_carpeta, terminar_y_denegar, suspender_proceso; alertar y notificar_admin sin confirmación |
| 5b CU-01 paso 6 | requerimientos.tex:286 | según lo pedido |
| 5c HU-03 c2 | requerimientos.tex:422 | según lo pedido |
| 5d | producto.tex:51 | "El agente la ejecuta y, si modifica el equipo, confirma el resultado:" |
| 6 Tabla 9.IV | producto.tex:257 | fila agregada (ver abajo la corrección) |
| 7 RNF-10 | requerimientos.tex:246 | según lo pedido; estado sigue "Implementado" |
| 8 pruebas | requerimientos.tex:163, producto.tex:138, conclusiones.tex:45 | 11 → **12** (ver abajo) |
| 9 RNF-08 | requerimientos.tex:242 | campos agregados |
| 10a | producto.tex:71 | "…más se apartan de los valores de la población de entrenamiento." |
| 11 | requerimientos.tex:69 y :139 | "tabla en la que la aplicación solo inserta"; "historial en el que la aplicación solo inserta" |
| 12 Tabla 4.X | requerimientos.tex:581 | "Transversal (CU-01, paso 4)" |

## Confirmado en el código
- **1**: `scripts/export_clue_combinado.py`: `fetch_eventos_crudos_payloads` lee todos los `eventos_crudos` (sin WHERE); `filtrar_payloads`/`motivo_exclusion` (:74-87) descartan replays de CLUE-LDS (por fecha), uids de fixtures/tests, uids numéricos y uids de demo; `construir_clue_combinado` (:~160-175) copia `clue.json` byte a byte y agrega los filtrados. Lo invoca `api/app/scoring/reentrenamiento_scheduler.py:201`. Matiz: el filtro también excluye replays del dataset CLUE-LDS, no solo "prueba y demostración".
- **2**: `api/app/scoring/notifications.py:222-254` (`_armar_datos_gemini`): usuario, nivel, score, hasta 10 eventos (hora, tipo, detalle) y explicación (feature, dirección, z_score). `detalle` (`hybrid_service.py:203-218`) es el archivo (eventos de archivo), el proceso (app_enabled/disabled) o `ip:puerto` (solo `public_share_accessed`). Es decir, "dirección y puerto remotos" aplica a ese tipo de evento.
- **5**: `agent/main.py:72-77` `ACCIONES_CONFIRMABLES` = terminar_procesos, denegar_carpeta, terminar_y_denegar, suspender_proceso.
- **6** `agent/enforcement.py:71-73,155-173`: sin `accion_id`, `apply` cae a `_apply_nivel`; `_alcanza` es acumulativo, así que **crítico ejecuta terminar y denegar**, no solo denegar. La descripción pedida ("crítico→denegar") no era exacta; escribí "alto→terminar, crítico→terminar y denegar". **Decidir si se acepta.**
- **8** `api/tests/test_gate_promocion.py`: `pytest --collect-only` (con `.venv` del repo; el Python global falla por `np.complex_`) reúne **13** casos: pasa_dentro_de_los_margenes, no_pasa_por_auc, no_pasa_por_fpr, decidir_en_el_borde_pasa, 5 failsafe, metricas_benchmark_sobre_scores_sinteticos, comparar_y_promover_hot_swap_y_registro[True/False], comparar_y_promover_failsafe_registra_solo_motivo. `test_metricas_benchmark…` prueba el cálculo de AUC/FPR, no el criterio; los otros 12 sí (los 3 de `comparar_y_promover` lo ejercitan vía promoción/rechazo). N = 12. El texto decía 11 y no coincidía con ninguna cuenta; si preferís contar solo los 9 de `evaluar_gate`, cambiarlo es trivial.
- **9** `agent/collectors.py:206` (`anterior` en el renombrado), :460-497 (`pid`, `ip_remota`, `puerto_remoto`, `agent_id` en params, `location.countryCode`, `isLocalIP`).

## Frenados / para decidir
- **10b BLOQUEADO**: "más se apartan de lo habitual" no existe en el capítulo de la encuesta (chapter04.tex) ni en ningún otro .tex. Solo estaba en producto.tex:71. Indicame dónde está o descartalo.
- **2d (regla 4, sin editar)**: producto.tex 9.6.2 (`sec:prompt-injection`): "Entrada" (~:266) no enumera lo enviado y "Quedan dos decisiones documentadas" (:~273) dice "Se envían nombres crudos de archivo y de proceso" sin mencionar identificador de usuario ni variables explicativas. Difiere de 2b.
- **Regla 4, no editadas**:
  - producto.tex:97 contiene otro "tiene 11 pruebas automatizadas" (quedó en 11, inconsistente con :138 que ahora dice 12). Pedí "producto.tex" en singular; edité :138. **Conviene cambiar también :97.**
  - arquitectura.tex:18: "El agente ejecuta la acción y confirma el resultado." (misma afirmación que 5).
  - HU-09 sin tocar, como pediste.

## Compilación (pdflatex+biber+pdflatex×2)
- Páginas: base `e75/cierre` recompilada = **264** (vos decías 263); ahora **266** (+2).
- Referencias "??" / undefined: 0.
- Overfull/Underfull: 329 → 330 líneas en el log (+1 neto); sobre la base hay 2 `Overfull \vbox` adicionales. No revisé visualmente en qué páginas caen; conviene mirar requerimientos y 9.5/9.IV.
- Tablas: no se arma ninguna nueva ni se pierde ninguna; todas son `longtable` y se parten entre páginas como antes. No hice inspección visual de cortes.
