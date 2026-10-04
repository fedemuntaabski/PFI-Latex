# Integración requerimientos v75b — resultado de compilación

Rama: `feature/cap-requerimientos-v75`. `chapters/requerimientos.tex` (versión nueva, sin commitear) no fue modificado; `main.tex` y `config/` intactos. Sin commits.

## Procedimiento
1. Borrados auxiliares de la raíz, todos verificados con `git check-ignore` (ignorados): `main.aux .toc .lof .lot .out .bcf .run.xml .upa .upb .log`. No existía `main.bbl`. Nada versionado tocado. `main.pdf` lo regenera latexmk.
2. Compilación: `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` desde la raíz (sin outdir, no hace falta `-auxdir`). Exit 0; latexmk corrió biber.

## Resultados
| Ítem | Resultado |
|---|---|
| Errores (`!` / `file:line:`) | 0 |
| `\ref` sin resolver | 0 |
| `\cite` sin resolver | 0 |
| Warnings de biber | 0 |
| Páginas totales | **182** |
| Profundidad del índice (`main.toc`) | chapter 12, section 46, subsection 78, subsubsection 38; **ningún** paragraph/subparagraph. Máximo = subsubsection (`tocdepth=3`) |
| Celda `[[ESTADO SEGÚN RNF-02]]` | intacta, `requerimientos.tex:220` |

## Overfull \hbox dentro de requerimientos.tex: 5 (antes 46)
`requerimientos.tex` entra por `\input` al inicio de `chapter03.tex` y ocupa `main.log` 3736–~4000. Los `\hbox` posteriores (líneas de fuente 160–667, log 4145+) pertenecen a chapter03/04, no a este archivo.

| Línea fuente | Magnitud | Contenido |
|---|---|---|
| 226 | 1.63 pt | fila RNF-05 (Disponibilidad) |
| 230 | 11.42 pt | fila RNF-07 (Configurabilidad) |
| 242 | 12.07 pt | fila RNF-13 (Confidencialidad en tránsito) |
| 515 | 6.84 pt | encabezado `Requerimiento / Caso de uso / Historias de usuario` (primera página del longtable) |
| 519 | 6.84 pt | mismo encabezado (repetido en páginas siguientes) |

Máximo 12.07 pt. Probable causa: celdas con términos largos sin guion posible (RNF-07, RNF-13) y encabezado de tabla con columnas anchas. No corregido (contenido no modificable).

## Fuera de alcance (informativo)
- Total en el documento: 11 `Overfull \hbox`; 6 son de otros capítulos (chapter03: líneas 160, 166–167, 273–274, 300; chapter04: 634, 667).
- 180 `Overfull \vbox (36.8594pt too high) ... while \output is active`: es el logo `UADE_LARGE.png` del encabezado (`main.tex:54`), recurrente por página; no viene de requerimientos.
- Warnings menores: 8× float `h` → `ht`, microtype `footnote`, `soulutf8` y `xcolor usenames` obsoletos.

## Estado git
Solo ` M chapters/requerimientos.tex` y este archivo sin trackear. Auxiliares ignorados.
