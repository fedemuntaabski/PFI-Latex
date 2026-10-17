# L2 — Forma (solo texto LaTeX)

Rama: `e75/correcciones-e50-v2`. Sin push.

## Tabla de cambios

| N.º | Archivo | Antes (resumido) | Después (resumido) | Estado |
|---|---|---|---|---|
| 1 | chapters/{arquitectura,producto,pruebas,conclusiones,e50_mercado,e50_diseno_ux,chapter04}.tex | Pretéritos en texto propio (67 cambios, ver lista abajo) | Presente | Aplicado |
| 2a | chapters/appendix/interview_5_ruiz.tex:1 | `Anexo G: Transcripción de la entrevista a Matías Gabriel Ruiz` | `Anexo G: Cuestionario escrito respondido por Matías Gabriel Ruiz` | Aplicado |
| 2b | chapters/chapter01.tex:136-138 (1.5) | `y los Anexos C a G, las transcripciones de las entrevistas a los cinco profesionales consultados.` | `los Anexos C a F, las transcripciones de las entrevistas a cuatro de los profesionales consultados, y el Anexo G, el cuestionario escrito respondido por el quinto.` | Aplicado |
| 3 | chapters/pruebas.tex:124 (10.3) | Párrafo terminaba en "...se informa como dato adicional." | Se agrega "La tabla~\ref{tab:cobertura-codigo} presenta los resultados por componente." (label real, ya existía) | Aplicado |
| 4a | chapters/chapter04.tex (11 ocurrencias en tablas y párrafos) | `IsolationForest` | `Isolation Forest` | Aplicado |
| 4b | chapters/chapter04.tex:211 y 215 | `top-3 \emph{features} por \emph{z-score}` / `las \emph{features} de IsolationForest (top-3 por z-score...)` | `las 3 variables con mayor z-score` / `las variables de Isolation Forest (las 3 de mayor z-score...)` | Aplicado |
| 5a | chapters/e50_mercado.tex:42 (11.2) | `Matriz de Fortalezas, Debilidades ... del producto frente al mercado...` | `La matriz FODA cruza las fortalezas y debilidades del producto (factores internos) con las oportunidades y amenazas del mercado relevado en el estado del arte (factores externos).` | Aplicado |
| 5b | chapters/chapter04.tex:219 (3.3) | `Profundiza lo señalado ... específicamente para el lado de IA/modelos, y muestra` | `Esta sección profundiza la comparación general ... en lo referido a los modelos de inteligencia artificial, y muestra` | Aplicado |
| 5c | chapters/chapter04.tex:186 (3.2) | `Verificación explícita de qué cubre ...` + `en caso de no haber información acerca de estas` | `La matriz verifica qué capacidades cubre cada alternativa, a partir de lo que la sección 2.2 documenta...`; redundancia borrada | Aplicado |
| 5d | chapters/chapter04.tex:389 (3.4) | `A partir de la propia conclusión del estado del arte de la documentación del proyecto (sección~\ref{sec:estado-del-arte}),` | `A partir de la conclusión del estado del arte (sección~\ref{sec:conclusion-estado-del-arte}),` | Aplicado |

Nota 5d: la subsección 2.2.6 ("Conclusión del estado del arte") no tenía `\label`; se agregó `\label{sec:conclusion-estado-del-arte}` en chapters/chapter02.tex:299 (sin cambio visible).

## 1. Cambios de tiempo verbal por capítulo

- Cap. 7 (arquitectura) (`arquitectura.tex`): 6
- Cap. 11 (mercado) (`e50_mercado.tex`): 1
- Cap. 5 (diseño UX) (`e50_diseno_ux.tex`): 1
- Cap. 3 (`chapter04.tex`): 1
- Cap. 9 (producto) (`producto.tex`): 21
- Cap. 10 (pruebas) (`pruebas.tex`): 31
- Cap. 13 (conclusiones) (`conclusiones.tex`): 6
- Total: 67

### Lista antes → después

- `arquitectura.tex`: «el inicio de sesión se verificó contra la API» → «el inicio de sesión se verifica contra la API»
- `arquitectura.tex`: «se verificó el canal de extremo a extremo con un agente real, que envió sus eventos por HTTPS con una credencial individual y llegó a ejecutar» → «se verifica el canal de extremo a extremo con un agente real, que envía sus eventos por HTTPS con una credencial individual y llega a ejecutar»
- `arquitectura.tex`: «y el canal se verificó de extremo a extremo» → «y el canal se verifica de extremo a extremo»
- `arquitectura.tex`: «TLS terminado en la propia instancia, y se verificó de extremo a extremo» → «TLS terminado en la propia instancia, y se verifica de extremo a extremo»
- `arquitectura.tex`: «por lo que no podía formar parte de los contenedores» → «por lo que no puede formar parte de los contenedores»
- `arquitectura.tex`: «porque implicaba más configuración» → «porque implica más configuración»
- `e50_mercado.tex`: «El prototipo se verificó en un entorno local» → «El prototipo se verifica en un entorno local»
- `e50_diseno_ux.tex`: «porque el día todavía no cerró» → «porque el día todavía no cierra»
- `chapter04.tex`: «Dado que cada participante podía seleccionar» → «Dado que cada participante puede seleccionar»
- `producto.tex`: «si se cumplió la periodicidad» → «si se cumple la periodicidad»
- `producto.tex`: «la demostración anterior se realizó con su script de evaluación, pero todavía no se ejecutó una promoción» → «la demostración anterior se realiza con su script de evaluación, pero todavía no se ejecuta una promoción»
- `producto.tex`: «El conjunto de variables del modelo quedó versionado: con la versión 1» → «El conjunto de variables del modelo queda versionado: con la versión 1»
- `producto.tex`: «que la regla anterior rechazó; se adoptó después como vigente por la consistencia» → «que la regla anterior rechaza; se adopta después como vigente por la consistencia»
- `producto.tex`: «se verificó de punta a punta con un agente real contra la instancia, y la API rechazó con 403» → «se verifica de punta a punta con un agente real contra la instancia, y la API rechaza con 403»
- `producto.tex`: «y se verificó con el script de evaluación; sin embargo» → «y se verifica con el script de evaluación; sin embargo»
- `producto.tex`: «produjeron candidatos que la regla anterior rechazó.» → «producen candidatos que la regla anterior rechaza.»
- `producto.tex`: «rechazado por la regla anterior, se adoptó después como vigente por consistencia del juego» → «rechazado por la regla anterior, se adopta después como vigente por consistencia del juego»
- `producto.tex`: «Por lo tanto, todavía no se ejecutó una promoción» → «Por lo tanto, todavía no se ejecuta una promoción»
- `producto.tex`: «La verificación del 6 de octubre de 2026 confirmó que» → «La verificación del 6 de octubre de 2026 confirma que»
- `producto.tex`: «El 10 de octubre de 2026 se verificaron la API» → «El 10 de octubre de 2026 se verifican la API»
- `producto.tex`: «Un agente real envió eventos por HTTPS con credencial individual y llegó al nivel crítico (97,06) con la acción de terminar el proceso y denegar la carpeta, que ejecutó; no se observó el nivel alto, porque el puntaje pasó de 52 a 97» → «Un agente real envía eventos por HTTPS con credencial individual y llega al nivel crítico (97,06) con la acción de terminar el proceso y denegar la carpeta, que ejecuta; no se observa el nivel alto, porque el puntaje pasa de 52 a 97»
- `producto.tex`: «El inicio de sesión del administrador entregó un \emph{token} de 43 caracteres distinto de las claves fijas, el operador recibió 403 en los \emph{endpoints} de administración y el \emph{token} quedó inválido» → «El inicio de sesión del administrador entrega un \emph{token} de 43 caracteres distinto de las claves fijas, el operador recibe 403 en los \emph{endpoints} de administración y el \emph{token} queda inválido»
- `producto.tex`: «por qué se tomó una acción» → «por qué se toma una acción»
- `producto.tex`: «la sesión del panel se verificaron en la instancia» → «la sesión del panel se verifican en la instancia»
- `producto.tex`: «quedaron resueltas y se retiraron de la tabla» → «quedan resueltas y se retiran de la tabla»
- `producto.tex`: «los umbrales se calibraron sin escenarios» → «los umbrales se calibran sin escenarios»
- `producto.tex`: «con un agente real se realizó el 10 de octubre de 2026» → «con un agente real se realiza el 10 de octubre de 2026»
- `producto.tex`: «la prueba manual de reversión se verificó en una consola elevada» → «la prueba manual de reversión se verifica en una consola elevada»
- `producto.tex`: «RF-21 queda con la limitación de que todavía no se ejecutó» → «RF-21 queda con la limitación de que todavía no se ejecuta»
- `producto.tex`: «incluidos los que fueron reiniciados» → «incluidos los que son reiniciados»
- `pruebas.tex`: «Una corrida del trabajo de la API falló porque faltaba la dependencia» → «Una corrida del trabajo de la API falla porque falta la dependencia»
- `pruebas.tex`: «se agregó a los requisitos de la API» → «se agrega a los requisitos de la API»
- `pruebas.tex`: «No se excluyó ningún módulo» → «No se excluye ningún módulo»
- `pruebas.tex`: «Se ejecutaron contra Redis y PostgreSQL reales» → «Se ejecutan contra Redis y PostgreSQL reales»
- `pruebas.tex`: «Cada corrida generó un reporte» → «Cada corrida genera un reporte»
- `pruebas.tex`: «el primer evento quedó en nivel medio, el nivel alto se alcanzó en el evento 15» → «el primer evento queda en nivel medio, el nivel alto se alcanza en el evento 15»
- `pruebas.tex`: «se verificó la lectura y modificación del umbral» → «se verifica la lectura y modificación del umbral»
- `pruebas.tex`: «Se verificó en vivo el reemplazo» → «Se verifica en vivo el reemplazo»
- `pruebas.tex`: «completó el \emph{pipeline} en aproximadamente 1~h~50~min y no promovió el modelo, porque el error de reconstrucción del LSTM empeoró de» → «completa el \emph{pipeline} en aproximadamente 1~h~50~min y no promueve el modelo, porque el error de reconstrucción del LSTM empeora de»
- `pruebas.tex`: «resultó correcta en el 100» → «resulta correcta en el 100»
- `pruebas.tex`: «no se produjeron errores, y el disparador que calcula la cadena de \emph{hashes} agregó en promedio» → «no se producen errores, y el disparador que calcula la cadena de \emph{hashes} agrega en promedio»
- `pruebas.tex`: «entre 3 y 4 de cada 20 fallaban por conflicto» → «entre 3 y 4 de cada 20 fallan por conflicto»
- `pruebas.tex`: «se completaron sin error 70 de 70» → «se completan sin error 70 de 70»
- `pruebas.tex`: «finalizó sin vulnerabilidades reportadas» → «finaliza sin vulnerabilidades reportadas»
- `pruebas.tex`: «La medición se realizó el 8 de octubre de 2026» → «La medición se realiza el 8 de octubre de 2026»
- `pruebas.tex`: «se tomaron 360 muestras sin pérdidas y el agente envió unos 112» → «se toman 360 muestras sin pérdidas y el agente envía unos 112»
- `pruebas.tex`: «La regla de promoción anterior rechazó ese juego» → «La regla de promoción anterior rechaza ese juego»
- `pruebas.tex`: «terminó en nivel alto y ninguno en crítico» → «termina en nivel alto y ninguno en crítico»
- `pruebas.tex`: «un modelo marcó anomalía y la regla de piso elevó el nivel» → «un modelo marca anomalía y la regla de piso eleva el nivel»
- `pruebas.tex`: «La proporción fue del 14,3» → «La proporción es del 14,3»
- `pruebas.tex`: «y se concentró en los usuarios con pocos días» → «y se concentra en los usuarios con pocos días»
- `pruebas.tex`: «Las inyecciones elevaron la mediana» → «Las inyecciones elevan la mediana»
- `pruebas.tex`: «de cada escenario quedó entre 63,5 y 65,6» → «de cada escenario queda entre 63,5 y 65,6»
- `pruebas.tex`: «ninguna variable superó el umbral de explicación» → «ninguna variable supera el umbral de explicación»
- `pruebas.tex`: «Todas las explicaciones generadas provinieron de» → «Todas las explicaciones generadas provienen de»
- `pruebas.tex`: «El conjunto de variables del modelo quedó versionado y, con la versión 1» → «El conjunto de variables del modelo queda versionado y, con la versión 1»
- `pruebas.tex`: «produjo la misma huella en ambos» → «produce la misma huella en ambos»
- `pruebas.tex`: «porque no se adoptó nada de lo explorado en DEV» → «porque no se adopta nada de lo explorado en DEV»
- `pruebas.tex`: «el ciclo automático de reentrenamiento quedó verificado de punta a punta» → «el ciclo automático de reentrenamiento queda verificado de punta a punta»
- `pruebas.tex`: «el valor esperado de ese caso cambió respecto» → «el valor esperado de ese caso cambia respecto»
- `pruebas.tex`: «extremo a extremo confirmaron el ciclo» → «extremo a extremo confirman el ciclo»
- `conclusiones.tex`: «la prueba manual de reversión dio resultado satisfactorio» → «la prueba manual de reversión da resultado satisfactorio»
- `conclusiones.tex`: «produjeron modelos candidatos» → «producen modelos candidatos»
- `conclusiones.tex`: «que la regla de promoción anterior rechazó, por lo que no se promovieron» → «que la regla de promoción anterior rechaza, por lo que no se promueven»
- `conclusiones.tex`: «se adoptó después como vigente por consistencia, no por promoción» → «se adopta después como vigente por consistencia, no por promoción»
- `conclusiones.tex`: «y se verificó con el script de» → «y se verifica con el script de»
- `conclusiones.tex`: «todavía no se ejecutó una promoción» → «todavía no se ejecuta una promoción»

### Casos NO cambiados (decide el autor)

- chapters/pruebas.tex:608: «Un agente con una clave válida podía enviar eventos a nombre de cualquier usuario, el agente aceptaba `http://` hacia cualquier servidor, usaba la clave de administración como respaldo y el inicio de sesión del panel entregaba esa clave al navegador.» (estado previo a la corrección)
- chapters/pruebas.tex:610: «La reversión de la denegación de una carpeta eliminaba todas las denegaciones del usuario en el árbol, incluidas las que existían antes de la intervención del agente.» (estado previo)
- chapters/pruebas.tex:612: «El modelo de lenguaje de la redacción asistida del correo recibe telemetría controlada por el usuario vigilado, que podía contener instrucciones.» (estado previo)
- chapters/pruebas.tex:546, 548, 550, 565, 586 (primera parte), 588, 590, 592, 594, 598, 614: tabla de hallazgos y problemas resueltos; columna "problema" en imperfecto/pretérito («se mostraban como un mensaje ilegible», «empeoró de 0,1155 a 0,1175», «hacían fallar la comparación», «quedaba guardado en disco», «agregaba unos 2 s», «agotaban el período de aprendizaje», «fallaba en un entorno limpio», «La cobertura ... era del 84,2 %»). Describen el estado previo a la corrección; el presente los volvería confusos. (La columna de tratamiento sí se pasó a presente: «queda verificado».)
- chapters/pruebas.tex:635: «el valor esperado de ese caso cambió...» se cambió a «cambia» (aplicado); el resto de esa oración queda en presente.
- chapters/pruebas.tex:349: «los usuarios que ya se encontraban en nivel alto» (estado previo a la inyección dentro de la definición de la métrica).
- chapters/pruebas.tex:295: «en la que las de detección y de alertas tampoco se cumplían» (estado de la evaluación exploratoria previa).
- chapters/pruebas.tex:511: «el mismo que estaba en producción antes de los experimentos» (se cambió solo «no se adoptó» → «no se adopta»; «estaba» es anterioridad real).
- chapters/conclusiones.tex:107: «en este proyecto las metas se fijaron después de una evaluación exploratoria, lo que le resta fuerza al contraste aunque los resultados no las alcanzaran.» (presente rompería la concordancia del subjuntivo y cambia el sentido)
- chapters/e50_diseno_ux.tex:295: «esos datos ya cambiaron desde que se cerró ese día» (anterioridad real).
- chapters/e50_diseno_ux.tex:101, 140, 256: «el detalle evento por evento que lo originó», «qué generó el score actual», «qué cambió y quién lo cambió» (trazabilidad retrospectiva por diseño).
- chapters/arquitectura.tex:45: «habría requerido» (condicional; solo «implicaba» → «implica» cambiado).
- chapters/negocio.tex:125: «el 2 de octubre de 2026 llegó a 650 puntos básicos, su máximo del año» (dato de mercado fechado y pasado, con cita).
- chapters/chapter04.tex:457 y 489: «no fue comunicada», «fueron detectados» (lo que declaran los encuestados).
- chapters/chapter02.tex (todo el estado del arte: 221, 226, 228, 250, 253, 255, 273, 285): trabajo de otros autores, queda en pasado según la regla.
- chapters/chapter04.tex:241: «como sí tenía este trabajo» (trabajo de otros autores).
- chapters/chapter04.tex:402: «entrevistas semiestructuradas a cinco profesionales»: el párrafo de 407 ya aclara que la consulta a Ruiz es por cuestionario escrito. No se tocó (sin mención de «transcripciones»).

## 3. Tablas y figuras sin mención en el cuerpo

Se revisaron los 121 `\label{tab:...}`/`\label{fig:...}` del cuerpo y anexos. Sin `\ref` directo hay 18 tablas, todas cubiertas por rangos en el texto: `comp-sentinel` a `comp-proyecto` (3.1, chapter04.tex:7), `algo-catboost` a `algo-proyecto` (3.3, chapter04.tex:219), `mockup-login` a `mockup-historial` (5.x, e50_diseno_ux.tex:24), `tec-api` a `tec-pipeline` (7.x, arquitectura.tex:50). **No hay tablas ni figuras huérfanas.**

## Verificación final

- `IsolationForest` fuera de código en el cuerpo y anexos: **0** (grep sin ocurrencias fuera de `\texttt`).
- grep de «Transcripción de la entrevista a Matías»: **0**.
- Compilación (pdflatex + biber + 2 pasadas): sin errores, sin «??», sin citas ni referencias indefinidas.
- Páginas del PDF: **278**.
- Log: 279 Overfull / 62 Underfull (avisos de cuerpo existentes, sin desbordes mayores a 20 pt); ninguno nuevo severo en las páginas tocadas. No se observaron tablas largas cortadas de forma anómala.
