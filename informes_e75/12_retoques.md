# E75 — Retoques: Gantt, bibliografía, costo fijo, referencias a futuro y "figura"

Las líneas son las del `.tex` **antes** de editar, salvo que se indique otra cosa.

## A. Anexo A (Gantt)

**`chapters/appendix/schedule_of_activities.tex`, l. 3**

- Antes: "Este anexo presenta el cronograma de los dos incrementos descriptos en la sección~\ref{sec:metodologia} (Figura~\ref{fig:gantt_actualizado}). El diagrama de Gantt muestra las tareas de cada fase, su duración y sus dependencias, junto con los hitos de entrega del proyecto."
- Después: "Este anexo presenta la planificación inicial del proyecto (figura~\ref{fig:gantt_actualizado}). El diagrama de Gantt muestra las fases, las tareas de cada una, su duración y sus dependencias, junto con los hitos del proyecto. La organización en dos incrementos que describe la sección~\ref{sec:metodologia} surge de la ejecución posterior."

El párrafo ya no dice que el Gantt muestre los incrementos. Cambia "hitos de entrega" por "hitos del proyecto" y no menciona fechas, porcentajes ni entregas de la materia. `\label{sec:metodologia}` sigue en uso.

El epígrafe ("Diagrama de Gantt del proyecto: planificación de hitos y distribución de tareas") ya estaba en minúscula: sin cambio.

**Ajuste de coherencia en `chapters/chapter01.tex`, l. 82-83 (sección 1.4).** Decía lo mismo que el anexo viejo y contradecía el nuevo.

- Antes: "El cronograma de ambos incrementos se presenta en el Anexo~A."
- Después: "La planificación inicial del proyecto, previa a esta organización en incrementos, se presenta en el Anexo~A."

## B. Bibliografía: instituciones con llaves dobles

Archivo: `biblio.bib`.

| Línea | Entrada | Antes | Después |
|---|---|---|---|
| 72 | Rose2020 | `INSTITUTION = {National Institute of Standards and Technology}` | `{{National Institute of Standards and Technology}}` |
| 82 | Hu2014 | ídem | ídem |
| 91 | NIST2023_800207A | ídem | ídem |
| 375 | Osterwalder2010 (publisher) | `{John Wiley \& Sons}` | `{{John Wiley \& Sons}}` |

Revisé también el resto de los campos `institution`, `organization` y `publisher` y los autores institucionales. No tienen "and" ni "&" o ya estaban con llaves dobles: Vassilev (l. 459), l. 230, 238, 392-437 y 466. El "\&" de Wiley no lo partía biblatex; lo envolví igual por consistencia.

Verificación: latexmk corrió biber. En la lista de referencias del PDF, Chandramouli y Butcher y Vassilev et al. dicen "National Institute of Standards and Technology". Rose2020 y Hu2014 son `@Article`, y el estilo no imprime la institución en ese tipo de entrada. Las llaves quedan igual por si se cambia el tipo.

## C. Tabla 12.II, fila "Costo fijo"

**`chapters/negocio.tex`, l. 112-113**

- Antes: "Equipo y soporte: USD 3.500 por mes el primer año (dos integrantes a tiempo parcial), que crece hasta USD 12.000 en el quinto; infraestructura base de nube: USD 250 por mes."
- Después: "Equipo y soporte, por mes: USD 3.500 el año 1 (dos integrantes a tiempo parcial), USD 6.000 el año 2, USD 9.000 el año 3, USD 11.000 el año 4 y USD 12.000 el año 5; infraestructura base de nube: USD 250 por mes todos los años."

Los valores salen de `documentacion/e75/modelo_financiero.py`: `fijo_mensual_por_anio = [3500, 6000, 9000, 11000, 12000]` e `infra_fija_mensual = 250`. Coinciden con la columna "Costo fijo mensual" de la tabla 12.VII (`tab:equilibrio-fin`): 3.750, 6.250, 9.250, 11.250 y 12.250, es decir, el costo fijo más USD 250. La numeración 12.II y 12.VII está confirmada en `build/main.aux`.

## D. Referencias a futuro

Busqué los giros pedidos con grep. También usé un script que recorre los `\input` desde `main.tex` y lista cada `\ref` a una sección o capítulo cuyo `\label` está más adelante en el documento.

### Corregido (justificación diferida), en `chapters/e50_diseno_ux.tex`

1. **La sección "Decisiones de diseño transversales" pasó al final de 5.1 (Metodología de diseño).** Antes era la sección 5.4 (l. 320-327), después del catálogo de pantallas. Ahora es la subsección 5.1.1: tiene el mismo texto y el mismo label (`sec:decisiones-transversales-mockups`) y queda antes del catálogo. No había otras referencias a ese label.
2. **l. 9**
   - Antes: "…sin el detalle de estilo final que sí se justifica por separado en la sección~\ref{sec:decisiones-transversales-mockups} y que se puede contrastar…"
   - Después: "…sin el detalle de estilo final, que se justifica a continuación y que se puede contrastar…"
3. **l. 84, tabla 5.II, fila RNF-15**
   - Antes: "…permitiendo priorizar de un vistazo (ver sección~\ref{sec:decisiones-transversales-mockups} para la justificación de la paleta)."
   - Después: "…permitiendo priorizar de un vistazo. La paleta es semafórica por nivel (verde, ámbar, naranja y rojo) y se repite en todas las vistas, de modo que el color conserva el mismo significado en cada pantalla (sección~\ref{sec:decisiones-transversales-mockups})."
   - La referencia ahora apunta hacia atrás, a la 5.1.1.

### Se dejaron (casos permitidos)

- Estructura del documento (1.5, `chapter01.tex` l. 101-119) y objetivos (1.1, l. 11 y 27).
- Anticipos de resultados o de la evaluación:
  - `datos.tex` l. 12 y 92;
  - `arquitectura.tex` l. 74;
  - `producto.tex` l. 4, 97, 138, 207, 209, 215 y 271;
  - `pruebas.tex` l. 98, 217, 230, 263 y 602;
  - `e50_mercado.tex` l. 30 ("se evalúa en la sección 12.x");
  - `chapter04.tex` l. 417 (contraste en la sección siguiente).

### Dudosos (sin tocar)

| Archivo | Línea | Texto | Por qué es dudoso |
|---|---|---|---|
| `chapter04.tex` | 175 | "No aplica (fila de referencia). La síntesis de diferenciadores se presenta en la sección~\ref{sec:sintesis-diferenciadores}." | La celda de la tabla comparativa se completa en una sección posterior del mismo capítulo. |
| `chapter04.tex` | 484 | "El tratamiento de los datos personales que realiza el sistema y su encuadre en la Ley 25.326 se analizan en la sección~\ref{sec:tratamiento-datos}." | Remite al capítulo de Producto para cerrar el tema legal que surge de la encuesta. |
| `chapter01.tex` | 97 | "…un \emph{pipeline} de integración continua … (sección \ref{sec:integracion-continua})" | La metodología (1.4) remite a Pruebas para el detalle del pipeline. |
| `requerimientos.tex` | 47 | "…los cuatro casos de uso definidos en la sección~\ref{sec:casos-de-uso}" | Usa los casos de uso antes de la sección que los define. |
| `producto.tex` | 95 | "…sobre los escenarios de DEV de la sección~\ref{sec:benchmark}" | El criterio de promoción depende de escenarios que se definen en Pruebas. |
| `producto.tex` | 169, 249 | "(sección~\ref{sec:prompt-injection})" | La tabla de riesgos se completa con una sección posterior del mismo capítulo. |
| `producto.tex` | 171 | "…borrar una fila impide verificar las siguientes (sección~\ref{sec:conservacion-datos})" | Igual que el caso anterior; la justificación está en la celda y la referencia amplía. |
| `pruebas.tex` | 126 | "RNF-01 y RNF-02 (mediciones de la sección~\ref{sec:pruebas-rendimiento})" | La tabla de verificación remite a la sección de mediciones. |
| `pruebas.tex` | 260 | "…cuyas causas se analizan en la sección~\ref{sec:interpretacion}." | Anticipa el análisis, pero la limitación se afirma antes de justificarla. |
| `pruebas.tex` | 357 | "…el benchmark confirma que empeora el ordenamiento en ventanas cortas (sección~\ref{sec:decisiones-pruebas})." | La evidencia de la afirmación está en una sección posterior. |
| `negocio.tex` | 116 | "construida por acumulación (ver el párrafo siguiente)" | Celda de la tabla 12.II que se justifica en el párrafo inmediato, no en otra sección. |

## E. "figura~\ref" y "tabla~\ref" en minúscula

Pasé a minúscula todos los `Figura~\ref` y `Figuras~\ref` que estaban en medio de oración: 40 en total. No había ninguno al principio de una oración (todos van detrás de "La", "la", "las" o de un paréntesis). Tampoco había `Tabla~\ref` con mayúscula ni variantes sin `~`.

| Archivo | Líneas | Antes → después |
|---|---|---|
| `chapters/chapter04.tex` (3.6) | 444, 448, 450 (2), 452, 456 (2), 462, 464, 468, 470, 474, 480, 484, 488, 494 | "(Figura~\ref" / "(Figuras~\ref" → "(figura~\ref" / "(figuras~\ref" (16) |
| `chapters/e50_diseno_ux.tex` | 18, 55, 98, 137, 174, 218, 253, 286 (2 por línea) | "La Figura~\ref…" y "y la Figura~\ref…" / "y las Figuras~\ref" → "La figura~\ref…" y "y la figura~\ref…" / "y las figuras~\ref" (16) |
| `chapters/e50_uml.tex` | 6, 19, 32, 44, 56 | "La Figura~\ref" → "La figura~\ref" (5) |
| `chapters/e50_mercado.tex` | 42, 102 | "La Figura~\ref" → "La figura~\ref" (2) |
| `chapters/appendix/schedule_of_activities.tex` | 3 | "(Figura~\ref" → "(figura~\ref" (1, dentro del cambio de A) |

## Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`, con biber:

- termina con código 0;
- no hay errores (`!`) ni referencias o citas sin definir en `build/main.log`;
- genera `build/main.pdf` con 246 páginas.

"Decisiones de diseño transversales" queda como sección 5.1.1, en la página 71.
