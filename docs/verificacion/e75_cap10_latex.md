# E75 — Capítulo 10 y Tabla 13.I contra los resultados vigentes

- Rama: `e75/cap10-pruebas` (creada desde `e75/cap4-requerimientos`, 957784d).
- Commit: `dfa99d6ad2e8596b733c64dc8197708555d8377f` — "docs: corrige capítulo 10 y Tabla 13.I contra los resultados vigentes". Sin trailers y sin push.
- Archivos: `chapters/pruebas.tex`, `chapters/conclusiones.tex` y `chapters/datos.tex` (15 inserciones, 14 eliminaciones). Preámbulo, paquetes y entornos sin tocar.
- Fuente de los valores: `docs/verificacion/e75_cap10_vs_repo.md` del repo de código (`e75/entrega`, 80cfe2f).
- Pre-verificación: los 16 textos "antes" se encontraron tal cual, cada uno con una única coincidencia. El script abortaba si la cuenta era distinta de 1. El punto 10 estaba cortado en dos líneas. Los finales de línea se respetaron: CRLF en `pruebas.tex` y `conclusiones.tex`, LF en `datos.tex`.
- Referencias: "sección 10.5" y "sección 10.7" se escribieron como `sección~\ref{sec:evaluacion-modelo}` y `sección~\ref{sec:benchmark}`, igual que en el resto del capítulo (numeración confirmada en `main.aux`: 10.5 y 10.7). En el punto 4 se usaron `\emph{buffer}` y `\emph{circuit breaker}`, como en pruebas.tex:21 y :70, producto.tex:49 y requerimientos.tex:236.

## Cambios

Las líneas indican la posición después del commit.

| Punto | Archivo:línea | Antes | Después | OK |
|---|---|---|---|---|
| 1 | pruebas.tex:43 | Herramienta: "Métricas no supervisadas y escenarios inyectados"; Alcance: "… escenarios de ataque simulados." | Herramienta: "Métricas no supervisadas, escenarios inyectados y escenarios etiquetados"; Alcance: "… escenarios de ataque simulados; detección y falsos positivos sobre escenarios con etiqueta conocida en una partición reservada (sección~\ref{sec:benchmark})." | ✓ |
| 2 | pruebas.tex:189 | (no existía; va después de la viñeta "Concurrencia (septiembre de 2026)", l.188) | `\item \textbf{Concurrencia sobre Redis (agosto de 2026).}` Contra el Redis gestionado, con hasta 15 escrituras simultáneas … 70 de 70 escrituras concurrentes. Este ensayo respalda RNF-14. | ✓ |
| 3 | pruebas.tex:186 | "una corrida real disparada por el planificador completó" | "una corrida real disparada por el planificador el 25 de agosto completó" | ✓ |
| 4 | pruebas.tex:166 | "RNF-03 a RNF-08 y RNF-11" | "RNF-03, RNF-04, RNF-06 a RNF-08 y RNF-11" | ✓ |
| 4 | pruebas.tex:168 | "RF-26 (… se verifica en forma manual)" | "RF-26 (… se verifica en forma manual); RNF-05 (el \emph{buffer}, el reenvío y el \emph{circuit breaker} tienen prueba automatizada; el descarte por vencimiento y por tope se verifica en el código)" | ✓ |
| 5 | pruebas.tex:295 | "Las metas se fijan antes de cualquier reentrenamiento posterior del modelo; si este cambia los resultados, se informan contra estas mismas metas." | "Las metas se fijan después de una primera evaluación exploratoria, en la que las de detección y de alertas tampoco se cumplían, y no se modifican al pasar al juego de modelos vigente; cualquier reentrenamiento posterior se informa contra estas mismas metas." | ✓ |
| 6 | pruebas.tex:329 | "Índice de Jaccard 0,111 (15 usuarios en común)" | "Índice de Jaccard 0,111 (6 usuarios marcados por ambos modelos)". "solo comparten 15 usuarios" (l.333) sin cambios | ✓ |
| 7 | pruebas.tex:377 | "entre 3,9 y 5,6 puntos"; "quedó entre 63,7 y 65,8" | "entre 3,5 y 5,6 puntos"; "quedó entre 63,5 y 65,6" | ✓ |
| 8 | pruebas.tex:396 | "El 99,946\,\% de los eventos del conjunto de datos" | "El 99,95\,\% de los eventos del conjunto de datos" | ✓ |
| 8 | datos.tex:135 | "El 99,946\,\% de los eventos utilizados tiene el país registrado como desconocido" | "El 99,95\,\% de los eventos utilizados …" | ✓ |
| 9 | pruebas.tex:586 | Resultado: "… empeoró (de 0,1155 a 0,1175)."; Decisión: "Conservar el modelo vigente; el ciclo automático … sin una promoción real." | Resultado: "… empeoró (de 0,1155 a 0,1175) (corrida automática del 25 de agosto)."; Decisión: "No promover ese juego; el ciclo automático … sin una promoción real. El juego en servicio es el de la corrida manual del 2 de septiembre, también rechazado, que se adopta después por consistencia (sección~\ref{sec:evaluacion-modelo})." | ✓ |
| 9 | pruebas.tex:610 | "La limitación queda resuelta." | "La limitación queda resuelta ejecutando el agente con privilegios de administrador." | ✓ |
| 10 | conclusiones.tex:29-30 | "frente a un 14,2\,\% de días normales que lo / superan" | "frente a un 15,4\,\% de días normales que terminan en nivel / alto" | ✓ |
| 11 | conclusiones.tex:31 | "con un ROC-AUC de 0,80 (sección~\ref{sec:benchmark})" | "con un ROC-AUC del híbrido entre 0,58 y 0,80 según el escenario (sección~\ref{sec:benchmark})" | ✓ |

### Apariciones de "99,946" en todos los .tex (punto 8)

Antes de editar había exactamente dos, y las dos se refieren al país desconocido:
- `chapters/datos.tex:135`: reemplazada.
- `chapters/pruebas.tex:395` (396 después del commit): reemplazada.

Después de editar: 0 apariciones.

## Compilación

Cadena: `pdflatex main` → `biber main` → `pdflatex main` → `pdflatex main`. biber terminó sin ERROR ni WARN. `main.log` no tiene referencias indefinidas ni avisos de recompilación, y en el texto del PDF no aparece "??".

**Páginas: 259** (antes 258, una más).

## Chequeo de desborde (todo el documento)

Se extrajo el texto con `pdftotext -layout` y se separó por página (`\f`). En cada página se buscó la última línea "Página N de M" y se verificó que no hubiera texto debajo.
- Páginas revisadas: 259.
- Páginas con texto debajo del pie: **0**.
- Páginas sin pie: 1 y 2 (carátulas, que no llevan pie).

## Greps sobre el PDF

Sobre el texto de `pdftotext` (UTF-8), con los cortes de línea y los guiones de partición normalizados:

| Patrón | Coincidencias |
|---|---|
| "3,9 y 5,6" | 0 |
| "63,7" | 0 |
| "99,946" | 0 |
| "15 usuarios en común" | 0 |
| "ROC-AUC de 0,80 (" | 0 |

Control positivo: "3,5 y 5,6" (1), "63,5 y 65,6" (1), "99,95" (2), "entre 0,58 y 0,80" (1), "Concurrencia sobre Redis" (1), "días normales que terminan en nivel alto" (1) y "marcados por ambos modelos" (1). En la celda de la Tabla 10.IX, la extracción intercala columnas ("0,111 (6 usuarios … marcados por ambos modelos)").
