# Revisión de modelos (28/10 – 13/11/2026)

> Borrador para pasar a LaTeX. Resume qué se revisó, cómo, qué se midió, qué se decidió y qué quedó abierto. Las cifras provienen de las mediciones registradas durante la revisión; los IC son al 95 % por bootstrap sobre usuarios salvo indicación. Lo marcado **[exploratorio]** no se usó para decidir con un criterio fijado de antemano.

---

## 1. Punto de partida

Al 08/10/2026 el sistema en producción era la **versión 1**:

- **IsolationForest** sobre el agregado usuario-día (8 variables: `n_events`, `n_distinct_types`, `n_distinct_countries`, `n_file_events`, `n_login_events`, `avg_hour`, `off_hours_ratio`, `type_entropy`).
- **Autoencoder LSTM** sobre secuencias de 50 eventos sin solape; el riesgo es la media acumulada del error de reconstrucción por chunk.
- **Score híbrido**: promedio 0,5 ISO / 0,5 LSTM, decaimiento exponencial con `vida_media_dias = 3`, umbrales 40/70/90 y regla de piso (si cualquier modelo marca anomalía, el nivel no baja de `alto`).
- Una evaluación previa (08/10) no había encontrado un candidato que superara a v1 de forma consistente; los modelos "v2" (sin país, hora de Viena) no se promovieron. La partición HOLDOUT se usó una sola vez: FPR ≥ alto 4 % en negativos y 5 % en la población de test.

La revisión partió de cuatro preguntas: ¿IsolationForest y el LSTM están bien planteados?, ¿qué tercer modelo conviene?, ¿funciona el reentrenamiento automático? y ¿cómo obtener métricas con datos reales?

---

## 2. Reglas metodológicas

1. **Solo datos reales.** Al principio se aceptó S1 (intercambio de historiales reales entre usuarios para simular sustitución de cuenta) como métrica y S2/S3 (exfiltración y horario inyectados) solo como ensayos de sensibilidad. El 29/10 se decidió retirar **todo** escenario construido (S1–S7), junto con sus generadores; desde entonces solo cuentan FPR, carga, oscilación y cobertura sobre días reales.
2. **Protocolo antes de medir.** Cada etapa fijó por escrito sus criterios de decisión antes de ver resultados; toda enmienda posterior se declaró como tal.
3. **Partición fija.** 63 usuarios DEV y 60 HOLDOUT, corte temporal `2021-08-02`. HOLDOUT no se usa para elegir.
4. **Sin tocar producción durante la medición.** Los experimentos corrieron en sandbox; los artefactos de producción se verificaron por SHA-256 antes y después.
5. **Verificación de punta a punta.** Cada cambio en la API se validó con la suite de tests, el test de regresión offline contra online y la demo del agente.

---

## 3. Datos

| dataset | uso | motivo |
|---|---|---|
| **CLUE-LDS** (nube, 2017–2022, sin etiquetas) | entrenamiento y FPR | dominio del sistema |
| **LANL 2017** (host Windows, sin ataques) | FPR en dominio de host | único dataset de host real disponible |
| **GUIDE** (Microsoft, incidentes reales etiquetados, CDLA-Permissive-2.0) | solo para probar la acumulación de alertas por cuenta | otro producto; no sirve para entrenar |
| **DARPA OpTC** | piloto de transferencia (3 positivos) | prueba de brecha de dominio |
| **LANL 2015** | **descartado** el 31/10 | una sola intrusión simulada, casi toda desde un host (Larroche, 2026) |
| SEA (Schonlau) | descartado | etiquetas construidas, sin licencia clara |

**Revisión de usuarios de CLUE.** La clasificación de Fase2 era por volumen total (más de 500.000 eventos en 5 años = cuenta de servicio). Con una regla de comportamiento (horas activas por día, % fuera de horario, % fin de semana), 4 de las 12 "cuentas de servicio" resultaron humanas intensas y 14 de las 291 "válidas", automáticas. La FPR para personas era 5,1 %, contra 0,9 % en cuentas automáticas. Se implementó la clasificación por comportamiento detrás de un parámetro (`PFI_CLASIFICACION=comportamiento`).

---

## 4. Diagnóstico de los modelos de la versión 1

### IsolationForest: bien planteado para lo que mide

- Detecta volumen y horario atípicos del día frente a la población; no mide identidad (S1 similar 0,534 [0,458–0,613]).
- Defectos encontrados: país como interruptor, horas en UTC con datos de Viena, scaler ajustado incluyendo test, corte temporal por percentil dinámico y conteos absolutos que no transfieren de dominio.
- Correcciones: corte temporal fijo y parametrizable, scaler solo con train (disponible por parámetro) y calibración por cuantiles sobre días reales.
- **Decisión:** se mantiene.

### Autoencoder LSTM: no cumple su propósito

- Debía captar el orden de las acciones y no lo hace: permutar los 50 pasos no cambia el ranking (Spearman 0,989); ~72 % del error viene de `country_changed`; sin país queda cerca del azar (ROC-AUC 0,52–0,63).
- El 95,4 % de la varianza de su riesgo es entre usuarios y su cambio diario mediano es 0: marca a la persona, no al día.
- El 19,6 % de los usuarios no llega a cerrar un chunk de 50 eventos y no recibe señal.
- Es el único componente que necesita TensorFlow (Fase5 tarda 26–38 min).
- **Decisión:** se retira del camino por defecto; código y artefactos quedan detrás de `SCORING_TERCER_MODELO=lstm`.

### Combinación

- Promediar con un componente débil diluye al bueno, y la FPR del híbrido dependía de que el LSTM casi siempre estuviera bajo: ISO ≥ 70 marca por construcción el 30 % de los días de train.
- Se reemplazó el promedio por un **máximo calibrado** (cuantiles 0,80/0,95/0,99 sobre días reales de train), que mantiene la escala de umbrales.

---

## 5. Cronología de la revisión

### Etapa 1 (28/10): tercer modelo y métricas reales

- **Alternativas evaluadas:** perfil de Markov por usuario, ECOD, autoencoder denso, grupos de pares. ECOD resultó redundante con ISO (no se adopta). No hay grupos de pares posibles: CLUE no trae roles reales.
- **Perfil de Markov en línea.** Con perfil fijo al entrenar, AUC en S1 disímil 0,34 y FPR 38 %; con actualización en línea, 0,90 y 2,7 % → se adopta en línea. Se eligió entre 48 variantes por un criterio único: orden 2, símbolo tipo × franja de 6 h en hora local, ventana de 90 días, mínimo 3 días (AUC media S1 0,848 contra 0,795 del prototipo).
- Se integró en la API detrás de `SCORING_TERCER_MODELO=markov`. En DEV, con el pipeline completo: FPR ≥ alto 4,4 % contra 5,6 % de v1.
- **Umbral por cuantil móvil** (validado sin etiquetas): FPR observada 4,61–4,64 % para un objetivo de 5 % y 0,99–1,02 % para 1 %. Se expuso en la API como informativo (`SCORING_UMBRAL_MOVIL`).
- **Eficiencia:** no invertir en GPU (solo la aprovecharía el LSTM, que sale).
- **Reentrenamiento corregido:** sin escribir los notebooks en el lugar, con `Auditoria2` antes de Fase6, modo de memoria baja, determinismo y corte fijo.

### Etapa 2 (28/10): detectores informativos

- **Novedad de recurso** (`novedad_service`): primer acceso a destino, proceso o carpeta en 90 días, como explicación; no cambia el score. La novedad de **proceso** no aportó sobre la de destino.
- Se midió quitar el decaimiento con Markov (recupera sensibilidad sin perder FPR); no se aplicó porque `vida_media_dias` es constante de negocio.
- Reentrenamiento solo con CLUE, sin mezclar los eventos del agente (`PFI_ORIGEN_REENTRENAMIENTO=clue`).

### Etapa 3 (29/10): solo datos reales

- Se borraron S1–S7 y sus generadores; el gate de promoción (RF-21) pasó a un único criterio: **no inferioridad de la FPR ≥ alto y de su p90 semanal en días reales DEV, margen 0,01**.
- **Corrección de un bug del Markov:** congelar el perfil también por la anomalía del propio Markov se realimentaba (FPR 11,3 % contra 4,5 %). Desde entonces solo ISO congela el perfil.
- Markov pasa a la instalación local; se aplica RLS a `historial_scores`.
- No se agrega un cuarto modelo: la carencia es de etiquetas, no de detectores.

### Etapa 4 (30/10): promoción y arranque en frío

- **Primera promoción de punta a punta** del reentrenamiento automático, en sandbox: 2 h 30 (pipeline 1 h 57, gate 32 min); candidato 4,64 % contra 4,76 % de FPR. No se pasó a producción.
- **Arranque en frío** (130 usuarios nuevos): FPR 11,43 % con ISO crudo; calibrar ISO la bajaba a 0 %, pero no se adoptó por riesgo de ceguera sin etiquetas. Markov poblacional para usuarios nuevos: **descartado** (2,86 % en CLUE, 15,06 % en LANL 2017, inestable) y su código borrado. Reparto de α por detector: descartado.

### Etapa 5 (30/10): evaluación por modelo

| detector (CLUE DEV) | FPR ≥ alto solo | % de alertas en el top 5 de usuarios | Spearman con la secuencia permutada | recomendación |
|---|---|---|---|---|
| ISO | 15,17 % | 59,9 % | — | mantener |
| LSTM | 10,01 % | 68,2 % | 0,989 | retirar del default |
| Markov | 3,10 % | 27,4 % | 0,30 (CLUE), 0,00 (LANL 2017) | mantener sin afirmar detección |
| Novedad de destino | — | — | — | prender en host con tope |

- Las alertas de los detectores son casi disjuntas (Jaccard ≤ 0,12).
- **Oscilación dentro del día:** 6,21 % de días ≥ alto al cierre, pero 14,63 % con algún evento ≥ alto, que es lo que ve el agente.

### Etapa 6 (30–31/10): nuevo camino por defecto

- **Default: ISO + Markov + novedad de recurso**, sin LSTM ni TensorFlow; pipeline de reentrenamiento sin Fase5.
- Novedad de recurso como tercer modelo: cuenta recursos de todas las clases contra un cuantil móvil poblacional (α 5 %, ventana 30 días, mínimo 50 muestras) y puede elevar al piso.
- La oscilación se atribuyó al piso de Markov (177 de 189 días transitorios).

### Etapa 7 (31/10): cierre de modelos

- **GUIDE_Test** confirma, en otro producto, que acumular detectores distintos por cuenta ordena mejor los incidentes: PR-AUC 0,493 contra 0,239 (diferencia +0,254 [+0,038; +0,382]). Es la única cifra confirmatoria de la revisión.
- **Corrección en la novedad:** la API dejaba entrar al cuantil los días sin recursos, a diferencia de la regla validada; corregida, la FPR en CLUE DEV bajó de 7,08 % a 5,37 %.
- Markov sin piso (detrás de `SCORING_PISO_MARKOV=0`): oscilación de 14,04 % a 4,70 %. Quedó apagado por defecto.
- Novedad con suma decaída: apagada y sin recomendación.

### Etapa 8 (31/10): comprobación

- Replay real completo (462.024 eventos) contra la simulación: **0 diferencias**.
- Se detectó que el gate RF-21 no evaluaba la novedad (veía 4,47 % donde la API daba 5,37 %).

### Etapa 9 (31/10): camino por defecto actual

- **LANL 2015 queda fuera** como evidencia. Consecuencia aceptada: sin recall medible en datos propios. La prioridad pasa a **menos ruido medible** (FPR, oscilación, carga).
- **Markov sale del default** por costo medido y falta de evidencia admisible (no por prueba de que no detecte). **Default: ISO + novedad de recurso.** Sin 3 días de historia se usa ISO sin calibrar: una variante que también calibraba en frío pasaba sus criterios, pero dejaba la demo sin nivel crítico.

| medida (CLUE DEV) | antes | después |
|---|---|---|
| FPR ≥ alto / p90 semanal | 5,37 % / 8,08 % | **2,66 % / 4,95 %** |
| Días con algún evento ≥ alto / al cierre (51 usuarios) | 14,04 % / 4,95 % | **2,66 % / 1,29 %** |
| Arranque en frío | 11,43 % | 11,43 % |

- **El gate RF-21 evalúa el default completo**, novedad incluida: candidato 2,95 % contra 2,66 %, promueve.
- **Cola por cuenta** (≥ 2 clases de señal en 7 días): PR-AUC 0,4703 contra 0,2337 en GUIDE Train; en CLUE DEV, 0,184 cuentas por día. Quedó detrás de `SCORING_COLA_CUENTA`, apagado.
- Novedad por popularidad del recurso: no alcanzó su criterio (−5,6 % en CLUE), no se implementó. Relación proceso padre → hijo: inestable (2 de 4 semanas), queda informativa.
- **ISO de CLUE en host:** 53,66 % de alertas contra 4,13 % de un ISO de host (Spearman −0,15). Es la limitación más grave; no se promovió un ISO de host sin telemetría propia.
- **El 08/11 la EC2 pasa al nuevo default.**

### Etiquetado de triage (11–13/11) [provisional]

- 403 usuario-días de CLUE DEV (las 163 alertas del default y 240 días sin alerta, muestreados con peso), etiquetados a ciegas (sin ver score, nivel ni detector) con un protocolo escrito antes de ver casos: "¿un analista SOC abriría el caso?".
- 14 de 162 alertas merecían revisión (8,6 %, IC 3,9–15,0); 13,5 % entre las de origen ISO y **0 de 58** entre las que solo dispara la novedad; 3 de 240 días sin alerta merecían revisión (1,05 % ponderado).
- Consistencia propia: 40 de 40 en el veredicto, kappa 0,91 en la categoría.
- Pendiente: confirmación por un analista. Con estas cifras no se cambió ningún modelo ni umbral.

---

## 6. Decisiones

### Tomadas

| decisión | motivo |
|---|---|
| Solo datos reales; borrar escenarios construidos | criterio metodológico del autor |
| Gate RF-21 por no inferioridad de FPR real, sobre el default completo | el criterio anterior no medía detección y no veía la novedad |
| Retirar el LSTM del default (código conservado) | no usa el orden; identifica a la persona |
| Retirar Markov del default (código conservado) | costo en oscilación; sin evidencia admisible de detección |
| Novedad de recurso en el default (α 5 %) | menor FPR en host y cobertura de "algo nuevo para esta cuenta" |
| Máximo calibrado en lugar de promedio | evitar diluir el componente útil |
| Corte temporal fijo `2021-08-02`, reentrenamiento determinista y de memoria baja | reproducibilidad y viabilidad en 16 GB |
| Clasificación de usuarios por comportamiento (por parámetro) | el volumen total no distingue personas de máquinas |
| Descartar LANL 2015, ECOD, Markov poblacional, reparto de α, popularidad y GPU | criterios no cumplidos o sin ganancia |
| No promover un ISO de host ni el candidato de sandbox | sin telemetría propia ni etiquetas |

### Abiertas

- Confirmación del etiquetado por un analista y qué hacer con la novedad al nivel si se confirman 0 de 58.
- Telemetría propia de host para reentrenar ISO en ese dominio.
- `W_PERSONAL_MAX` y el blend del baseline personal (no mejoró la FPR de forma consistente en 43 usuarios chicos).
- Calibrar ISO en arranque en frío.
- Activar la cola por cuenta.

---

## 7. Qué se puede afirmar y qué no

**Se puede afirmar:**

- Con el default actual, la FPR en días reales de CLUE DEV es 2,66 % (p90 4,95 %) y la oscilación dentro del día bajó de 14,04 % a 2,66 %.
- El reentrenamiento automático y el gate de promoción funcionan de punta a punta (en sandbox).
- Acumular señales distintas por cuenta mejora el orden de los incidentes en GUIDE (otro producto).
- El ISO entrenado en CLUE no está calibrado para telemetría de host.

**No se puede afirmar:**

- Que el sistema detecte ataques: no hay recall medible en datos del dominio.
- Que menos alertas sea mejor: sin etiquetas puede ser ceguera.
- Que Markov no detecte: se retiró por costo y falta de evidencia, no por prueba.
- Que "cobertura" sea detección.
- Que las cifras del etiquetado sean definitivas.
