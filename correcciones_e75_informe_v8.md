# Informe de correcciones E75, v8 (ronda 2 de código)

Fuente: `informe_fixes_e75_ronda2.md`. Rama `correcciones-e75-revision`. Sin push.

## Alcance
Aplicadas V1 y V2. **V3 (capturas) y V4 (publicación) no se tocaron**: el informe marca las partes C y D como "no autorizadas", y B4 (push y corrida de GitHub Actions) como pendiente.

## V1. Limitaciones
- `conclusiones.tex` (13.3): eliminado el ítem "Correcciones del planificador" (A1 aplicada). La lista es `\item`, se renumera sola.
- `producto.tex` (tabla 9.IV): eliminada la fila "Defectos menores del agente" (A2 aplicada, mapeo eliminado).
- `producto.tex` (9.2.1): agregada la oración sobre el circuit breaker abierto, el cierre de sesión y la vigencia de 3 horas (A3). La tabla 4.VIII (RNF-05) no se modificó.
- No se tocó la mención en 9.3 de "registro de los reentrenamientos fallidos": sigue siendo correcta.

## V2. Pruebas, cobertura y CI
| Dato | Antes | Ahora |
|---|---|---|
| Pruebas API / agente / total | 476 / 183 / 659 | 477 / 190 / 667 |
| Archivos (tabla 10.II) | 39 / 14 | 44 / 15 |
| Sentencias API / agente / total | 2804 / 1122 / 3926 | 2808 / 1107 / 3915 |
| Líneas API / agente / total | 94,8 / 90,2 / 93,5 | 94,8 / 91,8 / 93,9 |
| Líneas y ramas API / agente / total | 93,5 / 89,1 / 92,2 | 93,5 / 91,1 / 92,8 |
| API en CI (tabla 10.III) | 444 aprobadas, 23 omitidas | 445 aprobadas, 23 omitidas |
| Cobertura CI | 87,10 % líneas y ramas | 88,50 % líneas y 87,11 % líneas y ramas |

Lugares editados en `pruebas.tex`: 10.2.1, tablas 10.II, 10.III y 10.IV, 10.2.2, texto de CI de 10.2.4 y cierre de 10.11; en `conclusiones.tex`: tabla 13.I fila 9. 10.2.2 recupera el desglose de omitidas: 16 modelos entrenados, 3 paridad con la segunda versión, 3 benchmark controlado, 1 fase 6.

## Pendiente / a revisar por el autor
- **10.2.3 sin cambio**: "En la última corrida registrada, el pipeline finaliza con los cuatro trabajos aprobados." Sigue sin respaldo de la versión nueva hasta que se haga el push y se vean los 4 trabajos (B4).
- Las 23 omitidas de CI dan 445+23 = 468; coincide con B1.
- Parte D sin hacer: 9.3, 9.2.7, tablas 9.II y 9.IV (clave de administración) y 10.4.3 siguen diciendo que la corrección no está publicada.
- Parte C sin hacer: capturas y wireframes sin tocar.
- Incidente menor: `latexmk -C` borró `main.dvi` (versionado); restaurado con `git checkout`.

## Verificación
- Compilación desde cero (`latexmk -C` + `latexmk -pdf`): sin "Rerun" ni referencias indefinidas; 283 páginas, pie "Página 281 de 281" coherente.
- En el texto del PDF ya no aparecen 659, 90,2, 92,2, 87,10, 444, 3926, 1122, "Defectos menores" ni "Correcciones del planificador". Quedan 476 y 183 solo como falsos positivos (421.476, -183.466, 1 659 de una tabla de benchmark).
