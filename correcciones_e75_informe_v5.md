# Informe de correcciones E75 — tanda 5

Rama: `correcciones-e75-revision`. Sin push. Solo contenido; sin cambios de preámbulo, estilos, numeración ni paquetes. No se tocaron 1.1.1, 1.2 ni 1.3. Commits sin trailers de coautoría.

## Cambios aplicados

| ID | Archivo | Estado |
|---|---|---|
| P1-A | (compilación) | Verificado. Ver detalle abajo. |
| P1-B | chapter04.tex (3.VIII), requerimientos.tex (4.VIII), datos.tex (8.IV), pruebas.tex (10.IX, 10.XVIII) | Aplicado: fuente `{\small Fuente: …\par}` después de cada `longtable`, con el texto pedido y `\ref{sec:estado-del-arte}` en 3.VIII. Script de verificación: las 60 tablas con título tienen fuente. |
| P1-C | biblio.bib, e50_mercado.tex (11.2, intro, BCG), negocio.tex (lienzo 12.I), conclusiones.tex (13.2) | Aplicado. Ver detalle abajo. |
| P1-D | diagramas_ampliados.tex (Anexo H), e50_uml.tex (sección 6) | Aplicado con las dos redacciones pedidas. |
| P1-E | documentacion/e75/modelo_financiero.py | Aplicado. Ver detalle abajo. |
| P2-A | — | **No realizado** (opcional): ver abajo. |

## P1-A — compilación

`latexmk -C` y `latexmk -pdf main.tex` desde cero (1 min 9 s). El log no tiene avisos "Rerun", "Label(s) may have changed" ni referencias indefinidas. Una segunda pasada deja `main.toc` idéntico. PDF final: 273 páginas físicas; el encabezado dice "de 271" y la última página dice "Página 271 de 271" (las dos primeras páginas no llevan número).

Script sobre el PDF (`pdftotext`): el número de página de cada entrada coincide con la página donde empieza.

| Lista | Entradas | No coinciden |
|---|---|---|
| Índice (secciones, Bibliografía, Anexos A a H) | 243 | 0 |
| Lista de figuras | 65 | 0 |
| Lista de tablas | 60 | 0 |

La entrada "Anexo" (portada del apéndice, p. 197) no se verificó por texto porque la página no tiene título propio; el Anexo A figura en la 198 y empieza ahí. El "197 / 258 / 270" del PDF anterior era de una compilación vieja; con la actual no queda ninguna diferencia. No se modificó el contador de páginas ni el preámbulo. `latexmk -C` borra `main.dvi`, que está versionado; se restauró con `git checkout`.

## P1-C — tamaño del mercado

- `biblio.bib`: agregado `@report{Salerno2025}` tal como se pidió.
- Nueva sección 11.2 "Tamaño del mercado objetivo" (`sec:tamano-mercado`), entre marketing mix y FODA, con el texto pedido. FODA, Porter y BCG pasan a 11.3, 11.4 y 11.5; no había remisiones escritas a mano (todas son `\ref`). Se actualizó la oración introductoria del capítulo para mencionarla.
- Labels agregados (no cambian numeración): `sec:marketing-mix` (11.1), `sec:escenarios-fin` (12.4.2) y `sec:interpretacion-fin` (12.4.4, donde está el análisis de sensibilidad).
- BCG, lienzo (bloque "Segmentos de clientes") y conclusiones 13.2: reemplazos pedidos. En conclusiones se agregó además `(sección~\ref{sec:tamano-mercado})` al final de la frase.
- Cifras verificadas contra el documento: clientes al año 5 = 49 / 168 / 307 (tabla 12.IV), que sobre 10.500 dan 0,47 % / 1,6 % / 2,92 %; costo de adquisición de equilibrio del VAN base = USD 2.370 (ya figuraba en 12.4.4). 2 % de 523.207 = 10.464, redondeado a 10.500 como pide el texto.

## P1-E — modelo financiero

Parámetros: nube USD 0,10; costo fijo = equipo + contador y soporte (125 el año 1, 167 desde el 2) + infraestructura escalonada según los equipos de cada mes (tabla 12.II: 179 hasta 1.500 equipos, +45 sobre 1.500, +73 por cada 3.000 sobre los primeros 3.000, +20 por cada 5.000 sobre los primeros 5.000, +100 sobre 6.000; se verificó que reproduce 224, 317 y 583 del texto). El script ahora también imprime las sensibilidades a nube, costo de adquisición y abandono, y el punto de equilibrio. Docstring de cinco líneas al inicio.

Diferencias contra el documento (USD; máxima 9, ninguna supera 10):

| Tabla | Celda | Documento | Script | Dif. |
|---|---|---|---|---|
| 12.V flujos | Pesimista años 1–5 | −49.438 / −67.565 / −84.122 / −57.108 / −34.215 | −49.440 / −67.567 / −84.123 / −57.109 / −34.217 | 2 / 2 / 1 / 1 / 2 |
| 12.V | Base años 1–5 | −40.422 / −24.606 / 37.244 / 135.648 / 242.657 | −40.423 / −24.607 / 37.242 / 135.645 / 242.653 | 1 / 1 / 2 / 3 / 4 |
| 12.V | Optimista años 1–5 | −22.447 / 43.458 / 175.454 / 372.723 / 586.307 | −22.449 / 43.456 / 175.451 / 372.718 / 586.301 | 2 / 2 / 3 / 5 / 6 |
| 12.VI | VAN 25 % pes. / base / opt. | −183.466 / 83.059 / 421.476 | −183.469 / 83.054 / 421.468 | 3 / 5 / 8 |
| 12.VI | Necesidad máx. de fondos | 315.448 / 88.028 / 45.447 | 315.455 / 88.030 / 45.449 | 7 / 2 / 2 |
| 12.VI | TIR, recupero simple y descontado | 56,0 % / 3,4 / 3,9 años; 154,3 % / 2,0 / 2,1 años | idénticos | 0 |
| 12.VII | VAN 20 / 30 / 35 %, pesimista | −201.091 / −168.508 / −155.708 | −201.095 / −168.512 / −155.711 | 4 / 4 / 3 |
| 12.VII | Base | 110.716 / 61.148 / 43.650 | 110.710 / 61.143 / 43.645 | 6 / 5 / 5 |
| 12.VII | Optimista | 505.379 / 353.718 / 298.499 | 505.370 / 353.712 / 298.493 | 9 / 6 / 6 |
| 12.VIII nube 0,10 / 0,30 / 0,60 | Pesimista | −183.466 / −192.538 / −206.147 | −183.469 / −192.542 / −206.151 | 3 / 4 / 4 |
| 12.VIII | Base | 83.059 / 61.533 / 29.245 | 83.054 / 61.528 / 29.239 | 5 / 5 / 6 |
| 12.VIII | Optimista | 421.476 / 384.163 / 328.194 | 421.468 / 384.155 / 328.186 | 8 / 8 / 8 |
| 12.IX CAC 1.000 / 1.500 / 2.500 | VAN base | 130.806 / 83.059 / −13.758 | 130.800 / 83.054 / −13.763 | 6 / 5 / 5 |
| 12.IX abandono 1,5 / 2 / 3 % | VAN base | 111.805 / 83.059 / 33.579 | 111.800 / 83.054 / 33.574 | 5 / 5 / 5 |
| 12.IV clientes activos | todas | 5…49 / 11…168 / 22…307 | idénticos | 0 |
| Equilibrio | costo fijo mensual años 1–5 | 3.804 / 6.464 / 9.657 / 11.730 / 12.822 | 3.804 / 6.464 / 9.657 / 11.730 / 12.823 | 0 / 0 / 0 / 0 / 1 |
| Equilibrio | clientes necesarios | 12 / 21 / 31 / 37 / 41 | 12 / 21 / 31 / 37 / 41 | 0 |

Causa probable de las diferencias de unos pocos dólares: el documento usa 167 por mes de contador y soporte (probablemente 500/3 = 166,67 en la reconstrucción) y el script usa 167 redondeado. No se verificó contra el script de la reconstrucción porque no está en el repositorio. No se cambió ninguna tabla del documento.

## P2-A — vistas simplificadas (no realizado)

Se priorizó cerrar P1 con verificación. Rehacer la figura 6.3 en TikZ exige comprobar clase por clase y relación por relación contra el diagrama original (generado por separado en `images/diagramas/`), y reemplazar las mitades del Anexo H cambia la numeración de figuras y las listas. No se empezó para no dejar nada a medias. Queda pendiente para otra tanda.

## Para el autor

- Umbral del LSTM (0,0874 contra 0,1180): sigue pendiente de decisión (prompt de código, punto C1).
- Consentimiento de los entrevistados: sigue pendiente.
- Fuente de 11.2: las cifras provienen del texto pedido; no se verificaron contra el PDF de UCEMA (sin acceso desde esta sesión).
