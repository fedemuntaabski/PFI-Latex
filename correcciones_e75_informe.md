# Informe de correcciones E75

Rama: `correcciones-e75-revision` (desde `e75/correcciones-e50-v2`). Sin push.

## Cambios aplicados

| ID | Archivo | Estado |
|---|---|---|
| A1 RF-13 | chapters/requerimientos.tex:121 | Aplicado |
| A2 paleta 5.2 | chapters/e50_diseno_ux.tex:15 | Aplicado |
| A3 CU-02 | chapters/requerimientos.tex:291 | Aplicado |
| A4 HU-06 (título y criterios) | chapters/requerimientos.tex:342 | Aplicado |
| A5 otras menciones | grep `cantidad de niveles\|niveles adicionales\|RF-13` | Sin otras menciones de cantidad configurable. Quedan menciones legítimas de RF-13 (A1) y de la HU-06 reescrita. |
| B1, B2 | chapters/chapter04.tex (3.6.4) | Aplicado |
| B3 | chapters/producto.tex:180 | Aplicado |
| C1 "s" suelta | chapters/chapter02.tex:12 (línea con solo "s") | Aplicado |
| C2 | chapters/chapter02.tex:13 (+ `\parencite{Rose2020}`) | Aplicado |
| C3 RAdAC→RADAC | chapters/chapter02.tex (218, 261) | Aplicado |
| C4 | chapters/chapter02.tex:297 | Aplicado |
| C5 | chapters/pruebas.tex:600 | Aplicado |
| C6 | chapters/chapter02.tex:222-223 | Aplicado |
| C7 | chapters/chapter04.tex (tabla 3.VI) | Aplicado |
| C8 | chapters/chapter04.tex (tabla 3.IX) | Aplicado |
| C9 | chapters/chapter04.tex (tabla 3.X) | Aplicado |
| C10 | chapters/chapter04.tex (tabla 3.XIII) | Aplicado |
| C11 | chapters/chapter02.tex:268 | Aplicado |
| C12 | chapters/chapter04.tex (tabla 3.VIII, Sentinel y Exabeam) | Aplicado |
| C13 | solo reporte | `lstm_threshold = 0.0874` está en `images/diagramas/Cargar/05_objetos_evento.tex:110`; el umbral 0,1180 está en `chapters/datos.tex:110` y `chapters/pruebas.tex:278` (tabla 8.II). No modificado. |
| D1 Splunk UBA | chapters/chapter02.tex (2.2.1.2) | Aplicado |
| D2, D3 | chapters/e50_mercado.tex (Porter punto 3; FODA amenazas) | Aplicado |
| D4 | biblio.bib sin entradas de fabricantes (verificado); reformuladas 3 atribuciones en chapter02.tex | Aplicado |
| D5 | chapters/chapter02.tex (2.2.3.3 con `\parencite{Xiao2022}`; 2.2.5.2) | Aplicado |
| E1-E5 | chapters/chapter04.tex (3.6) | Aplicado |
| E6 | chapters/negocio.tex:31 (tabla 12.I) | Aplicado |
| F1 | biblio.bib | Aplicado (claves `Karantzas2021`, `Shen2024`; campo `journal`, como el resto del .bib) |
| F2, F3 | chapters/chapter02.tex (nueva 2.2.3.4, `\label{sec:ea-edr}`) | Aplicado |
| F4 | chapters/chapter02.tex (2.2.6) | Aplicado |
| F5, F6, F7 | chapters/chapter04.tex (tabla 3.VIII, lectura, síntesis 3.4) | Aplicado |
| F8 | chapters/e50_mercado.tex (lista "Diferencial del producto", 11.1.1) | Aplicado: ítem agregado al final de la lista de contraste; la lista es de tres ítems, no una lista titulada "Diferencial del producto" |
| F9 | chapters/e50_mercado.tex (Porter punto 1) | Aplicado |
| F10 | chapters/e50_mercado.tex (FODA) + images/diagramas/tikz/foda.tex | Aplicado. La figura 11.1 es TikZ, se agregó el ítem en Amenazas. |
| F11 | — | Sin cambios, como se pidió |

## Discrepancias a revisar
- Las tablas citan `VillarrealVasquez2021` y `Hariri2019` (el prompt decía 2023 y 2021). Se usó la clave existente `VillarrealVasquez2021` también en la nueva 2.2.3.4; verificar que corresponda al paper de LADOHD/EDR de 97,29 %.
- La figura FODA TikZ conserva "Sentinel percibido como incluido sin costo" (no era parte del pedido; D3 reformuló el ítem en el texto). Conviene alinearlo.
- Las referencias a "sección 2.2.3.4" se escribieron con `\ref{sec:ea-edr}`.
- E3: el reemplazo literal deja "Esto no implica que la privacidad sea poco relevante, aunque una lectura posible, que estos datos no permiten verificar, es que funcione como un requisito previo." Revisar la redacción.

## Compilación
`latexmk -pdf main.tex` (MiKTeX, pdflatex + biber): termina sin errores (`!`) tras corregir un error propio. Sin citas ni referencias indefinidas, sin `??`.

Warnings relevantes: 3 `Overfull \hbox` y 254 `Overfull \vbox ... while \output is active` en el log; no se comparó contra la compilación anterior, así que no se sabe cuántos son previos a estos cambios. Revisar visualmente la tabla 3.VIII (fila nueva) y la subsección 2.2.3.4.
