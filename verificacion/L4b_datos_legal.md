# L4b — datos y legal

Rama e75/correcciones-e50-v2. Formato de miles usado: `\,` (fino), el mayoritario del documento (ej. `50\,522\,931`); en 10.5 se reemplazó el formato con punto (`50.522.931`) por `\,`.

| # | Archivo | Cambio |
|---|---------|--------|
| 1 | chapters/datos.tex (8.1) | Párrafo nuevo sobre los 92 eventos de prueba, al final de 8.1. \ref a sec:validacion-escenarios, sec:benchmark (10.6 y 10.7), sec:limitaciones-pruebas (10.10), sec:particion-entrenamiento (8.3.3, label agregado). |
| 2 | chapters/datos.tex (8.2, 8.3.1, Tabla 8.II) | Frase sobre cifras del conjunto publicado; "908 usuarios de CLUE-LDS, más el usuario de prueba..., y 61\,284 pares"; 49\,047 → 49\,048. No había otras apariciones de 61 283 / 49 047. |
| 3 | chapters/pruebas.tex (10.5) | Reemplazo de "(50.522.931 ...sin efecto práctico, y con" por el texto nuevo, puntuación ajustada. |
| 4 | chapters/pruebas.tex (10.6.1, 10.6.2, 10.5.1) | E2 "(UTC)"; frase de corrida del 9/10/2026 al inicio de 10.6.2; la Tabla 10.VIII (metas) está en 10.5.1, se agregó la frase en su párrafo. El S3 del benchmark ("hora de Viena") no se tocó. |
| 5 | chapters/producto.tex (9.5.2) | Párrafo reemplazado por dos; \ref{tab:tratamiento-datos} (tabla de principios Ley 25.326) y \ref{sec:conservacion-datos} (9.5.1). Label sec:datos-entrenamiento agregado. |
| 6 | chapters/producto.tex (9.6.1) + conclusiones.tex | Fila nueva tras "Sin plazo de conservación...". 13.4 tenía ítem "Conservación de datos": se agregó "y la seudonimización de la telemetría usada en el reentrenamiento". |
| 7 | chapters/negocio.tex | `\parencite{MENDEZ2026RiesgoPais}` → `\footnote{...}` con la URL del .bib. Sin otras citas a la clave. Entrada del .bib se mantiene (no hay `\nocite{*}`); no sale en la bibliografía. |
| 8 | anexos 1–4 (entrevistas), requerimientos.tex | "Santiago Bernardo" → "Santiago" (4); 4.3.1 y celda RF-21 en presente. |

## Verificación
- Compila sin errores (latexmk, biber). 0 "??" en el PDF; 0 citas indefinidas. Único aviso: `pdfTeX warning (dest): name{Hfootnote.1}` de hyperref, por ser la primera nota al pie del documento; la nota se ve en la página 192.
- PDF: 280 páginas físicas (278 según el pie de página, sin carátula).
- grep sin resultados: "sin efecto pr", "61\,283", "49\,047", "Santiago Bernardo", "se verificó".
- "no requiere el tratamiento de datos de personas identificables": 1 aparición (primer párrafo nuevo de 9.5.2).
- "MÉNDEZ" no aparece en la Bibliografía.
- Tabla 8.II en la página 125, sin corte raro. Tabla de limitaciones de 9.6.1: la fila nueva queda en la página 151 junto a "Sin plazo de conservación"; corte normal de longtable entre filas.
- Observación: en 4.3.1 queda "El 10 de octubre de 2026 se verifica" (fecha pasada con verbo en presente, como se pidió).
