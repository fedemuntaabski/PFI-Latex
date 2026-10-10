# E75 — Capítulo 4 y Tabla 13.I contra el código

- Rama: `e75/cap4-requerimientos` (desde `e75/objetivos-especificos`, 8378807).
- Commit: `641a3c866c95bfa69de31c6c17e9642900271041` — "docs: corrige capítulo 4 y Tabla 13.I contra el código" (sin trailers, sin push).
- Archivos: `chapters/requerimientos.tex`, `chapters/conclusiones.tex` (35 inserciones, 25 eliminaciones). Preámbulo, paquetes, entornos, caps. 1, 9 y 10 y conteos sin tocar.
- Pre-verificación: los 26 textos "antes" se encontraron tal cual, cada uno con una única coincidencia (script con aborto si la cuenta ≠ 1). En `conclusiones.tex` las frases de N estaban cortadas en dos líneas (CRLF); se reemplazaron respetando el fin de línea.

## Cambios

Líneas = posición después del commit.

| Punto | Archivo:línea | Antes | Después | OK |
|---|---|---|---|---|
| A (RF-02) | requerimientos.tex:63, 67-69 | Celda Estado con el texto completo ("Implementado: cada agente se autentica … fuera de \emph{loopback}.") | Celda: "Implementado (ver nota a)"; tras la Tabla 4.II: "Notas:" + "a) " con el texto completo, sin cambios | ✓ |
| A (RNF-03) | requerimientos.tex:232, 260-262 | Celda Estado con el texto completo ("Implementado: el panel se autentica … (CSP) que lo mitigue") | Celda: "Implementado (ver nota a)"; tras la Tabla 4.IX: "Notas:" + "a) " con el texto completo (se agregó solo el punto final) | ✓ |
| A (RNF-06) | requerimientos.tex:238, 264 | Celda Estado con el texto completo ("Implementado: la denegación de carpeta … como administrador.") | Celda: "Implementado (ver nota b)"; "b) " con el texto completo | ✓ |
| B | requerimientos.tex:12 | "… en las conclusiones." | + "Cuando un requerimiento cumple lo especificado pero su verificación es limitada (sin prueba contra un servicio real o sin prueba automatizada), esa limitación se indica junto al estado sin modificarlo." | ✓ |
| C | requerimientos.tex:29 | "… y consulta la auditoría." | "… y consulta la auditoría (rol admin del \emph{dashboard})." | ✓ |
| C | requerimientos.tex:31 | "… justificar decisiones posteriores." | "… justificar decisiones posteriores (rol operador del \emph{dashboard}, de solo lectura)." | ✓ |
| D | requerimientos.tex:61 | "procesos ejecutados, accesos a archivos y carpetas, aplicaciones utilizadas y conexiones a recursos de red" | "procesos ejecutados (incluidas las aplicaciones de una lista vigilada), cambios en los archivos del primer nivel de las carpetas vigiladas (alta, baja, modificación y renombre) y conexiones a recursos de red" | ✓ |
| E | requerimientos.tex:89 | "eleve el nivel mínimo cuando" | "eleve el nivel mínimo (por defecto, alto) cuando" | ✓ |
| F | requerimientos.tex:135 | "… entre notificaciones por usuario." | "… entre notificaciones por usuario (10 minutos por defecto, definido en la configuración del servidor)." | ✓ |
| G | requerimientos.tex:139 | "identificador del actor (derivado de la clave utilizada)" | "identificador del actor (el rol de la sesión del panel o, para las claves que usan los scripts, un identificador derivado de la clave)" | ✓ |
| G | requerimientos.tex:453 | "con qué nivel de clave" | "con qué rol o clave" | ✓ |
| H | requerimientos.tex:209 | "incluirse en la respuesta del evento evaluado, como información para el administrador" | "incluirse en la respuesta del evento evaluado y mostrarse en el detalle del usuario del \emph{dashboard}, como información para el administrador" | ✓ |
| H | requerimientos.tex:284 | "este dato se muestra en el \emph{dashboard}" | "este dato se muestra en el detalle del usuario del \emph{dashboard}" | ✓ |
| I | requerimientos.tex:254 | Estado "Implementado" | "Implementado: el estado de cada usuario se guarda en claves separadas y se actualiza con transacciones optimistas con reintentos; verificado con un ensayo manual de contención sobre un usuario, sin prueba automatizada con varios usuarios" | ✓ |
| J | requerimientos.tex:275 | "(ejecuta un proceso, accede a un archivo, abre una aplicación o se conecta a un recurso de red)" | "(ejecuta un proceso, crea, modifica, renombra o borra un archivo en una carpeta vigilada, o se conecta a un recurso de red)" | ✓ |
| J | requerimientos.tex:287 | "… envía un correo al administrador; una falla en el envío no afecta la respuesta al agente." | "… envía un correo al administrador antes de responder; una falla en el envío no afecta la respuesta al agente, pero un servidor de correo lento la demora." | ✓ |
| K | requerimientos.tex:355 | "3a. El proceso se interrumpe: no se escribe ningún registro parcial y el planificador reintenta en el ciclo siguiente." | "3a. Un paso del \emph{pipeline} falla: se restauran los artefactos del modelo vigente, que sigue en servicio; el intento queda registrado en el historial como no finalizado y el próximo reentrenamiento se dispara al cumplirse nuevamente el período, lo que evita reintentos en bucle ante una falla persistente." | ✓ |
| K | requerimientos.tex:359 | "El modelo vigente es el de mejores métricas y …" | "El modelo vigente es el que cumple el criterio de promoción y …" | ✓ |
| K | requerimientos.tex:363 | "sin aceptar modelos de menor desempeño" | "sin aceptar modelos cuyo desempeño empeore más allá del margen de tolerancia" | ✓ |
| L | requerimientos.tex:471 | "para mantener la precisión frente a cambios de comportamiento sin arriesgar el servicio" | "para incorporar cambios de comportamiento sin degradar la detección más allá del margen tolerado ni arriesgar el servicio" | ✓ |
| M | requerimientos.tex:538 | "vincula cada requerimiento funcional con el caso de uso …" | "vincula cada requerimiento funcional, y el requerimiento no funcional RNF-03 que origina HU-14, con el caso de uso …" | ✓ |
| M | requerimientos.tex:583 | — | Fila nueva "RNF-03 & CU-02 & HU-14" | ✓ |
| N (fila 1) | conclusiones.tex:26 | "ligada a su identidad, sin respaldo en la clave de administración (RF-02)" | "ligada a su identidad y a los usuarios que monitorea (RF-02)" | ✓ |
| N (fila 3) | conclusiones.tex:33 | "medidos en el servidor de la API sin incluir el envío de notificaciones, en entorno local con Redis en memoria" | "medidos de extremo a extremo desde el cliente, en entorno local con Redis en memoria" | ✓ |

Formato: en K se escribió `\emph{pipeline}` y en C y H `\emph{dashboard}`, igual que en el resto del capítulo. El nuevo texto de N, fila 3, coincide con `pruebas.tex:199`, que describe la medición como "de extremo a extremo … desde el lado del cliente".

## Compilación

`pdflatex` → `biber` → `pdflatex` → `pdflatex`: todos con código de salida 0. Biber sin ERROR ni WARN. `main.log` sin referencias indefinidas, sin pedido de `Rerun` y sin errores `!`. En el texto del PDF no aparece `??`.

**Páginas: 258** (antes: 261, 3 menos).

| Tabla | Antes | Después |
|---|---|---|
| 4.I Actores | 51 | 52 |
| 4.II Módulo 1 | 53 | 53 |
| 4.III Módulo 2 | 55 | 54 |
| 4.IV Módulo 3 | 56 | 55 |
| 4.V Módulo 4 | 57 | 56 |
| 4.VI Módulo 5 | 58 | 57 |
| 4.VII Módulo 6 | 60 | 59 |
| 4.VIII Módulo 7 | 61 | 60 |
| 4.IX RNF | 61 | 60 |
| 4.X Trazabilidad | 77 | 73 |
| 13.I Objetivos | 181 | 178 |

## Chequeo de desborde (todo el documento)

`pdftotext -layout` y separación por página (`\f`). En cada página se buscó la última línea `Página N de M` y se verificó que no hubiera texto debajo.

- Páginas revisadas: 258.
- Páginas con texto debajo del pie: **0**.
- Páginas sin pie: 1 y 2 (carátulas, que no llevan pie).

Limitación: el chequeo no se corrió sobre el PDF anterior para confirmar que detectaba los 3 casos originales (ese PDF se sobrescribió al compilar).
