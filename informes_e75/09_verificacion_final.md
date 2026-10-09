# E75 — Verificación final

Rama `correcciones-e75-latex`. Fecha: 2026-10-09. Se leyeron los informes 00 a 08 antes de verificar.

## Resumen

| # | Chequeo | Resultado |
|---|---|---|
| 1 | Compilación limpia y warnings | OK. 0 errores. No hay warnings de tipo nuevo; solo cambian los conteos (ver abajo) |
| 2 | `??` y citas o referencias sin definir | OK. 0 |
| 3 | Marcadores `[[...]]` | OK. Quedan 22 `[[CODIGO...]]`, los mismos del inventario, y ningún `[[COMPLETAR...]]` |
| 4a | Heading seguido de heading sin texto | OK |
| 4b | Subsección con hijo único | **Corregido**: 9.6 → 9.6.1 (`chapters/producto.tex`) |
| 4c | Title Case en títulos y epígrafes | **Corregido** 1 epígrafe (`chapters/chapter04.tex:300`). El resto son excepciones ya aceptadas en el informe 02 |
| 4d | "Capítulo X.Y" usado para una sección | OK |
| 4e | "et al." con dos autores | OK |
| 4f | Figuras y tablas no mencionadas por su número | OK (23 tablas se mencionan dentro de un rango) |
| 4g | Figuras sin línea "Fuente:" | OK |
| 4h | Pretérito narrando trabajo propio fuera de los resultados | Sin cambios: 4 casos revisados, todos son hechos fechados. Se listan abajo |
| 4i | Mecánica de entregas fuera de las transcripciones | 1 caso que es de contenido (Anexo A). Se lista sin tocarlo |
| 5 | Título en carátula, portada, encabezado y metadatos | OK |
| 6 | Profundidad del índice ≤ 4 | OK |
| 7 | PDF final | `build/main.pdf`, **246 páginas** |

## 1. Compilación limpia

Se borró `build/` entero y se corrió `latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`, que ejecuta pdflatex, biber y las pasadas necesarias. Se volvió a compilar después de las correcciones y el resultado es el mismo.

| Concepto | Base (informe 00, 243 p.) | Final (246 p.) |
|---|---|---|
| Errores (`!`) | 0 | 0 |
| LaTeX `'h' float specifier changed to 'ht'` | 4 | 2 |
| Paquetes: xcolor `usenames`, microtype `footnote`, soulutf8 obsoleto | 3 | 3 |
| pdfTeX: PDF 1.7 en `Caratulafinal.pdf` | 3 | 3 |
| pdfTeX: destino duplicado `name{page.1}` | 2 | 2 |
| Overfull | 245 | 248 |
| Underfull | 64 | 64 |
| biber: warnings y errores | 0 | 0 |

**No aparece ningún tipo de warning nuevo.** Las diferencias son de cantidad:

- **Overfull 245 → 248.** Para ubicarlos se compiló el commit base (`ac9d85a`) en un worktree temporal y se compararon los dos logs, overfull por overfull:
  - Los 4 `\hbox` (líneas 166, 172-173, 286-287 y 315) son idénticos en la base y en la versión final.
  - Todos los demás son el mismo aviso, uno por página a partir de la portada interior: `Overfull \vbox (…pt too high) has occurred while \output is active`. Lo produce el encabezado, que es más alto que el espacio reservado para él (el logo UADE mide 36,86 pt de alto). En la base eran 241 (243 − 2 páginas) y ahora son 244 (246 − 2). La diferencia de 3 sale de las 3 páginas que se agregaron en los informes 02, 06 y 07. El exceso por página bajó de 44,12 pt a 36,86 pt con el encabezado nuevo del informe 01.
  - Este aviso ya estaba en la base y no se ve en el PDF. Se puede eliminar aumentando `\headheight` en el preámbulo, pero eso mueve el cuerpo de todas las páginas, así que no se tocó.
- **`h` → `ht`: 4 → 2.** Bajó con el cambio de paginación del informe 02.

## 2. Referencias y citas

`main.log`: 0 `undefined` y 0 `multiply defined`. `pdftotext` del PDF final: ninguna aparición de "??".

## 3. Marcadores

`grep` sobre los `.tex` que se compilan (sin `chapters/archivo/`): **0 `[[COMPLETAR`** y **22 `[[CODIGO`**. Son los mismos 22 del inventario, con los números de línea de hoy:

| Archivo:línea | Marcador |
|---|---|
| `chapters/chapter01.tex:59` | `[[CODIGO: confirmar estado del despliegue]]` |
| `chapters/chapter01.tex:59` | `[[CODIGO: confirmar según el resultado del Prompt C]]` |
| `chapters/requerimientos.tex:63` | `[[CODIGO: resultado del Prompt C]]` (RF-02) |
| `chapters/requerimientos.tex:248` | `[[CODIGO: resultado del Prompt C]]` (RNF-13) |
| `chapters/arquitectura.tex:249` | `[[CODIGO: resultado del Prompt C]]` |
| `chapters/arquitectura.tex:255` | `[[CODIGO: resultado del Prompt C]]` |
| `chapters/arquitectura.tex:298` | `[[CODIGO: resultado del Prompt C]]` (protocolos, HTTPS) |
| `chapters/arquitectura.tex:304` | `[[CODIGO: resultado del Prompt C]]` (protocolos, HTTP sin TLS) |
| `chapters/producto.tex:142` | `[[CODIGO: resultado del Prompt C]]` (estado del despliegue) |
| `chapters/producto.tex:165` | `[[CODIGO: cifrado TLS entre agente, panel y API; …]]` |
| `chapters/pruebas.tex:284` | `[[CODIGO: Pearson con el modelo vigente]]` |
| `chapters/pruebas.tex:334` | `[[CODIGO: usuarios y cobertura de las detecciones con el modelo vigente]]` |
| `chapters/pruebas.tex:347` | `[[CODIGO: curva completa con el modelo vigente]]` |
| `chapters/conclusiones.tex:25` | `[[CODIGO: TLS y autenticación mutua]]` y `[[CODIGO]]` |
| `chapters/conclusiones.tex:41` | `[[CODIGO: resultado de seguridad]]` y `[[CODIGO]]` |
| `chapters/conclusiones.tex:45-46` | `[[CODIGO: cantidad de pruebas y cobertura]]` (l. 45) y `[[CODIGO]]` (l. 46) |
| `chapters/conclusiones.tex:52` | `[[CODIGO: actualizar conteo con RNF-03 y RNF-13]]` |
| `chapters/conclusiones.tex:130` | `[[CODIGO: ajustar según el resultado de la cobertura]]` |
| `chapters/conclusiones.tex:134` | `[[CODIGO: limitaciones de seguridad que queden abiertas …; integración con un proveedor de identidad real.]]` |

No se modificó ningún marcador.

## 4. Chequeos de forma

Se usó un script sobre los 22 `.tex` que se compilan (capítulos, `requerimientos.tex`, `title.tex` y anexos), sin contar los comentarios.

### 4a. Heading seguido de heading sin texto: OK
No hay ningún caso, tampoco después de la corrección de 4b.

### 4b. Subsección con hijo único: corregido
- **Problema:** `chapters/producto.tex`, 9.6 "Limitaciones conocidas" tenía un solo hijo, 9.6.1 "Inyección de instrucciones en la redacción asistida", que se agregó en el informe 07.
- **Corrección:** se partió 9.6 en dos subsecciones, con el mismo criterio que 10.5 en el informe 02:
  - Párrafo nuevo bajo 9.6: "Esta sección presenta primero una síntesis de las limitaciones conocidas del producto y luego analiza en detalle una de ellas, la inyección de instrucciones en la redacción asistida del correo de notificación."
  - Heading nuevo `\subsection{Síntesis de las limitaciones}\label{sec:sintesis-limitaciones}` (9.6.1), antes de la oración existente "La tabla 9.IV reúne…" y de la tabla.
  - La inyección de instrucciones pasa a ser **9.6.2**. Las referencias usan `\ref{sec:prompt-injection}` (tabla 9.IV, tabla 9.III, 13.4) y se actualizan solas. No hay ningún "9.6.1" escrito a mano en los `.tex`. El informe 07 menciona "sección 9.6.1" porque registra el estado de ese momento.

### 4c. Title Case: 1 corregido
| Archivo:línea | Antes | Después |
|---|---|---|
| `chapters/chapter04.tex:300` | `\caption{Comparación de algoritmos: Clustering no supervisado}` | `\caption{Comparación de algoritmos: clustering no supervisado}` |

Las demás mayúsculas que encontró el script son las excepciones del informe 02: nombres propios y de productos (Microsoft Sentinel UEBA, Isolation Forest, LSTM Autoencoder, Matriz Boston Consulting Group, Cruz de Porter, Redis, Ley 25.326, Gantt, entrevistados); rótulos con código ("Módulo N: …", "CU-0N: …", "Épica N: …", "HU-NN: …", "Requerimientos funcionales del Módulo N") y nombres de pantalla del panel después de los dos puntos ("Acceso (Login)", "Usuarios", "Con historial", etc.).

### 4d. "Capítulo X.Y": OK
No hay ningún "capítulo" seguido de un número de sección ni de un `\ref{sec:…}`.

### 4e. "et al." con dos autores: OK
No hay "et al." literal en los `.tex`. Las citas de dos autores salen "Apellido y Apellido" con la configuración del informe 03. En el PDF no aparece "et al." para ninguna de las obras de dos autores (Larman, Osterwalder, Ansari, Atlam, Benova, Kuppa, Chandramouli).

### 4f. Figuras y tablas mencionadas por su número: OK
Todas las figuras tienen su `\ref` en el cuerpo. 23 tablas no tienen un `\ref` propio, pero se mencionan por número dentro de un rango ("Las tablas 3.I a 3.VII…"):
- `chapter04.tex:7`: `tab:comp-sentinel` a `tab:comp-proyecto`.
- `chapter04.tex:224`: `tab:algo-catboost` a `tab:algo-proyecto`.
- `requerimientos.tex:47`: `tab:rf-modulo1` a `tab:rf-modulo7`.
- `e50_diseno_ux.tex:15`: `tab:mockup-login` a `tab:mockup-historial`.
- `arquitectura.tex:50`: `tab:tec-api` a `tab:tec-pipeline`.

No hay ningún float con epígrafe y sin `\label`.

### 4g. Figuras sin "Fuente:": OK
Todos los entornos `figure` tienen su línea "Fuente:".

### 4h. Pretérito narrando trabajo propio: sin cambios (contenido)
No hay pretérito en primera persona del plural. Se revisaron los casos impersonales fuera del capítulo 10 (resultados) y de las transcripciones:

| Archivo:línea | Frase | Por qué no se tocó |
|---|---|---|
| `chapters/producto.tex:97` | "la demostración anterior **se realizó** con su script de evaluación"; "**se adoptó** después como vigente" | Hechos fechados (demostración anterior, septiembre de 2026). En presente cambiaría el sentido |
| `chapters/producto.tex:138` | "todavía no **se verificó** con un agente"; "**se adoptó** después como vigente" | Estado del despliegue y decisión fechada |
| `chapters/producto.tex:163` | "por qué **se tomó** una acción" | Habla de una acción del sistema, no del trabajo del equipo |
| `chapters/conclusiones.tex:40` | "**se adoptó** después como vigente" | El mismo hecho fechado que en 9.x, en el resumen de resultados |

En el capítulo 10 aparecen `pruebas.tex:143-144` ("se verificó"), `:193` ("se realizó", "se tomaron") y `:468` ("no se adoptó"). Son resultados, que la consigna excluye.

Si se quiere eliminar todo pretérito, `producto.tex:97` y `:138` necesitan reescribirse (por ejemplo, "la demostración anterior usa…"). Es una decisión de contenido.

### 4i. Mecánica de entregas fuera de las transcripciones
No aparece "50 %", "25 %", "75 %", "esta entrega" ni "fuera de alcance del 50 %". Los "entrega" de `chapter01.tex:69, 76` (la iteración entrega una versión) y de `negocio.tex:2` ("crea, entrega y captura valor"), y los "fuera del alcance" de `requerimientos.tex:125, 127` (alcance de un requerimiento), no hablan de la mecánica de entregas.

**Caso de contenido, sin tocar:** `chapters/appendix/schedule_of_activities.tex:3` ("…junto con los **hitos de entrega** del proyecto") y el epígrafe de la l. 10 ("planificación de **hitos** y distribución de tareas"). Describen la Figura A.1, cuyo Gantt sí muestra los hitos de las entregas del 25, 50 y 75 % (informe 05). Sacar la palabra haría que el texto ya no describa la figura. Hay que resolverlo junto con la reexportación del Gantt (pregunta 05.1).

## 5. Título: OK
El título se define una sola vez, en `\UmbralTitulo` (`main.tex:57`), y en los cuatro lugares coincide carácter por carácter: "UMBRAL: agente inteligente de vigilancia conductual y mitigación de riesgo de identidad para PyMEs argentinas (2026)".
- Carátula (pág. 1, `cover/Caratulafinal.pdf`): `pdftotext` de la pág. 1.
- Portada interior (pág. 2): `chapters/title.tex:7` usa la macro.
- Encabezado (por ejemplo, pág. 12): `main.tex:62` usa la macro.
- Metadatos: `main.tex:233`, y `pdfinfo` muestra `Title: UMBRAL: agente inteligente …`.

## 6. Índice: OK
`\setcounter{tocdepth}{3}` (`main.tex:22`). `build/main.toc` tiene 4 niveles: chapter (15), section (80), subsection (124) y subsubsection (38). Los anexos entran como section bajo la entrada "Anexo".

## 7. PDF final
`build/main.pdf`: **246 páginas** (el pie dice "de 244", porque no cuenta las dos carátulas). 0 errores, 0 `??`.

## Problemas de contenido (listados, sin tocar)
1. Pretérito con hechos fechados en `producto.tex:97, 138` y `conclusiones.tex:40` (4h).
2. "Hitos de entrega" en el texto y el epígrafe del Anexo A (4i).
3. "Figura~\ref" con mayúscula en medio de oración o entre paréntesis (`chapter04.tex`, sección 3.6, y `schedule_of_activities.tex:3`), cuando otros capítulos usan "la figura~\ref". Pendiente desde el informe 02.
4. Overfull del encabezado (`\headheight`): es de formato, pero el arreglo mueve el cuerpo de todas las páginas, así que queda a tu decisión.

## Preguntas abiertas de los informes anteriores
- **01 (título):** si el título cambia, hay que volver a correr `cover/generar_caratula.js`.
- **02 (estructura):** unificar "Figura~\ref" / "figura~\ref" (punto 3 de arriba).
- **03 (citas):** `Aliyu2024` tiene `and others` en la `.bib`. ¿Se completan los autores reales?
- **04 (transcripciones):** las 22 preguntas de su sección "Preguntas para vos" siguen abiertas, entre ellas:
  - las palabras dudosas de C a F (C l. 16, 46-50, 66; D l. 24, 34, 48; E l. 8, 44, 54, 110, 122; F l. 26-28, 36, 86, 90, 96, 114, 126, 142);
  - si se pone la forma correcta entre corchetes en lugar de `[inaudible]`;
  - la frase del 18 de agosto y del "50 % del avance" en el Anexo E, l. 10: ¿queda, se recorta o se comenta?;
  - los turnos mezclados del Anexo D, que necesitan el audio.
  
  También siguen abiertos los puntos de "Sin cambios: para que decidas" ("logonear", palabras dudosas existentes, "Y." y "Okay").
- **05 (Gantt):** el Gantt no está organizado por los dos incrementos de 1.4; queda el marcador rojo del 13/06; la etiqueta "[HITO] Defensa Final…" está cortada en la imagen; impreso no se lee (hace falta reexportarlo partido en páginas).
- **06 (equilibrio):** ¿se detallan en la tabla 12.II los costos fijos de los años 2 a 4? La necesidad de fondos pesimista dice 360.837 y la suma redondeada da 360.838 (es redondeo).
- **07 (Gemini):**
  - confirmar en el navegador el año y el título de `OWASP2025LLM`;
  - las entradas NIST existentes (`Rose2020`, `Hu2014`, `NIST2023_800207A`) llevan la institución entre llaves simples y pueden salir como "National Institute of Standards y Technology" en la lista de referencias;
  - quedan los 10 puntos de "Para verificar en el código", que podrían pasar controles de "recomendado" a "implementado" y RF-31 a "con prueba".
- **08 (encuesta):** las fechas de difusión de la encuesta se omitieron por decisión tuya; 3.6 y el Anexo B no dan período.

## Archivos modificados
- `chapters/producto.tex`: párrafo introductorio de 9.6 y nueva subsección 9.6.1 "Síntesis de las limitaciones".
- `chapters/chapter04.tex`: epígrafe de la tabla de clustering.
- Este informe.
