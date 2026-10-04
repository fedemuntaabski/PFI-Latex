# fix_bib_detalles_pfi75

Rama `fix/bib-detalles-pfi75` (desde `fix/bib-imagenes-pfi75`). Solo `biblio.bib` modificado. Sin commit ni push.

## 1. `VillarrealVasquez2021`
Agregado: `volume = {20}`, `number = {1}`, `pages = {451--462}`, `note = {Publicado en vol. 20, n.º 1, 2023}`. `year = {2021}` y clave sin cambios.
Crossref confirma: TDSC vol. 20, n.º 1, pp. 451-462, published-print 2023-01.

**Opción elegida: mantener year=2021 + `note`.** Cambiar a 2023 obliga a renombrar la clave en 5 `\cite` (chapter02.tex:163, 200, 202; chapter03.tex:278; chapter04.tex:250), y pediste no tocar `.tex`. Las citas siguen diciendo "2021" (verificado en el PDF).
Limitación: ISO 690 estricto prefiere el año de la versión de registro (2023). Si autorizás tocar `.tex`, el cambio ideal es `year=2023` + clave `VillarrealVasquez2023TDSC`.

## 2. `JNSM2025`
Verificado con Crossref (DOI 10.1007/s10922-025-09998-x):
- Título: "Zero Trust Architecture: A Systematic Literature Review" (ya era correcto).
- Autores: **Muhammad Liman Gambo** y Ahmad Almulhem.
- Revista: Journal of Network and Systems Management, vol. 34, n.º 1, article-number 25.

Cambios: `author`, `journal` (antes decía "Springer"), `publisher = Springer`, `volume = 34`, `number = 1`, `pages = {25}` (número de artículo).
Discrepancia: Crossref da publicación online 2025-11-13 y published-print **2026-01**. Dejé `year = 2025` como pediste. Si ISO 690 estricto, correspondería 2026. No se cita hoy.

## 3. Compilación
`latexmk -pdf` con outdir fuera del árbol (`%TEMP%\pfi75build`, rc=0). `main.blg`: 0 warnings/errors de biber. Única referencia no resuelta: `appendix*.1` de hyperref, preexistente y ajena al `.bib`. `git status`: solo `biblio.bib` modificado (más este .md).
