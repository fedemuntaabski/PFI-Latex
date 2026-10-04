# fix_bib_imagenes_pfi75

Rama: `fix/bib-imagenes-pfi75` (desde `analysis/redaccion-pfi75`). Sin commit ni push.

## 1. Imágenes
Revisados todos los `\includegraphics` contra `git ls-files` (comparación exacta). Solo 2 desajustes:

| Archivo:línea | Antes | Después |
|---|---|---|
| chapters/chapter03.tex:1069 | `images/diagramas/Redis.png` | `images/diagramas/redis.png` |
| chapters/chapter03.tex:1077 | `images/diagramas/Supabase.png` | `images/diagramas/supabase.png` |

`schedule_of_activities.tex:7` (`Cronograma.png`) está comentado; no se tocó.

## 2. biblio.bib
- Eliminadas: `Will2026`, `Abramsky1993`, `AltenkirchGrattage2005`, `MDPIFutures2025`, `Landauer2022CLUELDS` (reemplazada por `Landauer2022Dataset`).
- Duplicados resueltos: `Artioli2024` (1 entrada), `AlShehari2023` (1), `JNSM2025` (1), `Kuppa2022` (queda "Learn to Adapt…", Comput. Electr. Eng. 102, 108239, DOI 10.1016/j.compeleceng.2022.108239; eliminado "Towards Adversarial Evaluations…" y la copia del bloque de merge).
- Sintaxis: eliminadas las líneas `=========` y `>>>>>>>>> Temporary merge branch 2` (junk at toplevel).
- `AlShehari2023`: DOI **10.1109/ACCESS.2023.3326750**, vol. 11, pp. 118170–118185, autor "Alfakih".
- `JNSM2025`: agregado `doi = {10.1007/s10922-025-09998-x}` (ninguna entrada original tenía DOI; el de la URL resuelve en Crossref).
- `VillarrealVasquez2023` → `VillarrealVasquez2021` (year=2021, TDSC, DOI 10.1109/TDSC.2021.3135639).
- `Landauer2023` → `Landauer2022` (year=2022, BigData 2022, DOI 10.1109/BigData55660.2022.10020672).
- Nuevas: `Landauer2022Dataset` (Zenodo, 2022, DOI 10.5281/zenodo.7119953, `note = {Licencia CC BY 4.0}`), `Landauer2023Survey` (MLWA 12, art. 100470, DOI 10.1016/j.mlwa.2023.100470), `Benova2024` (Sensors 24(3), 746, DOI 10.3390/s24030746).
- `Fahrmann2022`: `\&` → `and`.

## 3. Citas reasignadas
`Landauer2023` → `Landauer2023Survey`:

| Archivo:línea | Frase |
|---|---|
| chapter02.tex:170 | "…la revisión sistemática realizada por \textcite{…} sobre técnicas de detección de anomalías en registros de eventos…" |
| chapter02.tex:204 | "Investigaciones como el análisis de \textcite{…} destacan que algoritmos como LSTM, redes basadas en grafos (GNN) y autoencoders…" |
| chapter02.tex:213 | "La revisión sistemática de \textcite{…} sobre técnicas de detección de anomalías en registros de eventos…" |
| chapter02.tex:228 | "entre ellas las de \textcite{Artioli2024} y \textcite{…}, coinciden en que no existe un único algoritmo…" |
| chapter04.tex:346 | Tabla "Comparación de algoritmos: revisión sistemática", fila "Fuente académica" |
| chapter04.tex:376 | "Síntesis directa de las recomendaciones de \textcite{Artioli2024} y \textcite{…}: enfoque híbrido…" |

Ningún uso de `Landauer2023` hablaba del dataset, así que `Landauer2022` (paper del dataset) no queda citada en el texto.

Otros cambios de clave:
- `VillarrealVasquez2023` → `VillarrealVasquez2021`: chapter02.tex:163, 200, 202; chapter04.tex:250.
- `Landauer2022CLUELDS` → `Landauer2022Dataset`: chapter02.tex:231 (dataset CLUE-LDS).

## 4. chapter03.tex:278
`(Villarreal-Vásquez et al., Benova \& Hudec)` → `\parencite{VillarrealVasquez2021, Benova2024}`.

## Verificación web
- **Al-Shehari**: Crossref resuelve 10.1109/ACCESS.2023.3326750 a "Insider Threat Detection Model Using Anomaly-Based Isolation Forest Algorithm", IEEE Access 11, 118170–118185. El DOI …3323769 no existe en Crossref ni doi.org (404). Correcto: …3326750.
- **Landauer survey**: Machine Learning with Applications, vol. 12, art. 100470, junio 2023, DOI 10.1016/j.mlwa.2023.100470 (Crossref).
- **Tian et al. 2023** (solo reporte): el abstract (Semantic Scholar) dice que proponen el modelo ITDE (GNN heterogéneo con atención de dos capas) y lo validan en **CERT r4.2**, superando métodos del estado del arte. **El abstract no reporta ninguna mejora de F1** ni cifras; ese dato requiere el texto completo.
- **Zenodo CLUE-LDS**: 10.5281/zenodo.7119953 es la versión v1 (28/09/2022, CC BY 4.0); 10.5281/zenodo.7119952 es el DOI conceptual. Se usó …953 como pediste.
- **Benova & Hudec**: Crossref confirma Sensors 24(3), 746, 2024.

## Puntos para revisar
- `VillarrealVasquez2021`: el DOI es de early access (dic. 2021), pero Crossref lo ubica en TDSC vol. 20, n.º 1, pp. 451–462, publicado 2023-01. Se dejó year=2021 como pediste. La entrada no tiene vol/pp; se podría agregar.
- `JNSM2025`: el autor figura como el nombre de la revista. Los autores reales son Gambo y Almulhem (JNSM 34, art. 25, 2025). No se cambió porque altera el texto de `\textcite`.
- `main.pdf` versionado tenía 165 págs, pero estaba desactualizado: HEAD sin mis cambios compila a 176 págs.

## 5. Compilación
`latexmk -pdf -outdir=<scratchpad>/build main.tex` (biber).
- Biber: sin warnings ni errores (`main.blg` limpio; antes: "Duplicate entry key" ×5 y junk at toplevel).
- Citas sin resolver: ninguna.
- Warning restante (preexistente): `name{appendix*.1} has been referenced but does not exist, replaced by a fixed one`.
- Páginas: **176** (HEAD sin cambios, compilado en las mismas condiciones: 176; PDF versionado: 165).
