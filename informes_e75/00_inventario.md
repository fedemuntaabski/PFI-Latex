# Inventario E75 del documento LaTeX

Relevamiento sin modificaciones de los `.tex`. Rama `correcciones-e75-latex`, creada desde `e75/paquete` (commit `ac9d85a`). Fecha: 2026-10-09.

## Estructura

### Archivo principal
- `main.tex`, con todo el preámbulo inline.
- Clase: `\documentclass[a4paper, 12pt, oneside, titlepage, openany]{book}` (`main.tex:5`).
- `config/symbols.tex` se incluye con `\input` desde el preámbulo. `config/environment.tex` **no se incluye en ningún lado** (está huérfano).

### Orden de inclusión (`main.tex:242-286`)
1. Carátula en PDF: `\includepdf{cover/Caratulafinal.pdf}` (`main.tex:244-252`).
2. `\input{chapters/title}` (segunda carátula, en LaTeX) (`main.tex:254`).
3. `acknowledgments`, `summary` y `abstract` están comentados.
4. `\tableofcontents`.
5. Capítulos (número en el PDF → archivo):

| Cap. | Archivo | Título |
|---|---|---|
| 1 | `chapters/chapter01.tex` | Introducción |
| 2 | `chapters/chapter02.tex` | Antecedentes |
| 3 | `chapters/chapter04.tex` | Análisis comparativo del estado del arte |
| 4 | `chapters/e50_requerimientos.tex` → `\input{chapters/requerimientos}` | Requerimientos, casos de uso e historias de usuario |
| 5 | `chapters/e50_diseno_ux.tex` | Justificación de diseño y mockups |
| 6 | `chapters/e50_uml.tex` | Diagramas UML |
| 7 | `chapters/arquitectura.tex` | Arquitectura y tecnologías |
| 8 | `chapters/datos.tex` | Datos |
| 9 | `chapters/producto.tex` | Producto implementado |
| 10 | `chapters/pruebas.tex` | Pruebas y resultados |
| 11 | `chapters/e50_mercado.tex` | Análisis de mercado y competitividad |
| 12 | `chapters/negocio.tex` | Modelo de negocio y viabilidad económico-financiera |
| 13 | `chapters/conclusiones.tex` | Conclusiones y trabajo futuro |

6. Bibliografía: `\addcontentsline` + `\printbibliography{}` (`main.tex:277-278`).
7. `\appendix` → `\input{chapters/appendix/annex}`. `annex.tex` define `\anexo{}` (numeración `\Alph`, `\chapter*` y entrada en el TOC como section) e incluye:

| Anexo | Archivo |
|---|---|
| A — Cronograma de actividades | `chapters/appendix/schedule_of_activities.tex` |
| B — Resultados de la encuesta | `chapters/appendix/surveys.tex` |
| C — Entrevista a Pablo Rodolfo Villarino | `chapters/appendix/interview_1_pablo.tex` |
| D — Entrevista a Luciana Jacubovich | `chapters/appendix/interview_2_jacubovich.tex` |
| E — Entrevista a Guillermo Pita | `chapters/appendix/interview_3_guillermo.tex` |
| F — Entrevista a Alejandro Francisco Peña | `chapters/appendix/interview_4_pena.tex` |
| G — Entrevista a Matías Gabriel Ruiz | `chapters/appendix/interview_5_ruiz.tex` |

8. `\listoffigures` y `\listoftables` al final, después de los anexos (`main.tex:283`, `main.tex:285`).

### Archivos `.tex` que no se compilan
`chapters/abstract.tex`, `acknowledgments.tex`, `summary.tex` (comentados); `chapters/conclusion.tex` (versión vieja, comentada); `chapters/appendix/interviews.tex` (plantilla con la entrevista a Feynman); `chapters/archivo/obsoleto_e50.tex`; `figures/example.tex`; `tables/table_example.tex`; `config/environment.tex`.

### Preámbulo relevante
- Encabezado y pie: paquete **titleps** (no fancyhdr), `\newpagestyle{ruled}` (`main.tex:53-66`). Logo `images/UADE_LARGE`, texto central en `main.tex:55` y autores a la derecha. Pie: "Página X de Y" con `lastpage`. `\ps@plain` se iguala a `ruled`.
- Títulos: `titlesec`, todos de 14 pt en negrita (al final del preámbulo). `tocloft` da formato a los títulos del índice y de las listas (`main.tex:203-218`).
- Idioma: `babel` `[spanish,es-nodecimaldot]` + `csquotes`. Captions redefinidas en `\addto\captionsspanish` (`main.tex:131-136`).
- Tablas numeradas `\thechapter.\Roman{table}`.
- Fuente: `mathptmx` (Times). Interlineado `\onehalfspacing`. Márgenes con `vmargin`.
- `hyperref` sin colores; el bloque `hidelinks` para la entrega final está comentado.
- Otros paquetes: graphicx, pdfpages, xcolor, placeins, microtype, enumitem, longtable/multirow, amsmath, todonotes, pdfcomment, ulem, setspace.

### Bibliografía
- `biblatex` con `backend=biber`, `style=iso-authoryear`, `language=spanish`, `uniquelist=false` (`main.tex:16`). Base: `biblio.bib` (`main.tex:18`).
- Strings personalizados: `\DefineBibliographyStrings{spanish}` (online, urlfrom, andothers) y formato de `urldate`.
- Comandos de cita usados (sin contar `archivo/`): `\cite` 67, `\parencite` 56, `\textcite` 11. No se usan `\autocite` ni `\footcite`.

### Figuras
- No hay `\graphicspath`; las rutas son relativas a la raíz.
- `images/`: `diagramas/` (incluye `diagramas/v75/*.pdf`), `mockups/`, `Imagenes_encuestas/1..18.png`, `pruebas/curva_umbral.pdf`, `cronograma.jpg` (Gantt), `logo_umbral.png`, `UADE.png`, `UADE_LARGE.png`, `swagger/`.
- `figures/` y `tables/` solo tienen ejemplos de la plantilla.
- `cover/`: PDFs de carátula (`Caratulafinal.pdf` es el que se usa).

## Compilación base

Comando: `latexmk -pdf -interaction=nonstopmode -outdir=build main.tex` (MiKTeX; `build/` está en `.gitignore`). latexmk corrió pdflatex, después biber y dos pasadas más de pdflatex.

- **Compila**: sí. Salida `build/main.pdf`, **243 páginas** (el pie numera "de 241" porque las dos carátulas no cuentan).
- **Errores (`!`)**: 0.
- **Warnings**:
  - LaTeX: 4, todos `'h' float specifier changed to 'ht'`.
  - Paquetes: 3 (`xcolor`: opción `usenames` obsoleta; `microtype`: no aplica el patch `footnote`; `soulutf8` obsoleto).
  - pdfTeX: 3 por `Caratulafinal.pdf` (PDF versión 1.7, se admite hasta 1.5) y 2 por `destination with the same identifier (name{page.1})` (destino duplicado por las carátulas).
  - Overfull box: 245. Underfull box: 64.
  - biber (`main.blg`): 0 warnings y 0 errores.
- **Referencias sin definir**: 0. **Citas sin definir**: 0. **Labels con definición múltiple**: 0.

## Marcadores

Hay 24 marcadores `[[...]]` en archivos compilados: 22 `[[CODIGO...]]` y 2 `[[COMPLETAR...]]`. `chapters/archivo/` no tiene ninguno. `requerimientos.tex` se compila a través de `e50_requerimientos.tex`.

### `[[CODIGO...]]` (no se tocan)

| Archivo:línea | Texto |
|---|---|
| `chapters/chapter01.tex:53` | `[[CODIGO: confirmar estado del despliegue]]` |
| `chapters/chapter01.tex:53` | `[[CODIGO: confirmar según el resultado del Prompt C]]` |
| `chapters/requerimientos.tex:63` | `[[CODIGO: resultado del Prompt C]]` (RF-02) |
| `chapters/requerimientos.tex:246` | `[[CODIGO: resultado del Prompt C]]` (RNF-13) |
| `chapters/arquitectura.tex:249` | `[[CODIGO: resultado del Prompt C]]` (tabla, envío de eventos desde un agente) |
| `chapters/arquitectura.tex:255` | `[[CODIGO: resultado del Prompt C]]` |
| `chapters/arquitectura.tex:298` | `[[CODIGO: resultado del Prompt C]]` (tabla de protocolos, HTTPS) |
| `chapters/arquitectura.tex:304` | `[[CODIGO: resultado del Prompt C]]` (tabla de protocolos, HTTP sin TLS) |
| `chapters/producto.tex:142` | `[[CODIGO: resultado del Prompt C]]` (estado del despliegue) |
| `chapters/producto.tex:165` | `[[CODIGO: cifrado TLS entre agente, panel y API; autenticación mutua entre agente y API; credenciales del panel fuera del navegador; claves de agente ligadas a su identificador]]` |
| `chapters/pruebas.tex:283` | `[[CODIGO: Pearson con el modelo vigente]]` |
| `chapters/pruebas.tex:333` | `[[CODIGO: usuarios y cobertura de las detecciones con el modelo vigente]]` |
| `chapters/pruebas.tex:346` | `[[CODIGO: curva completa con el modelo vigente]]` |
| `chapters/conclusiones.tex:20` | `[[CODIGO: TLS y autenticación mutua]]` y `[[CODIGO]]` (2 marcadores) |
| `chapters/conclusiones.tex:36` | `[[CODIGO: resultado de seguridad]]` y `[[CODIGO]]` (2 marcadores) |
| `chapters/conclusiones.tex:40-41` | `[[CODIGO: cantidad de pruebas y cobertura]]` (l. 40) y `[[CODIGO]]` (l. 41) |
| `chapters/conclusiones.tex:47` | `[[CODIGO: actualizar conteo con RNF-03 y RNF-13]]` |
| `chapters/conclusiones.tex:122-123` | `[[CODIGO: ajustar según el resultado de la cobertura]]` |
| `chapters/conclusiones.tex:126-127` | `[[CODIGO: limitaciones de seguridad que queden abiertas después del trabajo del repo de código; integración con un proveedor de identidad real.]]` |

### `[[COMPLETAR...]]`

| Archivo:línea | Texto |
|---|---|
| `chapters/chapter04.tex:437-438` | `[[COMPLETAR: canal, por ejemplo redes sociales y contactos personales y laborales del equipo]]` |
| `chapters/chapter04.tex:438` | `[[COMPLETAR: fechas]]` |

## Ubicaciones

### Carátulas, título y encabezado
- **Carátula 1 (principal)**: es un PDF externo, `cover/Caratulafinal.pdf`, incluido con `\includepdf` en `main.tex:244-252`. **No se edita desde LaTeX: el usuario la regenera desde una página web** y reemplaza el PDF. pdfTeX avisa que el PDF es versión 1.7 (aviso inofensivo).
- **Carátula 2**: `chapters/title.tex` (entorno `titlepage`), incluida en `main.tex:254`.
  - Título: `chapters/title.tex:7` ("UMBRAL: agente inteligente de vigilancia conductual y mitigación de riesgo de identidad para PyMEs argentinas (2026)").
  - Autores y LU: l. 10 y 14. Tutor: l. 18-22. Año (`\the\year`): l. 25.
- **Texto del encabezado** "UMBRAL — VIGILANCIA CONDUCTUAL Y RIESGO DE IDENTIDAD": `main.tex:55`, como `\MakeUppercase{UMBRAL --- Vigilancia conductual y riesgo de identidad}` dentro de `\newpagestyle{ruled}` (`main.tex:53-66`). Los nombres de los autores en el encabezado están en `main.tex:60-61`.

### Headings
| Número | Archivo:línea | Heading |
|---|---|---|
| 1.1 | `chapters/chapter01.tex:5` | `\section{Objetivos}` |
| 10.5 | `chapters/pruebas.tex:214` | `\section{Evaluación del modelo sin etiquetas}` |
| 10.5.1 | `chapters/pruebas.tex:219` | `\subsection{Metas de evaluación}\label{sec:metas-modelo}` |
| 12.4 | `chapters/negocio.tex:78` | `\section{Viabilidad económico-financiera}\label{sec:viabilidad-fin}` |
| 12.5 | `chapters/negocio.tex:239` | `\section{Identidad de marca}` |
| 13 | `chapters/conclusiones.tex:1` | `\chapter{Conclusiones y trabajo futuro}\label{chap:conclusiones}` |
| 13.4 | `chapters/conclusiones.tex:97` | `\section{Trabajo futuro}` (va hasta el final del archivo, l. 128) |

### Sección 12.4 (`chapters/negocio.tex`)
- 12.4 Viabilidad económico-financiera: l. 78.
- 12.4.1 Supuestos: l. 80.
- 12.4.2 Escenarios: l. 130.
- 12.4.3 Indicadores: l. 181.
- 12.4.4 Interpretación: l. 221-238 (12.5 empieza en l. 239).

### "Lista de Figuras" y "Lista de Tablas"
- Se definen en `main.tex:131-136`: `\addto\captionsspanish{ ... \renewcommand{\listfigurename}{Lista de Figuras} (l. 133) \renewcommand{\listtablename}{Lista de Tablas} (l. 134) ... }`. Ahí también se redefinen `\contentsname` (Índice) y `\tablename` (TABLA).
- Formato de los títulos: tocloft, `\cftloftitlefont` y `\cftlottitlefont` (`main.tex:211-212`).
- Se insertan en `main.tex:283` (`\listoffigures`) y `main.tex:285` (`\listoftables`).

### Epígrafe de la Figura A.1 (Gantt)
- `chapters/appendix/schedule_of_activities.tex:15`: `\caption{Diagrama de Gantt del Proyecto --- Planificación de Hitos y Distribución de Tareas.}`. La imagen es `images/cronograma.jpg` (l. 14, rotada 90°). En la l. 8 hay un caption viejo comentado.

### Texto suelto "dor de identidad real. ]" (final de 13.4)
- Origen: `chapters/conclusiones.tex:126-127`, `\item [[CODIGO: limitaciones de seguridad ... proveedor de identidad real.]]`.
- Causa: `\item [` se interpreta como el argumento opcional (etiqueta) de `\item`. La etiqueta abarca `[CODIGO: ... real.` hasta el primer `]`, se compone en la caja de la etiqueta (se ve el fragmento "dor de identidad real.") y el segundo `]` queda como texto del ítem.
- Atención: el arreglo toca una línea con marcador `[[CODIGO...]]`. Se puede proteger con `\item{}` o `\item\relax` antes del marcador sin cambiar el texto del marcador.

### Citas a Larman y Basili (2003) y Osterwalder y Pigneur (2010)
- `biblio.bib:445` `@Article{Larman2003}` (Larman, Craig and Basili, Victor R.; Computer 36(6), 47-56).
  - Uso: `chapters/chapter01.tex:61` `\parencite{Larman2003}`.
- `biblio.bib:372` `@book{Osterwalder2010}` (Osterwalder, Alexander and Pigneur, Yves).
  - Usos: `chapters/negocio.tex:2` `\parencite{Osterwalder2010}`; `chapters/negocio.tex:18` `\textcite{Osterwalder2010}`; `chapters/negocio.tex:56` `\textcite{Osterwalder2010}` (fuente del lienzo).

### Anexos C a G (transcripciones)
Ver la tabla de Estructura: `chapters/appendix/interview_1_pablo.tex` (C), `interview_2_jacubovich.tex` (D), `interview_3_guillermo.tex` (E), `interview_4_pena.tex` (F), `interview_5_ruiz.tex` (G). El título de cada uno está en la l. 1 (`\anexo{...}`). No confundir con `interviews.tex`, que es la plantilla de Feynman y no se compila.

### Menciones a Gemini (todas en archivos compilados)
| Archivo:línea | Contexto |
|---|---|
| `chapters/arquitectura.tex:185` | Tabla de servicios: "Gemini & Redacción asistida del correo de notificación…" |
| `chapters/arquitectura.tex:298` | Tabla de protocolos: "API $\rightarrow$ Gemini y proveedor IAM" |
| `chapters/e50_mercado.tex:98` | Porter, proveedores: "(Redis, Postgres, API de Gemini)" |
| `chapters/producto.tex:169` | Tabla legal, transferencia internacional (art. 12) |

### Párrafo inicial de la sección 3.6 (encuesta)
- Heading: `chapters/chapter04.tex:434` `\section{Contraste con la percepción de los usuarios finales: resultados de la encuesta}`, con `\label{sec:encuesta-usuarios}` en la l. 435.
- Primer párrafo: l. 437-443 ("La encuesta se difunde [[COMPLETAR…]] entre [[COMPLETAR: fechas]]. Se trata de una muestra no probabilística por conveniencia…").
- Segundo párrafo: l. 445 ("Como complemento… 135 respuestas… 112 respuestas (83 %)…").
