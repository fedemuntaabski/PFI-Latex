# E75 — Gantt del Anexo A (Figura A.1)

## Imagen

| Dato | Valor |
|---|---|
| Archivo | `images/cronograma.jpg` |
| Formato | JPEG, RGB, 6,4 MB, sin ppp en los metadatos (pdflatex la toma a 72 ppp: 1 px = 1 bp) |
| Tamaño | 9570 × 4920 px |
| Relación de aspecto | 1,95 : 1 (apaisada) |
| Contenido | Exportación de Instagantt ("Read-only view, generated on 13 Jun 2026"). Tiene unas 95 filas de 50 px. El texto de las etiquetas mide unos 24 px de cuerpo. A la izquierda hay una tabla (Activities truncadas, Assignee "Unassigned", EH, Start, Due, Status, %) y a la derecha la línea de tiempo, de junio a diciembre de 2026, con el nombre completo de cada tarea junto a su barra. |

**¿Tiene resolución suficiente para leerse ampliada?** Sí. En la página queda a **918 ppp efectivos**, medidos con `pdfimages -list`. Al ampliar en el visor de PDF (300–400 %) el texto se lee nítido. Lo que limita no es la resolución sino el tamaño físico: el Gantt es muy ancho para su altura de letra.

## Opciones evaluadas

Página A4 sin `geometry` (book, 12 pt). En apaisado, el área útil es de unos 22 × 13 cm, descontado el epígrafe. Para que se lea impreso, un texto necesita unos 6 pt.

| Opción | Cuerpo de letra impreso | Problema |
|---|---|---|
| Anterior: página vertical, `angle=90`, `width=0.85\textheight` | ~1,5 pt | La imagen con tabla incluida ocupa solo parte de la página |
| **1 página apaisada, tabla recortada (elegida)** | **~1,9 pt** | No se lee en papel; sí con zoom en pantalla |
| 1 página apaisada, imagen completa | ~1,6 pt | Igual que la anterior y conserva "Not started" |
| 2 páginas (mitad de filas o mitad de fechas) | ~1,9 pt | No mejora nada: el ancho de la línea de tiempo sigue mandando, o la altura pasa a mandar |
| 2 × 2 = 4 páginas | ~3,5 pt | Apenas legible; las etiquetas y las flechas de dependencia se cortan en los bordes del recorte |
| 3 × 3 = 9 páginas | ~5–6 pt | Legible, pero 9 páginas con cortes en medio de las etiquetas |

**Opción elegida:** una página apaisada con `pdflscape`, en la que la imagen ocupa todo el ancho útil. Además, con `trim=1466 0 0 0, clip` se recorta la tabla de la izquierda. Razones:

- Es la opción con el texto más grande que no corta ninguna etiqueta ni ninguna dependencia.
- `pdflscape` gira la página en el visor (atributo `/Rotate 90`), así que en pantalla se lee sin girar la cabeza. Ampliar en el visor es la forma natural de leer un Gantt de este tamaño.
- La tabla recortada no aportaba información nueva: los nombres estaban truncados ("Investigación del estado del arte en arquit…") y aparecen completos junto a las barras. Las fechas siguen en el eje. Las columnas "Unassigned", "Not started" y "Finished" contradecían un documento final. Además, recortarla agranda el texto un 18 %.
- Las opciones partidas multiplican páginas y cortan etiquetas, y aun así no llegan a un tamaño cómodo con menos de 9 recortes.

## Verificación

- `latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`: compila sin errores. `build/main.pdf` tiene 244 páginas.
- La Figura A.1 queda en la página 176 del pie (página física 178 del PDF), con `/Rotate 90`. El párrafo del anexo queda solo en la página anterior.
- Rasterizado con `pdftoppm`:
  - a 60 ppp: página apaisada correcta, imagen a ancho completo, epígrafe y fuente debajo;
  - a 300 ppp, equivalente a un zoom de ~400 %: los nombres de tareas, los meses, los días y las semanas se leen;
  - a 600 ppp: nítido.
- Veredicto: **se lee en pantalla con zoom; no se lee impreso** (~1,9 pt).

## Qué haría falta para que se lea impreso (no se generó ningún Gantt nuevo)

Exportar de nuevo desde Instagantt (o la herramienta que corresponda):

1. **Formato:** PDF vectorial, que es lo ideal porque el texto se escala sin perder calidad. Si no se puede, PNG a 300 ppp o más al tamaño final.
2. **Orientación:** apaisada, A4.
3. **Columnas:** solo el nombre de la tarea y la línea de tiempo. Sin Assignee, EH, Status ni %.
4. **Páginas:** 30–35 filas por página, para que el texto quede en 7–8 pt. Dos cortes posibles:
   - **por incremento** (lo más coherente con la sección 1.4): página 1 con el incremento 1 y página 2 con el incremento 2;
   - **por fechas:** junio–julio, agosto–septiembre y octubre–diciembre de 2026, con escala semanal.
5. **Limpieza:** sin la línea "generated on 13 Jun 2026", sin el marcador del día actual (el círculo rojo del 13/06) y sin estados "Not started".

Con eso se reemplaza el `\includegraphics` por uno por página, dentro del mismo `landscape`, con "(continuación)" en el epígrafe de las siguientes.

## Texto del anexo

Antes: "Se adjunta el diagrama de Gantt correspondiente al proyecto en curso, permitiendo visualizar el estado de las actividades realizadas y el cronograma de las planificadas (Figura A.1)."

Ahora: "Este anexo presenta el cronograma de los dos incrementos descriptos en la sección 1.4 (Figura A.1). El diagrama de Gantt muestra las tareas de cada fase, su duración y sus dependencias, junto con los hitos de entrega del proyecto."

Para la referencia se agregó `\label{sec:metodologia}` a la sección 1.4, "Metodología de desarrollo" (`chapters/chapter01.tex`). También se borró el `figure` viejo que estaba comentado.

## Observaciones para que decidas

1. **El Gantt no está organizado por incrementos.** Usa fases (I.b User Research, Fase I…, Bloque A/B/C) y entregas del 25, 50 y 75 %, mientras que la sección 1.4 habla de dos incrementos. El texto nuevo dice "los dos incrementos" porque así lo pediste, pero el lector no los va a encontrar con ese nombre en la figura. Una nueva exportación partida por incremento lo resolvería.
2. **La imagen es una foto de la planificación del 13/06/2026.** Casi todas las tareas figuran "Not started" en la tabla recortada. En la línea de tiempo esto ya no se ve, pero queda el marcador rojo del día 13 en el eje.
3. **Hay una etiqueta cortada en la imagen original.** "[HITO] Defensa Final del PFI — Presentación ante el jurado" llega al borde derecho de la exportación. No se puede arreglar con LaTeX.
4. Se agregó el paquete `pdflscape` en `main.tex`.
