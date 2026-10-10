# E75 — Objetivos específicos 1, 3, 4 y 6 (sección 1.1.2)

- Rama: `e75/objetivos-especificos` (desde `e75/cierre`; `e75/cifras-finales` ya era ancestro).
- Commit: `83788077cf83ff0156989d95ae8dfebf544a35e6` — "docs: alinea objetivos específicos 1, 3, 4 y 6 con el código" (sin trailers, sin push).
- Archivo tocado: solo `chapters/chapter01.tex` (9 inserciones, 8 eliminaciones). Formato conservado: `5\,\%`, `150\,MB`, `500\,ms`, sigla `(ACL)` definida en el mismo ítem.

## Cambios

| Ítem | Antes | Después |
|---|---|---|
| 1 | Implementar un agente para equipos Windows que recolecte únicamente metadatos de actividad (procesos, archivos y conexiones de red), los envíe a una API central por un canal cifrado con TLS, autenticándose con una credencial individual y revocable por agente, ligada a su identidad y sin respaldo en la clave de administración, y consuma como máximo el 5 % de la CPU y 150 MB de memoria residente. | Implementar un agente para equipos Windows que recolecte únicamente metadatos de actividad (procesos, archivos y conexiones de red), los envíe a una API central por un canal cifrado con TLS, autenticándose con una credencial individual y revocable por agente, ligada a su identidad y a los usuarios que monitorea, y consuma como máximo el 5 % de la CPU y 150 MB de memoria residente. |
| 3 | Calcular un puntaje de riesgo de 0 a 100 por evento, con continuidad entre sesiones y decaimiento temporal, con una latencia de evaluación de percentil 95 menor o igual a 500 ms, medida en el servidor de la API sin incluir el envío de notificaciones por correo. | Calcular un puntaje de riesgo de 0 a 100 por evento, con continuidad entre sesiones y decaimiento temporal, con una latencia de evaluación de percentil 95 menor o igual a 500 ms, medida de extremo a extremo en un entorno local. |
| 4 | Ejecutar en el equipo una respuesta graduada según el nivel de riesgo, desde una alerta hasta la terminación de procesos y la denegación de acceso a carpetas, reversible cuando el sistema operativo lo permita: la suspensión se reanuda y el acceso a la carpeta se restaura al estado previo exacto desde un respaldo de la lista de control de acceso (ACL); la terminación de procesos no es reversible. | Ejecutar en el equipo una respuesta graduada según el nivel de riesgo, desde una alerta hasta la terminación de procesos y la denegación de acceso a carpetas, reversible cuando el sistema operativo lo permita: la suspensión se reanuda y, cuando el agente se ejecuta con privilegios de administrador, el acceso a la carpeta se restaura al estado previo exacto desde un respaldo de la lista de control de acceso (ACL); la terminación de procesos no es reversible. |
| 6 | Mantener la vigencia del modelo mediante un reentrenamiento periódico que se ejecuta en procesos separados del servicio de producción y promueve el modelo nuevo solo si mejora las métricas de comparación, y tratar a los usuarios nuevos con un período de aprendizaje. | Mantener la vigencia del modelo mediante un reentrenamiento periódico que se ejecuta en procesos separados del servicio de producción y promueve el modelo nuevo solo si sus métricas de comparación no empeoran más allá de un margen de tolerancia (criterio de no inferioridad), y tratar a los usuarios nuevos con un período de aprendizaje. |

## Apariciones fuera de 1.1.2 (solo reporte, sin modificar)

Búsqueda multilínea (tolera cortes de línea) en todos los `.tex`.

| Frase | Archivo:línea | Oración completa |
|---|---|---|
| "sin respaldo en la clave de administración" | `chapters/conclusiones.tex:26` | (Tabla 13.I, fila 1, Evidencia) "Recolección de metadatos implementada (RF-01, RNF-08); canal con TLS en el despliegue y rechazo de `http` fuera de *loopback* (RNF-13); credencial individual por agente, revocable y ligada a su identidad, sin respaldo en la clave de administración (RF-02); consumo medio de 0,09 % de CPU y 33 MB de memoria residente (RNF-02); verificado el 10 de octubre de 2026 con un agente real contra la instancia por HTTPS, con credencial individual (sección estado-despliegue)" |
| "medida en el servidor de la API" / "sin incluir el envío de notificaciones" | `chapters/conclusiones.tex:34-35` | (Tabla 13.I, fila 3, Evidencia) "Continuidad y decaimiento implementados (RF-03, RF-04); percentil 95 de 14,9 ms y percentil 99 de 148,9 ms, medidos en el servidor de la API sin incluir el envío de notificaciones, en entorno local con Redis en memoria" |
| "solo si mejora" | — | Sin apariciones fuera de 1.1.2. |
| "estado previo exacto" | — | Sin apariciones fuera de 1.1.2. |

Equivalentes relacionados (criterio de no inferioridad; coherentes con el nuevo objetivo 6):

- `chapters/producto.tex:95` — "Luego aplica un criterio de promoción de no inferioridad sobre los escenarios de DEV de la sección~\ref{sec:benchmark}: el modelo candidato y el vigente se puntúan sobre los mismos escenarios, y HOLDOUT nunca participa."
- `chapters/requerimientos.tex:159` — RF-21: "El sistema debe promover el modelo nuevo solo si no es inferior al vigente en la detección de escenarios de referencia (ROC-AUC medio no menor que el del vigente menos 0,02 y tasa de falsos positivos en nivel alto no mayor que la del vigente más 0,01), reemplazándolo sin reiniciar la API." Estado: "Implementado: el criterio de no inferioridad tiene 11 pruebas automatizadas y se verificó con el script de evaluación (el vigente contra sí mismo se promueve y el juego v2 se rechaza por falsos positivos); todavía no se ejecutó una promoción desde el planificador con un modelo genuinamente nuevo".
- `chapters/requerimientos.tex:464` — "Dado un modelo nuevo que cumple el criterio de no inferioridad sobre los escenarios de referencia, entonces reemplaza al vigente sin reiniciar la API."
- `chapters/pruebas.tex:587` — "Ese criterio de comparación se reemplaza después por el de no inferioridad sobre escenarios etiquetados (sección~\ref{sec:reentrenamiento-producto})."

## Tabla 13.I (cumplimiento de objetivos, `chapters/conclusiones.tex:14-60`)

- **Fila 1 — repite texto viejo.** La evidencia conserva "sin respaldo en la clave de administración" y no menciona "ligada … a los usuarios que monitorea" (eso sí aparece en la fila 7: "ligada a su identificador y a sus usuarios (403 si no corresponde)"). No contradice el nuevo objetivo, pero no lo refleja.
- **Fila 3 — contradice el nuevo objetivo.** El objetivo dice ahora "medida de extremo a extremo en un entorno local"; la evidencia dice "medidos en el servidor de la API sin incluir el envío de notificaciones". Las cifras (P95 14,9 ms; P99 148,9 ms) corresponden a la medición en servidor, no a una de extremo a extremo.
- **Fila 4 — coherente.** Ya explica que la restauración exacta requiere consola elevada (`SeRestorePrivilege`) y que sin elevación cae a `/remove:d`.
- **Fila 6 — coherente, con un matiz.** Cita el criterio de no inferioridad; la frase "produjeron modelos candidatos que no superaron al vigente" usa todavía el vocabulario de "superar/mejorar" en lugar de "no inferioridad".

## Compilación

Cadena: `pdflatex main` → `biber main` → `pdflatex main` → `pdflatex main`. Códigos de salida 0; biber sin ERROR/WARN; `main.log` sin referencias indefinidas, sin `Rerun` pendiente ni `??`.

**Páginas: 261** (antes: 261, sin cambio).
