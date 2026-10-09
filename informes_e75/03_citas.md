# E75 — Citas ISO 690: obras de dos autores, citas narrativas y Villarreal-Vasquez

Rama `correcciones-e75-latex`. Fecha: 2026-10-09.

## Causa encontrada

La causa no estaba en el texto ni en la `.bib`:
- **No había texto escrito a mano.** En los archivos compilados no aparece "et al." literal; todas las citas usan `\parencite` o `\textcite`.
- **La `.bib` está bien cargada.** `Larman2003` (`biblio.bib:446`, `{Larman, Craig and Basili, Victor R.}`) y `Osterwalder2010` (`biblio.bib:373`, `{Osterwalder, Alexander and Pigneur, Yves}`) separan los autores con `and`. biber los lee como 2 autores (`\name{author}{2}` en `build/main.bbl`), y la lista de referencias los muestra completos ("LARMAN, Craig y BASILI, Victor R., 2003").
- **La causa es el estilo.** `biblatex-iso690` v0.4.1, en `iso-authoryear.cbx` l. 4-8, fija:
  ```latex
  % Use only one name in citation to be consistent
  \ExecuteBibliographyOptions{maxcitenames=1, mincitenames=1}
  ```
  Con `maxcitenames=1`, cualquier obra de más de un autor se abrevia en la cita como "Primero et al.", aunque tenga solo dos. `main.tex` no cambiaba esos valores.
- **Segundo problema, que aparece al corregir el primero.** `iso.bbx` l. 150 y 154 define el separador entre nombres (`multinamedelim`) como "; " y usa el mismo para el último nombre (`finalnamedelim`). Si solo se sube `maxcitenames`, la cita sale "(Larman; Basili, 2003)" en lugar de "(Larman y Basili, 2003)".

El problema no se limitaba a Larman y Osterwalder: afectaba a las **7 obras de dos autores** del documento (Larman2003, Osterwalder2010, Ansari2025, Atlam2025, Benova2024, Kuppa2022 y NIST2023_800207A).

## Corrección de fondo (`main.tex`)

| Archivo:línea | Antes | Después |
|---|---|---|
| `main.tex:16` | `\usepackage[backend=biber, style=iso-authoryear, language=spanish, uniquelist=false]{biblatex}` | `\usepackage[backend=biber, style=iso-authoryear, language=spanish, uniquelist=false, maxcitenames=2, mincitenames=1]{biblatex}` |
| `main.tex:19-20` | (no existía) | `% ISO 690 en las citas: dos autores unidos por "y" (el estilo usa "; " entre nombres)`<br>`\DeclareDelimFormat[cite,parencite,textcite,citeauthor]{finalnamedelim}{\addspace\bibstring{and}\space}` |

Resultado en las citas:
- 1 autor: "Apellido".
- 2 autores: "Apellido y Apellido".
- 3 o más: "Apellido et al." (con `maxcitenames=2`, una lista de 3 o más nombres se corta en `mincitenames=1`).

El separador se cambia solo en los contextos de cita (`cite`, `parencite`, `textcite`, `citeauthor`); la lista de referencias no cambia de formato. `\bibstring{and}` en español es "y". Ninguno de los segundos autores actuales empieza con i/hi, así que no hace falta "e".

## Citas narrativas convertidas a parentéticas

| Archivo:línea | Antes | Después |
|---|---|---|
| `chapters/negocio.tex:17-18` (texto de 12.2) | "…resume el modelo en los nueve bloques del lienzo de `\textcite{Osterwalder2010}`." → PDF: "lienzo de Osterwalder et al. (2010)." | "…resume el modelo en los nueve bloques del lienzo `\parencite{Osterwalder2010}`." → PDF: "lienzo (Osterwalder y Pigneur, 2010)." |
| `chapters/negocio.tex:56` (fuente de la tabla 12.I) | "Fuente: elaboración propia con el esquema de `\textcite{Osterwalder2010}`." | "Fuente: elaboración propia sobre el esquema del lienzo del modelo de negocio `\parencite{Osterwalder2010}`." → PDF: "(Osterwalder y Pigneur, 2010)." |
| `chapters/chapter04.tex:388` (tabla 3.XV, celda "Relación con el diseño del proyecto") | "Síntesis directa de las recomendaciones de `\textcite{Artioli2024}` y `\textcite{Landauer2023Survey}`: enfoque híbrido…" | "Síntesis directa de las recomendaciones de la literatura `\parencite{Artioli2024, Landauer2023Survey}`: enfoque híbrido…" → PDF: "(Artioli et al., 2024; Landauer et al., 2023)" |

Se mantienen como `\textcite`, porque son celdas "Fuente académica" de las tablas del capítulo 3:

| Archivo:línea | PDF |
|---|---|
| `chapter04.tex:141` (tabla 3.VI) | Aliyu et al. (2024) |
| `chapter04.tex:238` (tabla 3.IX) | Aliyu et al. (2024) (ad-RACs) |
| `chapter04.tex:262` (tabla 3.X) | Villarreal-Vasquez et al. (2021) |
| `chapter04.tex:286` (tabla 3.XI) | Tian et al. (2023) |
| `chapter04.tex:310` (tabla 3.XII) | Artioli et al. (2024) |
| `chapter04.tex:334` (tabla 3.XIII) | Hariri et al. (2019) |
| `chapter04.tex:358` (tabla 3.XIV) | Landauer et al. (2023) |

Después del cambio, las únicas citas narrativas "Apellido et al. (año)" del PDF son estas siete.

## Villarreal-Vasquez

**No se encontraron variantes; no hubo que cambiar nada.** La `.bib` (`biblio.bib:263`) dice `Villarreal-Vasquez`, y las 5 citas usan la clave `VillarrealVasquez2021` (`chapter02.tex:228, 267, 269`; `chapter04.tex:262`; `requerimientos.tex:380`). Búsqueda sin distinguir mayúsculas de "Vásquez", "Vasquez", "Villareal" y "Vazquez" en todos los `.tex`, `.bib` y `.bbl`, incluidos los que no se compilan: solo aparece "Villarreal-Vasquez". En el PDF final aparece 5 veces "Villarreal-Vasquez" en las citas y 1 vez "VILLARREAL-VASQUEZ, M." en la bibliografía. Si el profesor vio "Vásquez", no fue en la versión actual del documento.

## Revisión de todas las citas

Método: script que extrae `\cite`/`\parencite`/`\textcite` de los 22 archivos compilados (no hay `\autocite`, `\footcite` ni `\nocite`) y cruza cada clave con `build/main.bbl` (autores según biber y año). Después se compara la forma impresa en el PDF (`pdftotext`).

Resultado: **37 claves citadas, todas con entrada en la bibliografía; no hay entradas sin citar ni citas sin definir.** El año impreso coincide con el de la `.bib` en todos los casos.

| Clave | Autores en .bib | Año | Forma en el PDF | Ubicaciones | Estado |
|---|---|---|---|---|---|
| AAIP2018 | 1 (institución) | 2018 | (Agencia de Acceso a la Información Pública, 2018) | chapter02:139 | OK |
| Aliyu2024 | Aliyu + `and others` | 2024 | (Aliyu et al., 2024) / Aliyu et al. (2024) | chapter02:217; chapter04:141, 238 (Fuente académica) | OK (ver nota 1) |
| AlShehari2023 | 5 | 2023 | (Al-Shehari et al., 2023) | chapter02:72 | OK |
| Ansari2025 | 2 | 2025 | (Ansari y Syed, 2025) | chapter01:57 | **Corregido** (antes "Ansari et al.") |
| Artioli2024 | 3 | 2024 | (Artioli et al., 2024) | chapter02:15, 32, 226, 267, 273, 297; chapter04:310 (Fuente académica), 388 | OK; l. 388 pasada a parentética |
| Atlam2025 | 2 | 2025 | (Atlam y Yang, 2025) | chapter02:55 | **Corregido** (antes "Atlam et al.") |
| Bagui2025 | 5 | 2025 | (Bagui et al., 2025) | chapter02:90 | OK |
| Benova2024 | 2 | 2024 | (…; Benova y Hudec, 2024) | requerimientos:380 | **Corregido** (antes "Benova et al.") |
| DNPDP2016 | 1 (institución) | 2016 | (Dirección Nacional de Protección de Datos Personales, 2016) | chapter02:141 | OK |
| Glockler2023 | 4 | 2023 | (Glöckler et al., 2023) | chapter02:35 | OK |
| Hariri2019 | 3 | 2019 | (Hariri et al., 2019) / Hariri et al. (2019) | chapter02:233; chapter04:334 (Fuente académica) | OK |
| Henderson1970 | 1 | 1970 | (Henderson, 1970) | e50_mercado:102 | OK |
| Hu2014 | 10 | 2014 | (Hu et al., 2014) | chapter02:45 | OK |
| Kent2015 | 1 | 2015 | (Kent, 2015) | pruebas:224 | OK |
| Kuhn2010 | 3 | 2010 | (Kuhn et al., 2010) | chapter02:40 | OK |
| Kuppa2022 | 2 | 2022 | (Kuppa y Le-Khac, 2022) | chapter02:94 | **Corregido** (antes "Kuppa et al.") |
| Landauer2022 | 4 | 2022 (a) | (Landauer et al., 2022a; …) | datos:8 | OK |
| Landauer2022Dataset | 4 | 2022 (b) | (Landauer et al., 2022b) | datos:8; pruebas:221, 263, 390 | OK |
| Landauer2023Survey | 4 | 2023 | (Landauer et al., 2023) / Landauer et al. (2023) | chapter02:235, 271, 283, 297; chapter04:358 (Fuente académica), 388; pruebas:263 | OK; l. 388 pasada a parentética |
| Larman2003 | 2 | 2003 | (Larman y Basili, 2003) | chapter01:67 (sección 1.4) | **Corregido** (antes "Larman et al.") |
| Ley20744 | 1 (institución) | 1974 | (República Argentina, 1974) | chapter02:146 | OK |
| Ley25326 | 1 (institución) | 2000 | (República Argentina, 2000) | chapter02:106 | OK |
| Ley27483 | 1 (institución) | 2019 | (República Argentina, 2019) | chapter02:143 | OK |
| Ley27699 | 1 (institución) | 2022 | (República Argentina, 2022) | chapter02:144 | OK |
| Nielsen1994 | 1 | 1994 | (Nielsen, 1994) | pruebas:479 | OK |
| NIST2023_800207A | 2 | 2023 | (Chandramouli y Butcher, 2023) | chapter02:100 | **Corregido** (antes "Chandramouli et al.") |
| Osterwalder2010 | 2 | 2010 | (Osterwalder y Pigneur, 2010) | negocio:2, 18, 56 | **Corregido** (antes "Osterwalder et al."); l. 18 y 56 pasadas a parentéticas |
| Porter1979 | 1 | 1979 | (Porter, 1979) | e50_mercado:91 | OK |
| Rose2020 | 4 | 2020 | (Rose et al., 2020) | chapter01:18; chapter02:11, 18, 97, 100, 302; requerimientos:8; arquitectura:8; e50_mercado:114 | OK |
| Sharma2020 | 3 | 2020 | (Sharma et al., 2020) | chapter02:267 (dos citas) | OK |
| Stylios2023 | 4 | 2023 | (Stylios et al., 2023) | chapter02:253, 255 | OK |
| Tian2023HGNN | 6 | 2023 | (Tian et al., 2023) / Tian et al. (2023) | chapter02:230; chapter04:286 (Fuente académica) | OK |
| VillarrealVasquez2021 | 4 | 2021 | (Villarreal-Vasquez et al., 2021) / Villarreal-Vasquez et al. (2021) | chapter02:228, 267, 269; chapter04:262 (Fuente académica); requerimientos:380 | OK |
| Weihrich1982 | 1 | 1982 | (Weihrich, 1982) | e50_mercado:42 | OK |
| Wu2021GNN | 6 | 2021 | (Wu et al., 2021) | chapter02:275 | OK |
| Xiao2022 | 5 | 2022 | (Xiao et al., 2022) | chapter02:50 | OK |

Las líneas son las del archivo indicado (`chapter01` = `chapters/chapter01.tex`, etc.).

**Nota 1 — Aliyu2024.** La entrada tiene `author = {Aliyu, M. B. and others}` (`biblio.bib:253`): solo se cargó el primer autor y el resto figura como "otros". Por eso la cita sale "Aliyu et al." (correcto si el artículo tiene más de un autor) y la bibliografía dice "ALIYU, M. B. et al.". No se modificó. Si se quiere la lista completa en la bibliografía, hay que completar los autores en la `.bib` a partir del artículo; la cita no cambiaría mientras tenga 3 o más autores.

## Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`; latexmk corre biber:
- Compila sin errores (`!`: 0). biber (`main.blg`): 0 warnings y 0 errores.
- **Citas sin definir: 0. Referencias sin definir: 0.** `pdftotext` del PDF no encuentra "??".
- Lista de referencias sin cambios de formato (por ejemplo, "LARMAN, Craig y BASILI, Victor R., 2003. …").
