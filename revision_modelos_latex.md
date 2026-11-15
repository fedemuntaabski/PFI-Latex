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

