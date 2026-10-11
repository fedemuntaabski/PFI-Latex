# E75 — Capítulo 13: conclusiones con métricas y trabajo futuro

- Rama: `e75/cap13-conclusiones` (creada desde `e75/cap10-pruebas`, 90ad393).
- Commit: `ca9f27ea81418c283e82fdce124d15d308db4737` — "docs: conclusiones con métricas y trabajo futuro actualizado". Sin trailers y sin push.
- Archivo: solo `chapters/conclusiones.tex` (11 inserciones, 12 eliminaciones). Preámbulo, paquetes y entornos sin tocar. Se respetó el final de línea CRLF.
- Pre-verificación: los 8 textos "antes" se encontraron tal cual, cada uno con una única coincidencia. El script abortaba si la cuenta era distinta de 1. Los puntos 2, 4, 5, 6 y 7 estaban cortados en dos líneas.
- Formato: se siguieron las convenciones del archivo. Se usaron `\,\%` y `\,ms`, y `33~MB` como en la línea 26 de la Tabla 13.I. El signo menos se escribió `$-$202.527`, igual que en la Tabla 12.V (`tab:indicadores-fin`, negocio.tex:197). Se usaron `\emph{circuit breaker}` y `\emph{pipeline}` (como en arquitectura.tex y chapter01.tex), `\emph{buffer}` (como en pruebas.tex) y `\emph{token}` (como en conclusiones.tex:51). En el ítem 6 se conservó el formato de rótulo en negrita: `\textbf{Correcciones del agente y del planificador}:`.

## Cambios

Las líneas indican la posición después del commit.

| Punto | Antes | Después | OK |
|---|---|---|---|
| 1 (Tabla 13.I, fila 5, l.40) | "…evaluación heurística con cuatro problemas mayores corregidos & Cumplido" | "…cuatro problemas mayores corregidos; la explicación cubre las variables de Isolation Forest y el LSTM no tiene explicación (RNF-11, parcial) & Cumplido" | ✓ |
| 2 (13.2, l.72) | "y lo hace con una latencia muy por debajo de la que exige una respuesta en / tiempo casi real." | "y lo hace con un percentil 95 de latencia de 14,9\,ms frente al límite de 500\,ms, un consumo medio del agente de 0,09\,\% de CPU y 33~MB de memoria, y 530 pruebas automatizadas con una cobertura de líneas del 93,9\,\% en la API y del 89,3\,\% en el agente." | ✓ |
| 3 (13.2, l.95) | "con un VAN de USD 35.084 al 25\,\%, pero que su viabilidad depende" | "con un VAN de USD 35.084 al 25\,\%; en el escenario pesimista no recupera la inversión (VAN de USD $-$202.527), por lo que su viabilidad depende" | ✓ |
| 4 (13.3, viñeta 2, l.106-107) | "Sin etiquetas, la evaluación del modelo necesita metas definidas de antemano y escenarios controlados; las métricas no supervisadas por sí solas no dicen si el sistema detecta." | "Sin etiquetas, la evaluación del modelo necesita metas definidas antes de la primera evaluación y escenarios controlados: en este proyecto las metas se fijaron después de una evaluación exploratoria, lo que le resta fuerza al contraste aunque los resultados no las alcanzaran. Las métricas no supervisadas por sí solas no dicen si el sistema detecta." | ✓ |
| 5 (13.4, ítem 6, l.136-137) | "\textbf{Correcciones del agente}: informar como fallida la suspensión que no se pudo registrar y no intentar envíos nuevos con el \emph{circuit breaker} abierto." | "\textbf{Correcciones del agente y del planificador}: informar como fallida la suspensión que no se pudo registrar, no intentar envíos nuevos con el \emph{circuit breaker} abierto y registrar como fallido el intento de reentrenamiento cuyo \emph{pipeline} no termina, que hoy queda como no finalizado." | ✓ |
| 6 (13.4, ítem 7, l.138-139) | "sacar la llamada al modelo del procesamiento del / evento" | "sacar la redacción y el envío del correo del procesamiento del / evento" | ✓ |
| 7 (13.4, ítem 8, l.141) | "agregar pruebas al \emph{frontend} y al módulo de métricas de la promoción de / modelos" | "agregar pruebas al \emph{frontend}, a la cadena de hashes (RNF-09), al descarte del \emph{buffer} local (RNF-05) y a la concurrencia con varios usuarios (RNF-14)" | ✓ |
| 8 (13.4, ítem 9, l.145) | "…asociada a la clave del agente), agregar una política…" | "…asociada a la clave del agente), rechazar la clave de administración en el nivel de los agentes, hacer que el panel vuelva al inicio de sesión cuando el \emph{token} vence, agregar una política…" (el resto, sin cambios) | ✓ |

## Compilación

Cadena: `pdflatex main` → `biber main` → `pdflatex main` → `pdflatex main`. biber terminó sin ERROR ni WARN. `main.log` no tiene referencias indefinidas ni avisos de recompilación, y en el texto del PDF no aparece "??". En `main.aux`, la Tabla 13.I es `tab:cumplimiento-objetivos` y la Tabla 12.V es `tab:indicadores-fin`.

**Páginas: 260** (antes 259, una más).

## Chequeo de desborde (todo el documento)

Se extrajo el texto con `pdftotext -layout` y se separó por página (`\f`). En cada página se buscó la última línea "Página N de M" y se verificó que no hubiera texto debajo.
- Páginas revisadas: 260.
- Páginas con texto debajo del pie: **0**.
- Páginas sin pie: 1 y 2 (carátulas).

## Greps sobre el PDF

Sobre el texto de `pdftotext` (UTF-8), con los cortes de línea y los guiones de partición normalizados:

| Patrón | Coincidencias |
|---|---|
| "muy por debajo de la que exige" | 0 |
| "llamada al modelo" | 0 |
| "pero que su viabilidad" | 0 |
| "de antemano y escenarios" | 0 |
| "módulo de métricas de la promoción" | 1 (pruebas.tex:148, cap. 10, fuera de alcance) |

Control positivo: "14,9 ms frente al límite de 500 ms" (1), "−202.527" (2: Tabla 12.V y 13.2), "(RNF-11, parcial)" (1), "metas se fijaron después de una evaluación exploratoria" (1), "del agente y del planificador" (1), "queda como no finalizado" (1), "redacción y el envío del correo del procesamiento" (1), "concurrencia con varios usuarios (RNF-14)" (1) y "rechazar la clave de administración en el nivel" (1).
