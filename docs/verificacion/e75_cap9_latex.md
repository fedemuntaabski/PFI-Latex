# e75 — ajustes capítulos 4, 9, 7 y 13 (rama e75/cap9-producto)

Rama creada desde e75/cierre (36d0380). Sin push, sin trailers.

## Paso 0 — chequeo en el código (e75/entrega, solo lectura)

El agente rechaza `http://` en todo host que no sea loopback, incluidas IP de LAN:

- `agent/api_client.py:51` — `LOOPBACK_HOSTS = frozenset({"127.0.0.1", "::1", "localhost"})`
- `agent/api_client.py:54-55` — `es_url_loopback`: compara el hostname exacto con ese conjunto.
- `agent/api_client.py:58-66` — `exigir_https_fuera_de_loopback`: lanza `ValueError` si el esquema no es https y el host no es loopback.
- `agent/config.py:236` — la validación la invoca.

Resultado: se aplicaron 1b, el título y la celda de 2f.

## Ediciones

| Commit | Archivo | Ediciones | Estado |
|---|---|---|---|
| aa1ac6c cap4 | requerimientos.tex | 1a, 1b (loopback + clave de administración) | todas aplicadas |
| c26e572 cap9 | producto.tex | 2a–2h, filas nuevas de la Tabla 9.IV | todas aplicadas |
| 73da1ee cap7 | arquitectura.tex | Tabla 7.II: 32 endpoints | aplicada |
| 1d1e1d6 cap13 | conclusiones.tex | 4a, 4b | aplicadas |

Todos los textos «antes» existían; ninguno se omitió.

Desvíos respecto del pedido:

- Las referencias «sección 9.6.1» se escribieron con `\ref{sec:sintesis-limitaciones}` y resuelven a 9.6.1 en el PDF (6 apariciones de «(sección 9.6.1)»).
- La referencia «sección 13.4» de la fila nueva de la Tabla 9.IV usa `\ref{sec:trabajo-futuro}`. Esa etiqueta no existía: se agregó `\label{sec:trabajo-futuro}` a `\section{Trabajo futuro}` en conclusiones.tex (commit cap13). La fila queda en el commit cap9, que no compila sola hasta que llega el commit cap13.
- 2g usa `\ref{chap:arquitectura}`; en el PDF dice «capítulo 7».
- En cap4 1a, «sección 9.6.1» también se resolvió con `\ref`.
- Los \mbox{RF-21} de 4a son las dos únicas apariciones de RF-21 del capítulo 13, ambas dentro de la Tabla 13.I.
- Ítem 6 de 13.4: «…con el circuit breaker abierto, registrar como fallido el intento… cuyo pipeline falla, que hoy queda como «pipeline en curso», registrar también los que terminan por una excepción y fijar un tiempo máximo al pipeline.»
- main.tex/pdf: archivos de compilación no versionados.

## Compilación

pdflatex → biber → pdflatex → pdflatex. 261 páginas físicas, sin errores. Cero «??» (pdftotext y main.log).

## Verificación con pdftotext (espacios normalizados)

Frases nuevas:

| Frase | Apariciones |
|---|---|
| «pipeline en curso» | 3 (cap. 4: 1, pág. PDF 69; cap. 9: 1, pág. 134; cap. 13: 1, pág. 188) |
| 32 endpoints | 2 |
| Clave de administración aceptada en el nivel de agente | 1 (en una celda de tabla, por eso el texto se parte en líneas) |
| Reentrenamiento fallido registrado como en curso | 1 (ídem) |
| Canal HTTP en loopback | 1 |
| produjeron candidatos que la regla anterior rechazó | 1 |
| capítulo 7 (9.4) | resuelto: «se presenta en el capítulo 7» |

Frases viejas: «no finalizado», «31 endpoints», «red local, el agente», «Fuera de una red local», «bucle ante una falla», «versión instalada es anterior», «tampoco produjeron un modelo mejor», «Canal sin cifrar», «capítulo de arquitectura»: 0 apariciones cada una.

Otros controles:

- «RF-» al final de línea: ninguno en el documento; en la Tabla 13.I (págs. PDF 183-186) «(RF-21)» queda entero.
- Texto debajo de «Página N de M»: ninguna página.
- Conteo de RF intacto: «Los 31 requerimientos funcionales están implementados» (4 apariciones); no existe la redacción «31 de los 31».
- Total: «Página 259 de 259» (261 páginas físicas; las 2 primeras no se numeran).

## Páginas de inicio (índice contra PDF)

| Capítulo | Índice | Página impresa | Página PDF |
|---|---|---|---|
| 9 Producto implementado | 118 | 118 | 120 |
| 10 Pruebas y resultados | 137 | 137 | 139 |
| 13 Conclusiones y trabajo futuro | 180 | 180 | 182 |
| Bibliografía | 188 | 188 | 190 |

Coinciden con el índice.

## Fuera de alcance, pendiente

- `docs/verificacion/e75_cap13_ajustes.md` y `e75_cap13_latex.md` siguen sin versionar, sin tocar.
- Este archivo no se commitea.
