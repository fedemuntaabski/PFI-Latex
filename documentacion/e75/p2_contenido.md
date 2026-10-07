# P2 — Contenido nuevo E75

Rama `e75/paquete`. Fuente: `documentacion/e75/textos_e75.md` (T6, T7, T8, T9, T10, T13). Un commit
por bloque. Cada bloque compila con 0 errores y sin "??" en el PDF (`pdflatex`, `biber`, `pdflatex` ×2).
Los textos se insertaron sin cambios; solo se adaptaron etiquetas, claves de cita, la línea "Fuente"
y el especificador del float (según `p0_estado.md`). Las líneas indicadas corresponden al estado final.

## T6 — Requerimientos en forma positiva (`chapters/requerimientos.tex`)

- RNF-04 (l.226), RNF-05 (l.228), RNF-08 (l.234): se reemplazó la columna "Requerimiento" por el texto
  de T6. Categoría y estado no cambian. Adaptación de marcado como en el resto de la tabla:
  `\emph{scoring}`, `\emph{buffer}`, `\emph{circuit breaker}`, `20\,000`, `NIST SP~800-207`.
- RF-04 (l.79): se agregó al final "El decaimiento tiene una vida media de 3 días." con su `[[VERIFICAR]]`.
  Coincide con `producto.tex:69` ("vida media de 3 días").
- RNF-08 nuevo coincide con la lista de metadatos de `producto.tex:47` y RF-01.
- Observación (sin cambio): RNF-04 dice que el agente "ejecuta únicamente la acción que el PDP indica
  para cada evento"; el agente también tiene un comando local de reversión y un modo de simulación
  (`producto.tex:60`). No es una decisión de riesgo, pero conviene tenerlo presente.

RF/RNF que siguen redactados en negativo (no se cambiaron):

| ID | Fragmento |
|---|---|
| RF-01 | "No captura contenido, pantallas ni pulsaciones de teclado." |
| RF-04 | "dentro del día el puntaje es provisional y no modifica el acumulado" |
| RF-08 | "Esta última no ejecuta ninguna acción en el agente" |
| RF-12 | "La dimensión ``rol'' en los umbrales queda fuera del alcance." |
| RF-13 | "Un motor de reglas libres, sin orden entre niveles, queda fuera del alcance." |
| RF-25 | "(no el nivel informado)"; "La notificación por correo no se atenúa." |
| RF-30 | "no es una variable de entrada del modelo" |
| RNF-02 | "El agente debe ser liviano y no degradar el uso normal del equipo" |
| RNF-10 | "El reentrenamiento no debe afectar la disponibilidad ni la latencia…" |
| RNF-12 | "sin servidor propio ni contenedores" |

## T7 — Muestreo de la encuesta (`chapters/chapter04.tex`, 3.6)

- Párrafo de muestreo al inicio de 3.6 (l.437), tras `\label{sec:encuesta-usuarios}`.
- Sustituciones aplicadas (solo los tres patrones de T7):
  1. 3.6.1 (l.449): "para una parte importante de los empleados" → "…de los participantes".
  2. 3.6.9 (l.501): "la encuesta respalda la premisa central" → "los resultados de la encuesta son
     consistentes con la premisa central".
  3. "los empleados" → "los participantes": sin otras apariciones que sean generalizaciones.
- No se cambió "reacción de los empleados" (l.485, 491, 503): es el nombre de una opción de respuesta.
- Otras generalizaciones fuera de los patrones, sin cambiar:
  - l.459 (3.6.2): "percibidos por los usuarios".
  - l.477 (3.6.5): "los usuarios valoran un sistema integral"; "las prioridades expresadas por la
    población objetivo".
  - l.501 (3.6.9): "Los resultados también respaldan varias decisiones de diseño".

## T8 — Nota de autoevaluación (`chapters/chapter04.tex`)

- Tabla 3.VII (`tab:comp-proyecto`), celda "Diferenciador del proyecto propuesto" (l.175): texto de T8.
  La fila no cerraba con `\\`; se agregó `\\` y `\hline` como en las demás tablas.
- Nota de autoevaluación, texto idéntico en dos lugares: tras la tabla 3.VII (l.179) y al final de 3.2,
  tras "Lectura de la matriz" (l.217). Al final de 3.2 "esta tabla" y "la matriz de capacidades" se
  refieren a la misma tabla, y el párrafo de apertura de 3.2 ya explica N/D.
- Etiqueta creada: `sec:sintesis-diferenciadores` (3.4, l.393).

## T10 — Aporte del Anexo G (`chapters/chapter04.tex`, 3.5.1)

- Párrafo al final de 3.5.1 (l.412), antes de 3.5.2.
- Etiqueta creada: `sec:validacion-diseno` (3.5.2, l.420).
- No se aplicó la indicación adicional de T10 (nombrar a los entrevistados por apellido en 3.5): no
  estaba en el pedido de esta tanda.

## T9 — Metas de evaluación (`chapters/pruebas.tex`, 10.5)

- `\subsection{Metas de evaluación}` (10.5.1, l.215) al comienzo de 10.5, tras
  `\label{sec:evaluacion-modelo}`, con la tabla (l.224) y el párrafo de justificación (l.246).
- Ubicación: no se agregó ningún título adicional, así que el párrafo de apertura de 10.5 y la tabla de
  métricas no supervisadas quedan dentro de 10.5.1. La primera oración de T9 repite lo que dice ese
  párrafo (CLUE-LDS sin etiquetas).
- Adaptaciones: `landauer2022b` → `Landauer2022Dataset`; `sec:escenarios` → `sec:validacion-escenarios`;
  `[H]` → `[h]` + `\FloatBarrier`; `\fuente{Elaboración propia.}` → `{\small Fuente: elaboración propia.\par}`.
- Etiqueta creada: `sec:interpretacion` (10.6.4, l.341).
- `[[DECIDIR]]` queda en el .tex debajo de la tabla (l.244). El `[[VERIFICAR]]` del comando de fuente
  no se insertó porque ya quedó resuelto (p0, §7).
- Numeración: la tabla nueva es 10.VII; las métricas no supervisadas pasan a 10.VIII, los escenarios
  a 10.IX y los demás se corren uno.

Verificación de la columna "Resultado":

| Métrica | T9 | Documento | ¿Coincide? |
|---|---|---|---|
| Tasa de anomalías de Isolation Forest | 0,79 % | 10.5, tabla 10.VIII: 0,79 % (97 de 12 235) | Sí |
| Tasa de anomalías del LSTM | 3,99 % | 10.5, tabla 10.VIII: 3,99 % (1 487 de 37 254) | Sí |
| Detección atribuible de E4, umbral 70 | 13,3 % (2 de 15) | 10.6.2, tabla 10.IX: E4 atribuibles = 2; 15 usuarios | Sí |
| Detección atribuible promedio, umbral 70 | 6,7 % (4 de 60) | Tabla 10.IX: 1 + 1 + 0 + 2 = 4 de 4 × 15 = 60 | Sí |
| Usuario-días sin inyección en alto o crítico | 16,8 % | 10.6.2: 16,8 % en alto, ninguno en crítico | Sí |
| Latencia p95 (RNF-01) | 14,9 ms; meta ≤ 500 ms | 10.4.1, tabla 10.V: 14,91 ms; RNF-01: p95 ≤ 500 ms, "p95 de 14,9 ms" | Sí |

No hay diferencias. Las metas de las columnas "Meta" (1–3 %, 3–7 %, ≥ 50 %, ≥ 33 %, ≤ 10 %) son la
propuesta de T9 y no tienen un dato equivalente en el documento, salvo los parámetros que citan
(contaminación 0,02 y umbral en el percentil 95, `datos.tex:84,88`) y la meta de latencia (RNF-01).
Los valores de "Cumple" son coherentes con la comparación entre la meta y el resultado.

## T13 — Viabilidad técnica (`chapters/arquitectura.tex`)

- `\subsection{Viabilidad técnica}` (7.5.4, l.260) al final de 7.5 "Arquitectura de despliegue", tras
  "Contenedores". El capítulo termina en la sección "Síntesis", por eso no va al final literal.
- Tensión con el documento (texto sin cambios): T13 dice que "la API y el almacenamiento corren sobre
  servicios de nube"; 7.5 dice que el camino verificado es local (la API corre en un equipo Windows y
  solo Redis y PostgreSQL están en la nube) y que el despliegue en la nube está aplicado en forma
  parcial, sin red de distribución. Además, T13 cita RNF-02, que todavía no tiene medición.

## Marcadores `[[...]]` pendientes

Agregados en esta tanda:

| Ubicación | Marcador |
|---|---|
| `requerimientos.tex:79` (RF-04) | `[[VERIFICAR: si la vida media es configurable, agregar su rango; si no, decir "fija".]]` |
| `chapter04.tex:437` (3.6) | `[[COMPLETAR: canal, …]]` |
| `chapter04.tex:438` (3.6) | `[[COMPLETAR: fechas]]` |
| `pruebas.tex:218` (10.5.1) | `[[COMPLETAR: una oración que explique por qué versiones anteriores …]]` |
| `pruebas.tex:244` (10.5.1) | `[[DECIDIR: los valores de las metas …]]` (con `[[CODIGO]]` adentro) |

Preexistentes, sin cambios: `requerimientos.tex:222` (estado de RNF-02), `pruebas.tex:204,206,210`
(medición e interpretación de RNF-02), `producto.tex:129`.
