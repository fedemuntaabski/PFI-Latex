# Plan: actualizar la memoria en LaTeX con la revisión de modelos y el estado de entrega

Repositorio de trabajo: `G:\Latex\PFI-Latex` (remoto `github.com/fedemuntaabski/PFI-Latex`).
Insumos: `G:\pfi\corregir_en_latex\` (cuatro archivos `.md`, descritos abajo).
Repositorio del sistema (solo lectura, para verificar datos): `G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad`, rama `entrega/limpieza`.

---

## 0. Contexto: leer antes de empezar

1. `G:\pfi\corregir_en_latex\cambios_por_capitulo.md` — **la guía principal.** Para cada sección de la memoria dice qué dice hoy, qué cambia y propone texto con el registro de la memoria. Fue escrita contra `main.pdf` del 20/10 (281 páginas); los `.tex` actuales pueden haber cambiado después (el PDF actual tiene 283 páginas). **Siempre comparar contra el `.tex` vigente, no contra el PDF.**
2. `G:\pfi\corregir_en_latex\revision_modelos.md` — qué se revisó entre el 28/10 y el 13/11, con qué método, qué cifras y qué decisiones. Fuente de las secciones nuevas 10.6 y 10.7.
3. `G:\pfi\corregir_en_latex\limitaciones_provisional.md` — limitaciones con cifras. Fuente de la tabla 9.IV y de 10.10.
4. `G:\pfi\corregir_en_latex\etiquetado_aparte.md` — **NO se integra.** Queda fuera de este trabajo hasta que el autor decida si se envía.
5. En el repo de LaTeX: `main.tex` (orden de capítulos), `README.md` (compilación) y `LIMITACIONES_Y_ESTADO.md` (síntesis previa de limitaciones).

**Correspondencia de capítulos con archivos** (`main.tex`, líneas 273–291):

| Capítulo | Archivo |
|---|---|
| 1 Introducción | `chapters/chapter01.tex` |
| 2 Antecedentes | `chapters/chapter02.tex` |
| 3 Análisis comparativo | `chapters/chapter04.tex` |
| 4 Requerimientos | `chapters/e50_requerimientos.tex` |
| 5 Diseño y mockups | `chapters/e50_diseno_ux.tex` |
| 6 Diagramas UML | `chapters/e50_uml.tex` |
| 7 Arquitectura | `chapters/arquitectura.tex` |
| 8 Datos | `chapters/datos.tex` |
| 9 Producto implementado | `chapters/producto.tex` |
| 10 Pruebas y resultados | `chapters/pruebas.tex` |
| 11 Mercado | `chapters/e50_mercado.tex` |
| 12 Negocio | `chapters/negocio.tex` |
| 13 Conclusiones | `chapters/conclusiones.tex` |
| Anexos | `chapters/appendix/` |

---

## 1. Reglas duras

1. **Timer primero.** Lo primero que se hace es crear un recordatorio cada 20 minutos para revisar que el trabajo siga en pie y que el último avance esté commiteado. No se cancela hasta terminar el cierre (sección 5).
2. **Rama nueva.** Trabajar en `revision-modelos-latex`, creada desde la rama actual (`correcciones-e75-revision`). Antes de crearla: no tocar el borrado pendiente de `images/cronograma.jpg` ni el `LIMITACIONES_Y_ESTADO.md` sin versionar; dejarlos como están.
3. **Commit y push tras cada avance importante** (como mínimo, uno por capítulo terminado). Mensajes en español, descriptivos. **Sin trailers `Co-Authored-By`, sin "Generated with" y sin ninguna mención a herramientas de IA** en commits, archivos o textos.
4. **No inventar cifras.** Toda cifra nueva sale de los tres archivos de insumo. Si una cifra del `.tex` no coincide con los insumos y no está cubierta por ellos, no se cambia: se anota en la bitácora (regla 7) como pendiente para el autor.
5. **Mismo registro que la memoria.** Impersonal ("se adopta", "se calcula"), tablas con `\caption` en el formato de las existentes (`TABLA X.Y` + "Fuente: elaboración propia."), referencias cruzadas con `\ref`/`\label` y no con números fijos, números con coma decimal y espacio de miles como en el resto del documento. Revisar cómo están escritas las tablas y las referencias del mismo capítulo antes de agregar una.
6. **Compilar después de cada capítulo** con `pdflatex main`, `biber main` y `pdflatex main` (dos veces si cambian referencias). Sin errores; los *warnings* nuevos de referencias indefinidas se corrigen antes de commitear.
7. **Bitácora.** Crear `revision_modelos_latex.md` en la raíz del repo de LaTeX al empezar y actualizarlo al cerrar cada capítulo: qué se cambió, qué se dejó pendiente y por qué.
8. **No integrar el etiquetado** (`etiquetado_aparte.md`) ni mencionarlo en ninguna sección.
9. **No hay cifras de LANL 2015 en la memoria** (verificado). Si aparece alguna, se retira y se anota en la bitácora.

---

## 2. Preparación

1. `git status` en `G:\Latex\PFI-Latex`; crear la rama `revision-modelos-latex`.
2. Copiar los insumos a una carpeta del repo: `G:\Latex\PFI-Latex\corregir_en_latex\` con `cambios_por_capitulo.md`, `revision_modelos.md` y `limitaciones_provisional.md` (**no** copiar `etiquetado_aparte.md`). Commit: "Insumos de la revisión de modelos para la memoria".
3. Crear la bitácora `revision_modelos_latex.md`.
4. Compilar el estado inicial y anotar en la bitácora la cantidad de páginas y de *warnings*, para comparar al cierre.

---

## 3. Trabajo por capítulo (en este orden)

Seguir `cambios_por_capitulo.md`. Resumen de lo que cubre cada paso:

1. **Capítulo 8, Datos (`datos.tex`).** 8.1 (reemplazar el párrafo de escenarios inyectados y agregar la tabla de datos complementarios), 8.2 (clasificación por comportamiento), 8.3 (introducción nueva, calibración, partición DEV/HOLDOUT, corte fijo, nuevas 8.3.4 Novedad de recurso y 8.3.5 Caminos alternativos), 8.4 (último párrafo con la brecha 53,66 % contra 4,13 %), 8.5.1 (las siete tablas con RLS).
2. **Capítulo 9, Producto (`producto.tex`).** 9.2.2 Motor de scoring, 9.2.5 Reentrenamiento (criterio de promoción nuevo), 9.3 Estado del despliegue, 9.5 tabla de limitaciones (filas modificadas y nuevas).
3. **Capítulo 10, Pruebas (`pruebas.tex`).** Es el cambio más grande:
   - 10.2.2, 10.2.3 y 10.2.4 con las cifras re-medidas el 14/11 (547 / 508 + 30 / 200; cobertura API 95,25 % y 93,86 %, agente 91,90 % y 91,20 %).
   - En 10.2.3, el aviso del CI: **no afirmar que el pipeline finaliza con los cuatro trabajos aprobados.** Usar la redacción que reporta la reproducción local del trabajo de la API y dejar el estado del CI como pendiente en la bitácora.
   - 10.3, 10.4.2 (optimización del listado) y 10.4.3 (release vigente y demo en la nube del 08/11).
   - 10.5: anteponer que describe la versión 1 y cambiar las metas.
   - **Reemplazar por completo 10.6 y 10.7** (escenarios inyectados y etiquetados, con sus tablas y figuras) por las nuevas "10.6 Revisión de modelos con datos reales" y "10.7 Evaluación del camino por defecto". Las tablas y figuras que queden sin uso se borran del `.tex`; si algún archivo de `tables/` o `figures/` queda huérfano, se anota en la bitácora en lugar de borrarlo.
   - 10.9 (filas nuevas) y 10.10 (prueba de regresión y nota final).
4. **Capítulo 2, Antecedentes (`chapter02.tex`).** Nuevas 2.1.5.3, 2.1.5.4 y 2.1.5.5; párrafo en 2.1.6. Agregar a `biblio.bib` la cita de Larroche (2026) solo si el `.tex` la usa; si falta la referencia completa, dejar un `% TODO` y anotarlo.
5. **Capítulo 3, Análisis comparativo (`chapter04.tex`).** 3.3.7: título y párrafo final.
6. **Capítulo 13, Conclusiones (`conclusiones.tex`).** Tabla 13.I, segundo párrafo de 13.2 y lista de 13.3.
7. **Anexo D, Contenido de la entrega** (`chapters/appendix/`): crear siguiendo el formato de los anexos existentes y sumarlo al índice de anexos.
8. **Barrido final de coherencia:** buscar en todos los `.tex` las menciones que quedaron desactualizadas ("LSTM Autoencoder" como componente vigente, "escenarios inyectados", "benchmark de detección", "S1"–"S7", "E1"–"E4", "b499fa3", "477", "445", "190 aprobadas", "94,76", "87,10") y corregirlas según los insumos, o anotarlas si no está claro. El capítulo 1 (objetivos y alcance) y el resumen se revisan con el mismo criterio.

---

## 4. Verificación

1. Compilación limpia: sin errores y sin referencias ni citas indefinidas nuevas.
2. Revisar el PDF resultante en las secciones tocadas: numeración de tablas y figuras continua, índice actualizado y ninguna referencia a secciones retiradas (por ejemplo, "sección 10.7.6").
3. Buscar en el `.tex` las cifras clave y verificar cada una contra los insumos: 2,66 %, 4,95 %, 14,04 %, 1,29 %, 5,37 %, 53,66 %, 4,13 %, 11,43 %, 0,493, 0,239, 547, 508, 200, 95,25 %, 91,90 %.
4. Confirmar con `git grep -i` que ningún archivo del repo de LaTeX menciona herramientas de IA ni "/goal".

---

## 5. Cierre

1. Actualizar `LIMITACIONES_Y_ESTADO.md` del repo de LaTeX con las limitaciones nuevas, tomadas de `limitaciones_provisional.md`.
2. Cerrar la bitácora `revision_modelos_latex.md` con: capítulos tocados, páginas antes y después, pendientes para el autor (estado del CI, cifras no cubiertas por los insumos, archivos huérfanos, decisión sobre el etiquetado).
3. Último commit y push de la rama `revision-modelos-latex`. No hacer merge a ninguna otra rama.
4. Recién entonces cancelar el timer.
