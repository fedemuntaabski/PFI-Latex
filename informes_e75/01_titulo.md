# E75 — Título unificado

Rama `correcciones-e75-latex`. Fecha: 2026-10-09.

Título único (consigna: producto + problema + quién + dónde + cuándo):

> **UMBRAL: agente inteligente de vigilancia conductual y mitigación de riesgo de identidad para PyMEs argentinas (2026)**

## Qué se cambió

| Archivo:línea | Cambio |
|---|---|
| `main.tex:52-54` | Nueva macro `\newcommand{\UmbralTitulo}{…}`. Es la **única definición** del título. |
| `main.tex:59` | Encabezado: `\MakeUppercase{UMBRAL --- Vigilancia conductual y riesgo de identidad}` → `\footnotesize\UmbralTitulo` (título completo). |
| `main.tex:230-231` | `\hypersetup`: se agregan `pdftitle = {\UmbralTitulo}` y `pdfauthor = {Santiago Mociulsky; Federico Muntaabski}` (antes no había metadatos). |
| `chapters/title.tex:7` | Portada interior: el texto literal se reemplaza por `\UmbralTitulo` (mismo formato: negrita, 16 pt). |
| `cover/Caratulafinal.pdf` | Carátula exterior regenerada con el título nuevo (ver abajo). |
| `cover/generar_caratula.js` | Nuevo. Script que genera la carátula exterior leyendo el título de la macro. |

### Carátula exterior
La carátula sale del generador web de la Biblioteca UADE (`crearCaratula.html`). Ese generador funciona en el navegador: carga la plantilla oficial `PFI-FAIN.pdf` y escribe los textos con pdf-lib 1.16.0. `cover/generar_caratula.js` reproduce la función `generarPDF()` de esa página para la opción "PROYECTO FINAL DE INGENIERÍA":
- misma plantilla, descargada del mismo sitio;
- misma versión de pdf-lib;
- título en Helvetica 25 pt en (80, 680), cortado en líneas de 40 caracteres, con 25 pt entre líneas;
- mismos rótulos, tamaños y coordenadas para autores, carrera, tutor y año.

Los datos son los de la carátula anterior. El título lo toma de `\UmbralTitulo` en `main.tex`, así que los tres lugares salen de la misma definición. **Si el título cambia, hay que volver a correr el script**; las instrucciones de uso están en su cabecera.

Resultado: el título queda en 3 líneas ("UMBRAL: agente inteligente de vigilancia" / "conductual y mitigación de riesgo de" / "identidad para PyMEs argentinas (2026)"), en el mismo bloque que ocupaba el título anterior, que también tenía 3 líneas. El script mide cada línea con `widthOfTextAtSize` y aborta si alguna pasa el ancho de la página; no fue necesario. Comparé la carátula anterior y la nueva rasterizadas: el diseño, la fuente, el tamaño y la posición de los demás campos son idénticos y solo cambia el texto del título.

## Encabezado: qué texto quedó y por qué
Quedó el **título completo**, escrito igual que en la portada (sin mayúsculas forzadas), en `\footnotesize` (10 pt con la clase de 12 pt), dentro de la misma columna central `\parbox[b]{0.43\textwidth}`.

- Se sacó `\MakeUppercase`. Con mayúsculas el texto ocupa ~40 % más (no entraba en 3 líneas) y "PyMEs" se convertía en "PYMES", así que ya no era el mismo título.
- Se redujo la letra a `\footnotesize`. Así entra en 3 líneas: "UMBRAL: agente inteligente de vigilancia" / "conductual y mitigación de riesgo de identidad" / "para PyMEs argentinas (2026)".
- No hubo que ensanchar la columna ni usar la versión corta.

En la página rasterizada (pág. 12 del PDF) el bloque queda entre el logo UADE y los autores, alineado por la base y por encima de la regla. Es legible y no pisa nada.

## Otras apariciones del título
- `grep` en `.tex`/`.bib`/`.sty` (sin `chapters/archivo/`): la única aparición es la macro en `main.tex:54`.
- `chapters/summary.tex` y `chapters/abstract.tex` (no se compilan) no contienen el título.
- Metadatos del PDF: `pdfinfo build/main.pdf` → `Title: UMBRAL: agente inteligente de vigilancia conductual y mitigación de riesgo de identidad para PyMEs argentinas (2026)`, `Author: Santiago Mociulsky; Federico Muntaabski`. Los acentos se ven bien.
- No se modificaron las notas históricas en `documentacion/e75/*.md` (`p6_introduccion.md`, `textos_e75.md`), que mencionan las versiones anteriores del encabezado. Son registro de trabajo y no forman parte del documento.

## Compilación
`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`: compila sin errores, 243 páginas, sin referencias ni citas indefinidas. Warnings iguales a la base de `00_inventario.md`:
- 4 de LaTeX (`h` → `ht`) y 3 de paquetes (xcolor, microtype, soulutf8);
- 245 overfull y 64 underfull;
- 3 avisos de pdfTeX por la versión del PDF de la carátula (pdf-lib escribe PDF 1.7, igual que antes).

No aparecieron warnings de `headheight` ni de `Token not allowed in a PDF string`.

## Revisión visual
Rasterizado con `pdftoppm`:
- **Pág. 1 (carátula)**: título en 3 líneas dentro del margen, sobre la zona clara del fondo amarillo, igual que el título anterior. No se superpone con "PROYECTO FINAL DE INGENIERÍA" ni con "Autor/es". El `\includepdf` (escala 1.01, offset y clip) no recorta nada.
- **Pág. 2 (portada interior)**: sin cambios visibles; el título sigue en 2 líneas en negrita de 16 pt.
- **Pág. 12 (cuerpo)**: encabezado de 3 líneas legible, sin superposición.

Ningún problema visual pendiente.
