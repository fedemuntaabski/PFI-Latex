# E75 — Verificación de cierre

Rama `correcciones-e75-latex`. Fecha: 2026-10-09. Se leyeron antes los informes 09, 11 y 12.

## Resumen

| # | Chequeo | Resultado |
|---|---|---|
| 1 | Compilación limpia, errores, `??`, citas y referencias sin definir | OK. Todo en 0. Los warnings son los mismos que en el informe 09 |
| 2 | Marcadores | OK. 22 `[[CODIGO`, 0 `[[COMPLETAR`, 0 `[inaudible]` |
| 3 | Mecánica de la materia en el texto del PDF | OK en el texto. **Contenido:** la imagen del Gantt (figura A.1) muestra "[HITO] Entrega del 25 %" y "del 50 %" |
| 4a | Heading seguido de heading sin texto | OK |
| 4b | Hijo único | **Corregido**: 5.1 → 5.1.1 (`chapters/e50_diseno_ux.tex:11`) |
| 4c | Title Case | OK. Solo aparecen las excepciones ya aceptadas |
| 4e | "et al." con dos autores | OK |
| 4g | Figuras sin "Fuente:" | OK |
| 5 | Revisión visual | **2 problemas de forma corregidos** (puntos suspensivos en los anexos C a F; espacio faltante en 4.5.2, CU-02). Sin desbordes, tablas mal cortadas, títulos viudos ni superposiciones |
| — | PDF final | `build/main.pdf`, **246 páginas** (el pie dice "de 244") |

## 1. Compilación limpia

Se borró `build/` y se corrió `latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`, que ejecuta pdflatex y biber. Después de las correcciones de este informe se volvió a borrar `build/` y a compilar, con el mismo resultado.

| Concepto | Informe 09 | Ahora |
|---|---|---|
| Errores (`!`) | 0 | 0 |
| Referencias o citas sin definir; `multiply defined` | 0 | 0 |
| `??` en el PDF (pdftotext) | 0 | 0 |
| `'h' float specifier changed to 'ht'` | 2 | 2 |
| Paquetes (xcolor `usenames`, microtype `footnote`, soulutf8) | 3 | 3 |
| pdfTeX (PDF 1.7 de la carátula ×3, `name{page.1}` duplicado ×2) | 5 | 5 |
| Overfull `\vbox` (encabezado, una por página desde la portada interior) | 244 | 244 |
| Overfull `\hbox` | 4 | 4 |
| Underfull | 64 | 64 |
| biber: warnings y errores | 0 | 0 |
| Páginas | 246 | 246 |

No aparece ningún tipo de warning nuevo y los conteos son iguales. Los 4 overfull `\hbox` son los mismos del informe 09. Ahora figuran en las líneas 175, 181-182, 295-296 y 324 de `e50_diseno_ux.tex`, en vez de 166, 172-173, 286-287 y 315, porque el informe 12 subió la sección de decisiones transversales 9 líneas.

## 2. Marcadores

Se buscó con grep en los `.tex` que se compilan (`chapters/*.tex`, `chapters/appendix/*.tex` y `main.tex`):

- **22 `[[CODIGO`**, en los mismos archivos y líneas que la tabla del informe 09: `chapter01.tex:59` (×2), `requerimientos.tex:63, 248`, `arquitectura.tex:249, 255, 298, 304`, `producto.tex:142, 165`, `pruebas.tex:284, 334, 347`, `conclusiones.tex:25` (×2), `:41` (×2), `:45, 46, 52, 130, 134`.
- **0 `[[COMPLETAR`** y **0 `[inaudible]`**.

## 3. Avance y entregas en el PDF

Se buscó en `pdftotext` del PDF final, página por página, sin distinguir mayúsculas: "50 %", "50\%", "avance", "18 de agosto", "entreg" y "hito".

| Pág. PDF | Término | Contexto | Clasificación |
|---|---|---|---|
| 13 | entrega | "…implementación y prueba, y **entrega** una versión ejecutable del sistema completo…" (1.4) | Metodología del proyecto, no de la materia |
| 13 | entrega | "…pero sí la **entrega** frecuente de versiones verificables." (1.4) | Ídem |
| 139 | 50 % | "Detección atribuible del escenario combinado (E4) … ≥ **50 %** de los usuarios" (tabla de metas) | Métrica técnica |
| 147 | 50 % | "…no alcanza el **50 %** de la meta de detección." | Métrica técnica |
| 162 | entrega | "…cómo el producto crea, **entrega** y captura valor (Osterwalder y Pigneur, 2010)" | Negocio |
| 179 | hito | "…junto con los **hitos** del proyecto." (Anexo A) | Texto pedido en el informe 12 |
| 180 | hito | Epígrafe de la figura A.1: "planificación de **hitos** y distribución de tareas" | Ídem |
| 219 | hito | Pita: "…dos grandes **hitos** de trabajo, el bloqueo y la alerta" (Anexo E) | Dicho del entrevistado |
| 243 | hito | Índice de figuras (epígrafe de A.1) | Ídem pág. 180 |

No aparecen "avance" ni "18 de agosto". **El texto está OK.**

**Problema de contenido (sin tocar):** el texto de la imagen `images/cronograma.jpg` no se extrae con pdftotext. En una ampliación a 300 ppp de la figura A.1 se leen las etiquetas "[HITO] Entrega del 25% — Fundamentos Teóricos Completados", "[HITO] Entrega del 50% — Diseño Metodológico e Integración Base" y la tarea "Redacción de la sección metodológica del informe para el hito del 50%". Muestran la mecánica de entregas de la materia. Se resuelve reexportando el Gantt, que ya está pendiente desde el informe 05.

## 4. Chequeos de forma

Un script recorre los `.tex` que se compilan, siguiendo los `\input` desde `main.tex` y sin contar los comentarios.

### 4a. Heading sin texto: OK
No hay ningún caso.

### 4b. Hijo único: corregido
- **Problema:** el informe 12 había movido "Decisiones de diseño transversales" como `\subsection` dentro de 5.1 "Metodología de diseño". Así 5.1 quedó con un solo hijo, 5.1.1.
- **Corrección:** `chapters/e50_diseno_ux.tex:11`, `\subsection{Decisiones de diseño transversales}` → `\section{…}`. Ahora es la sección **5.2** y sigue antes del catálogo de pantallas (5.4), así que la tabla 5.II remite hacia atrás. Lo que eran 5.2 "Arquitectura de navegación" y 5.3 "Catálogo de pantallas" pasan a 5.3 y 5.4. No hay números de sección escritos a mano. La frase de 5.1 "…que se justifica a continuación" sigue siendo correcta.
- Después de la corrección, el script no encuentra ningún hijo único.

### 4c. Title Case: OK
Todos los casos que encuentra el script son las excepciones del informe 02:
- nombres propios y de productos: Zero Trust Architecture, User and Entity Behavior Analytics, LSTM Autoencoder, Isolation Forest, Microsoft Sentinel UEBA, Entra ID Protection, Splunk UBA, Exabeam, Okta Adaptive MFA, CatBoost, Graph Neural Networks, Redis, Ley 25.326, Cruz de Porter, Matriz Boston Consulting Group, Gantt;
- rótulos con código: "Módulo N: …", "Requerimientos funcionales del Módulo N", "CU-0N: …", "Épica N: …", "HU-NN: …";
- nombres de pantalla después de los dos puntos;
- nombres de los entrevistados.

### 4e. "et al." con dos autores: OK
No hay "et al." literal en los `.tex`. En el PDF, las obras de dos autores se citan "Apellido y Apellido": Ansari y Syed, Atlam y Yang, Benova y Hudec, Chandramouli y Butcher, Kuppa y Le-Khac, Larman y Basili, Osterwalder y Pigneur.

### 4g. Figuras sin "Fuente:": OK
Todos los entornos `figure` tienen su línea "Fuente:".

## 5. Revisión visual

Se rasterizó con `pdftoppm -r 100` y se miró cada imagen. Las páginas son las físicas del PDF; entre paréntesis va el número del pie.

| Zona | Páginas | Resultado |
|---|---|---|
| 9.6, 9.6.1, 9.6.2 y lista de controles | 126, 130-131 (124, 128-129) | OK. El título 9.6.2 tiene texto debajo en la misma página, y la lista de seis controles se lee completa, sin cortes raros |
| Tabla 9.IV, incluida la fila de prompt injection | 126-130 (124-128) | OK. El longtable corta entre filas y repite el encabezado en cada página. La fila "Prompt injection en la redacción asistida" queda entera en la pág. 128, con su referencia a 9.6.2 |
| Tabla 9.III, fila de transferencia internacional | 123-125 (121-123) | OK. La fila está entera en la pág. 122. Observación sin cambios: en la pág. 121 queda un tercio libre, porque la fila "Seguridad (art. 9)" es alta y no entra; es el comportamiento normal del longtable |
| Módulo 4 (tabla 4.V) con RF-31 y matriz de trazabilidad (tabla 4.X) | 57-58, 72 (55-56, 70) | OK. RF-31 pasa a la pág. 56 con el encabezado repetido. La matriz incluye "RF-15, RF-17, RF-31 → CU-02 → HU-07". **Problema de forma** en el texto de CU-02 (ver 6) |
| Primer párrafo de 3.6 y del Anexo B | 47, 181 (45, 179) | OK. El título de 3.6 (dos líneas) tiene dos líneas de texto debajo en la misma página |
| Tablas 12.II y 12.VII | 164-165, 167 (162-163, 165) | OK. La fila "Costo fijo" con los cinco años entra en la pág. 163 sin desbordes. La tabla 12.VII entra en el ancho. Observación: en 12.VI y 12.VII el epígrafe y la nota de fuente quedan muy pegados a la tabla; es así desde el informe 06 y no se tocó |
| Ítems de 13.4 | 173-174 (171-172) | OK. Los 11 ítems se leen; el 9 y el 11 llevan marcadores `[[CODIGO]]` |
| Una página de cada anexo, C a F | 192, 207, 217, 234 (190, 205, 215, 232) | **Problema de forma** en los puntos suspensivos (ver 6). Etiquetas, sangrías y párrafos OK. En E se ve la l. 10 sin la frase de la entrega |
| Anexo A: Gantt y su párrafo | 179-180 (177-178) | Párrafo OK. La figura apaisada no se superpone con el encabezado girado. Impresa no se lee (ya pendiente del informe 05) y muestra hitos de entregas (ver 3) |
| Lista de referencias (NIST) | 175, 178 (173, 176) | OK. Chandramouli y Butcher y Vassilev et al. dicen "National Institute of Standards and Technology". Rose et al. y Hu et al. son `@Article` con revista "NIST" y no muestran la institución (ver contenido) |
| Capítulo 5 (5.1 y 5.2 nuevas) | 73 (71) | OK |

## 6. Correcciones de forma

| Archivo:línea | Problema | Antes → después |
|---|---|---|
| `chapters/e50_diseno_ux.tex:11` | Hijo único en 5.1 (4b) | `\subsection{Decisiones de diseño transversales}` → `\section{Decisiones de diseño transversales}` |
| `chapters/requerimientos.tex:320` | Faltaba el espacio después del punto. En el PDF salía "…RF-17 y RF-31.Historias de usuario: HU-05…" | `RF-31.\textbf{Historias` → `RF-31. \textbf{Historias` |
| `main.tex:19` (línea nueva) | Los "…" del informe 11 se componen con `\textellipsis`, que deja un espacio fijo después del último punto. En el PDF quedaba un hueco antes de la coma ("monetario en . . . , no") y un espacio doble ("Ah . . .  pero"). Solo se usa "…" en los Anexos C a F | Se agregó `\DeclareUnicodeCharacter{2026}{\textellipsis\unkern}`, que saca ese espacio final. Ahora se lee "en . . ., no" y "Ah . . . pero". No cambia ningún carácter de las transcripciones |

Después de estos cambios se volvió a compilar desde cero: las cifras son las del punto 1 y las páginas siguen siendo 246. Se volvieron a mirar las páginas 215 y 232 (pie) y la 71.

## Problemas de contenido (listados, sin tocar)

1. **Gantt (figura A.1):** la imagen muestra "[HITO] Entrega del 25%" y "[HITO] Entrega del 50%" y una tarea "…para el hito del 50%". Hay que reexportar el Gantt sin esas etiquetas; queda junto con los otros pendientes del informe 05 (legibilidad impresa, marcador rojo, etiqueta cortada).
2. **Rose2020 y Hu2014:** son `@Article` con `JOURNAL = {NIST}`, así que en la lista de referencias salen como artículos de una revista "NIST" y sin la institución. Serían `@TechReport`, como NIST2023_800207A.
3. **Anexo E, l. 10:** queda "hicimos una etapa inicial donde nosotros presentamos la idea…". La decisión está pendiente desde el informe 11.
4. Siguen abiertos los puntos de contenido de los informes 09, 11 y 12:
   - pretérito con hechos fechados en `producto.tex:97, 138` y `conclusiones.tex:40`;
   - las referencias a futuro dudosas del informe 12;
   - la altura del encabezado (`\headheight`).

## Archivos modificados

- `main.tex`: definición de "…" sin el espacio final.
- `chapters/e50_diseno_ux.tex`: "Decisiones de diseño transversales" pasa a ser sección (5.2).
- `chapters/requerimientos.tex`: espacio después de "RF-31.".
- Este informe.

PDF final: `build/main.pdf`, **246 páginas**.
