# Integración datos v75

Rama `feature/cap-datos-v75` desde `feature/cap-producto-v75`. Sin push, sin trailers, preámbulo, `datos.tex` y `pruebas.tex` sin modificar por mí.

## Commit previo
`9dde3b6 informe` en `feature/cap-producto-v75`: solo `integracion_producto_v75.md`.

## Dependencias de datos.tex
- `Landauer2022` (biblio.bib:198) y `Landauer2022Dataset` (biblio.bib:389): existen.
- `sec:evaluacion-modelo`: pruebas.tex:209, existe.
- Imágenes `images/diagramas/v75/` NO estaban en esta rama: traídas con `git checkout feature/diagramas-v75 -- images/diagramas/v75/` (commit 27e8167). Se trajo el directorio completo (28 archivos: clases, despliegue y ER), incluidos `er_postgres_scoring_eventos.pdf` y `er_postgres_config_modelos.pdf`.
- Referencias internas de datos.tex (tab:claves-redis, tab:entrenamiento, fig:er-config, fig:er-scoring, tab:mapeo-agente, tab:seleccion-datos, tab:tablas-postgres): resueltas.

## main.tex
`\input{chapters/datos} % provisorio: reordenar luego` inmediatamente antes de producto. Orden: chapter03, datos, producto, pruebas, chapter04.

## Compilación (aux borrados, latexmk)
- Errores: 0
- \ref/\cite sin resolver: 0
- Overfull \hbox: datos.tex 0; pruebas.tex 0
- Páginas: 217 (antes 205)
- Índice: tocdepth=3 (15 chapter, 68 section, 101 subsection, 38 subsubsection)
- Marcadores `[[...]]` (solo RNF-02): producto.tex:127; pruebas.tex:200, 202, 206; requerimientos.tex:220. El de pruebas.tex:309 (evaluación heurística) ya no existe.

## Solo lectura: contenido del E50 obsoleto o duplicado por datos.tex (nada borrado)
| Archivo:línea | Título / contenido | Motivo |
|---|---|---|
| chapters/chapter02.tex:230 | `\subsection{El Dataset CLUE-LDS}` (2.2.6; párrafos 231-235, "50 millones de eventos", 5.000 usuarios) | datos.tex §Conjunto de datos lo cubre |
| chapters/chapter02.tex:24 | `\subsection{User and Entity Behavior Analytics: fundamentos y dataset de referencia}` | menciona dataset de referencia; revisar solapamiento |
| chapters/chapter02.tex:69 | `\subsection{Introducción a los Datasets: Datos Reales vs. Datos Sintéticos}` | posible solapamiento con selección de datos |
| chapters/chapter03.tex:677 | `\section{Diagrama de Bases de Datos}` (figuras con caption "Diagrama de Bases de Datos." en :682 redis.png y :690 supabase.png; labels fig:diagrama-bases-de-datos-redis / -supabase) | reemplazado por Modelo de datos y los ER v75 de datos.tex |
| chapters/chapter03.tex:600 | fila `imbalanced-learn` de `\subsection{Pipeline offline (ml\_core/, scripts/)}` (586): "253 sesiones etiquetadas sobre 7,6 millones de eventos" | única aparición de "253 sesiones", "7,6 millones" e "imbalanced-learn" fuera de datos.tex |
| chapters/chapter04.tex:370 | fila "Dataset / validación" de `\subsection{IsolationForest + LSTM Autoencoder (proyecto propuesto)}` (358): CLUE-LDS ~50M eventos | duplica cifras del dataset |

Nota: grep de "253", "7,6", "7.6", "7\,6" y "millones" no halló otras menciones (chapter02:163, chapter03:461 y appendix/interview_2 no tienen relación con el dataset).
