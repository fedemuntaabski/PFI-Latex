# P6 — Introducción y título (T1 a T5)

Fecha: 08/10/2026. Rama `e75/paquete`. Compilación: `pdflatex`, `biber`, `pdflatex` ×2, sin
errores, sin referencias ni citas indefinidas (233 páginas físicas).

## 1. Título y encabezado (T1)

- Portada LaTeX (`chapters/title.tex`): **UMBRAL: agente inteligente de vigilancia conductual y
  mitigación de riesgo de identidad para PyMEs argentinas (2026)**.
- Carátula externa (`cover/Caratulafinal.pdf`): es el PDF del formulario UADE, sin fuente
  editable; hoy dice "Agente inteligente de vigilancia conductual y mitigación de riesgo de
  identidad". **Pendiente del equipo**: regenerarla con el título nuevo y reemplazar el archivo.
- Metadatos del PDF: `\hypersetup` no define `pdftitle` ni `pdfauthor`; no hay nada que cambiar.

### Encabezado elegido: `UMBRAL — VIGILANCIA CONDUCTUAL Y RIESGO DE IDENTIDAD`

Se probaron las dos versiones en una página del cuerpo (pág. 11, sección 1.3 → 1.4), con la
columna central de `\parbox[b]{0.43\textwidth}` sin modificar:

| Versión | Líneas | Superposición con autores |
|---|---|---|
| `UMBRAL: AGENTE DE VIGILANCIA CONDUCTUAL Y MITIGACIÓN DE RIESGO DE IDENTIDAD` | 3 ("UMBRAL: AGENTE DE VIGILANCIA / CONDUCTUAL Y MITIGACIÓN DE / RIESGO DE IDENTIDAD") | No |
| `UMBRAL — VIGILANCIA CONDUCTUAL Y RIESGO DE IDENTIDAD` | 3 ("UMBRAL — VIGILANCIA / CONDUCTUAL Y RIESGO DE / IDENTIDAD") | No |

La versión larga supera las dos líneas, por lo que, según la regla acordada, se usa la corta.
**La corta también ocupa tres líneas**: la columna central mide 0,43 del ancho de texto y con
mayúsculas de 12 pt entran unos 25 caracteres por línea. En la página renderizada el bloque queda
a la derecha del logo UADE, alineado por la base con "Mociulsky, Santiago / Muntaabski, Federico",
y la tercera línea ("IDENTIDAD") queda a la altura del segundo autor, por encima de la regla del
encabezado; no pisa el texto ni el bloque de autores. Para llegar a dos líneas habría que ensanchar
el `\parbox` (formato, fuera de este paquete) o acortar más el texto, por ejemplo
`UMBRAL — RIESGO DE IDENTIDAD` → **[[DECIDIR]]**.

## 2. Objetivos (T2) vs. tabla de cumplimiento (cap. 13)

Orden 1 a 9: **igual**. Sentido: **igual**. Diferencias solo de redacción del rótulo:

| # | Objetivo específico (1.1.2) | Rótulo en `tab:cumplimiento-objetivos` | Diferencia |
|---|---|---|---|
| 1 | Agente Windows, solo metadatos, canal cifrado y autenticado, ≤ 5 % CPU y 150 MB | Agente liviano con canal cifrado y autenticado | El rótulo no nombra los límites; la evidencia los cubre con "consumo [[CODIGO: RNF-02]]" |
| 2 | Modelo híbrido evaluado contra las metas de `sec:metas-modelo` | Modelo híbrido evaluado contra metas | — |
| 3 | Puntaje 0–100 por evento, continuidad, decaimiento, p95 ≤ 500 ms | Puntaje con continuidad y latencia ≤ 500 ms | El rótulo no dice "0 a 100 por evento" ni "decaimiento" (la evidencia sí) |
| 4 | Respuesta graduada, reversible cuando el SO lo permita | Respuesta graduada y reversible | — |
| 5 | Panel con explicación y configuración sin reinicio | Panel con explicación y configuración en tiempo de ejecución | — |
| 6 | Reentrenamiento aislado y período de aprendizaje | Reentrenamiento aislado y período de aprendizaje | — |
| 7 | Credenciales y canal: cifrado en tránsito y autenticación mutua | Credenciales y canal protegidos | — |
| 8 | Análisis de Ley 25.326 y normativa laboral | Análisis de la normativa de datos personales | — |
| 9 | Pruebas con cobertura ≥ 85 %, e2e y evaluación de usabilidad | Pruebas con cobertura ≥ 85 % | El rótulo omite e2e y usabilidad (la evidencia las menciona) |

Aviso: `pruebas.tex` (10.2) dice que la cobertura no se midió. El objetivo 9 depende del
marcador `[[CODIGO: cantidad de pruebas y cobertura]]` de la tabla 13.

## 3. Alcance (T5)

Texto de 1.2 reemplazado por el bloque T5 (presente, "entrenado por el equipo", Windows, PyMEs
argentinas y límite del análisis legal).

## 4. Metodología de desarrollo (T3, nueva 1.4)

- Cita `\parencite{Larman2003}`; entrada agregada a `biblio.bib` como `@Article` en el formato de
  las demás (datos de T22).
- `\label{sec:integracion-continua}` creada en 10.2.3 (`chapters/pruebas.tex`).
- `[[VERIFICAR: nombrar las seis fases…]]` → `[[CODIGO: nombres de las seis fases del pipeline]]`.
- `[[VERIFICAR: división de tareas…]]` borrado (confirmada).
- "pipeline" en cursiva (`\emph{pipeline}`), como en el resto del documento.

## 5. Estructura del documento (T4, nueva 1.5)

- Etiquetas creadas: `chap:antecedentes` (`chapter02.tex`), `chap:comparativo` (`chapter04.tex`),
  `chap:diseno` (`e50_diseno_ux.tex`), `chap:uml` (`e50_uml.tex`). Todas las referencias usan
  `chap:`.
- Cotejo con el PDF compilado: 13 capítulos en el orden del texto (1 Introducción … 11 Mercado,
  12 Negocio, 13 Conclusiones); anexos A Cronograma, B Encuesta, C a G las cinco entrevistas.
  **Coincide**; el texto de T4 no requirió ajustes.
- Se borró el comentario `%` de ejemplo de estructura al final del capítulo 1.

## 6. Párrafo de apertura del capítulo 1

"Este capítulo presenta los objetivos del proyecto, su alcance, una descripción general del
sistema propuesto y de sus componentes, la metodología de desarrollo y la estructura del
documento."

## 7. Marcadores agregados

| Ubicación | Marcador |
|---|---|
| 1.3, tras "una API central desplegada en la nube" | `[[CODIGO: confirmar estado del despliegue]]` |
| 1.3, tras "Estos datos se envían de forma segura a la API" | `[[CODIGO: confirmar según el resultado del Prompt C]]` |
| 1.4, final del párrafo del pipeline | `[[CODIGO: nombres de las seis fases del pipeline]]` |

## 8. Pendientes

- Regenerar `cover/Caratulafinal.pdf` con el título nuevo (equipo).
- Encabezado en tres líneas: decidir si se acepta o se acorta (ver 1).
