# Informe de correcciones E75 — tanda 4

Rama: `correcciones-e75-revision`. Sin push. Solo contenido; sin cambios de preámbulo, estilos, numeración ni paquetes. No se tocaron 1.1.1, 1.2 ni 1.3.

## Cambios aplicados

| ID | Archivo | Estado |
|---|---|---|
| P1-A | chapter04.tex (3.I–3.V, 3.VII, 3.XV), requerimientos.tex (4.I–4.VII), datos.tex (8.I–8.III), producto.tex (9.I, 9.II, 9.IV), pruebas.tex (10.I–10.III, 10.V–10.VII) | Aplicado: 26 líneas `{\small Fuente: …\par}` con el mismo formato que las tablas que ya la tenían. 3.I–3.V remiten a `\ref{sec:estado-del-arte}` (2.2); 8.I cita `\parencite{Landauer2022Dataset}` (Landauer et al., 2022b). Ver excepciones abajo. |
| P1-B | requerimientos.tex (4.3) | Aplicado: "(tablas 4.I a 4.VII)" con `\ref{tab:rf-modulo1}` y `\ref{tab:rf-modulo7}`. |
| P1-C | negocio.tex (12.3) | Aplicado: la frase de los precios pasó al final del párrafo; "Por eso la mayor parte del gasto…" sigue ahora a "…crece con el volumen almacenado.". |
| P1-D | chapter04.tex (3.5) | Aplicado, con la redacción pedida. |
| P1-E | pruebas.tex (10.7, 10.7.6, 10.6.4), chapter04.tex (3.XV), producto.tex (9.2.5, 9.IV) | Aplicado en los seis puntos. Para remitir a 10.7.2 se agregó `\label{sec:benchmark-particion}` a la subsección "Partición y métricas" (no cambia la numeración). |
| P2-A | producto.tex (9.2.2) | Aplicado: "mediante el algoritmo incremental de Welford \parencite*{Welford1962}". La variante con asterisco imprime solo el año en el estilo `iso-authoryear`; el PDF muestra "Welford (1962)". |
| P2-B | negocio.tex (tabla nueva y párrafo en 12.4.4) | Aplicado. Ver detalle abajo. |
| P2-C | chapters/appendix/diagramas_ampliados.tex, annex.tex, e50_uml.tex, chapter01.tex (1.5) | Aplicado en un commit aparte (revertible); ver advertencia abajo. |

Corrección adicional (no pedida): en `chapter04.tex` (3.7, lista de síntesis) la viñeta de "Plataformas EDR/XDR para PyMEs" tenía `\item <tab>extbf{…}` (el `\t` de `\textbf` se había perdido), por lo que el texto salía sin negrita. Restituido a `\textbf{…}`.

## P1-F — umbral del LSTM (pendiente del autor)

No se modificó nada. `images/diagramas/Cargar/05_objetos_evento.tex:110` dice 0.0874; `datos.tex:112` (tabla 8.II) y `pruebas.tex:284` (tabla 10.VII) dicen 0,1180. Se buscó 0.0874 y 0.118x en el repo de código (solo lectura, `.json/.py/.md/.yaml`) y no aparece en ningún archivo, por lo que no se pudo confirmar el valor vigente desde ahí. Hace falta que el autor indique cuál es. Si es 0,1180, se cambia solo el diagrama; si es 0.0874, las tablas no se tocan y conviene aclarar en el epígrafe de la figura 6.10 que el diagrama refleja otro juego de artefactos.

## P2-B — sensibilidad a costo de adquisición y abandono

El modelo existe: `documentacion/e75/modelo_financiero.py`. **Pero está desactualizado respecto del texto**: usa costo de nube de USD 0,60 por equipo (el texto usa 0,10), infraestructura fija de USD 250 por mes (el texto la escalona por equipos) y no incluye el costo de contador y mesa de ayuda. Su escenario base da VAN de USD 35.084, no 83.059. Por eso no se usó tal cual. Se reconstruyó el modelo del texto (nube 0,10; costo fijo = equipo + contador/soporte + infraestructura escalonada según los equipos de cada mes) en un script temporal, que reproduce la tabla 12.VI con una diferencia de USD 5 en el VAN base (83.054 contra 83.059) y de menos de USD 5 en cada flujo anual. Las celdas de la tabla nueva incluyen ese ajuste de USD 5 para que la columna base coincida con la tabla 12.VI.

Resultados (VAN al 25 %, escenario base, un supuesto por vez):

| Costo de adquisición (USD) | 1.000 | 1.500 | 2.500 |
|---|---|---|---|
| VAN (USD) | 130.806 | 83.059 | −13.758 |

| Abandono mensual | 1,5 % | 2 % | 3 % |
|---|---|---|---|
| VAN (USD) | 111.805 | 83.059 | 33.579 |

El VAN base se vuelve negativo con un costo de adquisición de unos USD 2.370 (58 % sobre el supuesto) o con un abandono mensual cercano al 3,8 %.

- Tabla nueva `tab:sensibilidad-cac`, después de la 12.VIII, con fuente "elaboración propia a partir del modelo financiero". **Numeración**: con la numeración automática sale como **12.IX** (no 12.X, como decía la consigna), y el punto de equilibrio pasa de 12.IX a 12.X. Todas las remisiones usan `\ref`, así que no queda ninguna desactualizada.
- Párrafo de dos oraciones en 12.4.4, con esos números.
- **Recomendación**: actualizar `modelo_financiero.py` (parámetros y escalonado de infraestructura) para que reproduzca las tablas 12.IV a 12.IX; no se modificó porque está fuera de la consigna.

## P2-C — Anexo H: Diagramas ampliados

Compila sin errores. Se usan los PDF vectoriales que el documento ya incluye (`images/diagramas/uml/`), recortados con `trim`/`clip`; no hizo falta generar PDF nuevos. Ocho figuras (H.1 a H.8, una por página, mitad izquierda y derecha de las figuras 6.1, 6.2, 6.3 y 6.5), cada una con epígrafe y fuente. Se agregó "Una versión ampliada se presenta en el Anexo H." al párrafo de cada una de las cuatro figuras de la sección 6 y la mención en 1.5. Las figuras originales no se modificaron.

**Advertencia, a decisión del autor**: la mejora de escala es de aproximadamente 1,4 veces (las mitades quedan limitadas por la altura de página, no por el ancho) y el texto de los diagramas queda en torno a 5–6 pt: se lee con zoom y en pantalla, pero es justo en papel. Además, el corte por la mitad geométrica atraviesa algunas cajas y carriles. Si no resulta aceptable, se revierte con `git revert` del commit del anexo, sin afectar el resto. La página con la introducción del anexo queda mayormente vacía porque la primera figura ocupa la página siguiente.

## Excepciones de la verificación de fuentes

Verificación por script sobre las tablas con `\caption` dentro de `table`/`longtable` (ahora 60, con la nueva): 55 con línea de fuente y 5 sin ella. No se completaron porque la consigna pedía listarlas, y la fuente correcta de algunas no es evidente:

| Tabla | Título | Archivo |
|---|---|---|
| 3.VIII | Matriz de capacidades | chapter04.tex |
| 4.VIII | Requerimientos no funcionales | requerimientos.tex |
| 8.IV | Tablas del modelo relacional | datos.tex |
| 10.IX | Resultados de la validación por escenarios (15 usuarios por escenario) | pruebas.tex |
| 10.XVIII | Decisiones tomadas a partir de los resultados de las pruebas | pruebas.tex |

La consigna indicaba que la 3.VIII ya tenía fuente; no la tiene. Sugerencias: "elaboración propia" en 3.VIII, 4.VIII, 8.IV y 10.XVIII, y "elaboración propia a partir de las mediciones del sistema" en 10.IX.

## Pendiente del autor

- P1-F: valor vigente del umbral del LSTM.
- Consentimiento de los entrevistados (final de 3.5.1): no agregado.
- Decidir si se conserva el Anexo H.

## Verificación

- `latexmk -pdf main.tex` compila sin errores ni referencias o citas indefinidas (272 páginas).
- `pdftotext` sobre el PDF: 0 apariciones de `efsec`, `ref{`, `chap:`, `tab:` y `??`. Las de `sec:` y `fig:` son código en los diagramas de clases, no referencias rotas.
- Los finales de línea se conservaron archivo por archivo.
