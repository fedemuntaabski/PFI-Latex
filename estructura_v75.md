# Estructura v75 — refactor/estructura-v75

## FASE A — Mapa previo
main.tex (cuerpo, antes): title, chapter01, chapter02, chapter03, arquitectura*, datos*, producto*, pruebas*, chapter04, (conclusion comentado), bibliografía, anexo, listas. (*con "% provisorio")

| Archivo | \chapter | Líneas | Labels |
|---|---|---|---|
| chapter01 | Introducción | – | – |
| chapter02 | Antecedentes (2.2.6 CLUE-LDS L230–236) | – | – |
| chapter03 L1–2 | `\input{requerimientos}` suelto | 1–2 | – |
| chapter03 | Justificación de Diseño y Mockups | 3–314 | sec:decisiones-transversales-mockups, fig/tab:mockup-* |
| chapter03 | Diagramas UML | 315–367 | fig:diagrama-flujo/componentes/clases-agente/clases-api/objetos |
| chapter03 | Análisis de Mercado y Competitividad | 368–466 | fig:matriz-foda, fig:matriz-bcg |
| chapter03 | Tecnologías | 467–675 | sec:tecnologias, tab:lenguajes, tab:frameworks-{api,agente,frontend,mlcore}, tab:protocolos |
| chapter03 | Modelo de Datos | 676–705 | fig:diagrama-bases-de-datos-{redis,supabase}, fig:diagrama-arquitectura |
| chapter03 | Demo | 706–801 | fig:demo-* (11) |
| chapter04 | Análisis Comparativo del Estado del Arte | – | – |

No había capítulos fuera de la lista. chapter04 confirmado como análisis comparativo.

## FASE B — Partición
- e50_requerimientos (1–2), e50_diseno_ux (3–314), e50_uml (315–367), e50_mercado (368–466), archivo/obsoleto_e50.tex (467–fin + CLUE-LDS de chapter02).
- Los `\clearpage` previos a cada `\chapter` quedaron al final del archivo anterior.
- Verificación: `cat e50_* + obsoleto_e50 (sin líneas %%ORIGEN, sin bloque CLUE) | diff - chapter03.tex` → **diff vacío**. chapter03.tex eliminado (`git rm`).

## FASE C
`\subsection{El Dataset CLUE-LDS}` (3 párrafos + línea en blanco) movida sin cambios de texto de chapter02 a obsoleto_e50.tex.

## FASE D
Orden en main.tex: chapter01, chapter02, chapter04, e50_requerimientos, e50_diseno_ux, e50_uml, arquitectura, datos, producto, pruebas, e50_mercado. Comentarios "provisorio" removidos. Secciones comentadas intactas.

## FASE E — Refs a labels solo-obsoletos
Ninguna. (`tab:lenguajes` y `tab:protocolos` también están definidos en arquitectura.tex; antes estaban duplicados, ahora no.)

## FASE F — Compilación (latexmk, aux borrados antes)
- Errores: 0
- \ref/\cite sin resolver: 0
- Labels duplicados: 0
- Páginas: 206
- Warnings (5, no críticos): xcolor usenames obsoleto, microtype footnote patch, soulutf8 obsoleto, 2× `h` float → `ht`
- Índice: 13 chapter (11 numerados + Bibliografía + Anexo), 67 section, 101 subsection, 38 subsubsection (máximo nivel: subsubsection)
- Capítulos numerados: 1 Introducción · 2 Antecedentes · 3 Análisis Comparativo del Estado del Arte · 4 Requerimientos, Casos de Uso e Historias de Usuario · 5 Justificación de Diseño y Mockups · 6 Diagramas UML · 7 Arquitectura y tecnologías · 8 Datos · 9 Producto implementado · 10 Pruebas y resultados · 11 Análisis de Mercado y Competitividad

## Observaciones
- En main.toc la entrada Bibliografía apunta a `figure.11.2` (addcontentsline de plantilla, preexistente; no tocado).
