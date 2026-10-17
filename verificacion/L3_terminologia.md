# L3 – terminología

Rama: e75/correcciones-e50-v2. Compilación: sin errores, sin "??", sin citas/referencias indefinidas.

## 1. "capítulo" → "sección" (conteo por archivo)

| Archivo | Reemplazos |
|---|---|
| chapters/chapter01.tex | 14 |
| chapters/chapter02.tex | 1 |
| chapters/chapter04.tex | 3 |
| chapters/arquitectura.tex | 1 |
| chapters/datos.tex | 1 |
| chapters/producto.tex | 6 |
| chapters/pruebas.tex | 3 |
| chapters/e50_mercado.tex | 1 |
| chapters/e50_uml.tex | 1 |
| chapters/negocio.tex | 2 |
| chapters/conclusiones.tex | 1 |
| chapters/requerimientos.tex | 4 |


### Lista antes → después (patrones aplicados)

| Antes | Después |
|---|---|
| Este capítulo | Esta sección |
| El capítulo~\ref | La sección~\ref |
| el capítulo~\ref / el capítulo de X | la sección~\ref / la sección de X |
| del capítulo(~\ref / anterior) | de la sección |
| los capítulos de producto y de pruebas | las secciones de producto y de pruebas |
| trece capítulos | trece secciones |
| (capítulo~\ref{chap:conclusiones}) | (sección~\ref{chap:conclusiones}) |
| y el \n capítulo~\ref (chapter01 L124, 132, 134) | y la sección~\ref (concordancia corregida en el artículo de la línea previa, L123, 131, 133: "El"→"La", "y el"→"y la") |

### Excepciones (no cambiadas)
- main.tex: 2 menciones (preámbulo/comandos LaTeX).
- chapters/archivo/obsoleto_e50.tex: 2 menciones, archivo no incluido por main.tex.
- Anexos y bibliografía: 0 menciones.

grep -i "cap[ií]tulo" sobre los .tex incluidos por main.tex (chapters/): 0 resultados.

## 2. Etiqueta del entrevistador

`MOCIULSKY SANTIAGO BERNARDO:` → `MOCIULSKY SANTIAGO:` (interview_1_pablo 17, interview_2_jacubovich 8, interview_3_guillermo 7, interview_4_pena 17; total 49).

Sin cambiar, reportado: "Mociulsky Santiago Bernardo" en la línea \textbf{Entrevistadores} de los 4 anexos (4 ocurrencias) y en archivos .md fuera del .tex (informes_e75/04 y 11, documentacion/e75_correcciones_forma.md y las 4 transcripciones de documentacion 50%).

## 3. Sección 3.5 (chapter04.tex:402)

- Antes: "...se realiza un relevamiento cualitativo mediante entrevistas semiestructuradas a cinco profesionales vinculados..."
- Después: "...se realiza un relevamiento cualitativo mediante cuatro entrevistas semiestructuradas y un cuestionario escrito a cinco profesionales vinculados..."
