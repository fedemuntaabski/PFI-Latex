# Bitácora: revisión de modelos en la memoria LaTeX

Rama: `revision-modelos-latex` (desde `correcciones-e75-revision`). Guía: `corregir_en_latex/plan_goal_latex.md`; insumos en `corregir_en_latex/`.

## Estado inicial (15/11/2026)

- Compilación (`pdflatex` + `biber` + `pdflatex` ×2): 283 páginas, 0 errores, 8 *warnings* (3 de paquetes: `xcolor usenames`, `microtype footnote`, `soulutf8`; 5 de `h` → `ht`), sin referencias ni citas indefinidas.
- `images/cronograma.jpg` está borrado sin commitear y el Anexo A todavía lo usa. Para compilar, se restaura temporalmente desde `HEAD` y se borra al terminar; el borrado pendiente no se toca.
- Decisiones del autor antes de empezar: el anexo nuevo va al final (Anexo I, no D); se versiona toda la carpeta `corregir_en_latex/`, pero el etiquetado no se integra en la memoria; las secciones nuevas del capítulo 10 se anclan con `\label` antes de escribirse, para que cada commit compile sin referencias indefinidas.

## Avance por capítulo

### Capítulo 8, Datos (`chapters/datos.tex`)

- **8.1:** se reemplazó el párrafo de los escenarios inyectados por el de la evaluación exclusiva con datos reales. Se agregó la subsección 8.1.1 "Conjuntos de datos complementarios" con su tabla (`tab:datos-complementarios`).
- **8.2:** se agregó el párrafo de la clasificación por comportamiento (4 de 12, 14 de 291, 5,1 % frente a 0,9 %).
- **8.3:** introducción nueva (camino por defecto: IF + novedad); corte fijo y parametrizable en la tabla de configuración; párrafo de calibración por cuantiles con la partición DEV (63) / HOLDOUT (60); párrafo del puntaje del camino por defecto en reemplazo del híbrido 0,5/0,5; nuevas 8.3.4 "Detección de novedad de recurso" (`sec:novedad-recurso`) y 8.3.5 "Caminos alternativos" (`sec:caminos-alternativos`). El párrafo del umbral del LSTM, que remitía a `sec:benchmark-controlado` (sección retirada), ahora aclara que describe la versión 1 y remite a 8.3.5.
- **8.4:** último párrafo con el corte fijo, `PFI_ORIGEN_REENTRENAMIENTO=clue` y la brecha del 53,66 % frente al 4,13 %.
- **8.5.1:** las siete tablas tienen RLS; `historial_scores` la incorporó el 29/10/2026 (también se corrigió "seis de las siete" en la misma oración).
- **8.6, síntesis:** el LSTM y Markov quedan como caminos alternativos.
- En `pruebas.tex` se agregaron los labels ancla `sec:revision-modelos`, `sec:revision-metodo`, `sec:revision-transferencia` y `sec:evaluacion-default` (provisionales hasta el capítulo 10).
- Compilación: 285 páginas, 0 errores, 8 *warnings* (los mismos de la línea base) y sin referencias indefinidas.
- **Pendientes para el autor:**
  - Referencia completa de Larroche (2026): se cita como texto con `% TODO`, sin entrada en `biblio.bib`, porque los insumos y el repo del sistema no la incluyen.
  - LANL 2017, GUIDE y DARPA OpTC no tienen referencia bibliográfica; los insumos no la dan.
  - La nota de la figura `fig:er-config` sigue mostrando `metricas_modelo.modelo: iso | lstm | benchmark_dev`, y la de `fig:er-scoring`, `drift_alerts.lado: iso | lstm`. Es el esquema de la base de datos y los insumos no lo cubren, así que no se tocó.

### Capítulo 9, Producto (`chapters/producto.tex`)

- **9.2.2:** motor de *scoring* con el camino por defecto (IF calibrado + novedad, regla de piso por IF o por recursos nuevos; caminos alternativos por configuración).
- **9.2.5:** criterio de promoción nuevo (no inferioridad de la FPR ≥ alto y de su p90 semanal en DEV, margen 0,01, sobre el camino por defecto completo), párrafo de los dos criterios anteriores y verificación en *sandbox* (2 h 30 min; 2,95 % frente a 2,66 %; no se llevó a producción). Se quitó la frase "con la versión 1 vigente, la salida del puntaje no cambia", que remitía a `sec:resultados-holdout`; ahora remite al camino `lstm`.
- **9.2.7, control de acceso:** el rechazo de la clave de administración ya forma parte de la release vigente (antes decía "todavía no publicada").
- **9.3:** segundo párrafo reemplazado: camino por defecto desde el 08/11 y release del 14/11; se conservó la remisión a la verificación del despliegue.
- **9.4, tabla de la Ley 25.326:** "RLS en seis de las siete tablas" pasó a "en las siete tablas".
- **9.5, tabla 9.IV:**
  - Filas modificadas: "Sensibilidad baja" (sin *recall* medible); "El país actúa como interruptor" (aplica a la versión 1); "Aporte limitado del LSTM" (tratamiento: retirado del camino por defecto); "Calibración sin datos independientes" (sin la remisión a los escenarios etiquetados; parámetros sin barrido, según `limitaciones_provisional.md` 2.7); "Partición del candidato con datos del agente", que pasó a "Promoción no ejercitada en producción" (corte fijo, promoción en *sandbox*, según `limitaciones_provisional.md` 3.5); "Eventos incorporados sin revisión" (el criterio protege contra regresiones de la FPR); "Clave de administración" (publicada en la release vigente).
  - Filas nuevas: brecha de dominio, sustitución de cuenta, arranque en frío y, en un grupo nuevo "Operación", latencia en la nube y `eventos_crudos` sin retención.
- **9.6, síntesis:** limitaciones principales actualizadas.
- Compilación: 285 páginas, 0 errores, 8 *warnings* y sin referencias indefinidas.
- **Pendientes para el autor:**
  - En 9.2.5 se conserva "El juego de modelos vigente proviene de la última corrida manual de reentrenamiento. La regla anterior lo rechaza…": los insumos no dicen de qué corrida provienen los modelos vigentes.
  - Se mantiene el nombre de la fila "Sensibilidad baja ante ataques de corta duración", como indica la guía, aunque ahora la sensibilidad no está medida. Conviene considerar renombrarla, por ejemplo a "Detección no medida".

### Capítulo 10, Pruebas (`chapters/pruebas.tex`)

- **Introducción y tabla de técnicas:** ya no se mencionan los escenarios inyectados ni el *benchmark*; la fila "Evaluación del modelo" remite a 10.5, 10.6 y 10.7.
- **10.2.1 a 10.2.4:**
  - Inventario: 747 pruebas (547 de la API y 200 del agente).
  - Tabla de ejecución: 547 / 508 + 30 omitidas / 200. Las omitidas se describen sin desglose.
  - Integración continua: se reemplazó "el *pipeline* finaliza con los cuatro trabajos aprobados" por la reproducción local del trabajo de la API (508 aprobadas, 30 omitidas, 86 % combinada).
  - Cobertura: API 95,25 / 93,86; agente 91,90 / 91,20; total 94,40 / 93,17; columna de pruebas 547 / 200 / 747. Integración continua: 86 % combinada.
- **10.3:** el ensayo de la cadena de decisión se repitió el 14/11 con el camino por defecto. El ítem de reentrenamiento aclara que el rechazo por el LSTM corresponde a la regla anterior y que ahora la promoción se verificó en un entorno aislado.
- **10.4.2:** párrafo de la optimización del listado (2,18 → 0,12 s; 0,32 → 0,05 s; 0,40 s en la instancia).
- **10.4.3:** se quitó "b499fa3". Ahora dice que corre la release vigente (14/11), con el servicio sano y el listado en 0,40 s, y que las verificaciones detalladas se hicieron sobre la release anterior. Se agregó la demostración del 08/11 (3 de 3; crítico entre 33,8 y 40,3 s; acción entre 46,3 y 49,1 s). Se retiró la oración de la suite en la instancia (372 / 3 / 3, 91,71 %), porque los insumos no dan cifras de la suite para la release vigente.
- **10.5:** se agregó el aviso de que describe la versión 1. En la tabla de metas se reemplazaron las tres metas de escenarios (E4, promedio y 15,4 % de días sin inyección) por dos metas de ruido: FPR en alto ≤ 5 % (2,66 %, cumple) y estabilidad dentro del día (2,66 % y 1,29 %, sin meta numérica). Se reescribió el párrafo de lectura de las metas.
- **10.6 y 10.7:** reemplazadas por completo por "Revisión de modelos con datos reales" (6 subsecciones, tablas `tab:evaluacion-detectores` y `tab:efecto-default`) y "Evaluación del camino por defecto". Se borraron del `.tex` la figura `fig:curva-umbral` y las tablas `tab:escenarios` y `tab:bench-*`.
- **10.9:** la fila de redondeo ahora remite al criterio sobre días reales; la fila de la prueba de regresión atribuye las seis diferencias al oráculo; la fila de la "validación por escenarios" se reemplazó por las 6 filas nuevas. Se retiraron los cuatro párrafos de variantes evaluadas con el *benchmark* (recalibración, agregación del LSTM, decaimiento y modelos corregidos) y se reemplazaron por una remisión a 10.6.
- **10.10:** ítem de la prueba de regresión con el texto nuevo; promoción verificada en un entorno aislado; ítems de escenarios y *benchmark* reemplazados por "sin *recall* medible / día cerrado" y "HOLDOUT usado una vez con la versión 1" (`limitaciones_provisional.md` 1.1, 1.3 y 1.4); se retiró el ítem de escenarios controlados; se agregó la nota final.
- **10.11, síntesis:** cifras nuevas y lectura de la revisión.
- Los capítulos 3, 11 y 13 todavía citan labels de las secciones retiradas (`sec:validacion-escenarios`, `sec:benchmark`, `sec:benchmark-particion`, `sec:lectura-benchmark`, `sec:interpretacion`). Se dejaron como anclas provisionales en 10.6 hasta actualizar esos capítulos.
- Compilación: 276 páginas, 0 errores, 6 *warnings* (3 de paquetes y 3 `h` → `ht`) y sin referencias indefinidas.
- **Pendientes para el autor:**
  - **Estado del CI:** desde el 08/11 el *pipeline* de GitHub Actions termina en `startup_failure` en todas las ramas; la última corrida exitosa es del 04/11. La memoria ya no afirma que los cuatro trabajos aprueban; hay que resolverlo y volver a correrlo.
  - Desglose de las 30 pruebas omitidas: correr `pytest -rs` en la configuración de integración continua.
  - Inventario (10.2.1): siguen las cantidades de archivos (44 y 15); cobertura (10.2.4): siguen las sentencias (2 808, 1 107 y 3 915). Los insumos no cubren estas cifras.
  - En la integración continua se retiró el 88,50 % de líneas; el insumo solo da el 86 % combinado.
  - 10.4.1: la frase de que las latencias más altas coinciden con la inferencia del LSTM corresponde a la medición de la versión 1; no se re-midió.
  - 10.4.3: los detalles de la verificación (SHA-256 de seis artefactos, TLS, códigos HTTP, agente real con 97,06) son de la release anterior; habría que repetirlos sobre la release del 14/11.
  - 10.5.2: la meta de estabilidad dentro del día no tiene valor numérico en los insumos.
  - **Archivos huérfanos (no se borraron):** `images/pruebas/curva_umbral.pdf` y `images/pruebas/curva_umbral.png`.

### Capítulo 2, Antecedentes (`chapters/chapter02.tex`)

- **2.1.5:** se agregaron 2.1.5.3 "Detección de novedad por usuario", 2.1.5.4 "Perfiles de transición (cadenas de Markov)" y 2.1.5.5 "Umbrales por cuantil móvil", con el texto propuesto.
- **2.1.6:** párrafo final sobre la regla de evaluar solo con datos reales y el retiro de los escenarios construidos, con remisiones a 10.6.1 y 10.7. El texto lo redactó el equipo, porque la guía no lo propone.
- **Larroche (2026):** el capítulo 2 no lo cita, así que no se agregó a `biblio.bib`. Solo aparece como texto en la tabla de datos complementarios (cap. 8), con un `% TODO`.
- Compilación: sin errores, 6 *warnings* y sin referencias indefinidas.
- **Pendiente para el autor:** los subapartados nuevos no tienen citas bibliográficas, porque los insumos no las proponen. Conviene agregar referencias de detección de novedad, de cadenas de Markov aplicadas a UEBA y de umbrales adaptativos.

### Capítulo 3, Análisis comparativo (`chapters/chapter04.tex`)

- **3.3.7:** título "Isolation Forest + novedad de recurso (proyecto propuesto)" y párrafo final, con el texto propuesto. En la tabla `tab:algo-proyecto`, las filas de validación, métrica, limitación y relación ya no remiten a las secciones de escenarios. Se retiró el ROC-AUC de 0,58 a 0,80 (escenarios retirados) y se puso en su lugar la FPR de 2,66 % / 4,95 % y la brecha de 53,66 % frente a 4,13 %.
- **Barrido del capítulo (LSTM como componente vigente):** fila "Diferenciador" (l. 29); tecnología del proyecto (l. 176, caminos alternativos); XAI de la matriz (l. 219: IF + recurso de la novedad); "elección inicial" (l. 228); filas de relación con el diseño en LSTM secuencial, grafos, híbridos, IF extendido y revisión de la literatura (l. 274, 298, 322, 346 y 370).
- Compilación: sin errores, 6 *warnings* y sin referencias indefinidas. Ya no quedan referencias del capítulo 3 a las anclas provisionales.

### Capítulo 13, Conclusiones (`chapters/conclusiones.tex`)

- **Tabla 13.I:**
  - Fila 2: texto nuevo (ruido medido, 2,66 %; detección no medible).
  - Fila 5: la explicación cubre IF y el recurso de la novedad.
  - Fila 6: criterio sobre días reales y promoción en *sandbox*, en línea con 9.2.5; se retiraron "13 pruebas" y "juego v2".
  - Fila 9: 747 pruebas (547 / 200) y cobertura del 95,25 % y el 91,90 %.
- **13.2:** segundo párrafo reemplazado por el texto propuesto, con remisiones a 10.6.3 y 10.6.6.
- **13.3:**
  - Se agregaron los 4 ítems nuevos al principio, en el orden indicado.
  - Se retiraron "Rediseño del LSTM" (ya resuelto: retirado del camino por defecto), "Datos propios" (absorbido por el ítem 1 nuevo) y "Benchmark con reproducción evento a evento" (dependía de los escenarios retirados).
  - "Capacidad de detección" pasó a "Modelos": sin la transición gradual del LSTM y con la evidencia de detección del camino `markov`.
  - En "Redacción asistida" se quitó "sacar del procesamiento del evento", que ahora está en el ítem 3.
- Compilación: sin errores, 6 *warnings* y sin referencias indefinidas.
- **Pendiente para el autor:** el primer párrafo de 13.1 sigue diciendo que siete de los nueve objetivos se cumplen y dos en forma parcial (2 y 6). Con los cambios, esa cuenta no varía.

### Anexo I, Contenido de la entrega (`chapters/appendix/contenido_entrega.tex`)

- Anexo nuevo con el texto propuesto, agregado al final de `annex.tex`. Por decisión del autor queda como Anexo I y no D, para no correr las letras A–H. La cita "Landauer et al., 2022b" se resolvió como `\parencite{Landauer2022Dataset}` (el conjunto en Zenodo).
- Compilación: 278 páginas, sin errores, 6 *warnings* y sin referencias indefinidas.

### Barrido final de coherencia

- **Búsqueda** en `chapters/*.tex` y `chapters/appendix/*.tex`; se excluyó `chapters/archivo/`, que no se compila. Términos: "escenarios inyectados", "benchmark", b499fa3, 477, 445, "190 aprobadas", 94,76, 87,10/87,11, S1–S7, E1–E4, LANL 2015 y LSTM como componente vigente. Lo que queda está corregido, es histórico (versión 1) o es una cita de los insumos ("retirar los escenarios S1–S7" en la tabla de decisiones; LANL 2015 como descartado, sin cifras).
- **Capítulo 1:**
  - Objetivo específico 2: dice "evaluarlo con datos reales, en una partición de desarrollo y un conjunto reservado, informando la tasa de alertas sobre actividad normal y la estabilidad del nivel". Antes decía "escenarios de ataque inyectados… tasa de detección".
  - Párrafo del *pipeline*: el reentrenamiento por defecto omite el LSTM.
- **Capítulo 4, requerimientos:** introducción; RF-03 (camino por defecto, con el comportamiento de la versión 1 como camino `lstm`); RF-21 (criterio de no inferioridad sobre días reales de DEV con el p90 semanal, según 9.2.5); RNF-11; CU-03 (evaluación sobre días reales; rechazo cuando falta la partición); CU-04 (cobertura parcial solo en el camino `lstm`); HU-09.
- **Capítulo 5, diseño:** introducción (motor de *scoring* con el camino por defecto).
- **Capítulo 7, arquitectura:** TensorFlow solo para el camino `lstm`.
- **Capítulo 11, mercado:** descripción del producto (IF + novedad) y la debilidad de la detección (no medida; brecha de dominio), que antes remitía a `sec:benchmark`.
- Se quitaron las anclas provisionales de `pruebas.tex`: ya no quedan referencias a las secciones retiradas.
- Compilación: 279 páginas, sin errores, 7 *warnings* (3 de paquetes y 4 `h` → `ht`, el mismo tipo que en la línea base) y sin referencias indefinidas.
- **Pendientes para el autor:**
  - **Objetivo 2 del capítulo 1:** se reformuló la forma de evaluación para que coincida con la regla de datos reales. Conviene confirmar que la redacción sea aceptable, porque modifica un objetivo declarado.
  - **Capítulo 6, UML:** los diagramas y su texto (l. 50, 60 y 70) siguen mostrando el servicio del LSTM, el *buffer* del LSTM y la "combinación híbrida", y no incluyen la novedad ni Markov. Las figuras no se regeneraron.
  - `e50_diseno_ux.tex` l. 123: la nota «En calibración» se justifica porque la explicación no cubre el LSTM. Hay que verificar en el *dashboard* si la nota sigue vigente.
  - `arquitectura.tex` l. 55 y `chapter01.tex`: las "seis fases" del *pipeline* y "el puntaje híbrido" describen la versión 1.
  - **Resumen y *abstract*:** `summary.tex` y `abstract.tex` contienen el texto de ejemplo de la plantilla y no se incluyen en `main.tex`, así que no hubo nada que revisar.

