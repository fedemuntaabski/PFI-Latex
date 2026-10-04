# Integración capítulo Pruebas (v75)

Rama `feature/cap-pruebas-v75` (desde `feature/cap-requerimientos-v75`). Sin commits.

## Cambios
- `main.tex`: `\input{chapters/pruebas} % provisorio: reordenar luego` entre `chapter03` (Demo, cap. 9) y `chapter04`. Pruebas queda como cap. 10; Análisis comparativo pasa a 11. Único cambio en main.tex.
- `chapters/pruebas.tex` e `images/pruebas/` traídos del working tree de `feature/diagramas-v75` (no existían en la rama de requerimientos). Contenido sin modificar. Cambios originales guardados en `git stash` ("wip-pruebas-diagramas-v75").
- `biblio.bib`: agregada `Nielsen1994`. DOI `10.1145/191666.191729` verificado vía doi.org (CSL JSON): título, autor, SIGCHI, pp. 152-158 coinciden.
- `Landauer2022Dataset` (biblio.bib:389) y `Landauer2023Survey` (biblio.bib:206) existen.

## Figura
- `images/pruebas/curva_umbral.pdf` NO existía. Generado desde el PNG con Pillow (300 dpi): **raster, no vectorial**.
- PROBLEMA: el PNG presente es la versión VIEJA (con título interno, leyenda con nombres de variable como `E1_exfiltracion`, sin marcadores distintos por escenario, ejes "Porcentaje (%)" / "Umbral t sobre el score híbrido"). No coincide con lo descrito en `curva_umbral_pfi75.md` (16×9 cm, sin título, leyenda en español). Hay que traer el PDF vectorial nuevo del repo del script (`scripts/analysis/curva_umbral.py`) y reemplazar.
- Legible: sí, a ancho de texto (pág. PDF 108, impresa 106, Fig. 10.1), aunque la fuente interna es chica.

## Compilación (latexmk, auxiliares borrados antes)
- Errores: 0. Exit 0.
- `\ref`/`\cite` sin resolver: 0. Biber sin warnings (31 citekeys).
- Páginas: 194 (PDF). Numeración impresa "de 192".
- Índice: máximo `subsubsection` (13 chapter, 56 section, 88 subsection, 38 subsubsection). tocdepth=3.
- Overfull \hbox `pruebas.tex`: ninguno.
- Overfull \hbox `requerimientos.tex` (líneas del .tex, magnitud): 50 (3,5pt), 46-52 (7,5), 54 (3,5), 52-56 (7,5), 56-61 (7,5), 68 (3,5), 64-70 (7,5), 72 (3,5), 70-74 (7,5), 74-85 (7,5), 92 (3,5), 88-94 (7,5), 96 (3,5), 94-98 (7,5), 105-106 (25,3), 98-107 (7,5), 114 (3,5), 110-116 (7,5), 118 (3,5), 116-120 (7,5), 120-133 (7,5), 140 (3,5), 136-142 (7,5), 144 (3,5), 142-146 (7,5), 146-157 (7,5), 164 (3,5), 160-166 (7,5), 168 (3,5), 166-170 (7,5), 170-181 (7,5), 188 (3,5), 184-190 (7,5), 192 (3,5), 190-194 (7,5), 194-201 (7,5), 207-213 (7,5), 213-217 (7,5), 226 (1,6), 228-229 (13,9), 230 (11,4), 242 (12,1), 217-248 (7,5), 266-267 (5,4), 515 (6,8), 519 (6,8). Mayormente tablas (celda "Prioridad"/"Requerimiento" y alineaciones); peor caso 25,3 pt en l.105-106.
- Overfull \vbox 36,86 pt repetido (logo UADE del header, preexistente en todo el documento).

## Marcadores `[[...]]` (a propósito)
- `pruebas.tex:200` `[[CPU MEDIA]]`, `[[CPU P95]]`, `[[CPU MÁX]]`
- `pruebas.tex:202` `[[RSS MEDIA]]`, `[[RSS P95]]`, `[[RSS MÁX]]`
- `pruebas.tex:206` `[[INTERPRETACIÓN DE RNF-02 SEGÚN EL RESULTADO]]`
- `pruebas.tex:309` `[[RESULTADOS DE LA EVALUACIÓN HEURÍSTICA: ...]]`

## Nota
`requerimientos.tex` de la rama de requerimientos difiere del de `feature/diagramas-v75` (19 líneas); se usó el de la rama base, sin tocarlo.
