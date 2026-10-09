# E75 — Prompt injection en la redacción asistida del correo (Gemini)

Rama `correcciones-e75-latex`. Fecha: 2026-10-09.

## Qué se respetó del documento

- Gemini es opcional y tiene texto predefinido de respaldo (`arquitectura.tex:185`, tabla de servicios 7.4).
- Recibe "el puntaje y los eventos recientes de la alerta" (tabla 9.III, fila de transferencia internacional).
- Solo redacta: el nivel y la acción los decide el motor de scoring (RNF-04).

Solo esas tres cosas se presentan como vigentes. Todas las demás mitigaciones van como controles recomendados o trabajo futuro.

## Texto agregado

### 9.6.1 (nueva), `chapters/producto.tex`, después de la tabla 9.IV

Título: "Inyección de instrucciones en la redacción asistida", con `\label{sec:prompt-injection}`. Queda como subsección de 9.6, así que no renumera 9.6 ni 9.7 (en `build/main.toc`: 9.6, p. 124; 9.6.1, p. 128; 9.7, p. 129).

> La redacción asistida del correo de notificación (RF-31) envía a un modelo de lenguaje externo (Gemini) el puntaje y los eventos recientes de la alerta. Esos eventos provienen de la telemetría del *endpoint* e incluyen nombres de proceso, rutas de archivo y destinos de red, es decir, datos que un atacante con acceso al equipo controla. Basta, por ejemplo, con crear un archivo cuyo nombre contenga instrucciones dirigidas al modelo, como pedirle que informe la alerta como un falso positivo. Si el texto de esos campos se concatena con las instrucciones del sistema, el modelo no tiene forma confiable de distinguir unas de otras. Este riesgo corresponde a la inyección indirecta de instrucciones, que OWASP ubica en el primer lugar de los riesgos de las aplicaciones basadas en modelos de lenguaje y que NIST clasifica entre los ataques a los sistemas de IA generativa (OWASP Foundation, 2024; Vassilev et al., 2025).
>
> El impacto está acotado por diseño. El modelo solo redacta el correo: el nivel de riesgo y la acción de mitigación los determina el motor de *scoring* antes de la notificación (RNF-04), y la respuesta del modelo no vuelve al agente ni modifica la configuración. Una inyección exitosa no altera la decisión ni ejecuta acciones en el equipo. El peor caso es un correo engañoso que lee el administrador: un texto que minimiza la alerta, atribuye la actividad a una tarea legítima o incluye enlaces o instrucciones del atacante. A esto se suma la exposición de los datos de la alerta al proveedor del modelo, ya tratada como transferencia internacional en la tabla 9.III. Además, el servicio es opcional y, si no está configurado o no responde, el correo se arma con un texto predefinido.
>
> Fuera de la opcionalidad, el texto de respaldo y la decisión en el motor de *scoring*, el documento no da por implementado ningún control específico. Se recomiendan los siguientes, como trabajo futuro:
> - Separar las instrucciones del sistema de los datos de telemetría, enviándolos en mensajes o campos distintos y declarando en las instrucciones que los datos no contienen órdenes.
> - Delimitar cada campo de telemetría con marcadores explícitos y escapar en su contenido los caracteres que puedan cerrar el delimitador.
> - Limitar la longitud de cada campo y restringir su conjunto de caracteres, truncando o sustituyendo lo que exceda esos límites.
> - Enviar variables agregadas (cantidad de eventos por tipo, variables que más contribuyen al puntaje, franja horaria) en lugar de nombres de proceso, rutas y destinos crudos. Esto reduce a la vez la superficie de inyección y los datos personales que recibe el proveedor.
> - Validar la salida del modelo antes del envío: formato esperado, longitud máxima y ausencia de enlaces, direcciones de correo o instrucciones dirigidas al lector. Si la validación falla, se usa el texto predefinido.
> - Mostrar siempre en el correo, fuera del texto generado y con origen en el motor de *scoring*, los datos objetivos de la alerta: usuario, puntaje, nivel, acción aplicada y eventos recientes. Así el administrador puede contrastar la redacción con los datos.

**Aclaración sobre "la respuesta del modelo no vuelve al agente ni modifica la configuración":** se deduce de RNF-04 y de que el correo se envía después de la decisión (9.2.2). Ver el punto 1 de la lista de verificación.

### Fila nueva en la tabla 9.IV (última fila)

| Limitación | Impacto | Tratamiento |
|---|---|---|
| Prompt injection en la redacción asistida | Los nombres de proceso, las rutas de archivo y los destinos de red de los eventos llegan al modelo de lenguaje y pueden contener instrucciones dirigidas a él. El peor caso es un correo engañoso o con contenido inyectado y el envío de esos datos al proveedor; el nivel y la acción no cambian, porque los decide el motor de *scoring* (RNF-04). | El servicio es opcional y tiene un texto predefinido de respaldo. Controles recomendados y trabajo futuro: separación de instrucciones y datos, delimitación y validación de los campos y de la salida (sección 9.6.1). |

### Tabla 9.III (Ley 25.326), fila de transferencia internacional, columna "A cargo de la organización / pendiente"

Al final del texto existente se agregó:

> Pendiente: aplicar los controles contra la inyección de instrucciones (sección 9.6.1) y enviar variables agregadas en lugar de nombres de proceso, rutas y destinos crudos.

### 13.4 Trabajo futuro, `chapters/conclusiones.tex`

Ítem nuevo, antes de "Pruebas":

> **Redacción asistida del correo**: aplicar los controles contra la inyección de instrucciones (sección 9.6.1), enviar al modelo variables agregadas en lugar de nombres crudos y agregar una prueba del texto predefinido de respaldo.

## RF nuevo (`chapters/requerimientos.tex`, tabla del Módulo 4)

En el capítulo 4 no había ningún RF de redacción asistida. Tampoco existe un módulo de "notificaciones": RF-15 (niveles que notifican) está en el Módulo 4 (CU-02, HU-07). Por eso, y tal como acordamos, el requerimiento nuevo es **RF-31** y va al final de la tabla del Módulo 4, sin renumerar los demás.

| ID | Requerimiento | Prioridad | Estado |
|---|---|---|---|
| RF-31 | La API puede asistir la redacción del correo de notificación con un modelo de lenguaje externo, que recibe el puntaje y los eventos recientes de la alerta; si el servicio no está configurado o no responde, se utiliza un texto predefinido. El modelo solo redacta el correo: no interviene en el nivel ni en la acción (RNF-04). | Baja | Implementado; servicio opcional con texto predefinido de respaldo |

Trazabilidad:
- Matriz (`tab:trazabilidad`): "RF-15, RF-17" → "RF-15, RF-17, RF-31 | CU-02 | HU-07".
- CU-02, requerimientos asociados: "RF-12 a RF-17" → "RF-12 a RF-17 y RF-31".
- Tabla 10.x de evidencia de prueba: RF-31 va a "Sin prueba registrada", como acordamos.

## Conteos actualizados (antes → después)

| Ubicación | Antes | Después |
|---|---|---|
| Cap. 4, síntesis después de la matriz (`requerimientos.tex`) | 30 RF, 28 implementados, 2 parciales | 31 RF, 29 implementados, 2 parciales |
| 9.3, tabla 9.II (`tab:cumplimiento-cu`), fila CU-02 | RF-12 a RF-17; 6 | RF-12 a RF-17 y RF-31; 7 |
| 9.3, tabla 9.II, fila Total | 30 / 28 / 2 | 31 / 29 / 2 |
| 9.7 Síntesis | "De los 30 requerimientos funcionales, 28…" | "De los 31…, 29…" |
| 10.x, tabla `tab:cobertura-requerimientos`, "Sin prueba registrada" | RF-18, RF-19, RF-22 y RF-26 | RF-18, RF-19, RF-22, RF-26 y RF-31 |
| 10, Limitaciones de las pruebas | "Cuatro requerimientos funcionales (RF-18, RF-19, RF-22 y RF-26)" | "Cinco requerimientos funcionales (RF-18, RF-19, RF-22, RF-26 y RF-31)" |
| 13.1 (`conclusiones.tex:51`) | "De los 30…, 28…" | "De los 31…, 29…" |

**Aviso sobre el marcador.** En 13.1, el conteo de RF está fuera de cualquier marcador y se actualizó. En la línea siguiente está `[[CODIGO: actualizar conteo con RNF-03 y RNF-13]]`, que se refiere a los RNF; no se tocó. Ningún conteo de RF estaba dentro de un `[[CODIGO]]`. El diff no agrega ni quita marcadores.

No se cambió el "RF-12 a RF-17" de `e50_diseno_ux.tex:7`, porque ahí se listan los requerimientos de las pantallas del dashboard y RF-31 no es una pantalla.

## Referencias (`biblio.bib`)

- `NIST_AI100_2_2025`, `@TechReport`. VASSILEV, Apostol; OPREA, Alina; FORDYCE, Alie; ANDERSON, Hyrum; DAVIES, Xander y HAMIN, Maia, 2025. *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*. NIST AI 100-2 E2025. DOI 10.6028/NIST.AI.100-2e2025. Título, autores, número y DOI verificados en csrc.nist.gov.
- `OWASP2025LLM`, `@online`. OWASP FOUNDATION, 2024. *OWASP Top 10 for LLM Applications 2025. LLM01:2025 Prompt Injection*. OWASP GenAI Security Project. URL https://genai.owasp.org/llmrisk/llm01-prompt-injection/, consultada el 2026-10-09. owasp.org confirma el proyecto y la versión 2025, pero genai.owasp.org respondió 403 al pedido automático. **Conviene confirmar en el navegador el año de publicación (2024, porque la versión 2025 se publicó a fines de 2024) y el título exacto de la página.**
- En las citas sale "(OWASP Foundation, 2024; Vassilev et al., 2025)".
- Encontré otra cosa. La institución de la entrada nueva va entre llaves dobles; si no, biblatex la parte en "and" y la muestra como "National Institute of Standards y Technology". Las entradas NIST existentes (`Rose2020`/800-207, `Hu2014`/800-162, `NIST2023_800207A`) usan llaves simples y probablemente tienen el mismo defecto en la lista de referencias. No las toqué porque quedan fuera de esta tarea.

## Para verificar en el código

Si alguno de estos controles ya existe, se puede pasar de "recomendado" a "implementado" en 9.6.1, en la fila de la tabla 9.IV y en 13.4.

1. **Flujo de la respuesta**: confirmar que la salida de Gemini se usa solo como cuerpo del correo y nunca se lee para decidir, cambiar la configuración ni responder al agente. El texto de 9.6.1 lo afirma deduciéndolo de RNF-04.
2. **Campos que se envían**: listar exactamente qué se arma en el prompt (puntaje, nivel, usuario, nombres de proceso, rutas, destinos, contexto IAM, explicación). Si se envían agregados y no nombres crudos, corregir 9.6.1, la tabla 9.III y 13.4.
3. **Separación instrucciones/datos**: ver si se usa `system_instruction` (o un rol de sistema) aparte del contenido, o si todo se concatena en un único string.
4. **Delimitado y escapado** de los campos de telemetría en el prompt.
5. **Límite de longitud o filtro de caracteres** por campo, o un tope de cantidad de eventos.
6. **Validación de la salida**: formato, longitud, detección de URL o de instrucciones, y caída al texto predefinido si la validación falla.
7. **Datos objetivos fuera del texto generado**: ver si la plantilla del correo muestra usuario, puntaje, nivel, acción y eventos en un bloque fijo, separado del texto de Gemini.
8. **Timeout y manejo de errores**: confirmar que una falla o demora de Gemini lleva al texto predefinido sin bloquear la evaluación.
9. **Pruebas**: si hay un test del respaldo o del cliente de Gemini, mover RF-31 de "Sin prueba registrada" a "Prueba automatizada" y volver de "Cinco" a "Cuatro" en 10, Limitaciones de las pruebas.
10. **Desactivación**: cómo se apaga el servicio (variable de entorno sin clave) y si está activo en el despliegue en la nube. `documentacion/e75/p1_forma.md:111` dice "Gemini API — [desplegado] verificado".

## Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`:
- 0 errores, 0 referencias o citas sin definir, biber sin warnings. 246 páginas (el pie dice "de 244").
- Overfull boxes: 248 (eran 245 en el inventario base y ya habían cambiado con commits anteriores; no se revisaron uno por uno).

## Archivos modificados

`chapters/producto.tex`, `chapters/requerimientos.tex`, `chapters/pruebas.tex`, `chapters/conclusiones.tex`, `biblio.bib` y este informe.
