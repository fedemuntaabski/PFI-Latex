# Limitaciones del sistema (versión provisional)

> Borrador para completar el capítulo de limitaciones de la memoria. Cifras tomadas de `docs/contexto/estado_modelos.md`, `docs/contexto/limitaciones.md` y `docs/etiquetado/resultado_provisional.md` de la rama `entrega/limpieza` (2026-11-14). Las marcadas **[provisional]** dependen del etiquetado que todavía no confirmó un analista.

Cada limitación se presenta con qué es, por qué ocurre, cuánto pesa y qué haría falta para superarla. Se distinguen las **limitaciones de evaluación** (qué no se puede afirmar), las **de los modelos**, las **de la arquitectura y la operación** y las **decisiones de alcance** (recortes deliberados del PFI, no defectos).

---

## 1. Limitaciones de evaluación

### 1.1 No hay recall medible en datos del dominio

- **Qué es.** El sistema no tiene una cifra de detección (recall, precisión, F1) sobre ataques reales en su propio dominio.
- **Por qué.** CLUE-LDS, el dataset de entrenamiento, no trae etiquetas de ataque. LANL 2017 (host Windows) tampoco tiene ataques. LANL 2015, el único con red team, se descartó como evidencia: contiene una sola intrusión simulada, casi toda desde un mismo host (Larroche, 2026). Los escenarios construidos (S1–S7) se retiraron para evaluar solo con datos reales.
- **Cuánto pesa.** Solo se pueden medir tasa de falsos positivos (FPR), carga de alertas, oscilación y cobertura. "Cobertura" (fracción de usuario-días con primer acceso a un recurso raro que terminan en nivel ≥ alto) no es detección.
- **Qué haría falta.** Un dataset de dominio con incidentes reales etiquetados, o la confirmación del etiquetado de triage por analistas (ver 1.2).

### 1.2 Etiquetado de triage provisional y de un solo etiquetador **[provisional]**

- **Qué es.** Se etiquetaron 403 usuario-días de CLUE DEV (las 163 alertas del modelo por defecto y 240 días sin alerta, muestreados con peso) con la pregunta "¿un analista SOC abriría este caso?".
- **Resultados provisionales.** 14 de 162 alertas merecían revisión (8,6 %, IC 95 % 3,9–15,0, bootstrap por usuario); 13,5 % entre las alertas de origen ISO y 0 de 58 entre las que solo dispara la novedad de recurso; 3 de 240 días sin alerta merecían revisión (1,05 % ponderado, IC 0–3,8).
- **Por qué es limitado.** Hay un único etiquetador, sin confirmación todavía de un analista; el analista verá la etiqueta antes de decidir (sesgo de anclaje); la consistencia se midió solo contra el mismo etiquetador (40 de 40 en el veredicto, kappa 0,91 en la categoría, con un solo positivo en la muestra); y es juicio de triage, no verdad de ataque.
- **Circularidad parcial.** El protocolo ordena decidir primero por lo que el modelo no ve (tipo de operación, amplitud de rutas, ritmo), pero volumen, horario y recurso nuevo también son variables del modelo.
- **Qué haría falta.** La planilla confirmada por un analista y un segundo revisor ciego para medir el acuerdo real.

### 1.3 La evaluación es sobre día cerrado

- **Qué es.** El benchmark puntúa el usuario-día completo; en línea, la API puntúa el agregado parcial del día en cada evento.
- **Cuánto pesa.** Con el modelo por defecto, 2,66 % de los días tienen algún evento ≥ alto y 1,29 % terminan así al cierre. La oscilación dentro del día no la cubre la evaluación de día cerrado.

### 1.4 HOLDOUT usado una sola vez, con la versión 1

- La partición HOLDOUT (60 usuarios) se usó una única vez, con la versión 1 (IsolationForest + LSTM): FPR ≥ alto de 4 % en negativos y 5 % en la población de test. El modelo por defecto actual se midió solo sobre DEV (63 usuarios). Además, el LSTM v1 era in-sample para 47 de 57 víctimas de HOLDOUT, así que esa medición es optimista para el LSTM.

---

## 2. Limitaciones de los modelos

### 2.1 Brecha de dominio: entrenado en nube, aplicado en host

- **Qué es.** Los modelos se entrenaron con logs de colaboración en la nube (CLUE-LDS); el agente captura telemetría de host Windows y la traduce a ese vocabulario, con otra semántica.
- **Cuánto pesa.** Es la limitación más grave. Aplicado a telemetría de host (LANL 2017), el IsolationForest de CLUE alerta el **53,66 %** de los días, contra **4,13 %** de un IsolationForest entrenado en host, y los rankings no se parecen (Spearman −0,15). Ninguna métrica del benchmark se transfiere al agente sin más.
- **Qué haría falta.** Entrenar y calibrar con telemetría propia de host recolectada por el agente.

### 2.2 Un solo detector de score en el camino por defecto

- El default es IsolationForest + novedad de recurso. La novedad no cambia el score: solo puede elevar el nivel por la regla de piso. Con Markov fuera del default, ningún detector mira el orden de los eventos, y la **sustitución de cuenta queda sin cobertura** (vuelve con `SCORING_TERCER_MODELO=markov`).

### 2.3 Componente de secuencia descartado por falta de evidencia

- **LSTM (v1).** El 95,4 % de la varianza de su riesgo es entre usuarios y su cambio diario mediano es 0: identifica a la persona, no al comportamiento del día. Permutar los 50 pasos de la secuencia no cambia el ranking (Spearman 0,989) y, sin la variable de país, queda cerca del azar (ROC-AUC 0,52–0,63).
- **Markov.** Usa el orden (Spearman con secuencia permutada 0,30 en CLUE y 0,00 en LANL 2017), pero no hay evidencia admisible de que detecte. Se retiró del default por costo y porque su regla de piso explicaba la oscilación (177 de 189 días transitorios).

### 2.4 Variables de ubicación dominantes en la versión 1

- `n_distinct_countries` (IsolationForest) y `country_changed` (LSTM) funcionan como interruptor de ubicación: la detección "con país" y el nivel crítico de la demo con VPN salen de ahí, no del comportamiento.

### 2.5 Arranque en frío

- Durante los primeros 3 días de un usuario nuevo, la FPR ≥ alto es **11,43 %** (130 usuarios). Sin 3 días de historia en los últimos 90, ISO se usa sin calibrar. El estado `en_aprendizaje` (primeros 20 eventos) solo ablanda la acción, no el nivel.

### 2.6 Zona horaria

- Las horas se calculan en UTC; CLUE corresponde a Viena y el agente corre en Argentina, así que `avg_hour` y `off_hours_ratio` quedan corridos. En CLUE, calcularlas en hora de Viena cambia el 2,48 % de los días sin cambiar la FPR.

### 2.7 Parámetros de negocio sin calibración completa

- `vida_media_dias = 3` parte de un estadístico real (mediana del intervalo de actividad). `w_iso`, el nivel de la regla de piso, los umbrales 40/70/90, `W_PERSONAL_MAX = 0,7` y los parámetros de drift (7 días, 2 desvíos) son puntos de partida razonados, sin un barrido que los calibre.

### 2.8 Baseline personal

- El percentil personal mapea un valor siempre ≥ 0 (RMS de z-scores) con una normal de dos colas, lo que sesga hacia percentiles altos en usuarios con poca historia. Los eventos anómalos no actualizan el baseline y el corrimiento lento se detecta y audita (`drift_alerts`), pero no hay reinicio automático ante un posible *self-poisoning*. En 43 usuarios chicos, el blend no mejoró la FPR de forma consistente.

---

## 3. Limitaciones de arquitectura y operación

### 3.1 Latencia en la nube

- Local, `POST /eventos` tiene un p95 de **14,9 ms** (RNF-01). En la nube (API en EC2, Redis y Postgres gestionados en otra región), el p95 es **3.110 ms**: cada evento hace ~20 viajes secuenciales a Redis y Postgres de ~124 ms. La meta de 500 ms no se cumple de punta a punta con esa topología.
- En la demo en la nube, el nivel crítico llega a los 33,8–40,3 s de iniciado el ataque y la acción `terminar_y_denegar` se confirma a los 46,3–49,1 s (3 de 3 ensayos). El correo de notificación (redacción con Gemini + SMTP) corre dentro del request y le suma ~3 s al evento que dispara la acción.
- **Qué haría falta.** Ubicar la API junto a los datos, cachear la configuración (existe `SCORING_CONFIG_CACHE_SEG`, apagado) y sacar la notificación del request.

### 3.2 Persistencia

- `eventos_crudos` crece sin límite: no hay retención ni poda, y la escritura es síncrona en cada evento.
- El `uid` se guarda sin anonimizar; el sistema no implementa anonimización, firma HMAC ni criptografía propia.
- Postgres es best-effort: si no está disponible, el scoring sigue pero se pierde ese historial.

### 3.3 Identidad y acceso

- Sin API keys configuradas, la API queda abierta (fail-open), pensado para desarrollo. En la EC2 corre en modo estricto.
- El login del dashboard usa dos usuarios fijos (`admin`, `operador`) sin almacenamiento real de usuarios y sin límite de intentos.
- La resolución de rol y departamento contra el IAM es síncrona dentro de `POST /eventos`; el cache (30 min) y el cache de fallas (60 s) acotan su costo, y el enforcement no la espera.

### 3.4 Agente

- **Solo Windows.** La API no asume nada específico del sistema operativo, pero el agente sí.
- **Alcance de enforcement acotado a `DEMO_ROOT`**: restricción de seguridad deliberada para no modificar el sistema real durante la demo.
- **Ruido de procesos.** Listas de exclusión y agrupación mitigan el ruido de sistema y del navegador, pero no lo eliminan.
- **Sin heartbeat.** "Sin reportar" (15 min sin eventos) no distingue agente caído de usuario inactivo.
- **Un agente por usuario y por equipo**, y se asume que los relojes de agente y API están sincronizados.

### 3.5 Reentrenamiento

- El reentrenamiento automático y el gate de promoción (RF-20/21) funcionaron de punta a punta en sandbox (2 h 30), pero no se ejercitaron con un modelo genuinamente nuevo en el entorno de producción. El gate exige no inferioridad en FPR (margen 0,01), no prueba una mejor detección.

### 3.6 Frontend

- Sin suite de tests automatizados; se valida manualmente contra la API.

---

## 4. Decisiones de alcance (no defectos)

- Modelos no supervisados por falta de datos etiquetados.
- Modelos dentro del proceso de la API, sin microservicio de inferencia.
- Sin alta disponibilidad, TLS mutuo ni multi-tenant.
- Sin autenticación real de usuarios finales ni soporte multi-sistema operativo del agente.
- Docker queda como referencia; el despliegue usado es el de `infra/` (EC2 + Caddy).

---

## 5. Trabajo futuro sugerido (en orden de impacto)

1. Recolectar telemetría propia de host y reentrenar y calibrar IsolationForest en ese dominio (2.1).
2. Confirmar el etiquetado con un analista y medir el acuerdo con un segundo revisor (1.2).
3. Conseguir incidentes etiquetados en el dominio para tener recall (1.1).
4. Bajar la latencia en la nube: colocar la API junto a los datos y sacar la notificación del request (3.1).
5. Retención de `eventos_crudos`, anonimización del `uid` y límite de intentos en el login (3.2, 3.3).
