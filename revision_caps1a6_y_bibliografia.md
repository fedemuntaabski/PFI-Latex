# Revisión de los capítulos 1 a 6 y de la bibliografía

**Fecha:** 15/11/2026. **Rama:** `revision-modelos-latex`.
**Alcance:** capítulos 1 a 6 del PDF (`chapter01`, `chapter02`, `chapter04`, `requerimientos`, `e50_diseno_ux`, `e50_uml`), contrastados con el código en `G:/pfi/Agente-...` (commit `0f53d62`) y las entradas de `biblio.bib` que esos capítulos citan.
**No se modificó ningún archivo `.tex` ni `.bib`.** Este documento solo registra hallazgos.

**Cómo leer cada hallazgo:**
- 🔴 **Alta**: error de hecho, una contradicción con el código o una cita que no respalda lo que se afirma. Un evaluador lo puede detectar.
- 🟠 **Media**: una inconsistencia entre capítulos, texto desactualizado de la versión 1 o una afirmación que exagera.
- 🟡 **Baja**: redacción, formato o terminología.
- **[CÓDIGO]**: hay que revisar el código antes de decidir si se corrige el texto o el código.

---

## 0. Resumen de prioridades

| # | Prioridad | Dónde | Hallazgo |
|---|---|---|---|
| 1 | 🔴 [CÓDIGO] | Cap. 1, 2 y 4 (RF-19, HU-09, CU-03) | Con el corte temporal fijo (`2021-08-02`), los eventos del agente (2026) nunca entran al entrenamiento del Isolation Forest. El reentrenamiento "incorpora nuevos comportamientos" solo en el papel. |
| 2 | 🔴 | Cap. 2, marco legal | El art. 71 de la LCT exige poner los controles en conocimiento de la **autoridad de aplicación**, no del trabajador. |
| 3 | 🔴 | Cap. 2 y 3, LADOHD | El acrónimo está mal desarrollado, y el *paper* no menciona el *cold-start*, aunque se le atribuye dos veces (y una más en el cap. 4). |
| 4 | 🔴 | Cap. 2, Artioli2024 | El texto dice "datos reales de actividad de red". El artículo usa clickstream, **CLUE-LDS** y CERT r5.2. Tampoco afirma que una cuenta comprometida sea más riesgosa que una intrusión externa. |
| 5 | 🔴 | `biblio.bib`, Sharma2020 | Los nombres de los autores están mal: son Balaram Sharma y Prabhat Pokharel. No se pudo verificar la cifra del 0,03 %. |
| 6 | 🔴 | Cap. 6, diagrama de objetos | El diagrama es entero de la versión 1 (LSTM, `w_iso = 0,5`, "Score combinado ISO/LSTM") y se presenta como "instancia real". El propio `.tex` dice "valores ilustrativos". |
| 7 | 🟠 | Cap. 3, encuesta | Dice que el modelo "no evalúa el nombre del proceso ni del archivo" y que los procesos no habituales "no se detectan". La detección de novedad del camino por defecto hace justamente eso (proceso vigilado, carpeta, destino). |
| 8 | 🟠 | Cap. 3, lectura de la matriz | "La explicabilidad cubre solo Isolation Forest del *score* híbrido" contradice la matriz misma (IF + novedad) y el RNF-11. |
| 9 | 🟠 | Cap. 4, HU-15 frente a RF-09 y RNF-11 | La HU-15 dice que se persiste la explicación "de cada evento evaluado". Solo se persiste la del último evento del día. |
| 10 | 🟠 | Cap. 4, RF-02 | Remite a una "nota a" que no existe en la tabla del Módulo 1. La única nota a es del RF-31 (modelo de lenguaje). |
| 11 | 🟠 [CÓDIGO] | Cap. 2 (umbral por cuantil móvil) | Se presenta como algo que el proyecto adopta, pero en el código `SCORING_UMBRAL_MOVIL` está apagado por defecto y es solo informativo. Lo que sí usa el cuantil es la novedad, que además necesita al menos 50 usuarios-día para escalar. |
| 12 | 🟠 | Cap. 2, NIST SP 800-207 | El "Punto de Información de Políticas (PIP)" no es un componente formal de SP 800-207 (allí: PE, PA, PEP y fuentes de datos). El término viene de XACML y ABAC. |
| 13 | 🟠 | Cap. 2, soluciones comerciales | No hay ninguna cita para Sentinel, Splunk UBA (incluido el fin de venta), Exabeam, Entra, Okta, Defender ni Wazuh. Algunas limitaciones están desactualizadas (Entra CAE, Okta ITP). |
| 14 | 🟠 | Cap. 4, CU-04 | Cita a Benova2024 por el *cold-start*. Es un artículo sobre logs de servidor web y no se encontró que trate ese tema. |

---

## 1. Capítulo 1 — Introducción (`chapter01.tex`)

### 1.1 Contenido e inconsistencias

- 🔴 **[CÓDIGO] Objetivo 6 y Descripción (l. 77):** "el modelo se reentrena para incorporar nuevos comportamientos de los usuarios". En el código:
  - `scripts/_score_common.py:31`: `CORTE_TEMPORAL = "2021-08-02"`.
  - `Fase4_forest.ipynb`: `train_mask = df_sorted['date'] <= split_date`.
  - `export_clue_combinado.py:79`: los eventos del agente que se conservan son los que tienen `time > FIN_CLUE_LDS` (después de 2022).

  Conclusión: los eventos del agente caen todos en *test* y **no** entrenan el IF. El reentrenamiento vuelve a producir, en la práctica, el mismo modelo de CLUE (salvo efectos menores en referencias o *scalers*). Hay que decidir una de dos:
  - corregir el texto ("el mecanismo existe, pero con el corte fijo los eventos del agente no entran al entrenamiento"), o
  - cambiar el diseño, por ejemplo con un corte relativo o un *pipeline* para el dominio *host*.

  Afecta también al cap. 2 (2.1.7), al cap. 4 (RF-19, CU-03, HU-09) y al cap. 8 (l. 181: "ya incorpora los eventos crudos").
- 🟠 **Objetivo 2:** habla de evaluar "en una partición de desarrollo y un conjunto reservado (*holdout*)". Según la bitácora y el cap. 3, el camino por defecto se evaluó sobre DEV (2,66 %), y HOLDOUT "se usó una vez con la versión 1". Hay que confirmar si existe una cifra de HOLDOUT para el camino por defecto. Si no existe, el objetivo promete más de lo que el cap. 10 entrega.
- 🟠 **Descripción (l. 73):** el agente recolecta "intentos de acceso a sistemas, aplicaciones o recursos de red". El agente emite procesos de una lista vigilada, cambios de archivos, conexiones salientes y `login_successful`/`logout_occured`. No ve intentos de autenticación contra sistemas. Conviene alinear la frase con RF-01.
- 🟡 **Terminología:** "nivel de confianza" (l. 73, 75) y "nivel de riesgo" se usan como si fueran lo mismo. Lo mismo pasa en el cap. 5 (l. 63, 88) y en las tablas del cap. 3. Conviene elegir uno (el sistema calcula **riesgo**).
- 🟡 **Metodología (l. 104-105):** el camino por defecto "exporta ... el perfil de Markov". Es cierto en el código (`reentrenamiento_scheduler.py:292` corre `export_markov_reference.py` siempre). Leído junto a "Markov es un camino alternativo", confunde. Basta con aclarar que se exporta para el camino alternativo.
- 🟡 **Estructura del documento (l. 136-140):** enumera los Anexos A a H, pero `annex.tex` incluye también `contenido_entrega.tex`, que sería el **Anexo I**. Falta mencionarlo.
- 🟡 **Larman2003 (l. 82):** se lo cita como fuente de "proceso iterativo e incremental **guiado por casos de uso**". El artículo de Larman y Basili es una historia del desarrollo iterativo y no trata de casos de uso. Para esa parte sirve más el libro *Applying UML and Patterns* (Larman) o el Proceso Unificado (Jacobson et al.).
- 🟡 **Ansari2025:** IJIREEICE es una revista de bajo impacto. Se usa para una afirmación general ("las soluciones tradicionales han demostrado quedarse limitadas"). Conviene reforzarla o reemplazarla. En `biblio.bib` ya está **Verizon2025 (DBIR)**, que no se cita en ningún lado y es la fuente estándar sobre el uso de credenciales robadas.

---

## 2. Capítulo 2 — Antecedentes (`chapter02.tex`)

### 2.1 Marco teórico

- 🟠 **PIP (l. 21 y 25):** SP 800-207 define el *Policy Engine*, el *Policy Administrator* (que juntos forman el PDP) y el PEP, más "fuentes de datos" (CDM, inteligencia de amenazas, registros de actividad, etc.). El PIP con ese nombre es de XACML y ABAC (SP 800-162, Hu2014) y aparece en la guía práctica SP 1800-35, no en 800-207. Sugerencia: "las fuentes de datos que SP 800-207 describe (en la terminología de XACML, el PIP)" o citar SP 1800-35.
- 🟡 **"siete principios" (l. 19):** correcto. SP 800-207 tiene 7 *tenets*.
- 🔴 **Artioli2024 (l. 14):** "una cuenta comprometida representa un riesgo mayor que una intrusión externa". El artículo no hace esa comparación. Solo dice que los usuarios legítimos con privilegios son un riesgo si se usan de forma inusual. Conviene suavizar la frase o buscar otra fuente (por ejemplo el DBIR).
- 🟠 **Detección de novedad (2.1.5.3) [CÓDIGO]:** la descripción coincide con `novedad_service.py`: ventana de 90 días, cuantil 0,95 de "recursos nuevos por usuario-día" en 30 días. Faltan dos condiciones que cambian el comportamiento en una PyME:
  - se necesitan **3 días previos de historia** por usuario (`MIN_DIAS = 3`);
  - se necesitan **50 muestras poblacionales** en la ventana (`SCORING_NOVEDAD_NIVEL_MIN = 50`). Mientras tanto, `umbral_nuevos` devuelve `None` y **la novedad no eleva el nivel**.

  Con pocos usuarios (la demo, o una PyME en su primer mes), la regla de piso por novedad no se activa. Hay que mencionarlo aquí o en el RF-06.

  Otro detalle: el recurso "proceso" sale solo de `app_enabled` (la lista de aplicaciones vigiladas), no de todos los procesos.
- 🟠 **Umbrales por cuantil móvil (2.1.5.5) [CÓDIGO]:** el texto dice "el proyecto adopta ... el cuantil empírico sobre una ventana móvil". En `umbral_movil_service.py`, el umbral sobre el puntaje está **apagado por defecto** (`SCORING_UMBRAL_MOVIL=1` para activarlo) y es **informativo** ("`nivel_sugerido` no cambia"). Lo único que usa el cuantil móvil en el camino por defecto es el conteo de recursos nuevos. Hay que reformularlo o decidir activarlo.
- 🟢 **Markov (2.1.5.4):** "cadena observable de orden 2" coincide con el código (`prev1/prev2`, con *backoff*).
- 🟡 **Gama2014 (2.1.7.1):** se listan tres tipos de *drift* (gradual, súbito, recurrente). Gama et al. incluyen cuatro: falta el **incremental**.
- 🔴 **Ley de Contrato de Trabajo, art. 71 (l. 160):** el texto dice que los controles "deben ser conocidos por este [el trabajador] (art. 71)". El art. 71 de la LCT dice: *"Los sistemas, en todos los casos, deberán ser puestos en conocimiento de la autoridad de aplicación."* La obligación de informar al trabajador sale de la Ley 25.326 (art. 6) y de la jurisprudencia, no del art. 71. Hay que corregir la cita. El art. 70 (discreción, medios de selección automática) y el art. 72 (la autoridad verifica que no se afecte la dignidad) están bien.
- 🟡 **Art. 70:** el texto omite "destinados a la totalidad del personal", que es parte de la exigencia de "selección automática". Conviene agregarlo.
- 🟡 **DNPDP2016:** hay que confirmar que la Disposición 60-E/2016 siga vigente para las cláusulas tipo. La AAIP dictó normas posteriores sobre transferencia internacional, alineadas con el Convenio 108+. Revisar en InfoLEG.

### 2.2 Estado del arte

- 🟠 **Sin fuentes para las soluciones comerciales:** las subsecciones de Sentinel, Splunk UBA, Exabeam, Entra ID Protection, Okta Adaptive MFA, Defender for Business y Wazuh no tienen ninguna cita ("según la documentación pública del fabricante"). Hay que agregar las referencias `@online` de la documentación oficial, con fecha de consulta.
- 🟠 **Splunk UBA (l. 207):** las fechas son correctas (fin de venta en diciembre de 2025 y fin de soporte el 31/01/2027, según el FAQ y las notas de versión de Splunk), pero **no tienen cita**. Agregar el FAQ de fin de venta de Splunk.
- 🟠 **Limitaciones desactualizadas que el cap. 3 usa como diferenciador:**
  - Entra ID Protection, "no continuo": Entra tiene *Continuous Access Evaluation* (CAE) y riesgo de usuario evaluado fuera del inicio de sesión.
  - Okta, "concentrado en el login": Okta ofrece *Identity Threat Protection* con evaluación continua de la sesión.
  - Sentinel y Exabeam, "explicabilidad ×": Sentinel UEBA muestra *insights* por anomalía (por ejemplo, "primera vez que el usuario..."), y Exabeam muestra líneas de tiempo con las reglas que sumaron puntaje. Una "×" es discutible; "△ (razones por regla, modelos no públicos)" sería más defendible.

  Un evaluador del área puede objetar estas marcas.
- 🔴 **LADOHD (l. 250):** el texto lo desarrolla como "Long-term Anomaly Detection Over Historical Data". El *paper* lo define como **"LSTM-based Anomaly Detector Over High-dimensional Data"**. Además:
  - las cifras son correctas (38,9 millones de eventos, 30 equipos, 20 días, ataque de 4 días, TPR 97,29 %, FPR 0,38 %, 4 alertas del EDR). Ojo: el propio *paper* dice en otra parte "más de 30 máquinas durante 28 días". Conviene citar la versión del resumen;
  - **el *paper* no menciona *cold-start*** (se buscó en el texto completo). La frase "lo que puede afectar su desempeño ... con usuarios nuevos ... conocido como problema de *cold-start*" y la l. 296 ("Un estudio (VillarrealVasquez2021) señala...") le atribuyen algo que el *paper* no dice. Además, el modelo es **por equipo**, no por usuario. La misma atribución está en el cap. 3 (tabla `tab:algo-lstm`) y en el cap. 4 (CU-04).
- 🔴 **Artioli2024 (l. 248):** el texto dice "más de diez algoritmos" (fueron 15, correcto), pero "utilizando conjuntos de datos reales de actividad de red" es incorrecto. Usaron:
  - D1, clickstream de una tienda en línea;
  - D2, **CLUE-LDS**, el mismo conjunto del proyecto (vale la pena decirlo: es un antecedente directo);
  - D3, CERT r5.2, que es sintético.

  Tampoco concluyen que "densidad y jerárquico se adaptan mejor": el mejor algoritmo cambia según el conjunto (en CLUE-LDS ganaron K-means, GMM, BIRCH y FINCH), y destacan K-means y BIRCH por su relación entre rendimiento y escalabilidad. Esto también corrige la tabla `tab:algo-clustering` del cap. 3 ("mayor consumo de recursos en enfoques de densidad"). El *drift* sí aparece en el artículo (sección 7), así que la cita de la l. 300 se sostiene.
- 🟠 **Tian2023HGNN:** el cap. 3 dice "CERT r6.2" y "F1 +8,3 % vs. modelos secuenciales". No se pudo verificar ninguna de las dos cifras, y un registro bibliográfico del mismo título menciona **CERT r4.2**. Hay que revisarlo en el PDF de IEEE Xplore.
- 🟠 **Landauer2023Survey (l. 257 y 309):** es un *survey* de **aprendizaje profundo** para logs. La afirmación "Isolation Forest continúa siendo una alternativa eficiente en escenarios de baja latencia" probablemente no sale de ahí, porque el IF no es un método profundo. Hay que verificarlo o pasar la cita a Liu2008 o AlShehari2023. Pasa lo mismo en el cap. 3 (`tab:algo-revision`).
- 🟠 **NIST SP 800-207A (l. 315):** se cita como evidencia de que "la investigación UEBA ha comenzado a enfocarse en entornos cloud-native". 800-207A es una guía de control de acceso para aplicaciones *cloud-native* (*service mesh*) y no trata de UEBA. Es una atribución forzada.
- 🟠 **Sharma2020 (l. 294):** no se pudo verificar la cifra "menos del 0,03 %". Si sale de CERT, conviene decir que es un conjunto **sintético** con ataques inyectados.
- 🟡 **Shen2024 y Karantzas2021:** consistentes con los resúmenes. Para Karantzas, "la mayoría no fueron bloqueados ni registrados" conviene compararlo con la tabla del artículo: los resultados varían mucho por producto.
- 🟡 **Redundancia:** el RADAC aparece tres veces (2.1.4.3, 2.2.2.1 y 2.2.3.3). La tercera no agrega nada.
- 🟡 **"aislamiento preventivo del proceso" (l. 329):** el catálogo no tiene "aislamiento". Tiene terminar, suspender y denegar carpeta. Lo mismo en el cap. 3 (l. 431).

---

## 3. Capítulo 3 — Análisis comparativo (`chapter04.tex`)

- 🟠 **Lectura de la matriz (l. 224):** "la explicabilidad ... cubre solo el componente Isolation Forest del *score* híbrido" contradice la propia fila del proyecto (IF: 3 variables con mayor *z-score*; novedad: el recurso), el RNF-11 y el cap. 5. Además, "híbrido" es terminología de la versión 1.
- 🟠 **Explicabilidad [CÓDIGO]:** `explainability.py` calcula el *z-score* con el `StandardScaler` ajustado sobre **CLUE-LDS** (usuarios de una nube). En el agente, cada día de *host* se compara con la población de CLUE. Si el IF marca el 53,66 % de los días de *host* (brecha de dominio), las "señales que se desviaron" de un usuario real van a reflejar sobre todo esa brecha. Conviene decirlo en la limitación de la explicación (cap. 5, l. 97).
- 🟠 **Encuesta (l. 484 y 504):** "el modelo no evalúa el nombre del proceso ni del archivo ... los procesos no habituales y los accesos inusuales a archivos se recolectan, pero no se detectan como tales". En el camino por defecto, la novedad sí detecta el **primer acceso** a un proceso vigilado, a una carpeta y a un destino de red. Es texto de la versión 1. Hay que reformularlo: el IF no los evalúa, la novedad sí (a nivel de carpeta, no de archivo, y solo para las aplicaciones vigiladas).
- 🟠 **Tablas sin fuente:** `tab:comp-radac` y las seis tablas de algoritmos (`tab:algo-catboost` a `tab:algo-revision`) no tienen la línea "Fuente: ...". Las demás sí.
- 🟠 **`tab:algo-lstm`:** "Limitación reportada: Cold-start ... por usuario" no está en el *paper* (ver 2.2). Además, los datos son por equipo.
- 🟠 **`tab:algo-clustering`:** la limitación y la "relación con el diseño" se apoyan en una lectura de Artioli que no coincide con el artículo (ver 2.2).
- 🟡 **l. 228:** "muestra que la elección inicial de IF + LSTM no es arbitraria" y después se dice que el LSTM se retiró. Es coherente, pero conviene presentarlo como justificación **del diseño inicial**.
- 🟡 **Perfiles de entrevistados (l. 418):** "Tres de los cinco ... en entornos financieros o regulados": Jacubovich y Peña son del sector financiero. Pita trabaja en un organismo estatal, y que sea "regulado" es discutible. Conviene escribir "financieros o del sector público".
- 🟢 **Encuesta:** los porcentajes son consistentes (55/240 = 23 %; 40 + 35 = 75; 24/39/37; 46/54; 43/23/34). La pregunta de gobernanza suma 101 % por redondeo, lo que es aceptable, pero conviene aclararlo en una nota.
- 🟡 **`tab:algo-proyecto`:** "50 522 931 eventos ... 920 usuarios": hay que verificar que coincida con el cap. 8 y con Landauer2022.

---

## 4. Capítulo 4 — Requerimientos (`requerimientos.tex`)

### 4.1 Contradicciones y errores

- 🟠 **RF-02, "(ver nota a)":** la tabla del Módulo 1 no tiene bloque de notas. La "nota a" del Módulo 4 habla del modelo de lenguaje (RF-31). O falta la nota (por ejemplo, sobre la vigencia y el tope del *buffer*, que son las salvedades del RNF-05), o sobra la remisión.
- 🟠 **HU-15:** "La explicación y el motivo de **cada evento evaluado** deben persistirse en el historial". El RF-09 y el RNF-11 dicen que se persiste **una fila por día** con la explicación del **último evento**. La HU promete más de lo implementado.
- 🟠 **HU-01:** "cada proceso ejecutado o archivo **accedido**". El agente detecta altas, bajas, modificaciones y renombres en el **primer nivel** de las carpetas vigiladas (`collectors.py:146`, `os.scandir`), no lecturas, y solo los procesos de la lista vigilada (`AppAccessCollector`). Hay que alinearla con RF-01.
- 🟠 **HU-09:** "se reentrene automáticamente **con los eventos nuevos**". El CU-03 dice que "el planificador no verifica si se incorporaron eventos nuevos", y con el corte fijo esos eventos no entrenan el IF (hallazgo 1).
- 🟠 **RF-17 y RNF-07 frente al cap. 5:** el cap. 5 muestra que la auditoría registra cambios de "Proveedores de identidad (IAM)", y la pantalla de umbrales tiene una sección IAM. Los RF-17 y RNF-07 enumeran solo umbrales, acciones, notificaciones, reentrenamiento y umbral de aprendizaje. Falta el IAM en la lista, o el RF-28 debería decir que el proveedor se elige desde el panel.
- 🟠 **RF-28 frente al cap. 6:** el RF-28 menciona solo Keycloak. El cap. 6 (l. 80) presenta un adaptador para **Microsoft Entra ID**. En el código existe (`EntraIAMProvider`), pero con el comentario "NO validado en vivo (sin tenant)". El cap. 6 debería decirlo, y el RF-28 podría mencionarlo como "implementado sin validar".
- 🟠 **CU-04, cita Benova2024:** "Comprehensive Analysis and Evaluation of Anomalous User Activity in Web Server Logs" (Sensors, 2024). No se pudo verificar que trate el *cold-start* (MDPI bloqueó la descarga). Por el tema, es probable que esté mal asignada. Hay que revisarla. VillarrealVasquez2021 tampoco respalda el *cold-start* (ver 2.2).
- 🟡 **RF-24 [CÓDIGO]:** "el mismo umbral define la cantidad mínima de eventos a partir de la cual la línea base personal pondera". En `hybrid_service.py:132`, el peso es `min(total/umbral, 1) * 0,7`: crece de forma lineal **desde el primer evento** y llega al máximo (0,7) en el umbral. El umbral no es un mínimo. Hay que corregir el texto o el código. Tampoco se menciona `W_PERSONAL_MAX = 0,7`, que el propio código describe como "default sin evidencia empírica".
- 🟡 **CU-03 (l. 314):** dos oraciones seguidas dicen lo mismo ("Si se produce un fallo ... se restauran los artefactos" y "Si el pipeline falla ... se restauran los artefactos"). Conviene unirlas. El tiempo máximo es de 4 h (`TIMEOUT_PIPELINE_DEFAULT_SEGUNDOS`) y se podría mencionar.
- 🟡 **CU-03 (l. 318):** "modelos cuyo desempeño supere el margen de degradación" debería decir "cuya degradación supere el margen".
- 🟡 **RNF-01:** la medición en la nube da un p95 de 3,1 s, seis veces la meta. El requerimiento se acota a red local, y es correcto, pero conviene que el estado diga "Cumple en red local; no cumple en la nube" en lugar de "Implementado".
- 🟡 **RNF-08 y RF-01:** el agente también emite `login_successful`/`logout_occured` (`collectors.py:67-68`). No está en la lista de metadatos.
- 🟡 **RF-31 dentro del Módulo 4:** queda fuera del orden numérico. No es un error, pero llama la atención.

### 4.2 Valores verificados contra el código (todos coinciden)

| Afirmación | Código |
|---|---|
| Umbrales 40/70/90 | `models/score_hibrido/config_score_hibrido.json` |
| Vida media de 3 días | mismo archivo, `vida_media_dias: 3.0` |
| Piso en "alto" | `regla_piso.nivel_minimo` |
| Mapeo por defecto (alertar ×3, `terminar_y_denegar`) | `config_store.py:183-186` |
| > 500 000 eventos e IP sin puntaje | `coverage.py:19, 27` |
| Aprendizaje: 20 por defecto, rango 1–1000 | `config_store.py:351-353` |
| Caché IAM de 30 min | `iam_service.py:41` (1800 s). Las fallas se cachean 60 s, sin mencionar. |
| Notificaciones cada 10 min | `notifications.py:58` (600 s) |
| *Buffer* de 3 h y 20 000 eventos; *breaker* de 5 min | `agent/config.py:130, 135, 148` |
| Margen de promoción 0,01 (FPR y p90 semanal) | `metricas_service.py:43, 84-85` |
| Eventos sensibles = eventos de archivo | `hybrid_service.py` (`EVENTOS_RECURSO_SENSIBLE`) |
| OTP en Keycloak con alto o crítico | `iam_keycloak/realm-ueba-demo.json` |
| Lista de eventos recientes de 30 | `redis_state.py:475` |

### 4.3 Para revisar en el código (no contradicen el texto, pero llaman la atención)

- **[CÓDIGO] Notificaciones por defecto:** `NOTIF_NIVELES_DEFAULT = {"bajo": False, "medio": True, "alto": False, "critico": False}` (`config_store.py:292`). Por defecto se notifica en **medio** y **no** en crítico. Parece un resto de la demo. El texto no menciona el valor por defecto, pero si alguien lo pregunta, cuesta defenderlo.
- **[CÓDIGO] `.env` local con `SCORING_TERCER_MODELO=markov`:** la EC2 corre `iso`, y `demo/README.md` advierte que hay que sobrescribirlo, pero cualquier medición local hecha sin esa variable usó el camino Markov. Hay que confirmar con qué camino se midieron el RNF-01 (13,7 / 18,2 ms "con el camino por defecto") y las cifras del cap. 10.
- **[CÓDIGO] `config_score_hibrido.json`:** la condición de `regla_piso` sigue describiendo la versión 1 ("is_anomaly_iso OR is_anomaly_lstm_user"). Es solo documentación, pero el *health* o la UI podrían mostrarla.
- **[CÓDIGO] Nombre engañoso:** `tercer_modelo_markov()` devuelve `True` en el camino `iso` (el código lo aclara: "el nombre viene de cuando..."). El cap. 6 (l. 70) dice que `markov_service` "define el camino activo". Es correcto, pero un lector se confunde. Conviene renombrarlo o explicarlo en el cap. 6.

---

## 5. Capítulo 5 — Diseño y mockups (`e50_diseno_ux.tex`)

- 🟠 **Badge de cobertura [CÓDIGO]:** `coverage.py` define "completa" como "completó ≥ 1 *chunk* LSTM". En el camino por defecto el LSTM no se actualiza, así que **todos los usuarios quedan "parcial" para siempre**. El texto lo reconoce para la nota "En calibración" (l. 123), pero la l. 125 sigue diciendo que el *badge* "indica cuándo el puntaje proviene de un solo modelo". En el camino por defecto, eso es siempre. El *badge* y la columna "cobertura" del listado ya no informan nada. Es una deuda de la UI y del código, y conviene declararla.
- 🟡 **"operario" (l. 28) frente a "operador" (cap. 4, actores):** hay que unificar.
- 🟡 **l. 95:** "comportamiento típico aprendido por Isolation Forest". Lo correcto es "la distribución de entrenamiento (media y desvío del escalador)". El IF no aprende un comportamiento típico.
- 🟡 **l. 228:** "el mismo lenguaje de *badges* de estado (OK o *healthy*) que el resto del sistema utiliza para el nivel de riesgo". Los niveles de riesgo no usan "OK/healthy". Hay que reformular: "la misma forma de *badge*".
- 🟡 **l. 184:** "cada subformulario (umbrales, acciones, periodicidad y notificaciones)" omite el umbral de aprendizaje y el IAM, que también tienen su propio guardado.
- 🟡 **Pantalla de estado (l. 210):** lista `lstm_autoencoder` y no menciona los artefactos del camino por defecto (`iso_calibracion.json`). Hay que revisar qué devuelve hoy `/health` y si la captura es anterior a la revisión.
- 🟡 **l. 63 y 88:** "nivel de confianza" (ver cap. 1).

---

## 6. Capítulo 6 — Diagramas UML (`e50_uml.tex` + `images/diagramas/Cargar/*.tex`)

- 🔴 **Diagrama de objetos (`05_objetos_evento.tex`):** es completamente de la versión 1:
  - `LstmState`, `lstm_risk_user = 71.4`, `config.w_iso = 0.5`, `cobertura = "completa"`, `motivo = "Score combinado ISO/LSTM."`;
  - la flecha "0,5·iso + 0,5·lstm + decay, piso";
  - el comentario de la l. 2 dice "coherentes con la configuración vigente: w_iso = 0,5", que ya no es la configuración vigente.

  El capítulo lo presenta como "una instancia real del sistema", y el propio `.tex` dice "valores ilustrativos". Hay que rehacerlo con el camino por defecto (IF calibrado + novedad) o rotularlo como "versión 1, ilustrativo".
- 🟠 **l. 80, Entra ID:** aclarar "implementado, no validado contra un *tenant* real" (ver 4.1).
- 🟡 **l. 70:** explicar que `markov_service` aloja el selector de camino por razones históricas (ver 4.3).
- 🟡 **l. 60:** la descripción del estado coincide con el código (novedad de 90 días y días activos para la calibración; Markov y LSTM solo con su camino; umbral móvil como lista global). Conviene agregar que la calibración del IF exige **3 días previos** (`historia_iso`): sin ellos el puntaje es el IF sin calibrar ("Score 100% ISO: menos de 3 días de historia").
- Hay que revisar también las versiones completas del Anexo H (`04b_clases_api_scoring.tex`, etc.) por restos de `w_iso` o del híbrido. Aquí solo se revisaron las vistas de diseño y el diagrama de objetos.

---

## 7. Bibliografía

### 7.1 Método

- Se consultaron los metadatos de **31 DOI** en Crossref, comparando título, autores, año, volumen y páginas.
- Para los artículos clave se verificó el contenido de la afirmación leyendo el texto (LADOHD, Aliyu, Artioli) o buscando en la web (Splunk, PIP, Tian, Sharma).
- Las normas argentinas se contrastaron con el texto conocido de las leyes. InfoLEG no respondió durante la revisión, así que **conviene volver a abrirlas** para confirmar los números del Boletín Oficial.

### 7.2 Errores en las entradas

| Clave | Problema | Corrección sugerida |
|---|---|---|
| **Sharma2020** | 🔴 Autores incorrectos: "Bimal Sharma" y "Pradip Pokharel". Faltan las páginas. | `Sharma, Balaram and Pokharel, Prabhat and Joshi, Basanta`; `pages = {1--9}` |
| **Rashid2016HMM** | Faltan las páginas | `pages = {47--56}` |
| **Ho2021Hopper** | Faltan las páginas y la URL o el ISBN | USENIX Security 2021, pp. 3093–3110 (verificar) |
| **Shen2024** | Falta el DOI de ACM (solo tiene arXiv) | Agregar el DOI de ASIA CCS '24 |
| **Kim2018Markov** | Crossref no trae autores ni páginas; las páginas 1887–1898 no se pudieron confirmar | Verificar en el sitio de KSII TIIS |
| **Tian2023HGNN** | El *booktitle* omite "22nd" | `2023 IEEE 22nd International Conference on Trust, Security and Privacy...` |
| **Larman2003** | Correcta (Crossref muestra el título con una errata del editor) | — |
| **Hariri2019 / Glockler2023 / VillarrealVasquez2021** | La clave tiene un año distinto del año de la entrada (2021, 2024 y 2023). No es un error del PDF, pero confunde. | Opcional |
| **MDZ2026RiesgoPais / MENDEZ2026RiesgoPais** | Es la misma nota duplicada. Se cita MDZ, que no tiene autor. | Usar la versión con autora (Méndez) y borrar la otra |

Correctas según Crossref: Ansari2025, Rose2020, AlShehari2023, Artioli2024, Xiao2022, Atlam2025, Bagui2025, Kuppa2022, Glockler2023, Kuhn2010, Hu2014, NIST2023_800207A, Landauer2023Survey, VillarrealVasquez2021, Tian2023HGNN (salvo el *booktitle*), Hariri2019, Stylios2023, Wu2021GNN, Karantzas2021, Liu2008, Hochreiter1997, Gama2014, Welford1962, Rescorla2018, Haber1991, Siffer2017SPOT y Benova2024 (en cuanto a metadatos).

### 7.3 Citas que no respaldan lo que se afirma

| Clave | Afirmación en la tesis | Qué dice la fuente | Gravedad |
|---|---|---|---|
| VillarrealVasquez2021 | *Cold-start* como limitación (cap. 2 ×2, cap. 3, cap. 4) | El *paper* no lo menciona. El modelo es por equipo. | 🔴 |
| VillarrealVasquez2021 | "LADOHD (Long-term Anomaly Detection Over Historical Data)" | "LSTM-based Anomaly Detector Over High-dimensional Data" | 🔴 |
| Artioli2024 | "datos reales de actividad de red"; "densidad y jerárquico se adaptan mejor"; "cuenta comprometida más riesgosa que intrusión externa" | Clickstream + CLUE-LDS + CERT r5.2; no hay un ganador único (K-means/BIRCH destacan); no hace esa comparación | 🔴 |
| Ley20744 | Art. 71 = conocimiento del trabajador | Art. 71 = conocimiento de la autoridad de aplicación | 🔴 |
| Benova2024 | *Cold-start* (CU-04) | Logs de servidor web; tema no verificado | 🟠 |
| Landauer2023Survey | IF eficiente en baja latencia; XAI | *Survey* de *deep learning*; no es la fuente natural para el IF | 🟠 |
| NIST2023_800207A | La investigación UEBA se mueve a la nube | Guía de control de acceso *cloud-native*; no trata de UEBA | 🟠 |
| Rose2020 | PIP como componente de 800-207 | 800-207 no usa ese término como componente | 🟠 |
| Tian2023HGNN | CERT r6.2; F1 +8,3 % | No verificado; hay indicios de CERT r4.2 | 🟠 |
| Sharma2020 | Anomalías < 0,03 % | No verificado | 🟡 |
| Larman2003 | Proceso guiado por casos de uso | Historia del desarrollo iterativo, sin casos de uso | 🟡 |
| Aliyu2024 | Cifras de *recall*, F1 y precisión; CatBoost; MAN-SVMDT | ✅ Coinciden (*abstract* y tabla 2). Detalle: la política es de *Chinese Wall*, y "entornos con restricciones de latencia" es una inferencia (*edge*), no una medición. | ✅ |
| Gama2014 | Tres tipos de *drift* | Cuatro (falta el incremental) | 🟡 |

### 7.4 Entradas en `biblio.bib` que no cita ningún capítulo

Elbasheer2025, Fahrmann2022, Hamarsheh2025, Hanif2024, Hassan2025, JNSM2025, Kent2015, Mangla2025, MENDEZ2026RiesgoPais, Mohammed2023, Parimalla2025, SAJS2025 y Verizon2025.

Con biblatex no se imprimen (no hay `\nocite`), así que no afectan al PDF. Dos aclaraciones:
- **Mohammed2023** tiene la clave equivocada (los autores son Almansoori y Telek), y el apóstrofo de `Mikl{'o}s` está mal escapado: debería ser `Mikl{\'o}s`.
- **SAJS2025** tiene como autor el nombre de la revista.

Si se reactivan, hay que arreglarlas. **Verizon2025** sería útil en los caps. 1 y 2.

---

## 8. Cómo proceder (orden sugerido)

1. **Decidir lo del corte temporal (hallazgo 1).** Es lo único que cambia el sentido de un objetivo. Hay que definir si se corrige el texto ("el reentrenamiento con el corte fijo no incorpora la telemetría del agente; queda como trabajo futuro") o el código. El resto del texto sobre reentrenamiento depende de esta decisión.
2. **Corregir los errores de fuente que un evaluador puede comprobar**: art. 71 de la LCT, acrónimo LADOHD, *cold-start* atribuido a VillarrealVasquez y Benova, descripción de Artioli, autores de Sharma2020. Son cambios chicos de texto o del `.bib`.
3. **Barrer los restos de la versión 1** en los caps. 3, 5 y 6: lectura de la matriz (l. 224), procesos y archivos "no detectados" (l. 484 y 504), *badge* de cobertura, diagrama de objetos.
4. **Alinear los requerimientos**: HU-01, HU-09 y HU-15 con RF-01, RF-09 y RF-19; la nota a del RF-02; el IAM en RF-17 y RNF-07; Entra "no validado".
5. **Agregar las fuentes faltantes**: documentación oficial de las soluciones comerciales, FAQ de fin de venta de Splunk UBA, Verizon DBIR. Revisar Tian2023 y Landauer2023Survey en el texto completo.
6. **Revisar en el código**: notificaciones por defecto en "medio", mediciones locales hechas con el `.env` en `markov`, peso de la línea base personal frente al RF-24, mínimo de 50 muestras de la novedad.

---

## 9. Estado de aplicación (rama `revision-caps1a6-bibliografia`, commit `b54a8d1`)

El repositorio del código no se modificó (sigue en `0f53d62`, sin cambios). Compilación: 0 errores, 279 páginas. El aviso genérico "There were undefined references" ya estaba en `HEAD`, y todas las etiquetas agregadas están definidas.

| Hallazgo | Estado | Dónde se aplicó |
|---|---|---|
| 1. Corte temporal fijo y reentrenamiento | ✅ Aplicado en el texto, como limitación. El código no se tocó. | Cap. 1 (Descripción), RF-19 + nota a, CU-03, HU-09, cap. 8 l. 181 |
| 2. Art. 71 de la LCT | ✅ | Cap. 2, marco legal (se agregó también "totalidad del personal" al art. 70 y el art. 6 de la Ley 25.326) |
| 3. LADOHD: acrónimo y *cold-start* | ✅ | Cap. 2 (2 lugares), cap. 3 `tab:algo-lstm`, cap. 4 CU-04 |
| 4. Artioli2024 | ✅ | Cap. 2 (punto ciego, UEBA con ML, *cloud-native*), cap. 3 `tab:algo-clustering` |
| 5. Autores de Sharma2020 | ✅ Corregidos. La cifra del 0,03 % se quitó porque no se pudo verificar. | `biblio.bib`, cap. 2 |
| 6. Diagrama de objetos de la versión 1 | ⚠️ Parcial: se cambiaron el rótulo, el texto y el comentario del `.tex`. El diagrama no se rehízo. | Cap. 6, `05_objetos_evento.tex` |
| 7. Novedad frente a procesos y archivos en la encuesta | ✅ | Cap. 3 (2 lugares) |
| 8. Lectura de la matriz | ✅ | Cap. 3 |
| 9. HU-15 | ✅ | Cap. 4 |
| 10. Nota a del RF-02 | ✅ (remite al RNF-05) | Cap. 4 |
| 11. Umbral por cuantil móvil y condiciones de la novedad | ✅ | Cap. 2, RF-06 |
| 12. PIP en SP 800-207 | ✅ (atribuido a ABAC, Hu2014) | Cap. 2 |
| 13. Soluciones comerciales | ⚠️ Parcial: se agregaron la cita de Splunk, CAE de Entra, Identity Threat Protection de Okta y nuevas marcas en la matriz. Falta la documentación oficial de los demás productos. | Cap. 2, cap. 3 |
| 14. Benova2024 en el CU-04 | ✅ Cita retirada | Cap. 4 |
| Tian2023: CERT r6.2 y F1 +8,3 % | ✅ Cifras sin verificar quitadas; falta revisar el PDF | Cap. 3 |
| Landauer2023Survey: IF y baja latencia | ✅ Cita pasada a Liu2008 | Cap. 2, cap. 3 |
| NIST 800-207A | ✅ Afirmación reformulada | Cap. 2 |
| Gama2014: tipos de *drift* | ✅ | Cap. 2 |
| Larman2003 | ✅ Frase reformulada | Cap. 1 |
| Terminología (riesgo/confianza, operador, aislamiento) | ✅ | Caps. 1, 2, 3, 5 |
| RF-17, RNF-07 (IAM), RF-28 y cap. 6 (Entra sin validar) | ✅ | Caps. 4 y 6 |
| RF-24 (peso de la línea base), RNF-01, RNF-08, CU-03 duplicado | ✅ | Cap. 4 |
| Cap. 5: *badge* de cobertura, *z-score*, PUT de los subformularios, *badges* de salud | ✅ | Cap. 5 |
| Cap. 6: calibración con 3 días y `markov_service` | ✅ | Cap. 6 |
| `.bib`: páginas, *booktitle*, escape, duplicado MDZ, Splunk | ✅ | `biblio.bib`, `negocio.tex` |
| Objetivo 2 (*holdout*) y Anexo I | ✅ | Cap. 1 |
| §4.3 Revisiones de código (notificaciones en "medio", `.env` en `markov`, etc.) | ⏸️ No aplicado: requiere cambios en el código o mediciones, fuera de alcance | — |
| Normas argentinas (números del Boletín Oficial, vigencia de 60-E/2016) | ⏸️ Pendiente de verificar en InfoLEG | — |
