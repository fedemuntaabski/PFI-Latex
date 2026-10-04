# Relevamiento de redacción — PFI 75 %

Rama: `analysis/redaccion-pfi75`. Solo lectura; no se modificó ningún archivo existente ni se commiteó.

**Alcance:** texto que entra al PDF: `title.tex`, `chapter01–04.tex`, `appendix/annex.tex`, `appendix/schedule_of_activities.tex`, `appendix/surveys.tex`. Excluidos: entrevistas (`interview_*.tex`), comentarios `%`, y los archivos hoy comentados en `main.tex` (`abstract`, `summary`, `acknowledgments`, `conclusion`). Las tablas RF/RNF se recorrieron por regex, no se leyeron línea por línea.
**Método:** regex por categoría + lectura manual de cada hit; ortografía por revisión de las ~1.600 palabras de aparición única (no hay `aspell`/`hunspell`). **[V]** = hit literal verificado. **[I]** = criterio de estilo/inferencia.
Las líneas son del archivo `.tex` actual.

## Conteo por categoría

| # | Categoría | Hallazgos |
|---|---|---|
| 1 | Primera persona | 1 |
| 2 | Registro coloquial / publicitario | 21 |
| 3 | Notas internas de proceso | 24 |
| 4 | Ortografía / tipografía / cortes de palabra | 7 |
| 5 | Afirmaciones absolutas sin cita | 8 |
| 6 | Términos inconsistentes | 11 |
| | **Total** | **72** |

---

## 1. Primera persona

Búsqueda de `pudimos|hicimos|decidimos|nuestro/a|vamos a|…amos/…imos|nos`: sin otros casos **[V]**. Los verbos en primera persona de entrevistas/encuesta están en citas literales o en captions de preguntas.

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter02.tex:238` | "…pudimos evidenciar una carencia en la etapa final del control de acceso…" | "…se evidencia una carencia…" / "…el análisis evidencia…" |

## 2. Registro coloquial o publicitario

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter03.tex:763` | `\textbf{¿Cuál es el diferencial?}` (pregunta retórica como título) | "Diferencial del producto" |
| `chapter03.tex:763` | "entre ``detecté algo raro'' y ``hice algo al respecto''" | Reformular impersonal: "entre la detección de una anomalía y la ejecución de una respuesta" |
| `chapter03.tex:763` | "ese hueco" (×2) | "esa brecha" |
| `chapter03.tex:763` | "No es ``una alerta más clara'' ni ``un dashboard más prolijo'', es la diferencia entre un sistema que avisa y un sistema que reacciona." | Frase tipo eslogan; reemplazar por descripción técnica de la diferencia (detección vs. respuesta automática en el endpoint) |
| `chapter03.tex:763` | "en segundos, sin depender de que haya un humano mirando la pantalla" | "sin intervención manual" (y ver cat. 5) |
| `chapter03.tex:767` | "va a buscar la actividad directamente al endpoint del usuario" | "recolecta la actividad directamente en el endpoint" |
| `chapter03.tex:773` | "no tendría sentido, invalidaría todo el posicionamiento de Plaza…" | "resultaría incoherente con el segmento objetivo" |
| `chapter03.tex:822` | solución "todo en uno" | "integrada" / "solución integral (SIEM + UEBA + SOAR)" |
| `chapter03.tex:848` | "en pleno auge académico e industrial ahora mismo" | "en expansión actual" |
| `chapter03.tex:849` | "y acá los tres líderes relevados…" | "y en este caso los tres líderes…" (**"acá"** es coloquial) |
| `chapter03.tex:849` | "participación de mercado literalmente en cero al día de hoy" | "participación de mercado nula a la fecha" |
| `chapter03.tex:849` | "``cero clientes'' y ``tres competidores…''" (comillas enfáticas) | Redactar sin comillas enfáticas |
| `chapter04.tex:354` | "El proyecto adopta literalmente la combinación…" | "adopta la combinación…" |
| `chapter03.tex:249` | "(``¿su API debe ser agresiva o informativa?'')" | Reformular como enunciado (pregunta retórica entre comillas) |
| `chapter03.tex:480` | "``¿qué tan grave es esto ahora?''" | Reformular como enunciado |
| `chapter04.tex:124` | "no cubre lo que pasa después de que el acceso ya fue concedido" | "no cubre el comportamiento posterior a la concesión del acceso" **[I]** |
| `appendix/surveys.tex:8` | "¿Usás una computadora provista por tu empresa…?" | Voseo en caption (pregunta de encuesta). Si es literal del formulario, indicar "Pregunta tal como fue formulada:"; si no, usar usted/impersonal |
| `appendix/surveys.tex:44` | "Cuando te alejás de tu computadora, ¿qué hacés habitualmente?" | idem (voseo: alejás, hacés) |
| `appendix/surveys.tex:59,66,74` | "¿Cuánta confianza tenés…?", "…qué tan protegido creés…", "…política…que vos conozcas?" | idem (voseo: tenés, creés, vos conozcas) |
| `appendix/surveys.tex:89,127,135` | "¿Qué importancia le asignás…?", "…qué tan probable creés…", "…cuánto tiempo estimás…" | idem. **[I]** Todos los captions de encuesta (18) usan tuteo/voseo y signo de pregunta; criterio único recomendado (líneas con voseo: 8, 23, 44, 51, 59, 66, 74, 81, 89, 119, 127, 135) |

## 3. Notas internas de proceso

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter03.tex:4` | "…la entrega del Hito 50\% implementa y demuestra CU-01 y CU-02…" | Quitar referencia a hitos de entrega; indicar "alcance implementado" |
| `chapter03.tex:4` | "…ni de la demo de esta entrega: se abordan en la segunda mitad del proyecto" | "CU-03 y CU-04 se encuentran planificados" |
| `chapter03.tex:4` | "``Fuera de alcance del 50\%''" | "Alcance posterior" / "No implementado en esta etapa" (y alinear en los demás títulos) |
| `chapter03.tex:109` | "(Nota de alcance: la dimensión ``rol''/``departamento'' fue evaluada y descartada para esta entrega…)" | Pasar a limitación del alcance (sin "nota", sin "entrega") |
| `chapter03.tex:111` | "(Misma nota de alcance que RF-12: sin dimensión ``rol'' en esta entrega.)" | idem |
| `chapter03.tex:123` | `soporta CU-03 (fuera de alcance del 50\%)` | ver arriba |
| `chapter03.tex:147` | `soporta CU-04 (fuera de alcance del 50\%)` | ver arriba |
| `chapter03.tex:251` | `CU-03 … (fuera de alcance del 50\%)` | ver arriba |
| `chapter03.tex:269` | `CU-04 … (fuera de alcance del 50\%)` | ver arriba |
| `chapter03.tex:342` | `Módulo 3 … (CU-03), fuera de alcance del 50\%` | ver arriba |
| `chapter03.tex:363` | `Módulo 4 … (CU-04), fuera de alcance del 50\%` | ver arriba |
| `chapter03.tex:388` | "(Nota de alcance: excluida de la auditoría de cumplimiento de esta entrega, por decisión del autor; ver RNF-03.)" | Eliminar "por decisión del autor"; justificar técnicamente la exclusión |
| `chapter03.tex:399` | "…a partir de las pantallas ya construidas y validadas…" | **[I]** Evitar describir el proceso ("ya construidas"); describir el resultado |
| `chapter03.tex:401` | "…esta pantalla ya validada…" | idem |
| `chapter03.tex:767` | "según el propio Estado del Arte ``no incorpora…''" | Citar la fuente (`\parencite`) en lugar de autorreferencia al documento |
| `chapter03.tex:769` | "que el Estado del Arte describe con ``falta de visibilidad…''" | idem |
| `chapter03.tex:768` | "(cita textual del Estado del Arte)" (ítem de Splunk UBA) | Citar la fuente original |
| `chapter03.tex:781` | "el propio Estado del Arte describe como compleja" | idem |
| `chapter03.tex:796, 800, 831` | "el propio Estado del Arte identifica…", "…que el Estado del Arte señala en Sentinel", "…que señala el propio Estado del Arte" | idem |
| `chapter03.tex:848` | "toda la bibliografía citada en anteriores entregas es de 2025 en adelante" | **Referencia a entregas previas** y además falsa (ver cat. 5). Eliminar |
| `chapter03.tex:848` | "…la propia sección de Conocimientos del proyecto" | Referencia a una sección que no existe con ese nombre; usar `\ref` al apartado real |
| `chapter03.tex:1051` | "(Nota de alcance: mejora planteada para después del hito del 50\%, sujeta a los tiempos y alcance restante del proyecto.)" | "Mejora futura" |
| `chapter03.tex:1059` | idem | idem |
| `chapter04.tex:381` | "A partir de la propia Conclusión del Estado del Arte de la documentación del proyecto" | "A partir de la conclusión del Estado del Arte (Sección~\ref{…})" |

No se encontraron referencias a ramas, `.md`, "sesión de trabajo" ni `TODO` en texto activo **[V]**. "Sesión" aparece solo en sentido técnico.

## 4. Errores ortográficos, tipográficos y cortes

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter04.tex:5–6` | "…en cinco dimens⏎iones:…" (palabra cortada por salto de línea; en el PDF sale "dimens iones") | "dimensiones" en una línea |
| `chapter02.tex:202` | "Un estudios realizado por…" (y doble espacio antes de "señala") | "Un estudio realizado por" |
| `chapter03.tex:401` | "Se dibujaron en fromato de un wireframe…" | "formato" |
| `chapter03.tex:401` | "ya validada(agrupación de información…" (falta espacio antes del paréntesis) | "validada (agrupación…" |
| `chapter03.tex:31` | "definidos en la seccion ~\ref{…}" | "sección~\ref{…}" (tilde y espacio) |
| `chapter04.tex:179` | "en caso de no haber informacion acerca de estas" | "información" |
| `chapter03.tex:401` | "…el Capítulo~\ref{sec:decisiones-transversales-mockups}" **[I]** | Verificar que el label apunte a un capítulo y no a una sección |

Limitación: sin corrector automático; puede haber errores no detectados en palabras de frecuencia ≥ 2.

## 5. Afirmaciones absolutas sin cita

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter03.tex:848` | "toda la bibliografía citada en anteriores entregas es de 2025 en adelante" | **[V] Falsa:** el `.bib` cita `Rose2020`, `Hu2014`, `Kuhn2010`, `Landauer2023` (2022), `Hariri2019`, `Xiao2022`, etc. Eliminar o precisar ("buena parte de las referencias recientes") con cita |
| `chapter03.tex:763` | "exactamente la ventana de tiempo que un atacante… necesita" | Atenuar o citar |
| `chapter03.tex:763` | "en segundos, sin depender de que haya un humano…" | Sustentar con métrica medida o citar; si no, "con baja latencia" |
| `chapter03.tex:773` | "invalidaría todo el posicionamiento…" | Atenuar |
| `chapter03.tex:849` | "casi independientemente de qué tan bueno sea el producto… la participación de mercado se gana con tiempo" | Afirmación general sin cita; citar o atenuar |
| `chapter02.tex:19` | "Las decisiones… dependen completamente del Punto de Decisión de Políticas" | Citar NIST SP 800-207 (`Rose2020`) o atenuar |
| `chapter04.tex:442` | "en lugar de aplicar siempre la máxima restricción" | Verificar contra dato de encuesta; atenuar |
| `chapter04.tex:208` | "ningún competidor relevado cubre por completo" | Ya matizada con "salvedad"; **[I]** acotar a "de los relevados" |

Revisadas y aceptables **[V]**: `chapter02.tex:161, 228` ("no existe un único algoritmo…") llevan `\parencite`.

## 6. Términos inconsistentes

| Archivo:línea | Texto actual | Sugerencia |
|---|---|---|
| `chapter03.tex:396, 404` vs `:964` y catálogo | "las 6 pantallas navegables" (L396, L404) / "5 vistas" (L964); el catálogo (L406–L691) tiene **8** subsecciones (Login, Usuarios, Detalle, Alertas, Umbrales, Auditoría, Estado, Con historial) y la Demo **9** capturas | Unificar la cantidad y su definición (pantalla navegable vs. vista) |
| `chapter04.tex:5, 208, 389` vs `chapter03.tex:763, 814, 852` | "cuatro soluciones comerciales" vs "las tres soluciones" (Sentinel, Splunk, Exabeam); Cap. 4 compara 6 alternativas + proyecto | Aclarar cuáles son y mantener el número |
| `chapter03.tex:4, 31` vs módulos | RF: "Módulo 1–6" (L33–L147) y HU: "Módulo 1–5" (L288–L385) con títulos distintos; el texto dice "seis módulos" | Diferenciar ("Módulo RF-n" / "Épica HU-n") |
| `chapter01.tex:7, 12`, `chapter02.tex:6, 45`, `chapter04.tex:428` vs `chapter02.tex:27, 108, 204`, `chapter03` (29 usos de *score*), `chapter04.tex:407` | "nivel de confianza" (9×) / "puntaje de riesgo" (6×) / "score de riesgo" (3×) / "índice de riesgo" (1×) / "score" | Definir una vez (p. ej. "puntaje de riesgo (*score*)") y usarlo en todo el texto. **[I]** La Introducción habla de "nivel de confianza" mientras el cuerpo usa riesgo: polaridad inversa |
| `chapter01.tex:12, 16` vs `chapter03.tex:319` y `dashboard` (56×) | "panel de administración (dashboard)" / "panel de control" / "dashboard" | Elegir un término |
| `chapter02.tex:242` vs `chapter03` | "motor de IA" / "motor de riesgo" / "motor de scoring" | Unificar |
| `chapter03.tex:71–73, 224, 470, 697` vs `:241` y `chapter02.tex:145, 225` | Niveles "bajo/medio/alto/crítico" vs "riesgo moderado" (L241) vs "riesgo/niveles elevados" | Usar siempre los cuatro niveles definidos |
| `chapter03` (2×), `chapter04` (10×) vs `chapter02` (6×), `chapter03` (5×), `chapter04` (2×) | "IsolationForest" (12×, p. ej. `chapter04.tex:212`) y "Isolation Forest" (13×) | Una sola grafía ("Isolation Forest") |
| PDP/PEP | "API PDP" (3×), "Agente PEP" (10×), "PDP" (16×) y "PEP" (25×) sueltos vs "API"/"agente" | Definir la equivalencia en primera mención y mantenerla |
| `chapter02.tex:202` y resto | "cold-start" (12×) vs "arranque en frío" (1×, `chapter02.tex:202`) | Una forma (con cursiva) |
| `chapter04.tex:400` | "Zero Trust" (12×) vs "modelo de confianza cero" (1×) | Una forma |

Conteos **[V]** por grep sobre texto activo. "UBA" (21×) corresponde mayormente al producto "Splunk UBA" (legítimo).
