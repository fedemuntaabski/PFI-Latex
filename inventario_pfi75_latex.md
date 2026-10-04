# Inventario LaTeX PFI — preparación entrega 75 %

Rama: `analysis/inventario-pfi75`. Relevamiento solo lectura; único archivo nuevo = este informe. Sin commit/push.
Convención: **[V]** = verificado (grep/script/compilación). **[I]** = inferido.

---

## 1. Árbol de archivos

**[V]** Documento principal `main.tex`. Clase `book` (`a4paper, 12pt, oneside, titlepage, openany`). Sin `.cls`/`.sty` propio de UADE; `quiver.sty` en raíz (solo diagramas, cargado desde `config/symbols.tex`, que **no** se incluye desde `main.tex`).

Orden real de inclusión en `main.tex` (líneas activas, no comentadas):

| # | Archivo | Nota |
|---|---|---|
| 0 | `cover/Caratulafinal.pdf` (`\includepdf`) | carátula |
| 1 | `chapters/title.tex` | portada (titlepage) |
| 2 | `\tableofcontents` | |
| 3 | `chapters/chapter01.tex` | Introducción |
| 4 | `chapters/chapter02.tex` | Antecedentes |
| 5 | `chapters/chapter03.tex` | 8 `\chapter` (ver §3) |
| 6 | `chapters/chapter04.tex` | Análisis comparativo |
| 7 | `\printbibliography` | con `\addcontentsline` manual |
| 8 | `\appendix` + `chapters/appendix/annex.tex` | define `\anexo`; incluye `schedule_of_activities`, `surveys`, `interview_1..5` |
| 9 | `\listoffigures`, `\listoftables` | **después** de los anexos |

**[V]** Comentados en `main.tex` (no entran al PDF): `acknowledgments`, `summary`, `abstract`, `conclusion`.
**[V]** No referenciados desde `main.tex`: `chapters/appendix/interviews.tex` (no usado por `annex.tex`), `figures/example.tex`, `tables/table_example.tex`, `history.tex`, `history/*.tex`, `config/environment.tex`, `config/symbols.tex` (este último sí se carga: `\input{config/symbols}` en el preámbulo).
**[V]** Bibliografía: `biblio.bib` (46 claves únicas + 5 líneas duplicadas). Imágenes: `images/{Imagenes_encuestas,diagramas,mockups,swagger}`, `UADE.png`, `UADE_LARGE.png`, `cronograma.jpg`.
**[V]** `documentacion/`, `documento/`: material fuente (docx/md), fuera del documento.

## 2. Preámbulo (solo reporte)

| Aspecto | Valor [V] |
|---|---|
| Clase | `book`, A4, 12 pt, `oneside`, `openany` |
| Fuente | `mathptmx` (Times) + `lmodern`, `T1`, `utf8` |
| Interlineado | `\onehalfspacing` (`setspace`) |
| Sangría | `\parindent=36pt` + `indentfirst` |
| Márgenes | `vmargin`: `\setmarginsrb{2.7cm}{2cm}{2.3cm}{1.5cm}{0cm}{2cm}{0cm}{1cm}` |
| Títulos | `titlesec`: chapter/section/subsection/subsubsection todos 14 pt negrita, mismo formato |
| Encabezado/pie | `titleps` estilo `ruled`: logo UADE (3.7 cm) + título + autores; pie `Página X de N` (`lastpage`) |
| Tablas | caption `TABLA`, numeración `\thechapter.\Roman{table}` |
| Figuras | numeración por defecto de `book` (`cap.n`), caption “Figura” (babel) |
| Bibliografía | `biblatex`, `backend=biber`, `style=iso-authoryear`, `language=spanish`; `urldate` “consultado”; ítem 6 pt, `\small` |
| Índice | `tocdepth=3`, `secnumdepth=3` |
| Hyperref | `colorlinks=false` (línea para entrega final con `hidelinks` comentada) |
| Otros | `todonotes`, `framed`, `placeins[section,above,below]`, `tocloft`, `pdfcomment`, `babel spanish,es-nodecimaldot` |

**[V]** `chapters/appendix/annex.tex` redefine `\thechapter` a `\Alph{chapter}` (anexos A, B, …).
**[I]** `\Nico` / `\Fermat` (todonotes) siguen definidos; no hay usos activos relevados (no auditado en detalle).

## 3. Mapa de secciones

**[V]** Listado completo archivo:línea generado por script (resumen abajo; todos los niveles tienen su línea en el repo y se reproducen con `grep -n '\\\(chapter\|section\|subsection\|subsubsection\)' chapters -r`).

Profundidad máxima alcanzada: **`\subsubsection` (nivel 3)**. No hay `\paragraph` en el repo. `tocdepth=3` ⇒ todo entra al índice. **[V]** `main.toc` temporal: 12 chapter, 45 section, 77 subsection, 36 subsubsection.

| Archivo | Chapters (línea) | Secciones/Subsecciones destacadas |
|---|---|---|
| `chapter01.tex` | `Introducción` (1) | Objetivo (3), Alcance (6), Descripción (9) |
| `chapter02.tex` | `Antecedentes` (1) | Marco Teórico (3, 8 subsec.), Estado del Arte (100, 7 subsec.) |
| `chapter03.tex` | `Requerimientos, Casos de Uso e Historias de Usuario` (1); `Justificación de Diseño y Mockups` (393); `Diagramas UML` (703); `Análisis de Mercado y Competitividad` (756); `Tecnologías` (855); `Modelo de Datos` (1064); `Demo` (1094) | RF/RNF/CU/HU (L30–L391), catálogo de pantallas (L406–L691), FODA/Porter/BCG (L783–L853), etc. |
| `chapter04.tex` | `Análisis Comparativo del Estado del Arte` (1) | Comparación (3), Matriz (177), Algoritmos (210), Síntesis (380), Entrevistas (391), Encuesta (413) |
| `appendix/*.tex` | vía `\anexo{}` (chapter* manual) | Anexo A cronograma, B encuestas, C–G entrevistas |

**[V]** `chapter03.tex` contiene **7** `\chapter` (1, 393, 703, 756, 855, 1064, 1094) en un único archivo de 1188 líneas, con nombre que no refleja el contenido. El índice tiene 12 chapters en total. `conclusion.tex` define `\chapter{Conclusión}` pero está comentado.

## 4. Citas

**[V]** 29 claves citadas, 46 claves únicas en el `.bib` (51 bloques). Ninguna cita sin entrada.

**(a) Citadas sin entrada:** ninguna. **[V]** (biber no reportó claves faltantes).

**(b) Entradas nunca citadas (17):** **[V]**
`Mohammed2023, Will2026, MDPIFutures2025, SplunkSOAR, ExabeamPlatform, Elbasheer2025, Hanif2024, AltenkirchGrattage2005, JNSM2025, Hamarsheh2025, Mangla2025, Parimalla2025, Verizon2025, Fahrmann2022, SAJS2025, Hassan2025, Abramsky1993`.
**[V]** `Abramsky1993` y `AltenkirchGrattage2005` (lógica lineal / lenguaje cuántico) son restos de la plantilla, ajenos al tema. `biblatex` imprime solo las citadas (no hay `\nocite{*}`).

**Claves duplicadas en `biblio.bib` [V]** (biber: `WARN - Duplicate entry key ... skipping`):

| Clave | Líneas | Observación |
|---|---|---|
| `AlShehari2023` | 65, 213 | **DOIs distintos** (…3326750 vs …3323769): posiblemente dos papers distintos con una sola clave; biber usa el primero |
| `Artioli2024` | 84, 223 | mismo DOI |
| `JNSM2025` | 104, 249 | segunda sin DOI, con URL |
| `Kuppa2022` | 194, 257, 310 | L257 es **otro** título (“Towards Adversarial Evaluations…”); L194 y L310 son el mismo |

Además **[V]** biber: `line 310 / 321: junk seen at toplevel` (posible llave sin cerrar entre L310 y L321).
**[V]** `Fahrmann2022` (L94): campo `author` con `\&` (“Damer, Naser \& Kirchbuchner”) — **[I]** biber lo leería como un solo autor; sin cita activa hoy.
**[V]** `MDPIFutures2025` repite el título de `Atlam2025` (“Enhancing Healthcare Security…”), con autor “MDPI Futures”.

**(c) Año del campo ≠ año del DOI [V para el dato, I para la causa]:**

| Clave | `year` | Año en DOI | Comentario |
|---|---|---|---|
| `VillarrealVasquez2023` | **2021** | 2021 | La **clave** dice 2023 y el campo 2021; citada 4 veces. Inconsistencia clave/campo, no DOI/campo. |
| `Landauer2023` | 2023 | **2022** (`BigData55660.2022…`) | **[I]** la conferencia fue en 2022 |
| `Wu2021GNN` | 2021 | 2020 (`TNNLS.2020…`) | **[I]** early access 2020, volumen 2021: ambos años defendibles |

La mayoría de los DOI (IEEE/MDPI/Springer/NIST) no contienen año; esos no se pudieron comparar **[V]**. `Ansari2025`, `AlShehari2023`, `Artioli2024`, `Kuhn2010`, `Xiao2022`, `Kuppa2022`, `Tian2023HGNN`, `Hariri2019`, `Stylios2023`, `Hamarsheh2025`, `Mohammed2023`: coinciden.

**(d) Autores citados en prosa sin `\cite` [V]:**

| Archivo:línea | Texto | Problema |
|---|---|---|
| `chapter03.tex:278` | `(Villarreal-Vásquez et al., Benova \& Hudec)` | Cita manual. `Villarreal-Vásquez` sí tiene entrada (`VillarrealVasquez2023`). **`Benova & Hudec` no existe en `biblio.bib`** |

Otras coincidencias del script (“User and Entity”, “RF-01 & El”, etc.) son falsos positivos. No se detectó otro caso `Autor (año)`.

## 5. Referencias cruzadas

- **[V]** `\ref` rotos: **0** (todas las claves usadas existen). **[V]** Compilación: `name{appendix*.1} has been referenced but does not exist` (1 warning de hyperref por `\chapter*` + `\refstepcounter`, ver §7).
- **[V]** Labels sin uso: **80** de 104. Son sobre todo `tab:*` / `fig:*` (p. ej. todas las tablas `tab:rf-modulo*`, `tab:comp-*`, `tab:algo-*`, `fig:diagrama-*`, `fig:mockup-*`, `fig:demo-*`, `fig:gantt_actualizado`) más `sec:tecnologias`, `sec:matriz-capacidades`, `sec:comparacion-algoritmos`, `conclussions`. **[I]** Solo `fig:encuesta-1..18` y 7 `sec:*` se referencian.
- **[V]** Texto escrito a mano en vez de `\ref`:

| Archivo:línea | Texto |
|---|---|
| `chapter04.tex:416–466` (16 apariciones) | `Anexo B` fijo en paréntesis |
| `appendix/surveys.tex:3` | `Capítulo 4, Sección~\ref{…}` (el “Capítulo 4” está a mano) |
| `chapter01.tex:19` | `Capítulo 2`, `Capítulo 3` (**comentado**, no sale) |

**[I]** “Anexo B” depende del orden de `\anexo` (cronograma = A, encuestas = B); si se reordenan anexos, se rompe.

- **[V]** Sin referencias a tablas en el texto: las tablas no se citan con `\ref`.

## 6. Figuras y tablas

**[V]** Totales: 48 figuras activas (49 entornos; 1 está comentado), 37 tablas (`longtable` con `\caption`+`\label`), 176 páginas compiladas.

### Figuras (archivo de imagen, formato, resolución)

| Label | Caption | Archivo | Fmt | Px |
|---|---|---|---|---|
| `fig:encuesta-1..18` | preguntas de la encuesta (n=135/112) | `images/Imagenes_encuestas/1..18.png` | PNG | 554–734 × 313–381 |
| `fig:gantt_actualizado` | Diagrama de Gantt | `images/cronograma.jpg` | JPG | 9570×4920 |
| *(sin label)* | “Cronograma de actividades.” | `./././images/Cronograma.png` | — | **comentado**, archivo inexistente |
| `fig:mockup-*-wireframe` (8) | Wireframe de baja fidelidad: … | `images/mockups/mockup-*-wireframe.png` (+ `-real`) | PNG | 1600×1000 / 1920×945 |
| `fig:demo-mockup-*-real*` (9) | Pantalla real: … | `images/mockups/mockup-*-real*.png` (repetidas de la sección anterior) | PNG | 1905–1920 × 945 |
| `fig:diagrama-flujo` | Diagrama de flujo de información | `diagramas/diagrama-flujo.png` | PNG | 8192×5996 |
| `fig:diagrama-componentes` | Diagrama de componentes | `diagramas/diagrama-componentes.png` | PNG | 1235×940 |
| `fig:diagrama-clases-agente` | Clases Agente PEP | `diagramas/diagrama-clases-agente.png` | PNG | 2505×735 |
| `fig:diagrama-clases-api` | Clases API PDP | `diagramas/diagrama-clases-api.png` | PNG | **16941×3844 (3.6 MB)** |
| `fig:diagrama-objetos` | Diagrama de objetos | `diagramas/diagrama-objetos.png` | PNG | 1859×553 |
| `fig:matriz-foda` | Matriz FODA | `diagramas/Analisis_FODA.png` | PNG | 1170×854 |
| `fig:matriz-bcg` | Matriz BCG | `diagramas/BCG.png` | PNG | 1333×749 |
| `fig:diagrama-bases-de-datos-redis` | “Diagrama de Bases de Datos.” | `diagramas/Redis.png` | PNG | 3586×2067 |
| `fig:diagrama-bases-de-datos-supabase` | “Diagrama de Bases de Datos.” (mismo caption) | `diagramas/Supabase.png` | PNG | 6431×2067 |
| `fig:diagrama-arquitectura` | Diagrama de Arquitectura | `diagramas/diagramaarquitectura.png` | PNG | 5016×3980 |
| `fig:demo-swagger-endpoint1/2` | Swagger Parte 1/2 | `images/swagger/endpoint{1,2}.png` | PNG | 1433×876 / 1433×383 |

Ningún gráfico es vectorial (PDF/SVG). **[V]**

**Raster de baja resolución [I]:** con `width=0.8\textwidth` (~12 cm útiles) las capturas de encuesta 1–18 rinden ≈ 120–155 dpi (< 200). Los diagramas `diagrama-componentes`, `Analisis_FODA`, `BCG` rinden ≈ 250–300 dpi o más según ancho; se estimó sin medir el ancho exacto en página.
**[V]** Duplicación: las 9 capturas `-real` aparecen dos veces (catálogo de pantallas, L405–L690, y Demo, L1094–L1188).
**[V]** `images/Imagenes_encuestas/image.png` (665×341) no se usa. `images/UADE.png` y `UADE_LARGE.png` son idénticos en dimensiones (1091×382).

### Tablas
**[V]** 37 `longtable`: actores, RF módulo 1–6, RNF, 8 justificaciones de mockups (`tab:mockup-*`), lenguajes, frameworks ×4, protocolos (cap. 3); 7 comparativas, matriz de capacidades, 7 de algoritmos (cap. 4). Listado completo label/caption con `grep -n 'caption' chapters/chapter03.tex chapters/chapter04.tex`.

## 7. Compilación

**[V]** Se compiló con `latexmk -pdf -outdir=<scratchpad>/build main.tex` (salida fuera del árbol; biber vía latexmk). `git status` posterior: sin cambios versionados.
**[V]** Observación: aparecieron/actualizaron `main.aux .lof .lot .out .run.xml .toc .upb` **dentro del repo** (a las 09:41), todos ignorados por `.gitignore`. **[I]** Los generó MiKTeX durante la corrida, a pesar del `-outdir`, o la ejecución previa de `pdflatex main` del usuario; no se pudo determinar cuál. No hay efecto sobre archivos versionados.

Resultado: 176 páginas. Warnings relevantes **[V]**:

| Tipo | Detalle |
|---|---|
| Referencias | `1 undefined reference`: `name{appendix*.1}` (hyperref, anexos con `\chapter*`); `biblatex: Please rerun LaTeX` en el log final de latexmk |
| Citas | ninguna sin resolver |
| biber | 5 `Duplicate entry key`, 2 `junk seen at toplevel` (L310, L321) |
| Overfull `\vbox` | **174** (36.86 pt): **[I]** coincide con el logo del encabezado (`Requested size: 105.27pt x 36.86pt`) y `headheight=0cm` en `\setmarginsrb`; se repite por página |
| Overfull `\hbox` | 6 leves/moderados: 14.97 pt (líneas 548, 688), 18.48 pt (661–662), 7.3 pt (1055), ~1 pt (554, 1022) — **[I]** tablas del Cap. 3 |
| Floats | 8 × ``h' float specifier changed to `ht'` |
| Otros | `xcolor: usenames obsolete`, `microtype: patch footnote`, `soulutf8 obsolete`, `pdfTeX ext4: destination page.1 duplicate` |

## Hallazgos que afectan la rúbrica

**Formato**
1. **[V]** Orden de listas: `\listoffigures` y `\listoftables` van **después** de los anexos; `\tableofcontents` solo cubre hasta anexos. Revisar con la rúbrica UADE.
2. **[V]** Hyperref con bloque “entrega final” desactivado: hoy `colorlinks=false` pero sin `hidelinks`; el comentario del propio preámbulo exige revisarlo en entrega final.
3. **[V]** `abstract`, `summary` (Resumen), `acknowledgments` y `conclusion` están **comentados**; en 75 % faltarían Resumen/Abstract/Conclusiones si la rúbrica los exige.
4. **[V]** 174 Overfull `\vbox` por logo de encabezado (**[I]** causa).
5. **[V]** Figura de cronograma: Anexo A sí presente (requerido en entregas no finales).
6. **[V]** Capturas de encuesta baja resolución (**[I]**) y diagramas gigantes (`diagrama-clases-api.png` 3.6 MB, `diagrama-flujo.png`) sin versión vectorial.
7. **[V]** Mismo caption “Diagrama de Bases de Datos.” en 2 figuras; 9 capturas repetidas (cap. 3 mockups y Demo).
8. **[V]** Rutas con distinta capitalización: `Redis.png`/`Supabase.png` en el `.tex` vs `redis.png`/`supabase.png` en git (**falla en Linux/Overleaf**).
9. **[V]** `chapter03.tex` agrupa 7 `\chapter` (nombre de archivo no refleja contenido; solo organización, sin efecto en el PDF).

**Índice**
10. **[V]** `tocdepth=3`: índice incluye 36 subsubsections (profundidad máxima del repo); índice largo, 176 páginas totales.
11. **[V]** Anexos: entradas manuales `\addcontentsline{toc}{section}` bajo un `chapter` “Anexo” genérico; warning hyperref `appendix*.1`.
12. **[V]** `Bibliografía` agregada manualmente al TOC (`\addcontentsline`).

**Citas**
13. **[V]** `Benova & Hudec` citado a mano en `chapter03.tex:278` y **sin entrada en el `.bib`**; `Villarreal-Vásquez` también a mano (existe `VillarrealVasquez2023`).
14. **[V]** 4 claves duplicadas en el `.bib` (`AlShehari2023`, `Artioli2024`, `JNSM2025`, `Kuppa2022` ×3): biber descarta las repeticiones; `AlShehari2023` y `Kuppa2022` (L257) pueden ser **papers distintos** con la misma clave.
15. **[V]** `VillarrealVasquez2023`: clave 2023 / campo `year` 2021; `Landauer2023`: año 2023 vs DOI 2022 (**[I]** correcto es 2022).
16. **[V]** 17 entradas nunca citadas (2 de lógica cuántica heredadas de plantilla).
17. **[V]** `Fahrmann2022`: `\&` dentro de `author` (**[I]** autores mal separados si se llega a citar); L310–L321 con basura de sintaxis `.bib`.

**Referencias**
18. **[V]** `Anexo B` fijo ×16 en `chapter04.tex`; `Capítulo 4` fijo en `surveys.tex:3`.
19. **[V]** 80 labels sin uso; tablas/figuras del cap. 3–4 no se mencionan en el texto con `\ref`.
