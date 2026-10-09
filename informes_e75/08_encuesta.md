# Encuesta: difusión, Anexo B y alcance de los resultados

Rama `correcciones-e75-latex`. Fecha: 2026-10-09.

## Datos usados

Los datos del pedido llegaron como marcadores sin completar. El usuario confirma:

- Canal de difusión: grupos de WhatsApp.
- Herramienta: Google Forms.
- Fechas: se omiten (decisión del usuario). La oración se reescribe sin período.

## 1. Marcadores de la sección 3.6 (`chapters/chapter04.tex:437`)

- Antes: "La encuesta se difunde [[COMPLETAR: canal, por ejemplo redes sociales y contactos personales y laborales del equipo]] entre [[COMPLETAR: fechas]]."
- Después: "La encuesta se elabora en Google Forms y se difunde a través de grupos de WhatsApp."

No quedan marcadores `[[COMPLETAR...]]` en los `.tex`.

## 2. Anexo B (`chapters/appendix/surveys.tex:3`)

El anexo no decía cómo se reclutó la muestra. Se agrega al principio:

"La encuesta se elabora en Google Forms y se difunde a través de grupos de WhatsApp, por lo que la muestra es no probabilística y por conveniencia."

Canal y herramienta coinciden con 3.6; ninguno de los dos menciona fechas.

## 3. Limitación de muestreo y generalizaciones

- El párrafo de la muestra no probabilística por conveniencia es el primero de 3.6 y está antes del primer porcentaje (párrafo siguiente: 135 respuestas, 17 %, 83 %). No se mueve.
- Frases corregidas para que los resultados se refieran a los participantes:

| Ubicación | Antes | Después |
|---|---|---|
| 3.6, segundo párrafo | "correspondientes a empleados que trabajan sobre infraestructura corporativa" | "correspondientes a participantes que trabajan sobre infraestructura corporativa" |
| 3.6.4 | "La preferencia de los usuarios sugiere…" | "La preferencia de los participantes sugiere…" |
| 3.6.5 | "…encuentran respaldo en las prioridades expresadas por la población objetivo." | "…encuentran respaldo en las prioridades expresadas por los participantes." |
| 3.6.6 | "Respecto de la información que los usuarios considerarían intrusiva…" | "Respecto de la información que los participantes considerarían intrusiva…" |
| 3.6.8 | "Este resultado aporta evidencia cuantitativa sobre el problema que motiva el proyecto…" | "Este resultado aporta un indicio, entre los participantes, del problema que motiva el proyecto…" |
| 3.6.9 | "…la autenticación continúa siendo percibida principalmente como un evento puntual…" | "…la autenticación continúa siendo percibida por los participantes principalmente como un evento puntual…" |
| 3.6.9 | "…la confianza en el proveedor y la reacción de los empleados tienen mayor peso que la garantía de privacidad…" | "…tienen, para los participantes, mayor peso que la garantía de privacidad…" |
| 3.6.9 | "Por lo tanto, existe una oportunidad para este tipo de solución…" | "Por lo tanto, las respuestas sugieren una oportunidad para este tipo de solución…" |

No se tocan:
- "reacción de los empleados" (3.6.6, 3.6.7 y 3.6.9): es el nombre de una opción de la encuesta.
- "los encuestados" (3.6.3): ya se refiere a los participantes.
- La mención a "empresas argentinas" del párrafo de limitación: justamente dice que no se generaliza a ellas.

## Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`: compila, 246 páginas, 0 errores, 0 referencias o citas sin definir.
