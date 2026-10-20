# Informe de correcciones E75 — tanda 2

Rama: `correcciones-e75-revision`. Sin push. Solo contenido; sin cambios de preámbulo, estilos, numeración ni paquetes. No se tocaron 1.1.1, 1.2 ni 1.3; en 1.1.2 solo el cambio puntual de P2-D.

## Cambios aplicados

| ID | Archivo | Estado |
|---|---|---|
| P1-A (1) cap. 4 | chapters/requerimientos.tex (tras `\label{chap:requerimientos}`) | Aplicado |
| P1-A (2) cap. 6 | chapters/e50_uml.tex (tras `\chapter`); con `\ref` a las figuras en vez de números literales | Aplicado |
| P1-A (3) cap. 7 | chapters/arquitectura.tex | Aplicado |
| P1-A (4) 7.3 | chapters/arquitectura.tex (`sec:frameworks`) | Aplicado |
| P1-A (5) 7.5 | chapters/arquitectura.tex (`sec:despliegue`) | Aplicado |
| P1-A (6) 8.3 | chapters/datos.tex (`sec:variables-modelos`) | Aplicado |
| P1-A (7) cap. 9 | chapters/producto.tex | Aplicado |
| P1-A (8) 9.2 | chapters/producto.tex (`sec:funcionalidades`) | Aplicado |
| P1-A (9) cap. 10 | chapters/pruebas.tex | Aplicado |
| P1-A (10) 10.2 | chapters/pruebas.tex (`sec:pruebas-automatizadas`) | Aplicado |
| P1-A (11) 10.4 | chapters/pruebas.tex (`sec:pruebas-rendimiento`) | Aplicado |
| P1-A (12) 10.6 | chapters/pruebas.tex (`sec:validacion-escenarios`) | Aplicado |
| P1-A (13) 12.5 | chapters/negocio.tex (`\section{Identidad de marca}`) | Aplicado |
| P1-A verificación | script sobre chapter01, 02, 04, requerimientos, e50_diseno_ux, e50_uml, arquitectura, datos, producto, pruebas, e50_mercado, negocio, conclusiones | Ningún encabezado queda seguido directamente por otro. |
| P1-B figs. 6.3 a 6.9 | chapters/e50_uml.tex | Aplicado, con `\ref` a cada label existente (no hizo falta agregar labels). Ver nota 1. |
| P1-B2 epígrafe 6.10 | chapters/e50_uml.tex | Aplicado: `uid DESKTOP-DEMO-usuario1` (coincide con `05_objetos_evento.tex`). |
| P1-C | chapters/arquitectura.tex (7.6) | Aplicado |
| P1-D 2.2.5.4 | chapters/chapter02.tex | Aplicado, con `\parencite{Artioli2024, Landauer2023Survey}` (la clave del .bib es `Landauer2023Survey`, no `Landauer2023`). |
| P1-D tiempos verbales (6 cambios) | e50_mercado.tex, pruebas.tex (x4), negocio.tex | Aplicado. |
| P1-E 3.6.6 | chapters/chapter04.tex | Aplicado |
| P1-E FODA | images/diagramas/tikz/foda.tex | Aplicado |
| P2-A | chapters/conclusiones.tex (texto de 13.1 y fila 6 de la tabla 13.I) | Aplicado |
| P2-B | pruebas.tex (3 frases de 10.9), producto.tex (tabla 9.IV) | Aplicado. La referencia "sección 10.3" usa `\ref{sec:pruebas-e2e}`. |
| P2-C | chapters/pruebas.tex (10.4.2) | Aplicado; "sección 9.3" con `\ref{sec:estado-despliegue}`. |
| P2-D | chapter01.tex (objetivo 3) y conclusiones.tex (fila 3 de la tabla 13.I) | Aplicado |
| P2-E | chapters/producto.tex (tabla 9.IV): "Alcance de la observación" (grupo Agente local) y "Eventos incorporados sin revisión" (grupo Reentrenamiento) | Aplicado; "sección 2.1.7.2" con `\ref{sec:estrategias-drift}`. |
| P2-F | chapters/pruebas.tex (lista de 10.10) | Aplicado |
| P2-G | chapters/chapter04.tex (3.5.1) | Aplicado; "sección 12" con `\ref{chap:negocio}`. |
| P2-H | chapters/chapter04.tex (tablas 3.XIV y 3.XV) | Aplicado; "sección 10.7.4" con `\ref{sec:lectura-benchmark}`. |
| P2-I | chapters/chapter04.tex (3.2) | Aplicado |
| P2-J | negocio.tex (párrafo nuevo tras el de la tasa de descuento en 12.4.1; fila del impuesto), e50_mercado.tex (plan Enterprise) | Aplicado; "sección 13.3" con `\ref{sec:trabajo-futuro}` y "sección 9.2.5" con `\ref{sec:reentrenamiento-producto}`. |
| P2-K | chapters/chapter02.tex (2.1.6) | Aplicado. 2.1.7.2 se mantiene, como se pidió. |
| P3-A | chapters/e50_uml.tex | **No aplicado.** Ver nota 2. |
| P3-B | chapters/appendix/interview_1_pablo.tex (6 casos), interview_4_pena.tex (7 casos) | Aplicado, 13 casos. Ver nota 3. |
| P3-C | solo propuesta | Ver nota 4. |

## Notas

1. **Verificación de las clases citadas (P1-B).** Se abrieron los `.tex` fuente de cada diagrama (`images/diagramas/Cargar/*.tex`) y existen todos los nombres citados: `AgentConfig`, `Debouncer`, `EventFactory`, `ScoringClient` (con `breaker_open`), `Enforcer`, los cuatro colectores, `UserScoringState` y sus componentes (incluido `WelfordStat`), `hybrid_service` (con `regla_piso_aplicada` y `vida_media_dias`), `coverage`, `explainability`, `Artifacts` (`reload_artifacts`, hot-swap), `IAMProvider` con `MockIAMProvider`, `KeycloakIAMProvider` y `EntraIAMProvider`, `auth` (sesiones y claves de agente), `history_store`, `config_store`, `reentrenamiento_scheduler`, `metricas_service`, `EventoIn`, `EventoScoreOut` y `ConfirmarAccionOut`. No hubo que ajustar ningún párrafo. Detalles menores: en el texto del párrafo de 6.3 los nombres de clase van en `\texttt`; en el de 6.5, `UserScoringState` lleva puntos de corte (`User\-Scoring\-State`) para evitar un overfull.
2. **P3-A, revertido.** Se probó `\adjustbox{..., angle=90}` sobre las figuras 6.1, 6.2, 6.3 y 6.5 (el diagrama gira y las limitaciones de tamaño se invierten). La ganancia de escala es de solo 27 a 37 %: la 6.3, por ejemplo, pasa de 0,30 a unos 0,38. Además, la figura 6.1 ya no entraba debajo del encabezado y su texto, por lo que la página 90 quedaba casi vacía y los diagramas quedaban de costado. Por eso se revirtió y no hay cambios de P3-A. Para lograr legibilidad real hay que simplificar o dividir los diagramas (en especial el 6.3, de 1494 x 1181 pt), no rotarlos.
3. **P3-B.** El prompt estimaba unos 16 cortes; el patrón dio 13 en las transcripciones: interview_1_pablo (6: "porque. No", "que. Si", "porque. Siempre", "porque. Tienen", "de. Bueno", "de. Del") e interview_4_pena (7: "de. Ya", "de. Inspección", "un. Un", "el. Cómo", "se. Se", "de. De", "un. Es"). Se cambió el punto por "…" y la mayúscula por minúscula, sin tocar palabras. Se excluyó "así per se. Existen" (interview_3_guillermo), que es un final de oración legítimo. Interview_2 e interview_5 no tenían coincidencias; si el autor ve otros cortes con otra forma, no los detectó la regex.
4. **P3-C (propuesta, no aplicada).** Redacción en positivo:
   - HU-02: "el nivel no debe quedar por debajo del piso" → "el nivel se mantiene en el piso o por encima de él, que por defecto es alto".
   - HU-03: "al usuario que mantiene la sesión abierta no debe solicitársele un nuevo inicio de sesión" → "el usuario que mantiene la sesión abierta continúa sin repetir el inicio de sesión".
   - HU-14: "Un usuario sin sesión iniciada no debe acceder al dashboard" → "El dashboard solo es accesible para un usuario con sesión iniciada".
   - HU-15: "un reentrenamiento posterior no debe recalcular las explicaciones ya guardadas" → "tras un reentrenamiento posterior, las explicaciones ya guardadas se conservan sin cambios".
5. **Verbos del equipo en pretérito (P1-D), sin cambiar** (secciones 1 a 13, patrón sobre las formas "se + pretérito" más frecuentes):
   - chapters/arquitectura.tex:28 (cap. 7.2): "Se descartó un *backend* en Node.js porque…".
   - chapters/producto.tex:89 (9.2.5): "…se evaluaron con la regla anterior y ninguno se promovió".
   - chapters/pruebas.tex:237 (10.4.3): "…se verificaron en sesiones previas sobre la misma instancia…" (verificaciones previas con fecha; el autor debe decidir si es una descripción de hechos pasados o de la prueba).
   - chapters/requerimientos.tex:302: "no verifica si se incorporaron eventos nuevos…" (subordinada; probablemente correcta).
   La búsqueda cubre solo verbos de una lista fija; puede haber otros casos con verbos no incluidos.
6. **Menciones restantes a "demostración".** Solo se cambiaron las cuatro frases del prompt; la frase de 10.3 ("reproduce el guion de la demostración") y el renglón "Scripts de demostración y ensayo" de la tabla de estrategia de pruebas se dejaron como estaban.

## Compilación

`latexmk -pdf main.tex` (MiKTeX), 258 páginas, sin referencias ni citas indefinidas, sin `??` en el PDF.

Warnings:
- 3 overfull `\hbox` ya existentes: dos de 4,4 y 5,0 pt en párrafos de líneas 246 y 258 de un archivo cuyo texto no se tocó (celdas de "Configurabilidad" y "Confidencialidad") y uno de 10 pt en las líneas 231 a 232 de otro; ninguno está en un texto agregado en esta tanda.
- 1 overfull de 20 pt introducido por el párrafo de la figura 6.5 (`\texttt{UserScoringState}`), corregido con puntos de corte.
- Los `Overfull \vbox` de 36,9 pt que aparecen en cada página son anteriores a esta tanda (encabezado de página).
