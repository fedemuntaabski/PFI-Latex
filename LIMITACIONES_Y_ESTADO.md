# UMBRAL — Limitaciones, dataset y estado real de los requerimientos

Documento de síntesis elaborado a partir de `main.pdf` (283 páginas) y de los fuentes `chapters/*.tex`.

**Convenciones de referencia**
- `archivo:línea` apunta a `chapters/`.
- `p. N` es la página del PDF (no la impresa; el capítulo 4 empieza en la impresa 55 y en la 58 del PDF). En tablas multipágina puede variar en una unidad.

> **Actualización (15/11/2026, rama `revision-modelos-latex`).** Las secciones 1 a 6 describen la memoria anterior a la revisión de modelos (PDF de 283 páginas). Ya no corresponden a la memoria vigente: los escenarios inyectados y el *benchmark* etiquetado (S1–S7, E1–E4), retirados; el criterio de promoción por ROC-AUC; la release `b499fa3`; `historial_scores` sin RLS; las cifras de las pruebas (477 / 190 / 667); y las páginas y líneas citadas. La sección 0 resume las limitaciones vigentes, tomadas de `corregir_en_latex/limitaciones_provisional.md`, y el detalle de los cambios está en `revision_modelos_latex.md`.

---

## 0. Limitaciones vigentes tras la revisión de modelos

Se distinguen las limitaciones de evaluación (qué no se puede afirmar), las de los modelos, las de la arquitectura y la operación, y las decisiones de alcance.

### 0.1 Limitaciones de evaluación
- **Sin *recall* medible en datos del dominio.** CLUE-LDS no trae etiquetas de ataque y LANL 2017 (*host* Windows) tampoco tiene ataques. LANL 2015 se descartó como evidencia, porque contiene una sola intrusión simulada, casi toda desde un mismo *host* (Larroche, 2026). Los escenarios construidos (S1–S7) se retiraron para evaluar solo con datos reales. Solo se miden la FPR, la carga de alertas, la oscilación y la cobertura, y la cobertura no es detección. Para superarlo hace falta un conjunto del dominio con incidentes reales etiquetados.
- **Evaluación sobre día cerrado.** Con el camino por defecto, el 2,66 % de los días tiene algún evento ≥ alto y el 1,29 % termina así al cierre. La evaluación de día cerrado no cubre la oscilación dentro del día.
- **HOLDOUT usado una sola vez, con la versión 1** (IF + LSTM): FPR ≥ alto del 4 % en negativos y del 5 % en la población de prueba. El camino por defecto actual se midió solo sobre DEV (63 usuarios). El LSTM v1 era *in-sample* para 47 de las 57 víctimas de HOLDOUT, por lo que esa medición es optimista para el LSTM.

### 0.2 Limitaciones de los modelos
- **Brecha de dominio nube → *host*** (la más grave): sobre LANL 2017, el IF de CLUE marca el 53,66 % de los días, contra el 4,13 % de un IF entrenado en *host*, y los ordenamientos no se parecen (Spearman −0,15). Requiere telemetría propia del agente.
- **Un solo detector de *score* en el camino por defecto** (IF + novedad de recurso). La novedad solo eleva el nivel por la regla de piso. Sin Markov, ningún detector mira el orden de los eventos y la sustitución de cuenta queda sin cobertura (se recupera con `SCORING_TERCER_MODELO=markov`).
- **Componente de secuencia descartado por falta de evidencia.**
  - LSTM: el 95,4 % de la varianza de su riesgo es entre usuarios y su cambio diario mediano es 0. Permutar los 50 pasos no cambia el ordenamiento (Spearman 0,989), y sin la variable de país queda cerca del azar (ROC-AUC 0,52–0,63).
  - Markov: sí usa el orden (Spearman con la secuencia permutada de 0,30 en CLUE y 0,00 en LANL 2017), pero no hay evidencia admisible de que detecte. Se retiró del camino por defecto por su costo en oscilación (177 de 189 días transitorios).
- **Ubicación dominante en la versión 1:** `n_distinct_countries` (IF) y `country_changed` (LSTM) funcionan como interruptor de ubicación.
- **Arranque en frío:** FPR ≥ alto del 11,43 % en los primeros 3 días (130 usuarios). Sin 3 días de historia en los últimos 90, IF se usa sin calibrar. El período de aprendizaje (primeros 20 eventos) solo atenúa la acción, no el nivel.
- **Zona horaria:** las horas se calculan en UTC (CLUE es de Viena; el agente corre en Argentina). Calcularlas en hora de Viena cambia el 2,48 % de los días de CLUE, sin cambiar la FPR.
- **Parámetros sin barrido de calibración:** la vida media de 3 días parte de un estadístico real. `w_iso`, el nivel de la regla de piso, los umbrales 40/70/90, `W_PERSONAL_MAX = 0,7` y los parámetros de *drift* son puntos de partida razonados.
- **Línea base personal:** sesga hacia percentiles altos con poca historia y no tiene reinicio automático ante *self-poisoning*. En 43 usuarios chicos, el *blend* no mejoró la FPR de forma consistente.

### 0.3 Limitaciones de arquitectura y operación
- **Latencia en la nube:**
  - El p95 es de 3 110 ms (14,9 ms en local): unos 20 viajes secuenciales de unos 124 ms a Redis y PostgreSQL gestionados.
  - En la demostración en la nube, el nivel crítico llega entre 33,8 y 40,3 s y la acción se confirma entre 46,3 y 49,1 s (3 de 3).
  - El correo de notificación corre dentro del *request* y le suma unos 3 s al evento que dispara la acción.
- **Persistencia:** `eventos_crudos` crece sin límite (sin retención ni poda) y el `uid` se guarda sin anonimizar. PostgreSQL es *best-effort*: si no está disponible, se pierde ese historial.
- **Identidad y acceso:**
  - Sin API keys configuradas, la API queda abierta (*fail-open*, pensado para desarrollo); la EC2 corre en modo estricto.
  - El *login* del *dashboard* usa dos usuarios fijos y no limita los intentos.
  - La resolución IAM es síncrona en `POST /eventos`.
- **Agente:** solo Windows; *enforcement* acotado a `DEMO_ROOT`; ruido de procesos mitigado pero no eliminado; sin *heartbeat*; un agente por usuario y por equipo.
- **Reentrenamiento:** el ciclo con su criterio de promoción funcionó de punta a punta en *sandbox* (2 h 30), pero no se ejercitó con un modelo genuinamente nuevo en producción. El criterio exige no inferioridad en la FPR (margen 0,01); no prueba una mejor detección.
- **Integración continua:** desde el 08/11/2026 el *pipeline* de GitHub Actions termina en `startup_failure` (problema de la cuenta o de la configuración, no del código). El trabajo de la API se reprodujo localmente: 508 aprobadas, 30 omitidas, 86 % de cobertura combinada.
- ***Frontend*:** sin suite de pruebas automatizadas.

### 0.4 Decisiones de alcance (no defectos)
- Modelos no supervisados, por falta de datos etiquetados.
- Modelos dentro del proceso de la API.
- Sin alta disponibilidad, TLS mutuo ni *multi-tenant*.
- Sin autenticación real de usuarios finales ni agente multiplataforma.
- Docker queda como referencia; el despliegue usado es el de `infra/` (EC2 + Caddy).

### 0.5 Trabajo futuro sugerido (en orden de impacto)
1. Recolectar telemetría propia de *host* y reentrenar y calibrar IF en ese dominio.
2. Conseguir incidentes etiquetados en el dominio, para tener *recall*.
3. Bajar la latencia en la nube: ubicar la API junto a los datos y sacar la notificación del *request*.
4. Retención de `eventos_crudos`, anonimización del `uid` y límite de intentos en el *login*.

---

## 1. Resumen ejecutivo

1. **El PDF declara los 31 RF como "Implementado"** (`requerimientos.tex:36`, p. 58; `conclusiones.tex:37`, p. 193). Ningún RF figura como "Parcial" ni "No cumplido".
2. Los únicos estados "Parcial" literales son:
   - **RNF-05**, **RNF-09** y **RNF-11** (requerimientos no funcionales);
   - los **objetivos específicos 2 y 6** (`conclusiones.tex:8-38`, p. 191-192).
3. Varios RF tienen **salvedades reales** que el texto deja en otras secciones, en celdas de estado o en la tabla de limitaciones. Este documento las hace explícitas (sección 4). Las más relevantes: RF-21, RF-02, RF-08, RF-26, RF-28, RF-31.
4. **La principal limitación técnica es la capacidad de detección**: el sistema cumple las metas de latencia y de comportamiento del LSTM, pero no las de Isolation Forest, detección ni alertas (`pruebas.tex:305-324`, p. 156).
5. La detección operativa más alta proviene **de la ubicación (país), no del comportamiento** (`pruebas.tex`, p. 163).
6. El dataset (CLUE-LDS) **no tiene etiquetas**, es de **otro dominio** (archivos en la nube vs. telemetría Windows) y la variable país está casi degenerada (99,95 % "desconocido").

| Meta (tab:metas-modelo, p. 156) | Resultado | ¿Cumple? |
|---|---|---|
| Anomalías Isolation Forest 1–3 % | 0,81 % | No |
| Anomalías LSTM 3–7 % | 4,18 % | Sí |
| Detección E4 con umbral 70 ≥ 50 % | 13,3 % (2 de 15) | No |
| Detección promedio 4 escenarios ≥ 33 % | 5,0 % (3 de 60) | No |
| Usuario-días sin inyección en nivel alto/crítico ≤ 10 % | 15,4 % | No |
| Latencia p95 (RNF-01) ≤ 500 ms | 14,9 ms (local) | Sí |

---

## 2. Limitaciones del sistema

### 2.1 Alcance (`chapter01.tex:59-68`, p. 12)
- Agente UEBA solo para **Windows**, con API central, modelo de IA entrenado por el equipo y panel de administración. Orientado a PyMEs de Argentina.
- Análisis de datos personales incluido; **no** la implementación de los procesos organizacionales que la normativa exige a la empresa adoptante (información a empleados, inscripción de la base de datos).
- Fuera de alcance: dimensión "rol" en umbrales (RF-12), cantidad de niveles distinta de cuatro y motores de reglas libres (RF-13); la integración IAM es opcional y viene desactivada por defecto (RF-28).
- Metodología iterativa con dos incrementos y un equipo de dos personas.

### 2.2 Tabla "Limitaciones conocidas del producto" (`producto.tex:193-246`, p. 138-141)

#### Modelo y detección
| Limitación | Impacto | Tratamiento propuesto |
|---|---|---|
| Sensibilidad baja ante ataques de corta duración | Los escenarios inyectados rara vez alcanzan nivel alto y ninguno el crítico | Variables con granularidad menor al día; evaluar con datos etiquetados del dominio del agente |
| El país actúa como interruptor | La ubicación, no el comportamiento, decide la detección operativa de los ataques con país | Regla explícita de ubicación en el motor de decisión |
| Aporte limitado del LSTM | No aprovecha el orden: permutar los 50 eventos no cambia el ordenamiento (Spearman 0,989). El cambio de país explica ~72 % del error de reconstrucción en test. Un puntaje impulsado por el LSTM no identifica la causa. Al cerrar la primera secuencia el puntaje "pasa de golpe" de solo Isolation Forest a combinar ambos | Rediseñar el LSTM o reemplazarlo por un modelo explicable; transición gradual |
| Datos de entrenamiento de otro dominio | Archivos en la nube vs. telemetría Windows. Variables horarias en UTC, no hora local | Reentrenar con telemetría propia; usar hora local |
| Calibración sin datos independientes | Peso, regla de piso y umbrales se calibran sin escenarios etiquetados. La línea base personal tiende a valores altos con poco historial | La recalibración y cinco alternativas de línea base no mejoran la detección; umbrales editables en runtime |

#### Agente local
- **Captura por sondeo:** operaciones que ocurren y se deshacen entre dos consultas se pueden perder; las lecturas de archivos no generan eventos.
- **Alcance de las mitigaciones:** un proceso terminado no se restaura y la acción se reintenta mientras el nivel se mantiene. Sin `SeRestorePrivilege` (privilegios de administrador), la reversión de la denegación de carpeta usa `icacls /remove:d` y pierde las denegaciones que el usuario ya tenía.
- **Alcance de la observación:** solo se observan equipos con agente. Credenciales robadas usadas desde un equipo sin agente no generan telemetría; solo se cubre parcialmente vía IAM.

#### Reentrenamiento
- **Partición del candidato con datos del agente:** el pipeline recalcula el corte temporal y el criterio "rechaza por precaución todo candidato". El LSTM separa entrenamiento y prueba por sorteo de usuarios, que los usuarios nuevos alteran. Consecuencia: *todavía no se ha ejecutado una promoción desde el planificador con un modelo genuinamente nuevo (RF-21)*.
- **Eventos incorporados sin revisión:** riesgo de *drift* inducido por un atacante; el criterio de no inferioridad no protege contra esa contaminación.
- **Márgenes de promoción** (0,02 y 0,01) "del orden de la variación entre semillas": un candidato equivalente al vigente puede rechazarse por azar; el criterio protege contra regresiones grandes pero no distingue diferencias pequeñas (`producto.tex:88`).

#### Autenticación y comunicaciones
- La clave de administración se aceptaba en el nivel de agente. **Corregido en el código pero no publicado** en la instancia (release `b499fa3`, `producto.tex:131`).
- Sin mTLS ni firma de las respuestas del PDP. Una clave robada sirve para reportar eventos del usuario al que está ligada.
- Sin CSP en el dashboard; el token está en `sessionStorage` (un XSS podría leerlo).
- **Microsoft Entra ID** probado solo con respuestas simuladas, sin tenant real. Keycloak sí está validado contra un servidor real.
- Riesgo de inyección de instrucciones en la redacción asistida (Gemini); peor caso: correo engañoso. Tiene controles de entrada y salida (`producto.tex:66-68`, p. 130). La llamada es síncrona y puede demorar la respuesta al agente hasta 6 s.

#### Datos personales
- Los eventos crudos y las alertas de *drift* no se suprimen (conservación/seudonimización incompletas).
- La exportación para reentrenar copia eventos del agente **sin seudonimizar** a un archivo local que no se elimina (`producto.tex:183`).

### 2.3 Modelo de datos y despliegue
- **Sin claves foráneas**: la integridad referencial queda en la aplicación (`datos.tex:224`, p. 124).
- **`historial_scores` sin RLS** ("mejora pendiente"); seis de siete tablas sí lo tienen.
- **Despliegue** (`producto.tex:129-131`, p. 133):
  - CloudFront no está aplicado; el bucket del dashboard no se usa.
  - Publicación manual; instancia apagada fuera de pruebas y demos.
  - La release `b499fa3` **no incluye** estas correcciones: rechazo de la clave de administración, suspensión de procesos sin registro recuperable, buffer con circuit breaker abierto o tope alcanzado, registro de reentrenamientos fallidos, vuelta del panel al login al vencer la sesión.
  - Mientras tanto la instancia sigue aceptando la clave de administración en el envío de eventos y la confirmación de acciones.
  - En la nube el planificador de reentrenamiento está **desactivado** (`producto.tex:92`).
- **Latencia en la nube** (`pruebas.tex:224-229`, p. 152): p95 extremo a extremo **3.110 ms**; causa: ~20 viajes secuenciales de ~124 ms a Redis y PostgreSQL gestionados (API en us-east-2, datos en São Paulo). "La meta de RNF-01 se cumple en el cómputo de la evaluación, pero no de extremo a extremo con la topología actual".

### 2.4 Legal y datos personales (`producto.tex:135-187`, p. 134-137)
- Transferencia internacional a EE. UU. y Brasil: ninguno figura en la lista de países adecuados de la Disposición 60-E/2016; requiere cláusulas contractuales tipo.
- **Sin plazo de conservación definido; supresión incompleta.**
- La cadena de hashes tensiona con la supresión (`producto.tex:171-177`); se propone cerrarla por período.
- Descargo: un falso positivo puede afectar el trabajo legítimo del empleado.

### 2.5 Limitaciones de las pruebas (`pruebas.tex:669-684`, p. 170-171)
- La **prueba de regresión del puntaje no está en verde**: es un script fuera de la suite; 6 diferencias contra el cálculo offline (5 explicadas por componente personal inactivo con cobertura parcial; la sexta sin causa atribuida).
- 23 pruebas se omiten en CI sin modelos entrenados; 4 pruebas que levantan la API completa quedan fuera de CI.
- **Frontend sin pruebas automatizadas**, incluido el indicador de aprendizaje (RF-26).
- Mitigaciones probadas con `icacls` simulado; la ejecución real y la reversión se verifican a mano.
- Sin pruebas automáticas de la cadena de hashes (RNF-09), de concurrencia multiusuario (RNF-14) ni de verificación del certificado TLS en el despliegue.
- Latencia: medición local con Redis en memoria y sin carga concurrente; en la nube también secuencial. No se miden rendimiento/concurrencia en la nube, CPU/memoria de la API, disponibilidad, respaldos ni monitoreo. El consumo del agente se midió con uso normal, sin ráfagas de eventos de archivo.
- **Evaluación sin etiquetas reales**: el benchmark usa escenarios sintéticos (ráfagas uniformes, reubicación lineal) sobre el día cerrado, sin el agregado parcial ni la línea base personal de producción.
- Pocas víctimas (62 DEV, 57 HOLDOUT) e IC de ±0,05 a 0,10 de ROC-AUC. Cifras del LSTM optimistas: 47 de 57 víctimas de HOLDOUT están en su entrenamiento.
- No se mide la tasa de falsos positivos ante cambios legítimos de ubicación (viajes, VPN).
- Escenarios controlados S4–S7: solo DEV y exploratorios. Ventanas S6/S7 agrupadas por víctima (2 víctimas aportan el 62 % de los falsos positivos de S6).
- Resultados con "15 usuarios por escenario, una sola inyección por caso, escenarios diseñados por el propio equipo" (`pruebas.tex:398`): un usuario equivale a 6,7 puntos porcentuales.
- Usabilidad evaluada con heurística del propio equipo (15 problemas: 4 mayores, 5 menores, 6 cosméticos; corregidos los 4 mayores y 2 menores). Abiertos 3 menores: nivel mostrado no se recalcula al cambiar umbrales (comportamiento especificado en RF-12), configuración de reentrenamiento no indica si el modo automático está activo, auditoría en formato técnico (`pruebas.tex:615`, p. 167).

### 2.6 Supuestos y riesgo comercial (`negocio.tex:116-176`, p. 184; `conclusiones.tex:65-67`, p. 193)
- CAC, abandono y velocidad de incorporación son "supuestos del equipo, sin fuente externa ni datos propios".
- Impuesto a las ganancias simplificado al 25 %; prima por riesgo de emprendimiento de 13–14 pp.
- VAN base USD 83.059; **escenario pesimista USD −183.466**. El VAN se vuelve negativo con CAC ≈ USD 2.370 (+58 %) o abandono mensual ≈ 3,8 %. Requiere ≈1,6 % de un segmento de ~10.500 empresas al año 5.
- El plan Enterprise supone completar antes la promoción automática de modelos (`e50_mercado.tex:28`).

---

## 3. Dataset actual

### 3.1 Origen (`datos.tex:6-16`, p. 117)
- **CLUE-LDS** (*Cloud-based User Entity Behavior Analytics Log Data Set*), Landauer 2022.
- Registros **reales** de una plataforma de almacenamiento y colaboración de archivos en la nube, seudonimizados. Julio 2017 – septiembre 2022. Licencia CC BY 4.0.
- 44 tipos de evento. Campos: tipo, marca temporal, ID de usuario y su clase (nombre/IP), parámetros por tipo, ubicación si disponible.
- **Sin etiquetas** de actividad maliciosa → entrenamiento no supervisado; no se pueden calcular accuracy, precisión, recall, F1 ni ROC sobre el dataset (`pruebas.tex:269`).

### 3.2 Real vs. sintético
- Los modelos vigentes se entrenan "exclusivamente con registros reales de CLUE-LDS, sin generar, simular ni aumentar eventos, ni aplicar técnicas de balanceo".
- Lo único creado por el equipo son **escenarios de ataque inyectados** sobre historiales reales, usados solo para validar/evaluar (no para entrenar ni para los percentiles de referencia).
- "Como no se dispone de ataques reales etiquetados, la capacidad de detección aún no se ha validado frente a incidentes reales."

### 3.3 Tamaño y composición (`datos.tex:20-44`, p. 117-118)
Total: **50.522.931 eventos, 920 usuarios** identificados por nombre.

| Categoría | Criterio | Eventos | Usuarios |
|---|---|---|---|
| Válidos | 20 a 500.000 eventos | 8.494.589 | 291 |
| Baja actividad | < 20 eventos | 3.000 | 617 |
| Cuentas de servicio | > 500.000 eventos | 41.879.451 | 12 |
| Identificados por IP | usuario anónimo | 145.891 | — |

- Cuentas de servicio = **83 %** de los eventos; se excluyen (comportamiento automatizado). Los eventos por IP también.
- Entrenamiento efectivo: **8,5 millones de eventos reales de 908 usuarios** (291 válidos + 617 baja actividad), sin etiquetas (`datos.tex:238`).

### 3.4 Variables

**Isolation Forest** (`datos.tex:50-53`) — unidad: par usuario-día UTC; **61.284 pares** de 908 usuarios; 8 variables estandarizadas:
1. cantidad total de eventos;
2. diversidad de tipos de evento;
3. diversidad de países;
4. eventos de archivo (accesos, creaciones, escrituras);
5. eventos de autenticación;
6. hora promedio de actividad;
7. proporción fuera de horario (antes de 7:00 / después de 20:00);
8. entropía de tipos de evento.

**LSTM Autoencoder** (`datos.tex:55-56`) — secuencias de **50 eventos** consecutivos por usuario, sin solapamiento; 8 dimensiones por evento: tipo codificado, hora (sen/cos), día de la semana (sen/cos), tiempo desde el evento anterior, cambio de país, cambio de tipo de evento. 234 de 291 usuarios válidos tienen ≥1 secuencia → **169.737 secuencias**; los 57 restantes tienen < 50 eventos. El 19,6 % de los usuarios del dataset nunca completa una secuencia (cobertura parcial: solo IF, `pruebas.tex:648`).

### 3.5 Particiones y entrenamiento (`datos.tex:60-124`, p. 119-120)

| | Isolation Forest | LSTM Autoencoder |
|---|---|---|
| Estrategia | Temporal, corte 2-ago-2021 (cuantil 0,8) | Por usuario, semilla fija |
| Datos | Train 49.048 pares; test 12.236 pares | Train 70 % (163 usuarios, 111.742 sec.); val 15 % (35, 20.741); test 15 % (36, 37.254) |
| Configuración | 200 árboles, contaminación 0,02 | LSTM 64 y 32 unidades, embedding 8, decodificador simétrico, 67.375 parámetros, Adam, lotes de 128, early stopping |
| Resultado | — | Parada en época 22, pérdida de validación 0,0805 |
| Criterio de anomalía | Por contaminación | Error de reconstrucción > percentil 95 de train (0,1180) |

- Puntaje híbrido: 0,5/0,5, decaimiento con vida media de 3 días, umbrales 40/70/90.
- Solo **15 usuarios** coinciden en los conjuntos de prueba de ambos modelos → limita la comparación conjunta.
- Benchmark: 123 víctimas con ≥5 días activos posteriores al corte (DEV 63→62 válidas; HOLDOUT 60→57), estratificadas por actividad previa.

### 3.6 Sesgos y desbalances
- **Volumen:** 12 cuentas de servicio concentran el 83 % de los eventos y se excluyen.
- **Clases:** no aplica en entrenamiento (no hay clases). En el benchmark la prevalencia de positivos es 0,08–0,09 (= PR-AUC de un clasificador al azar).
- **País degenerado:** 99,95 % de los eventos con país "desconocido" (`datos.tex:167`). La variable casi no varía en entrenamiento y, cuando cambia, domina el error del LSTM (~72 %). Explica que E3 no se detecte.
- **Transferencia de dominio** (`datos.tex:127-169`, p. 120-121): el agente Windows se mapea a tipos CLUE (`file_created`, `file_written`, `file_renamed`, `file_deleted`, `app_enabled`, `app_disabled`, `public_share_accessed` para conexión saliente, `login_successful` al iniciar el agente, `logout_occured` al detenerlo). "Ninguno de los tipos de evento utilizados representa de forma nativa la ejecución de un proceso o una conexión de red". El modelo no considera nombre de proceso, archivo ni destino: detecta variaciones de volumen, diversidad y horarios. El indicador de IP local no se usa; renombrar/borrar archivos no suman a los eventos de archivo de IF.
- **Hora en UTC**, no local.
- **Sesgo por volumen del LSTM:** riesgo correlaciona −0,68 con log(volumen); tiende a marcar usuarios poco activos.
- **Línea base personal con historial escaso:** el 59,5 % de los usuarios no llega a 20 eventos en su primer día (`pruebas.tex:632`).

### 3.7 Datos generados por el equipo (escenarios)
- **Validación por inyección** (`pruebas.tex:334-343`, p. 158): 15 usuarios, semilla fija, 50–4.000 eventos y ≥5 días. E1 exfiltración (30–60 eventos cada 5 s), E2 fuera de horario (2–5 UTC), E3 cambio de país, E4 combinado. Referencia: 650 usuario-días sin inyección.
- **Benchmark etiquetado** (p. 161): S1 toma de cuenta (similar/disímil), S2 exfiltración (k = 2, 5, 10; y solo archivos), S3 fuera de horario; cada uno con y sin país atacante.
- **Controlados adicionales** (p. 164, solo DEV): S4 secuencia inusual, S5 pico corto, S6 control de identidad, S7 control benigno.

### 3.8 Métricas obtenidas

**Sin etiquetas** (p. 155): anomalías IF en test 0,81 % (99/12.236; contaminación fijada 2 %); LSTM 4,18 % (1.558/37.254); error de reconstrucción media 0,1225 / umbral 0,1180; puntaje híbrido mediana 42,0, p95 69,3, p99 82,8; correlación Pearson entre modelos −0,22 (n = 234), −0,41 con los 15 usuarios comunes (p = 0,13); Jaccard de anomalías 0,111.

**Validación por inyección** (p. 158-159): detección atribuible E1 = 0, E2 = 1, E3 = 0, E4 = 2 (ninguno crítico). 15,4 % de los días sin inyección terminan en nivel alto (100/650; 14,3 % con cobertura completa, 21,6 % parcial). Detección atribuible máxima 33,3 %; con umbral 40, el 98,9 % de los días normales lo supera. "En ningún umbral la detección atribuible supera con claridad a la tasa de alertas."

**HOLDOUT** (p. 162-163):
- ROC-AUC híbrido: S1 similar 0,58; S1 disímil 0,68; S2 k=2/5/10: 0,75/0,79/0,80; S2 solo archivos 0,67; S3 0,80.
- IF: S2 0,76–0,88, S3 0,90, S1 0,46–0,62. LSTM: 0,56–0,63 (cerca del azar).
- Recall híbrido (nivel alto o superior): sin país 0,11–0,30; **con país, exfiltración 0,91–0,99**; crítico sin país ≈ 0. FPR en nivel alto 0,04–0,06.
- Conclusión: "la detección operativa más alta del sistema proviene de la ubicación y no del comportamiento".

**Controlados** (p. 165-166): híbrido S4+S5 recall 0,070, precisión 0,275, F1 0,112, especificidad 0,966, ROC-AUC 0,56; S4 ROC-AUC 0,51 (IF 0,49); especificidad S6 0,937 y S7 0,947; LSTM por bloque ROC-AUC 0,68 (S4+S5); PR-AUC 0,19–0,21 y exactitud balanceada 0,50–0,53.

### 3.9 Por qué el dataset es limitado (síntesis)
1. Sin etiquetas: no hay métricas supervisadas ni ataques reales.
2. Dominio distinto (nube de archivos vs. endpoints Windows): mapeo semántico forzado; modelo ciego a proceso, archivo y destino.
3. País degenerado (99,95 % desconocido).
4. Concentración: 83 % de los eventos son de 12 cuentas excluidas; el resto son 291 usuarios válidos más 617 casi vacíos; 19,6 % no llega a 50 eventos.
5. Particiones distintas para IF y LSTM, solo 15 usuarios comunes en test.
6. Evaluación dependiente de escenarios inyectados por el propio equipo.
7. Reentrenamiento con telemetría propia bloqueado hoy por el criterio de promoción (`datos.tex:169`, p. 121).
8. Sin datos del agente real.

---

## 4. Requerimientos funcionales: estado declarado vs. salvedad real

Fuente: `requerimientos.tex`, tablas `tab:rf-modulo1` a `tab:rf-modulo7` (p. 58-63).

### 4.1 Cuáles están "parciales" y por qué
Ningún RF está marcado Parcial. Lo que sí hay son **salvedades** que los dejan en un estado efectivamente parcial o no verificado:

| RF | Estado literal | Por qué es parcial / qué falta |
|---|---|---|
| **RF-21** Promoción de modelo solo si no empeora (ROC-AUC ≥ vigente −0,02; FPR alto ≤ vigente +0,01) | Implementado | El criterio está probado (13 pruebas) pero **nunca se ejecutó desde el planificador con un modelo genuinamente nuevo**: el pipeline recalcula el corte temporal, el LSTM re-sortea usuarios y el criterio "rechaza por precaución todo candidato". Las 3 corridas reales (1 automática, 2 manuales) generaron candidatos rechazados. Origen del objetivo 6 "Parcial" (`producto.tex:251`). |
| **RF-02** Envío autenticado + buffer local | Implementado (ver nota a) | La nota a) citada **no existe** para RF-02 (la única nota a) del documento es del Módulo 4 y habla de RF-31, `requerimientos.tex:143`). Salvedad real: buffer con vigencia de 3 h y tope de 20.000; al superarlos se descartan eventos → **RNF-05 Parcial**; la corrección no está en la release desplegada. |
| **RF-08** Catálogo de 6 acciones | Implementado | Sin prueba automática de la ejecución real; verificada a mano; mitigaciones probadas con `icacls` simulado. |
| **RF-26** Dashboard muestra aprendizaje y progreso | Implementado | Sin prueba automatizada (frontend sin tests); verificado a mano. |
| **RF-28** Adaptador IAM | Implementado; Keycloak validado contra servidor real | **Entra ID solo con respuestas simuladas**, sin tenant real. |
| **RF-31** Redacción asistida con LLM (Gemini) | Implementado (ver nota a) | Servicio opcional con controles de entrada/salida; riesgo de inyección de instrucciones y llamada síncrona (hasta 6 s) siguen abiertos. |
| **RF-11** Reversión de acciones | Implementado; terminación de procesos no reversible (ver RNF-06) | Sin `SeRestorePrivilege`, la reversión pierde denegaciones previas del usuario. |
| **RF-19** Eventos crudos y exportación para reentrenar | Implementado | Exporta sin seudonimizar a un archivo local que no se elimina. |
| **RF-18** Periodicidad de reentrenamiento | Implementado | En la nube el planificador está desactivado. |
| **RF-20** Reentrenamiento aislado por planificador | Implementado | El planificador no verifica si hay eventos nuevos (`requerimientos.tex:310`). |
| **RF-22** Registro de reentrenamientos | Implementado | La corrección de registro de reentrenamientos fallidos no está en la release desplegada. |
| **RF-12 / RF-13** Umbrales editables / 4 niveles | Implementado | Dimensión "rol", otra cantidad de niveles y reglas libres fuera de alcance. Nivel mostrado no se recalcula al cambiar umbrales. |
| **RF-04** Decaimiento (vida media 3 días) | Implementado | Vida media fija; el decaimiento empeora el ordenamiento en ventanas cortas (`pruebas.tex:663`). |
| **RF-06** Regla de piso | Implementado | Calibrada sin etiquetas independientes. |
| **RF-03** Puntaje IF + LSTM | Implementado | Cobertura parcial (solo IF) hasta 50 eventos de tipo conocido; IP y cuentas > 500.000 eventos sin puntaje por diseño. |
| **RF-01** Agente en segundo plano | Implementado | Captura por sondeo; solo primer nivel de carpetas vigiladas. |
| **RF-09** Persistencia | Implementado | `historial_scores` sin RLS. |
| **RF-15** Notificación por correo | Implementado | La demora del servidor de correo puede retrasar la respuesta (`requerimientos.tex:288`). |
| **RF-16** Listado de usuarios | Implementado | Frontend sin pruebas. |
| **RF-17** Auditoría | Implementado | Formato técnico en la vista (menor abierto). |
| **RF-25** Atenuación en aprendizaje | Implementado | La notificación por correo no se atenúa. |
| **RF-27** Transición automática | Implementado | La cobertura puede seguir parcial hasta los 50 eventos. |
| **RF-30** Contexto IAM | Implementado | Solo informativo; no es variable de entrada del modelo. |

Sin salvedades relevantes: RF-05, RF-07, RF-10, RF-14, RF-23, RF-24, RF-29.

### 4.2 Requerimientos no funcionales con estado "Parcial" (`tab:rnf`, p. 63-64)
12 implementados y 3 parciales:

| RNF | Requisito | Razón del estado Parcial |
|---|---|---|
| **RNF-05** Disponibilidad | Buffer acotado (3 h, 20.000 eventos), reintentos, circuit breaker | "Descarte por vigencia y tope": al superar vigencia o tope se pierden eventos. La corrección del buffer con circuit breaker abierto / tope alcanzado no está en la release desplegada. |
| **RNF-09** Integridad y trazabilidad | Hash chain verificable, validación en ingesta | "Cadena verificada manualmente, sin test automatizado ni inmutabilidad; esquema no estricto". Trigger SHA-256 por usuario (+0,042 ms por inserción; 100 % de filas verificadas). |
| **RNF-11** Explicabilidad | Explicar el puntaje | "Cubre Isolation Forest; LSTM sin explicación". Todas las explicaciones provienen de variables de IF; en 7 de 60 casos ninguna supera el umbral. |

Notas de otros RNF: RNF-01 cumple en local (p95 14,9 ms; p99 148,9 ms) pero no extremo a extremo en la nube (3,1 s); RNF-02 CPU media 0,09 %, 33 MB; RNF-14 solo pruebas manuales (en Redis gestionado 3–4 de cada 20 escrituras simultáneas fallan por conflicto y se resuelven con reintentos; 70/70 OK); RNF-15 solo evaluación heurística.

### 4.3 Objetivos específicos parciales (`conclusiones.tex:8-38`, p. 191-192)
"Siete de los nueve objetivos específicos se cumplen y dos se cumplen en forma parcial."
- **Objetivo 2 (detección) — Parcial:** cumple 1 de las 5 metas de comportamiento/detección más la de latencia. Con umbral 70, detección atribuible 0–13,3 % por escenario frente a 15,4 % de días normales en nivel alto. ROC-AUC híbrido HOLDOUT 0,58–0,80.
- **Objetivo 6 (reentrenamiento) — Parcial:** ver RF-21.
- Observaciones adicionales: objetivo 8 (normativa) con plazo de conservación y supresión completa pendientes; objetivo 7 con autenticación mutua por certificado como extensión.

### 4.4 Cobertura de pruebas de los RF (`pruebas.tex:155`, p. 148)
Todos los RF tienen prueba automatizada **salvo RF-08** (ejecución real de acciones) **y RF-26** (indicador de aprendizaje), verificados a mano.

---

## 5. Trabajo futuro priorizado (`conclusiones.tex:71-104`, p. 194)

| # | Línea | Limitación que ataca |
|---|---|---|
| 1 | Capacidad de detección: variables con granularidad < 1 día; regla explícita de ubicación; transición gradual al cerrar la primera secuencia LSTM; revisar componente personal con poco historial | Sensibilidad baja, país como interruptor, línea base personal |
| 2 | Rediseño del LSTM o reemplazo por modelo no secuencial explicable | LSTM sin aporte de orden; RNF-11 |
| 3 | Datos propios: reentrenar con telemetría Windows y evaluar con escenarios etiquetados de ese dominio | Dominio distinto, sin etiquetas |
| 4 | Benchmark con reproducción evento a evento y partición del reentrenamiento por origen del dato | RF-21 / objetivo 6 |
| 5 | Conservación: cierre de la cadena de hashes por período, plazo configurable, seudonimización de la telemetría de reentrenamiento | Legal, RNF-09, RF-19 |
| 6 | Sacar la redacción asistida del procesamiento del evento; enviar variables agregadas; probar contra el servicio real | RF-31 |
| 7 | Pruebas: frontend, hash chain (RNF-09), concurrencia (RNF-14), mitigaciones automatizadas, latencia con Redis gestionado y varios agentes | Sección 2.5 |
| 8 | Seguridad: mTLS, firma de respuestas del PDP, CSP, Entra ID contra tenant real | Sección 2.2, RF-28 |
| 9 | Validación comercial: disposición a pagar y CAC vía MSSP | Sección 2.6 |

---

## 6. Mapa de páginas del PDF

| Tema | Páginas |
|---|---|
| Alcance | 12 |
| RF (módulos 1–7) / RNF | 58-63 / 63-64 |
| Dataset y selección | 117-118 |
| Variables y partición | 118-120 |
| Mapeo del agente | 120-121 |
| Modelo de datos | 124 |
| Estado del despliegue | 133 |
| Datos personales | 134-137 |
| Limitaciones conocidas | 138-141 |
| Latencia en la nube | 152 |
| Métricas sin etiquetas y metas | 155-156 |
| Escenarios inyectados | 158-159 |
| Benchmark | 161-166 |
| Limitaciones de las pruebas | 170-171 |
| Objetivos / trabajo futuro | 191-192 / 194 |
