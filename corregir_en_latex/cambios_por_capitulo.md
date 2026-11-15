# Cambios a la memoria, capítulo por capítulo

> Base: `main.pdf` del 20/10/2026 (281 páginas) contra el estado del sistema al 14/11/2026 (rama `entrega/limpieza`). Para cada sección se indica qué dice hoy el PDF, qué cambia y un texto propuesto con el mismo registro que el resto de la memoria. Las cifras salen de `revision_modelos.md` y `limitaciones_provisional.md`, en esta misma carpeta. El etiquetado de CLUE DEV se deja aparte, en `etiquetado_aparte.md`, porque todavía no se decidió si se incluye.

---

## 0. Verificaciones previas

- **LANL 2015:** el PDF no lo menciona en ninguna sección ni usa sus cifras. La única mención a un *red team* (pág. ~32) es la cita del estudio de LADOHD en el estado del arte y no tiene relación. No hay nada que retirar.
- **OpTC, Markov, novedad de recurso, LANL 2017, GUIDE:** no aparecen en el PDF. Se agregan donde corresponda (secciones 2, 8 y 10).
- **Escenarios construidos (S1–S7, E1–E4):** aparecen en 8.1, 9.2.5, 9.5, 10.5–10.7, 10.9, 10.10 y 13. Son el cambio principal: se retiraron el 29/10 por la regla de evaluar solo con datos reales.

---

## 1. Capítulo 2: Antecedentes

### 2.1.5 Modelos de inteligencia artificial para detección de anomalías conductuales

**Hoy:** 2.1.5.1 LSTM Autoencoder y 2.1.5.2 Isolation Forest.
**Cambio:** mantener ambas (el LSTM sigue siendo un camino disponible y explica la evolución del diseño) y agregar tres subsecciones.

**2.1.5.3 Detección de novedad por usuario (texto propuesto):**

> La detección de novedad parte de una idea simple: un recurso que el usuario nunca utilizó es, por sí mismo, una señal. En lugar de comparar la actividad del día contra la población, se mantiene para cada usuario el conjunto de recursos que tocó en una ventana reciente (destinos de red, procesos, carpetas) y se cuenta cuántos aparecen por primera vez. Para que el conteo sea comparable entre usuarios, el umbral no se fija a mano: se toma como un cuantil de la distribución poblacional de recursos nuevos por usuario-día, de modo que la proporción esperada de alertas quede acotada. Este enfoque es complementario de los modelos de aislamiento, que detectan días con un volumen u horario atípicos pero no distinguen un acceso nuevo de uno habitual.

**2.1.5.4 Perfiles de transición (cadenas de Markov) (texto propuesto):**

> Una cadena de Markov modela la probabilidad de cada evento en función de los eventos inmediatamente anteriores. Aplicada al comportamiento de un usuario, permite estimar cuán esperable es una secuencia de acciones para esa persona en particular, comparándola con la misma probabilidad estimada sobre la población. A diferencia de un autoencoder de reconstrucción, el modelo usa el orden de los eventos por construcción y su resultado se explica por las transiciones poco frecuentes.

**2.1.5.5 Umbrales por cuantil móvil (texto propuesto, breve):**

> Cuando no se dispone de etiquetas, un umbral fijo no permite controlar la tasa de alertas a medida que cambian los datos. Un umbral por cuantil móvil se recalcula sobre una ventana reciente de puntajes, de forma que la proporción de casos que lo superan se mantenga cerca de un valor objetivo (por ejemplo, el 5 %).

### 2.1.6 Introducción a los datasets

**Cambio:** agregar un párrafo que justifique la regla de evaluar solo con datos reales y la ausencia de escenarios construidos (ver capítulo 10).

---

## 2. Capítulo 3: Análisis comparativo

### 3.3.7 "Isolation Forest + LSTM Autoencoder (proyecto propuesto)"

**Cambio:** renombrar a **"Isolation Forest + novedad de recurso (proyecto propuesto)"** y agregar al final:

> El diseño inicial combinaba Isolation Forest con un LSTM Autoencoder. La revisión de modelos (sección 10.6) mostró que el LSTM no aprovechaba el orden de los eventos y que su riesgo identificaba a la persona más que al comportamiento del día, por lo que el camino por defecto pasó a combinar Isolation Forest con la detección de novedad de recurso. El LSTM se conserva como alternativa configurable.

---

## 3. Capítulo 8: Datos

### 8.1 Conjunto de datos

**Hoy (último párrafo):** "Los únicos datos creados por el equipo corresponden a escenarios de ataque inyectados sobre historiales reales (secciones 10.6 y 10.7)…"
**Reemplazar por:**

> Durante una primera etapa, la detección se estimó con escenarios de ataque construidos sobre historiales reales. Esos escenarios se retiraron al definirse que la evaluación se hace exclusivamente con datos reales (sección 10.6.1): desde entonces, el sistema se evalúa por su tasa de falsos positivos, su estabilidad y su carga de alertas sobre días reales. Como no se dispone de ataques reales etiquetados en el dominio, la capacidad de detección no está medida (sección 10.10).

**Agregar 8.1.1 Conjuntos de datos complementarios** (tabla nueva):

> TABLA 8.Ia: Conjuntos de datos complementarios
>
> | Conjunto | Uso | Motivo |
> |---|---|---|
> | LANL 2017 (equipos Windows, sin ataques) | Tasa de falsos positivos en el dominio de host | Único conjunto real de host disponible |
> | GUIDE (incidentes reales etiquetados) | Validar la acumulación de alertas por cuenta | Pertenece a otro producto; no se usa para entrenar |
> | DARPA OpTC | Piloto de transferencia de dominio | Pocos positivos; prueba de la brecha nube–host |
> | LANL 2015 | Descartado | Una sola intrusión simulada, casi toda desde un mismo equipo (Larroche, 2026) |
>
> Fuente: elaboración propia.

### 8.2 Selección y preparación

**Agregar al final:**

> La clasificación por volumen total resultó imperfecta: con una regla basada en el comportamiento (horas activas por día y proporción de actividad fuera de horario y en fines de semana), 4 de las 12 cuentas de servicio corresponden a personas con actividad intensa y 14 de los 291 usuarios válidos muestran un patrón automatizado. La tasa de falsos positivos en personas es del 5,1 %, frente al 0,9 % en cuentas automatizadas. El pipeline incorpora la clasificación por comportamiento como opción del reentrenamiento (`PFI_CLASIFICACION=comportamiento`); los modelos vigentes mantienen la clasificación por volumen.

### 8.3 Variables y modelos

**Hoy (intro):** "Cada uno de los dos modelos…"
**Reemplazar por:**

> El camino por defecto del sistema combina dos detectores: Isolation Forest, que evalúa la actividad agregada por día, y la detección de novedad de recurso, que registra los recursos que cada usuario utiliza por primera vez. El LSTM Autoencoder y un perfil de transición de Markov se conservan como caminos alternativos, seleccionables por configuración (sección 8.3.5). Esta subsección describe los modelos y presenta la partición de los datos y los parámetros de entrenamiento.

**8.3.3 Partición y parámetros:** reemplazar "correspondiente al cuantil 0,8 de la distribución de fechas" por:

> fijado en el 2 de agosto de 2021 (el cuantil 0,8 de la distribución de fechas al momento del primer entrenamiento), y parametrizable en el reentrenamiento para que los días de evaluación no pasen a formar parte del entrenamiento.

**Agregar después de la tabla 8.II:**

> Sobre el puntaje de Isolation Forest se aplica una calibración por cuantiles: los valores 0,80, 0,95 y 0,99 de la distribución de puntajes en los días reales de entrenamiento se hacen corresponder con la escala de los umbrales, de modo que el nivel medio, el alto y el crítico representen aproximadamente el 20 %, el 5 % y el 1 % de los días. La calibración se aplica cuando el usuario tiene al menos tres días de historia en los últimos 90; antes de ese plazo se usa el puntaje sin calibrar. Para la evaluación, los usuarios se reparten en dos particiones fijas: DEV (63 usuarios), que se usa para el desarrollo y para el criterio de promoción, y HOLDOUT (60 usuarios), reservada para la evaluación final.

**Hoy (párrafo del híbrido):** "Una vez obtenidas las puntuaciones de ambos modelos, se calcula un puntaje híbrido que asigna un peso de 0,5…"
**Reemplazar por:**

> En el camino por defecto, el puntaje del usuario es el de Isolation Forest calibrado, sobre el que se aplica un decaimiento temporal con una vida media de 3 días. Los umbrales predeterminados son 40, 70 y 90. La detección de novedad no modifica el puntaje: cuando el usuario accede a recursos nuevos en una cantidad superior al cuantil poblacional, eleva el nivel a alto por medio de la regla de piso. En la versión 1 (camino `lstm`), el puntaje combina Isolation Forest y el LSTM con igual peso.

**Agregar 8.3.4 Detección de novedad de recurso:**

> La detección de novedad mantiene, para cada usuario, los recursos utilizados en los últimos 90 días: destinos de red, procesos y carpetas, a partir de los parámetros que el agente ya envía con cada evento. Se activa cuando el usuario tiene al menos tres días de historia. Cada día cuenta los recursos que aparecen por primera vez y los compara con el cuantil 0,95 de la distribución poblacional de recursos nuevos por usuario-día, calculado sobre una ventana móvil de 30 días con un mínimo de 50 muestras; al cuantil solo entran los días con actividad sobre recursos. Superar ese valor cuenta como anomalía para la regla de piso. La detección no modifica el puntaje numérico y se explica directamente con el recurso involucrado ("primer acceso a…").

**Agregar 8.3.5 Caminos alternativos:**

> La variable de configuración `SCORING_TERCER_MODELO` permite seleccionar otros dos caminos sin modificar el código. Con el valor `markov`, se suma un perfil de transición por usuario de orden 2, en el que cada símbolo combina el tipo de evento y una franja de 6 horas en hora local, sobre una ventana de 90 días; el puntaje del día es el máximo calibrado entre Isolation Forest y el perfil de Markov. Con el valor `lstm`, el sistema vuelve exactamente a la versión 1. Solo este último camino requiere TensorFlow.

### 8.4 Adaptación de la telemetría del agente

**Hoy (último párrafo):** "…aunque hoy el criterio de promoción rechaza esos reentrenamientos por el corrimiento del corte temporal (sección 9.5)."
**Reemplazar por:**

> El mecanismo de reentrenamiento periódico ya incorpora los eventos crudos recibidos como insumo, con el corte temporal fijo (sección 8.3.3), aunque el reentrenamiento con datos de CLUE-LDS se puede aislar de los del agente (`PFI_ORIGEN_REENTRENAMIENTO=clue`). La medición sobre LANL 2017 cuantifica la brecha: aplicado a telemetría de host, el Isolation Forest entrenado con CLUE-LDS marca el 53,66 % de los días, contra el 4,13 % de un Isolation Forest entrenado en ese dominio (sección 10.6).

### 8.5.1 Modelo relacional

**Hoy:** "La tabla historial_scores constituye una excepción, ya que todavía no cuenta con esta protección…"
**Reemplazar por:** "Las siete tablas tienen activada la seguridad a nivel de fila (Row-Level Security, RLS); la última en incorporarla fue historial_scores, el 29 de octubre de 2026."

---

## 4. Capítulo 9: Producto implementado

### 9.2.2 Motor de scoring

**Reemplazar desde "Cada evento válido se evalúa…" hasta "…superen al menos una desviación estándar." por:**

> Cada evento válido se evalúa con los detectores del camino por defecto. Isolation Forest analiza la actividad diaria del usuario a partir de ocho variables agregadas (sección 8.3.1); su puntaje se calibra por cuantiles cuando el usuario cuenta con al menos tres días de historia. En paralelo, la detección de novedad registra los recursos que el usuario utiliza por primera vez (sección 8.3.4). El puntaje se integra con una línea base personal del usuario, actualizada de manera incremental mediante el algoritmo de Welford (1962), cuya influencia aumenta a medida que se acumula historial. Sobre esta base, el sistema calcula el riesgo acumulado, que disminuye con una vida media de 3 días; el decaimiento se consolida al cierre de cada día y se aplica de forma provisional a los eventos del día en curso. El nivel de riesgo se determina según los umbrales vigentes, con una regla de piso que lo eleva a alto cuando Isolation Forest marca una anomalía o cuando la cantidad de recursos nuevos del día supera el cuantil poblacional. A partir del nivel, se selecciona la acción mediante el mapeo nivel → acción, y se genera una explicación con hasta tres variables de Isolation Forest que presentan las mayores desviaciones respecto de la población de entrenamiento, siempre que superen una desviación estándar. Los caminos alternativos (perfil de Markov o versión 1 con LSTM) se seleccionan por configuración (sección 8.3.5).

### 9.2.5 Reentrenamiento periódico

**Reemplazar desde "Finalizado el entrenamiento, se aplica un criterio…" hasta "…pero no distingue diferencias pequeñas." por:**

> Finalizado el entrenamiento, se aplica un criterio de promoción de no inferioridad sobre los días reales de la partición de desarrollo (DEV), posteriores al corte temporal. El modelo candidato y el vigente se puntúan con el mismo procedimiento, que reproduce el camino por defecto completo (incluida la detección de novedad), sin que HOLDOUT participe en ningún caso. El candidato se promueve solo si cumple las dos condiciones siguientes:
>
> (a) su tasa de falsos positivos en nivel alto o superior sobre los días reales de DEV es, como máximo, la del modelo vigente más 0,01;
>
> (b) el percentil 90 de esa tasa calculada por semana es, como máximo, el del modelo vigente más 0,01.
>
> Si el candidato se promueve, la API recarga los modelos en memoria sin reiniciarse. El candidato tampoco se promueve, y se registra el motivo, cuando falta la definición de la partición, cuando su corte temporal no coincide con el de la partición original (sección 8.3.3) o cuando falla el puntuado. Ante cualquier rechazo se restaura el respaldo.
>
> Este criterio reemplaza a dos anteriores. El primero comparaba la tasa de anomalías de Isolation Forest y el error de reconstrucción del LSTM, magnitudes que no miden la detección. El segundo combinaba la tasa de falsos positivos con el ROC-AUC sobre escenarios construidos, que se retiraron al adoptarse la evaluación exclusiva con datos reales. El margen de 0,01 se fija de antemano y es del orden de la variación entre semillas de entrenamiento: el criterio protege contra regresiones, pero no prueba una mejor detección.

**Reemplazar el párrafo "El criterio está implementado y cuenta con 13 pruebas…" por:**

> El ciclo completo se verificó en un entorno aislado: el reentrenamiento terminó y promovió un candidato en 2 h 30 min (1 h 57 min de pipeline y 32 min de evaluación). Con el camino por defecto vigente, el candidato obtiene una tasa de falsos positivos del 2,95 % contra el 2,66 % del modelo vigente y se promueve. Ese candidato no se llevó a producción. En el despliegue en la nube, el planificador está desactivado.

### 9.3 Estado del despliegue

**Reemplazar el segundo párrafo por:**

> De la infraestructura definida en Terraform, todos los recursos están aplicados salvo CloudFront; el dashboard lo sirve la propia instancia. Las versiones se publican en forma manual y la instancia se mantiene apagada fuera de las pruebas y las demostraciones. Desde el 8 de noviembre de 2026, la instancia ejecuta el camino por defecto de Isolation Forest con detección de novedad; la release vigente (14 de noviembre de 2026) incluye todas las correcciones descritas en esta memoria, entre ellas el rechazo de la clave de administración en los endpoints del agente.

### 9.5 Limitaciones conocidas (tabla 9.IV)

**Cambios en filas existentes:**

- "Sensibilidad baja ante ataques de corta duración": el impacto citaba los escenarios inyectados. Reemplazar por: "No hay recall medible: ningún conjunto de datos del dominio trae ataques etiquetados. Se miden la tasa de falsos positivos, la estabilidad y la carga de alertas (sección 10.6)." Tratamiento: "Recolectar incidentes etiquetados en el dominio del agente."
- "El país actúa como interruptor": aclarar que aplica a la versión 1 (camino `lstm`); en el default, `n_distinct_countries` sigue siendo una de las ocho variables de Isolation Forest.

**Filas nuevas** (detalle en `limitaciones_provisional.md`):

| Limitación | Impacto | Tratamiento |
|---|---|---|
| Brecha de dominio nube → host | El Isolation Forest de CLUE-LDS marca el 53,66 % de los días de host, contra el 4,13 % de uno entrenado en host | Trabajo futuro: telemetría propia y reentrenamiento en el dominio |
| Sustitución de cuenta sin cobertura en el default | Ningún detector del camino por defecto analiza el orden de los eventos | Camino `markov` disponible; trabajo futuro: evidencia de detección |
| Arranque en frío | Tasa de falsos positivos del 11,43 % en los primeros 3 días del usuario | Período de aprendizaje que atenúa la acción |
| Latencia en la nube | Percentil 95 de 3 110 ms por evento | Ubicar la API junto a los servicios de datos |
| `eventos_crudos` sin retención | La tabla crece sin límite | Trabajo futuro: política de retención |

---

## 5. Capítulo 10: Pruebas y resultados

### 10.2.2 Resultados de la ejecución (tabla 10.III)

**Actualizar con las mediciones del 14/11/2026** (re-medidas sobre la rama de entrega):

| Suite | Antes (PDF) | Ahora |
|---|---|---|
| API, suite completa con los modelos entrenados | 477 aprobadas | **547 aprobadas, 0 fallidas, 0 omitidas** |
| API, configuración de integración continua (sin los modelos entrenados) | 445 aprobadas, 23 omitidas | **508 aprobadas, 30 omitidas, 0 fallidas** |
| Agente, suite completa en Windows | 190 aprobadas | **200 aprobadas, 0 fallidas** |
| Frontend, análisis estático y compilación | sin errores; advertencia por tamaño del paquete | sin cambios |

Las omitidas en la configuración de integración continua pasan de 23 a 30: son las pruebas que dependen de artefactos no versionados (modelos entrenados y salidas del benchmark). Para el desglose exacto, correr `pytest -rs` en esa configuración.

### 10.2.3 Integración continua

**Atención:** desde el 08/11/2026, el pipeline de GitHub Actions no llega a arrancar (`startup_failure`) en ninguna rama, incluida la anterior a la limpieza. El archivo del workflow no cambió desde la última corrida exitosa (04/11): es un problema de la cuenta o de la configuración de GitHub Actions, no del código. Antes de afirmar en la memoria que "el pipeline finaliza con los cuatro trabajos aprobados", hay que resolverlo y volver a correrlo. Mientras tanto, el trabajo de la API se reprodujo localmente sobre una copia limpia del repositorio (solo archivos versionados): 508 aprobadas, 30 omitidas y 86 % de cobertura combinada, por encima del umbral de 85 %.

### 10.2.4 Cobertura de código (tabla 10.IV)

**Actualizar** (medido con `scripts/cobertura_local.ps1`, con artefactos):

| Componente | Líneas (antes → ahora) | Combinada líneas + ramas (antes → ahora) |
|---|---|---|
| API | 94,76 % → **95,25 %** | 93,50 % → **93,86 %** |
| Agente | 90,20 % → **91,90 %** | 89,12 % → **91,20 %** |
| Total (ambos componentes) | 93,45 % → **94,40 %** | 92,21 % → **93,17 %** |
| Integración continua, sin artefactos | — | 87,10 % → **86 %** |

### 10.3 Pruebas funcionales de extremo a extremo

- La prueba de la cadena de decisión se re-ejecutó con el camino por defecto actual (14/11): el primer evento queda en medio, el alto se alcanza en el evento 15 y el crítico en el 44, con la acción de terminar procesos y denegar la carpeta y su confirmación registrada. **Las cifras del PDF siguen siendo válidas.**
- El ítem "Reentrenamiento y promoción" dice que la corrida real no promueve "porque el error del LSTM empeora de 0,1155 a 0,1175": esa era la regla anterior. Agregar que, con el criterio actual, el ciclo completo se verificó en un entorno aislado y el candidato se promovió (sección 9.2.5).

### 10.4.2 Latencia en la nube (agregar al final)

> La consulta que alimenta la pantalla principal del dashboard se optimizó después de esta medición. Recorrer las claves de Redis en lotes de 1 000 en lugar de 10 y leer el estado de todos los usuarios en una sola operación redujo el tiempo de recorrido de 2,18 s a 0,12 s, con 388 claves contra el Redis gestionado, y el de lectura de 0,32 s a 0,05 s, con 7 usuarios. En la instancia, la consulta responde en 0,40 s.

### 10.4.3 Verificación del despliegue

**Cambio:** reemplazar "release b499fa3" y las cifras de la suite por la release vigente. La demostración de extremo a extremo sobre la nube con el camino por defecto (8 de noviembre de 2026, 3 de 3 ensayos correctos): el nivel crítico se alcanza entre 33,8 y 40,3 s después de iniciado el ataque y la acción de terminar procesos y denegar la carpeta se confirma entre 46,3 y 49,1 s. Sobre la release del 14 de noviembre se verificó que el servicio queda sano tras la instalación y que el listado de usuarios responde en 0,40 s.

### 10.5 Evaluación del modelo sin etiquetas

**Cambio:** la tabla 10.VII describe la versión 1 (acuerdo entre Isolation Forest y el LSTM). Conservarla como caracterización de la versión 1, anteponiendo: "Las métricas de esta sección corresponden a la versión 1 del modelo (Isolation Forest y LSTM Autoencoder), punto de partida de la revisión de la sección 10.6." En 10.5.2, reemplazar las metas de detección basadas en escenarios por metas de ruido: tasa de falsos positivos en nivel alto ≤ 5 % y estabilidad dentro del día.

### 10.6 y 10.7: reemplazar por completo

Las secciones "10.6 Validación por escenarios inyectados" y "10.7 Evaluación con escenarios etiquetados" (incluida 10.7.6 y las tablas 10.IX a 10.XVII) se reemplazan por las dos secciones siguientes.

#### 10.6 Revisión de modelos con datos reales (texto propuesto)

> **10.6.1 Método.** La revisión partió de cuatro preguntas: si Isolation Forest y el LSTM Autoencoder estaban bien planteados, qué detector convenía agregar, si el reentrenamiento automático funcionaba de punta a punta y cómo obtener métricas con datos reales. Se adoptaron cuatro reglas: evaluar solo con datos reales, retirando todo escenario construido; fijar por escrito los criterios de decisión de cada etapa antes de medir; mantener fija la partición DEV/HOLDOUT, sin usar HOLDOUT para elegir; y ejecutar los experimentos en un entorno aislado, verificando por SHA-256 que los artefactos de producción no cambiaran. Cada cambio en la API se validó con las pruebas automatizadas, la prueba de regresión y la demostración del agente.
>
> **10.6.2 Diagnóstico de la versión 1.** Isolation Forest detecta volumen y horario atípicos frente a la población, que es lo que se espera de él, y se mantiene. El LSTM Autoencoder, en cambio, no cumple su propósito: permutar los 50 eventos de una secuencia no cambia el ordenamiento (correlación de Spearman de 0,989), alrededor del 72 % de su error proviene del indicador de cambio de país, y el 95,4 % de la varianza de su riesgo es entre usuarios, con un cambio diario mediano de 0, de modo que identifica a la persona y no el comportamiento del día. Además, el 19,6 % de los usuarios no completa una secuencia de 50 eventos.
>
> TABLA 10.IX: Evaluación por detector sobre los días reales de DEV
>
> | Detector | Falsos positivos en alto (solo) | Alertas en los 5 usuarios con más alertas | Spearman con la secuencia permutada | Decisión |
> |---|---|---|---|---|
> | Isolation Forest | 15,17 % | 59,9 % | No aplica | Mantener |
> | LSTM Autoencoder | 10,01 % | 68,2 % | 0,989 | Retirar del camino por defecto |
> | Perfil de Markov | 3,10 % | 27,4 % | 0,30 (CLUE-LDS), 0,00 (LANL 2017) | Conservar como alternativa |
>
> Fuente: elaboración propia.
>
> **10.6.3 Evolución del camino por defecto.** La revisión se desarrolló en nueve etapas entre el 28 y el 31 de octubre de 2026. Primero se incorporó un perfil de Markov en línea como reemplazo del LSTM y se corrigió el reentrenamiento (corte fijo, ejecución determinista y de memoria baja). Luego se retiraron los escenarios construidos y se redefinió el criterio de promoción sobre datos reales. El camino por defecto pasó a combinar Isolation Forest, el perfil de Markov y la detección de novedad, y finalmente se retiró el perfil de Markov, cuya regla de piso explicaba la mayor parte de la oscilación del nivel dentro del día (177 de 189 días transitorios). La tabla 10.X resume el efecto de este último cambio.
>
> TABLA 10.X: Efecto del camino por defecto vigente sobre los días reales de DEV
>
> | Medida | Isolation Forest + Markov + novedad | Isolation Forest + novedad |
> |---|---|---|
> | Falsos positivos en nivel alto / percentil 90 semanal | 5,37 % / 8,08 % | 2,66 % / 4,95 % |
> | Días con algún evento en alto / al cierre (51 usuarios) | 14,04 % / 4,95 % | 2,66 % / 1,29 % |
> | Falsos positivos en los primeros 3 días del usuario | 11,43 % | 11,43 % |
>
> Fuente: elaboración propia.
>
> Una reproducción completa de 462 024 eventos reales a través de la API coincidió sin diferencias con la simulación utilizada para estas mediciones.
>
> **10.6.4 Alternativas descartadas.** ECOD resultó redundante con Isolation Forest. Un perfil de Markov poblacional para usuarios nuevos fue inestable (15,06 % de falsos positivos en LANL 2017). La novedad por popularidad del recurso no alcanzó su criterio. La relación proceso padre → hijo fue inestable entre semanas y queda solo como información. Calibrar Isolation Forest también en el arranque en frío bajaba la tasa de falsos positivos al 0 %, pero no se adoptó por el riesgo de ceguera sin etiquetas y porque dejaba la demostración sin nivel crítico. El uso de GPU no se justificó, porque solo lo aprovechaba el LSTM.
>
> **10.6.5 Acumulación de alertas por cuenta.** Sobre GUIDE, un conjunto de incidentes reales etiquetados de otro producto, acumular detectores distintos por cuenta mejora el ordenamiento de los incidentes (PR-AUC de 0,493 contra 0,239; diferencia de +0,254, IC 95 % de +0,038 a +0,382). Es la única cifra confirmatoria de la revisión. El sistema lo incorpora como una cola de atención por cuenta (al menos dos clases de señal en 7 días), que no modifica el nivel ni la acción y queda desactivada por defecto.
>
> **10.6.6 Transferencia al dominio de host.** Sobre LANL 2017, el Isolation Forest entrenado con CLUE-LDS marca el 53,66 % de los días, contra el 4,13 % de un Isolation Forest entrenado en ese dominio, con ordenamientos sin relación (Spearman de −0,15). Es la limitación más grave de los modelos, y su tratamiento requiere telemetría propia del agente (sección 13.3).

#### 10.7 Evaluación del camino por defecto (texto propuesto)

> Sin ataques etiquetados en el dominio, el camino por defecto se evalúa por su ruido y su estabilidad. Sobre los días reales de DEV, la tasa de falsos positivos en nivel alto es del 2,66 %, con un percentil 90 semanal de 4,95 %, y el 1,29 % de los días termina en alto. La versión 1, evaluada una única vez sobre HOLDOUT, había mostrado una tasa del 4 % en los negativos y del 5 % en la población de prueba. Estos valores cumplen la meta de ruido de la sección 10.5.2. No permiten afirmar una capacidad de detección: menos alertas, sin etiquetas, también puede significar menor sensibilidad.

### 10.9 Decisiones tomadas a partir de los resultados (tabla 10.XVIII)

**Agregar filas:**

| Resultado observado | Decisión |
|---|---|
| Los escenarios construidos no representan ataques reales y orientaban las decisiones | Evaluar solo con datos reales y retirar los escenarios S1–S7 |
| El LSTM no usa el orden de los eventos e identifica a la persona | Retirarlo del camino por defecto, conservándolo como alternativa |
| La regla de piso del perfil de Markov explica la oscilación del nivel | Retirar el perfil de Markov del camino por defecto |
| El criterio de promoción no evaluaba la detección de novedad | Puntuar el camino por defecto completo |
| La clasificación por volumen confunde personas y cuentas automatizadas | Clasificación por comportamiento como opción del reentrenamiento |
| La consulta del listado de usuarios crecía con la cantidad de claves en Redis | Recorrido por lotes y lectura conjunta de estados |

### 10.10 Limitaciones de las pruebas

**Cambio:** reemplazar el párrafo de la prueba de regresión (re-ejecutada el 14/11/2026, camino versión 1, que es el que reproduce el cálculo fuera de línea) por:

> La prueba de regresión del puntaje compara el cálculo fuera de línea con el que produce la API al reproducir el historial de tres usuarios. La convergencia con el historial completo queda dentro de la tolerancia (diferencia de 0,31 sobre un máximo de 0,5; antes de corregir el tratamiento de los eventos duplicados era de 16,5). Persisten seis diferencias, todas de un mismo usuario y en días de cobertura parcial (entre 0,06 y 4,47 puntos). Se deben a que el oráculo fuera de línea se generó antes de esa corrección; la API coincide con el cálculo sin duplicados. El oráculo se regenerará en el próximo reentrenamiento. Se declara como limitación conocida y no como prueba superada.

Agregar al final de la sección: "La detección de novedad y el criterio de promoción se evaluaron sobre días reales de CLUE-LDS y LANL 2017, sin ataques etiquetados."

*Nota:* el PDF dice "cinco de un mismo usuario y la sexta de otro, sin causa atribuida". La corrida actual da las seis del mismo usuario, con las mismas fechas y valores que la verificación del 31/10. La causa quedó atribuida al oráculo desactualizado.

---

## 6. Capítulo 13: Conclusiones

### 13.1 (tabla 13.I)

**Cambio:** donde el cumplimiento del objetivo de detección cita los escenarios inyectados, reemplazar por: "Parcial: el ruido y la estabilidad del camino por defecto están medidos con datos reales (2,66 % de falsos positivos en alto); la detección no es medible sin ataques etiquetados del dominio."

### 13.2 Resultados principales

**Reemplazar el segundo párrafo ("El resultado más débil es la capacidad de detección…") por:**

> El resultado más débil sigue siendo la capacidad de detección, que no puede medirse con los datos disponibles: ningún conjunto del dominio incluye ataques etiquetados. La revisión de modelos permitió, sin embargo, reemplazar un componente que no cumplía su propósito (el LSTM Autoencoder) y reducir el ruido de forma medible: la tasa de falsos positivos en nivel alto bajó del 5,37 % al 2,66 % y la oscilación del nivel dentro del día, del 14,04 % al 2,66 %. La medición sobre telemetría de host mostró, además, que el modelo entrenado en la nube no está calibrado para ese dominio, lo que define el principal trabajo futuro.

### 13.3 Trabajo futuro

**Agregar, en este orden:**

1. Recolectar telemetría propia de endpoints y reentrenar y calibrar Isolation Forest en ese dominio.
2. Obtener incidentes etiquetados del dominio para medir la detección.
3. Reducir la latencia en la nube, ubicando la API junto a los servicios de datos y sacando la notificación del procesamiento del evento.
4. Definir la retención de los eventos crudos, la anonimización del identificador de usuario y un límite de intentos en el inicio de sesión.

---

## 7. Anexo nuevo: contenido de la entrega

> **Anexo D: Contenido de la entrega.** La entrega se compone de dos archivos. El primero contiene el código fuente del sistema (agente, API, dashboard, pipeline de entrenamiento, infraestructura y documentación técnica), sin historial de versiones. El segundo contiene los datos derivados y los artefactos necesarios para ejecutar el sistema: los eventos de CLUE-LDS limpios y clasificados por usuario, las variables y escaladores de los modelos, la partición DEV/HOLDOUT y los modelos entrenados con sus referencias de calibración. El conjunto de datos original no se incluye por su tamaño (unos 14 GB); se obtiene de su repositorio público (Landauer et al., 2022b) bajo licencia CC BY 4.0. El archivo `README.md` del código describe cómo ubicar los datos y ejecutar el sistema.
