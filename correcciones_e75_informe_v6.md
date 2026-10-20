# Correcciones E75, tanda 6 (informe v6)

Fuente única de números: `informe_fixes_e75.md` (repo de código, rama `fix/e75-limitaciones-menores`). Rama de trabajo: `correcciones-e75-revision`. Sin push. Preámbulo, estilos y numeración sin tocar.

| Unidad | Estado |
|---|---|
| U1 | Aplicada |
| U2 (C2, C3, C4, C5, C6, C7) | Aplicada |
| U3 | Aplicada (coberturas 94,76 % y 90,20 % ≥ 85 %) |
| U4 | Aplicada |
| U5 | No realizada: la parte B no se hizo en el repo de código y no hay `capturas_e75/` |

## U1. Umbral del LSTM
El valor vigente es 0,1180463… (= 0,1180). Cambiado `lstm_threshold = 0.0874` por `0.1180` en `images/diagramas/Cargar/05_objetos_evento.tex`. La figura 6.x se incluye desde `images/diagramas/uml/05_objetos_evento.pdf`, que era idéntico al PDF de `Cargar/`; se recompiló con `pdflatex` (como indica el encabezado del .tex) y se copió a `uml/`. El texto extraído del PDF nuevo dice `lstm_threshold = 0.1180`.

**Para decidir por el autor.** Según el informe de código (C1), en producción ese umbral no decide nada: solo se carga para el chequeo de presencia de `/health`. La regla de anomalía del LSTM usa el percentil 95 de la referencia por usuario (`LSTM_USER_PERCENTIL_PISO = 95`). El documento ya dice 0,1180 en `datos.tex:113` y en `pruebas.tex:289` (percentil 95 del error de entrenamiento), así que ahora es consistente. No toqué ningún texto que describa la regla de decisión del LSTM; conviene revisar que no afirme que este umbral decide.

## U2. Limitaciones
- **C2** (`producto.tex`): fila de la tabla 9.IV reescrita con el impacto pedido y el tratamiento "Corregido en el código; pendiente de publicar en la instancia." Último párrafo de 9.2.7: el nivel de agente rechaza la clave de administración con 403 en modo estricto y la acepta en el entorno local. En 13.3 se quitó "rechazar la clave de administración en el nivel de los agentes". No toqué la fila "Agente" de la tabla de niveles de autenticación ("Clave individual del agente o clave fija de administración"), porque sigue siendo cierta para la instancia desplegada.
- **C3, C4, C5**: la fila "Defectos menores del agente" queda solo con el mapeo de respaldo. El ítem de 13.3 "Correcciones del agente y del planificador" perdió lo corregido del agente. No había menciones de "se descartan los más recientes" fuera de esa fila; RNF-05 no lo menciona y su estado "Parcial: descarte por vigencia y tope" sigue siendo cierto.
- **C6**: eliminada la fila "Reentrenamiento fallido registrado como en curso". CU-03 (4.5.3) con la oración pedida. En 9.2.5 se agregó que el *pipeline* tiene un tiempo máximo de 4 horas por defecto, configurable con `SCORING_REENTRENAMIENTO_TIMEOUT_SEC`. **Dejé en 13.3 un ítem residual** ("Correcciones del planificador") porque el informe (sección 6) dice que una excepción dentro de `comparar_y_promover`, después de un *pipeline* exitoso, sigue dejando la fila "en curso". Si el autor prefiere no documentarlo, se borra el ítem.
- **C7**: se quitó de 13.3 "hacer que el panel vuelva al inicio de sesión cuando el token vence". No había menciones en 9.5 ni en 5.4.1; el texto de 8 horas de vigencia sigue siendo cierto.

## U3. Números
Antes → después, en `pruebas.tex` (10.2.1, tabla 10.II, tabla 10.III, tabla 10.IV, 10.2.4, 10.11) y `conclusiones.tex` (tabla 13.I, fila 9):

| Dato | Antes | Después |
|---|---|---|
| Pruebas total (API + agente) | 623 (446 + 177) | 659 (476 + 183) |
| Cobertura de líneas API / agente / total | 94,7 / 89,3 / 93,2 | 94,8 / 90,2 / 93,5 |
| Líneas y ramas API / agente / total | 93,5 / 88,1 / 91,9 | 93,5 / 89,1 / 92,2 |
| Sentencias API / agente / total | 2.784 / 1.116 / 3.900 | 2.804 / 1.122 / 3.926 |
| Integración continua (API) | 418 aprobadas, 19 omitidas; 87,03 % | 444 aprobadas, 23 omitidas, 0 fallidas; 87,10 % |

Redondeo a un decimal de 94,76, 90,20, 89,12, 93,45 y 92,21. El 93,45 % del total pasa a 93,5 por redondeo hacia arriba; si se calculó con más decimales y es 93,4x, habría que corregirlo.

**Pendientes por falta de dato en el informe (regla 3):**
1. Las 23 pruebas omitidas en CI: el texto de 10.2.2 decía "16 requieren los modelos entrenados y 3 verifican la paridad". Quité el desglose y dejé "dependen de artefactos que no están versionados, como los modelos entrenados y los de la segunda versión del modelo". Hace falta el desglose de las 23.
2. Columna "Archivos" de la tabla 10.II (39 de la API, 14 del agente): el informe no la trae. El repo de código agregó al menos `agent/tests/test_event_buffer_tope.py`, así que el agente probablemente tiene 15. No lo cambié.
3. El informe de código muestra 467 pruebas de API en la rama de partida contra 446 en el documento; el propio informe lo atribuye a la evaluación controlada y a pruebas anteriores. Los 476 son el valor medido.
4. El informe corrió CI en local con Python 3.12; el pipeline de GitHub Actions no se ejecutó. El documento dice que "el pipeline finaliza con los cuatro trabajos aprobados"; esa frase se refiere a una corrida anterior y no la modifiqué.

## U4. Estado del despliegue (9.3)
Se agregó al final del segundo párrafo: las correcciones del rechazo de la clave de administración en los *endpoints* del agente, de la suspensión de procesos sin registro recuperable, del *buffer* con el *circuit breaker* abierto y con el tope alcanzado, del registro de los reentrenamientos fallidos y de la vuelta del panel al inicio de sesión cuando la sesión vence están implementadas y probadas en el código, pero no forman parte de la release desplegada (b499fa3); hasta la próxima publicación, la instancia sigue aceptando la clave de administración en el envío de eventos y la confirmación de acciones.

## Efectos colaterales del código no reflejados en el documento
- Con el *circuit breaker* abierto, `SESSION_ENDED` también va al *buffer* y se pierde si el agente no vuelve a arrancar antes de las 3 horas de vigencia (informe, sección 6). No lo agregué a ninguna tabla.
- Después de un despliegue, todo lo que mande eventos a la instancia con la clave de administración recibirá 403 (scripts de demostración y ensayos). No está en el documento.
- El estado "fallido" se guarda como prefijo de texto en `variacion_metrica`, no como columna (el esquema no cambió). No se menciona en el documento.

## Verificación
- `latexmk -C` y `latexmk -pdf main.tex` desde cero: sin avisos "Rerun to get", sin referencias ni citas indefinidas. 273 páginas físicas, "Página 271 de 271", igual que en la tanda 5.
- Script sobre el PDF (`pdftotext`): índice 244 entradas, lista de figuras 65 y lista de tablas 60 (mismas cantidades que antes). Todas las páginas coinciden. Las 2 diferencias del índice son la portada del Anexo (sin título propio, como en la tanda 5) y el acento de "Bibliografía" en el texto del `.toc`, y las 15 de la lista de figuras son los pies largos de las figuras del Anexo B contra su título corto: en las tres la página coincide.
- Búsqueda en el texto del PDF de `623`, `446`, `177`, `94,7`, `89,3`, `93,2`, `87,03`, `418` y `0,0874`: sin apariciones.
- `latexmk -C` borra `main.dvi`, que está versionado; se restauró con `git checkout`.
- Archivos de código fuente del documento conservan CRLF.
