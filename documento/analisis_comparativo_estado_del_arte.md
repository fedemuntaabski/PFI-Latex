# Análisis Comparativo del Estado del Arte

## Comparación general de alternativas

Incluye las cuatro soluciones comerciales relevadas, la tecnología de autenticación adaptativa (Okta, tratada aparte porque no es UEBA de sesión completa sino un enfoque relacionado) y el modelo académico más cercano conceptualmente al proyecto (RADAC / ad-RACs), contra el proyecto propuesto. Cada alternativa se compara en cinco dimensiones: Tipo, Funcionalidad principal, Tecnología / IA, Alcance de monitoreo y Diferenciador del proyecto propuesto.

### Microsoft Sentinel UEBA

| Campo | Detalle |
|---|---|
| Tipo | SIEM + UEBA integrado (nube, ecosistema Microsoft) |
| Funcionalidad principal | Perfiles de comportamiento de usuarios y entidades (servidores, dispositivos de red) a partir de historial; calcula puntajes de riesgo por desviación de línea base |
| Tecnología / IA | Algoritmos propietarios no publicados; ingesta de logs de autenticación, red, dispositivos y servicios integrados |
| Alcance de monitoreo | Amplio (no se limita a usuarios individuales) pero centralizado en la nube, sin agente propio en el endpoint |
| Diferenciador del proyecto propuesto | El proyecto ejecuta la mitigación en el propio endpoint en tiempo casi real; su lógica de *scoring* (IsolationForest + LSTM) es propia y auditable, no una caja negra propietaria de costo variable por volumen de datos |

### Splunk UBA

| Campo | Detalle |
|---|---|
| Tipo | Plataforma UEBA especializada en *insider threats* y movimiento lateral |
| Funcionalidad principal | Perfiles de comportamiento + correlación de eventos entre sistemas y momentos distintos; prioriza alertas por riesgo |
| Tecnología / IA | Motor de correlación propietario; ingesta multi-fuente (autenticación, red, logs de sistema, accesos a recursos) |
| Alcance de monitoreo | Centralizado, depende de integración con fuentes externas; sin agente propio de recolección |
| Diferenciador del proyecto propuesto | Splunk UBA no incorpora de forma nativa mecanismos de respuesta adaptativa: se detiene en detectar y priorizar. El proyecto cierra el ciclo completo detección, decisión, acción, sin depender de integraciones externas |

### Exabeam

| Campo | Detalle |
|---|---|
| Tipo | SIEM + UEBA + SOAR combinado |
| Funcionalidad principal | Perfiles de comportamiento, correlación multi-fuente, asignación de riesgo a usuarios/dispositivos/actividades, con automatización de respuesta |
| Tecnología / IA | No transparente (funcionamiento interno de los modelos no público); depende de fuentes de datos ya existentes en la infraestructura |
| Alcance de monitoreo | Es el más cercano en concepto (incluye SOAR), pero no incorpora un agente ligero propio para recolección directa en el endpoint |
| Diferenciador del proyecto propuesto | El proyecto no depende de orquestar herramientas externas ya integradas para actuar: el propio agente PEP ejecuta la mitigación directamente sobre el proceso/carpeta del endpoint |

### Microsoft Entra ID Protection

| Campo | Detalle |
|---|---|
| Tipo | Protección de identidad (IAM) |
| Funcionalidad principal | Evaluación continua de señales de riesgo ligadas al usuario y al proceso de autenticación; aplica políticas de acceso condicional |
| Tecnología / IA | Señales propias del ecosistema Microsoft (ubicación, dispositivo, credenciales filtradas) |
| Alcance de monitoreo | Fuertemente atado al ecosistema Microsoft; enfocado en identidad, no en comportamiento operativo continuo durante el uso de recursos (limitación citada textualmente en la fuente) |
| Diferenciador del proyecto propuesto | El proyecto evalúa comportamiento durante toda la sesión activa, no solo señales de autenticación, y no depende de estar dentro del ecosistema de un proveedor de identidad específico |

### Okta Adaptive MFA

| Campo | Detalle |
|---|---|
| Tipo | Autenticación adaptativa basada en riesgo (no es UEBA de sesión completa) |
| Funcionalidad principal | Estima riesgo en el momento del *login* a partir de señales contextuales (ubicación, IP, dispositivo, red, patrones previos); aplica MFA adicional o bloqueo |
| Tecnología / IA | Motor de riesgo propietario de Okta, señales en tiempo real al momento de inicio de sesión |
| Alcance de monitoreo | La evaluación se concentra principalmente en la autenticación inicial; la re-evaluación durante la sesión, si existe, "no suele ser completamente continua ni profundiza en el comportamiento del usuario una vez que el acceso fue concedido" (cita textual de la fuente) |
| Diferenciador del proyecto propuesto | Es exactamente el "punto ciego post-*login*" que el proyecto toma como justificación central, Okta Adaptive MFA no cubre lo que pasa después de que el acceso ya fue concedido |

### RADAC académico (ad-RACs)

| Campo | Detalle |
|---|---|
| Fuente académica | Aliyu et al. (2024) |
| Tipo | Modelo académico de control de acceso adaptativo basado en riesgo |
| Funcionalidad principal | Autorización de acceso en tiempo real evaluando cuatro factores: contexto del usuario, sensibilidad del recurso, criticidad de la acción, historial de riesgo acumulado |
| Tecnología / IA | CatBoost (ML supervisado) para el *score* de riesgo por solicitud |
| Alcance de monitoreo | Modelo de decisión de acceso validado con métricas fuertes (*Recall* 100%, F1 98%), pero sin agente de *enforcement* local descrito: es una política de decisión, no una implementación de PEP en el endpoint |
| Diferenciador del proyecto propuesto | El proyecto es, en la práctica, una implementación *end-to-end* de este mismo paradigma RADAC, pero cerrando el circuito con un PEP real en el endpoint: no se queda en el nivel de política de decisión |

### Proyecto propuesto (fila de referencia)

| Campo | Detalle |
|---|---|
| Tipo | UEBA + *enforcement* local, arquitectura PDP/PEP (NIST SP 800-207) |
| Funcionalidad principal | *Score* dinámico de confianza por usuario, actualizado por evento, con decaimiento temporal y continuidad entre sesiones |
| Tecnología / IA | Modelo híbrido propio: IsolationForest (agregado diario) + LSTM Autoencoder (secuencias), código propio auditable |
| Alcance de monitoreo | Agente ligero propio en el endpoint (Windows) + motor de decisión centralizado en la nube |
| Diferenciador del proyecto propuesto | No aplica: esta fila es el punto de referencia contra el que se compara cada alternativa |

## Matriz de capacidades

Verificación explícita de qué cubre cada alternativa, usando solo lo que el Estado del Arte documenta sobre cada una. Donde la fuente no se pronuncia sobre una capacidad puntual de un competidor, se marca N/D (no documentado en el relevamiento) en vez de asumir una respuesta, es más defendible que completar casilleros con información no verificada sobre productos de terceros.

| Solución | Detección de anomalías | Score de riesgo dinámico | Continuo durante toda la sesión | Enforcement automático en el endpoint | Explicabilidad (XAI) |
|---|---|---|---|---|---|
| Microsoft Sentinel UEBA | ✓ | ✓ | N/D | N/D | ✗ |
| Splunk UBA | ✓ | ✓ | N/D | ✗ | N/D |
| Exabeam | ✓ | ✓ | N/D | ✓ (vía SOAR) | ✗ |
| Microsoft Entra ID Protection | ✓ | ✓ | ✗ | △ (solo acceso condicional/MFA) | ✗ |
| Okta Adaptive MFA | △ (solo en *login*) | △ | ✗ | △ (solo MFA/bloqueo en *login*) | N/D |
| RADAC académico (ad-RACs) | ✓ | ✓ | ✓ (por solicitud) | △ (política de acceso, sin PEP físico descrito) | N/D |
| Proyecto propuesto | ✓ | ✓ | ✓ | ✓ (terminar procesos / denegar carpeta) | △ (solo IsolationForest, top-3 *features* por *z-score*; LSTM sin XAI propio) |

**Lectura de la matriz.** Ninguna de las cuatro soluciones comerciales relevadas tiene, según lo que el propio Estado del Arte documenta, la combinación de continuidad durante toda la sesión, *enforcement* automático en el endpoint y algún grado de explicabilidad al mismo tiempo. Esa combinación es, con la evidencia ya reunida, el espacio que el proyecto ocupa y que ningún competidor relevado cubre por completo, con la salvedad de que, en el proyecto propuesto, la explicabilidad hoy es parcial: cubre las *features* de IsolationForest (top-3 por *z-score*, calculadas en cada evento) pero no tiene un mecanismo propio para el componente LSTM del *score* híbrido. De la misma manera, la marca "✓" en continuidad durante toda la sesión es real a nivel arquitectura, pero el comportamiento en frío (*cold-start*) de un usuario nuevo es una limitación conocida y declarada del *scoring*, no del mecanismo de continuidad en sí: por la regla de piso (condición OR entre `is_anomaly_iso` e `is_anomaly_lstm_user`), un usuario sin historial previo puede escalar a nivel alto desde el primer evento sin corroboración entre ambos modelos ni un período de warm-up.

## Comparación de algoritmos de inteligencia artificial

Profundiza lo señalado en la comparación general de alternativas específicamente para el lado de IA/modelos, y muestra que la elección de IsolationForest + LSTM no es arbitraria: responde directamente a limitaciones que la propia literatura relevada reporta sobre cada técnica por separado. Cada enfoque se compara en cinco dimensiones: Fuente académica, Dataset / validación, Métrica reportada, Limitación reportada y Relación con el diseño del proyecto.

### CatBoost (score de riesgo por solicitud)

| Campo | Detalle |
|---|---|
| Fuente académica | Aliyu et al. (2024) (ad-RACs) |
| Dataset / validación | Comparación vs. reglas estáticas/ACL |
| Métrica reportada | *Recall* 100%, Precisión 95%, F1 98% |
| Limitación reportada | No se reporta limitación explícita en el resumen relevado |
| Relación con el diseño del proyecto | El proyecto comparte el paradigma de *score* dinámico por evento, con un modelo distinto (no supervisado) porque no dispone de etiquetas de "acceso autorizado/denegado" como sí tenía este trabajo |

### LSTM secuencial

| Campo | Detalle |
|---|---|
| Fuente académica | Villarreal-Vásquez et al. (2021) |
| Dataset / validación | CMU-CERT r4.2 |
| Métrica reportada | Detección 93%, falsos positivos 4.1% |
| Limitación reportada | *Cold-start*: depende de historial suficiente por usuario, baja el rendimiento en usuarios nuevos |
| Relación con el diseño del proyecto | El proyecto usa LSTM Autoencoder con el mismo problema de *cold-start*, y lo declara explícitamente vía el estado de cobertura "parcial"/"sin *score*" en vez de ocultarlo |

### Graph Neural Networks (GNN)

| Campo | Detalle |
|---|---|
| Fuente académica | Tian et al. (2023) |
| Dataset / validación | CERT r6.2 |
| Métrica reportada | F1 +8.3% vs. modelos secuenciales |
| Limitación reportada | Alta complejidad de infraestructura para grafos a gran escala |
| Relación con el diseño del proyecto | El proyecto evaluó ese costo de infraestructura como desproporcionado para el alcance de un PFI y priorizó IsolationForest + LSTM por menor costo computacional y viabilidad de ejecución sin infraestructura de grafos dedicada |

### Clustering no supervisado (K-Means, DBSCAN, OPTICS, GMM)

| Campo | Detalle |
|---|---|
| Fuente académica | Artioli et al. (2024) |
| Dataset / validación | Datasets reales de actividad de red |
| Métrica reportada | Sin un único algoritmo ganador en todos los escenarios |
| Limitación reportada | Mayor consumo de recursos en enfoques de densidad; alta diversidad entre perfiles de usuario dificulta líneas base estables |
| Relación con el diseño del proyecto | El proyecto sigue exactamente la conclusión de este trabajo: combina dos técnicas (IsolationForest + LSTM) en vez de apostar a un único algoritmo |

### Isolation Forest

| Campo | Detalle |
|---|---|
| Fuente académica | Hariri et al. (2019) |
| Dataset / validación | Logs NGINX / tráfico e-commerce |
| Métrica reportada | Precisión 87% / *Accuracy* 93%, F1 92% |
| Limitación reportada | Falsas alertas ante usuarios con comportamiento legítimo muy variable |
| Relación con el diseño del proyecto | El proyecto mitiga esta limitación reportada combinando IsolationForest (agregado diario) con LSTM (secuencia) + regla de piso + decaimiento temporal, en vez de depender de IsolationForest solo |

### Revisión sistemática

| Campo | Detalle |
|---|---|
| Fuente académica | Landauer et al. (2023) |
| Dataset / validación | Múltiples datasets de logs |
| Métrica reportada | Concluye que LSTM/Autoencoders dominan para anomalías secuenciales; IsolationForest sigue siendo eficiente en baja latencia |
| Limitación reportada | Pocos trabajos enfocados específicamente en comportamiento de usuario (vs. logs de sistema en general) |
| Relación con el diseño del proyecto | El proyecto adopta literalmente la combinación que esta revisión identifica como dominante: no es una elección arbitraria de tecnología |

### IsolationForest + LSTM Autoencoder (proyecto propuesto)

| Campo | Detalle |
|---|---|
| Dataset / validación | CLUE-LDS: ~50M eventos reales anonimizados, 5.000+ usuarios, 5+ años de actividad de producción (Huemer Group) |
| Métrica reportada | `run_regression_test.py` es un test de consistencia/no-regresión (compara la salida actual contra *scores offline* guardados como referencia), no una métrica de performance/clasificación contra *ground truth* comparable al Recall/Precisión/F1 de las demás filas de esta tabla |
| Limitación reportada | *Cold-start* compartido con el resto de la literatura (declarado, no oculto) |
| Relación con el diseño del proyecto | Síntesis directa de las recomendaciones de Artioli et al. (2024) y Landauer et al. (2023): enfoque híbrido, sobre un dataset de producción real en vez de sintético/simulado como buena parte de los trabajos citados |

## Síntesis de diferenciadores

A partir de la propia Conclusión del Estado del Arte de la documentación del proyecto, el argumento central que sostiene esta comparación es el siguiente:

Las herramientas comerciales relevadas operan bajo un enfoque pasivo o reactivo. La telemetría se centraliza en la nube, se procesa, y ante una anomalía la respuesta se delega a una plataforma externa (SOAR) o requiere intervención manual de un administrador. Eso genera una ventana de exposición temporal explotable por un atacante para moverse lateralmente.

El proyecto cierra ese ciclo de forma autónoma, desplegando un agente local en el endpoint que actúa como *Policy Enforcement Point* (PEP), mientras la lógica de decisión se mantiene en la nube como *Policy Decision Point* (PDP), siguiendo el estándar NIST SP 800-207.

El agente mantiene conexión con el motor de IA e intercepta la respuesta casi en tiempo real. Ante una desviación conductual inusual durante la sesión activa, el sistema pasa de "monitoreo y alerta" a "respuesta adaptativa", ejecutando restricciones de permisos o aislamiento del proceso directamente en la máquina del usuario, sin intermediarios y sin depender de un *re-login*.

Ninguna de las cuatro soluciones comerciales relevadas hace esto: Sentinel y Splunk UBA se detienen en detección/priorización; Exabeam automatiza respuesta pero vía orquestación externa, no vía agente propio; Entra ID Protection actúa solo en el momento de autenticación, no durante el uso continuo de recursos.
