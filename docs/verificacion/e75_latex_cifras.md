# E75 — Cifras finales de pruebas y cobertura (código a2d1f8a)

- Rama base: `e75/cierre` (existía local y en origin) → rama nueva `e75/cifras-finales`.
- Commit: `eb0d6d4ed25cbd7c1c374a4971a6846a5fb32b6a` — "docs: cifras finales de pruebas y cobertura (a2d1f8a)", sin trailers, sin push.

## Cambios

| Punto | Archivo:línea | Antes | Después | OK |
|---|---|---|---|---|
| 1 | chapters/pruebas.tex:55 | 529 pruebas automatizadas, 352 de la API | 530 pruebas automatizadas, 353 de la API | ✔ |
| 2 | chapters/pruebas.tex:68 | API de scoring & 35 & 352 | API de scoring & 35 & 353 | ✔ |
| 3 | chapters/pruebas.tex:90 | 352 aprobadas, 0 fallidas, 0 omitidas | 353 aprobadas, 0 fallidas, 0 omitidas | ✔ |
| 4 | chapters/pruebas.tex:92 | 328 aprobadas, 15 omitidas, 0 fallidas | 326 aprobadas, 18 omitidas, 0 fallidas | ✔ |
| 5 | chapters/pruebas.tex:102 | Las 15 pruebas omitidas … son las que requieren los artefactos de modelo, que no están versionados. | Las 18 pruebas omitidas … dependen de artefactos que no están versionados: 15 requieren los modelos entrenados y 3 verifican la paridad de las variables con la segunda versión del modelo. | ✔ |
| 6 | chapters/pruebas.tex:113 | … había fallado …; se agregó a los requisitos de la API y el umbral de la API se fijó en el 74 %. … requieren los modelos entrenados (15 omitidas y cuatro archivos excluidos) | … falló …; se agregó a los requisitos de la API. Con esa corrección, el \emph{pipeline} finaliza con los cuatro trabajos aprobados. … requieren artefactos de modelo no versionados (18 omitidas y cuatro archivos excluidos) | ✔ |
| 7a | chapters/pruebas.tex:137 | API (PDP) & 352 & 2\,465 | API (PDP) & 353 & 2\,469 | ✔ |
| 7b | chapters/pruebas.tex:141 | Total & \textbf{529} & 3\,581 | Total & \textbf{530} & 3\,585 | ✔ |
| 8 | chapters/pruebas.tex:652 | Las 529 pruebas automatizadas (352 de la API | Las 530 pruebas automatizadas (353 de la API | ✔ |
| 9 | chapters/conclusiones.tex:59 | 529 pruebas automatizadas (352 de la API | 530 pruebas automatizadas (353 de la API | ✔ |

Notas:
- Punto 6: en la fuente, el tramo hasta "…se fijó en el 74 %." era una sola oración; se reemplazó completa. El umbral del 74 % sigue indicado en la lista de trabajos de CI (pruebas.tex:108).
- Punto 6: "pipeline" se escribió como `\emph{pipeline}`, igual que en el resto del capítulo (pruebas.tex:105).
- Porcentajes de la Tabla 10.IV sin cambios (93,9/92,4; 89,3/88,1; 92,5/91,1).

## Greps en todos los .tex

Patrones: `529`, `352`, `2\,465`/`2 465`, `3\,581`/`3 581`, `328`, `15 omitidas`, `quince` (y además `omitid`).

Antes de editar: coincidencias solo en chapters/pruebas.tex (L55, 68, 90, 92, 102, 113, 137, 141, 652) y chapters/conclusiones.tex:59, todas dentro de los 9 puntos. Fuera de ellos:
- `history/considerations.tex:14` — URL `tex.stackexchange.com/questions/511328/…` (contiene "328"); falso positivo, sin cambios.

Resumen, abstract, anexos e introducción: sin coincidencias.

Después de editar: solo queda el falso positivo de `history/considerations.tex:14`.

## Compilación

Cadena: `pdflatex main` → `biber main` → `pdflatex main` → `pdflatex main`. biber sin ERROR/WARN; main.log sin referencias indefinidas ni avisos de recompilación.

## PDF (pdftotext)

- Cifras viejas: `529` 0, `352` 0, `2 465` 0, `3 581` 0, `15 omitidas` 0, `quince` 0. `328` 1, solo en la bibliografía (DOI 10.3390/fi17080328), ajeno a pruebas.
- `??`: 0.
- Cifras nuevas presentes: 530/353 (inventario, Tablas 10.II–10.IV, síntesis, Tabla 13.I), `2 469`, `3 585`, `326 aprobadas`, `18 omitidas` (Tabla 10.III y párrafo de CI).
- Páginas: 261 (antes 261). Sin cambios.
