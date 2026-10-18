# Plan de corrección: partición del reentrenamiento y criterio de promoción (RF-19 / RF-21)

> Documento de trabajo para el repositorio del código. Describe el diagnóstico, la solución propuesta, los pasos de implementación y la validación. **No incluye cambios de código aplicados.** Las rutas son relativas a la raíz del repositorio.
>
> Fecha del diagnóstico: 2026-10-18. Estado del código revisado: commit `74d3eb0`.

---

## 1. Resumen

Con el diseño actual, **ningún reentrenamiento que incorpore datos del agente puede promoverse**:

1. El *pipeline* calcula el corte entre entrenamiento y prueba como el percentil 80 de las fechas del conjunto **combinado** (CLUE-LDS más los eventos del agente). Los eventos del agente son de 2026, así que el corte se corre.
2. El criterio de promoción exige que el corte del candidato sea exactamente el 2021-08-02. Si no lo es, rechaza por seguridad (*fail-safe*).
3. Fijar la fecha no alcanza. Si el corte queda en 2021-08-02, los eventos del agente caen en **prueba** y no en entrenamiento, y el reentrenamiento no aprende nada de ellos.

Hay un segundo problema, independiente del anterior. **El LSTM (v1) separa entrenamiento y prueba al azar por usuario**, y esa permutación cambia cuando aparecen usuarios nuevos. Así, víctimas del benchmark (DEV/HOLDOUT) pueden quedar en el entrenamiento del candidato, y el criterio de promoción no lo detecta.

**Solución propuesta:** decidir la partición **por origen del dato y no solo por fecha**:

- **Entrenamiento:** CLUE-LDS hasta el corte, más todos los datos del agente.
- **Prueba y benchmark:** CLUE-LDS posterior al corte, sin cambios.

Además, se congela la asignación de los usuarios de CLUE en el LSTM, se excluyen explícitamente las víctimas del benchmark del entrenamiento y el *pipeline* pasa a dejar un registro de la partición que el criterio de promoción verifica.

---

## 2. Diagnóstico

### D1. El corte se recalcula sobre el conjunto combinado
- `scripts/export_clue_combinado.py` arma `data/clue_combinado.json` con `data/clue.json` más `eventos_crudos`. Se filtran los eventos con `time <= FIN_CLUE_LDS` (2022-09-29T23:59:59Z), que son reproducciones, y los de prueba o demo.
- `scripts/Fase4_forest.ipynb`, celda 2:
  ```python
  split_date = df_sorted['date'].quantile(0.8)
  if V2:
      assert str(split_date) == sc.CORTE_TEMPORAL, split_date
  train_mask = df_sorted['date'] <= split_date
  ```
  - **Con v1 (vigente):** no hay `assert`, el corte se corre en silencio y el *pipeline* termina con un candidato de corte distinto.
  - **Con v2:** el `assert` falla, el paso del *pipeline* falla y el intento queda registrado como «*pipeline* en curso» (ver la limitación correspondiente).
- `scripts/Fase3_engineering.ipynb`, celda 11 (v2): tiene el mismo `quantile(0.8)` más el `assert` para el escalador de Isolation Forest.

### D2. El criterio de promoción fija la fecha
- `api/app/scoring/metricas_service.py`:
  ```python
  CORTE_TEMPORAL = "2021-08-02"
  PRIMER_DIA_TEST = "2021-08-03"
  ...
  primer = str(pd.read_parquet(test, columns=["date"])["date"].min())[:10]
  if primer != PRIMER_DIA_TEST:
      return "corte temporal del candidato distinto de ... dias DEV del benchmark podrian estar en train"
  ```
- La intención es correcta: impedir que los días de los escenarios de DEV (víctimas de CLUE posteriores al corte) entren al entrenamiento del candidato. La implementación, sin embargo, mide un indicio (el primer día de prueba) y no la propiedad que importa (si hay días de víctimas en el entrenamiento).

### D3. Fijar la fecha no resuelve el problema
Supongamos que `Fase4` usa directamente `sc.CORTE_TEMPORAL` en lugar del cuantil. Como todos los eventos del agente tienen fecha posterior a 2021-08-02, caen en `test_mask`. El modelo de Isolation Forest «reentrenado» se entrena con los mismos datos que el vigente, y RF-19 queda cumplido solo en apariencia.

### D4. El *split* del LSTM v1 depende del conjunto de usuarios
`scripts/Fase5_autoencoders.ipynb`, celda 3 (rama `not V2`):
```python
unique_users = np.unique(sequence_uid_map)
np.random.seed(42)
np.random.shuffle(unique_users)
train_users = set(unique_users[:int(n_users * 0.70)])
```
- Al agregar usuarios del agente, cambia `unique_users`, y con él la permutación completa: usuarios de CLUE que antes estaban en *test* pueden pasar a *train*.
- El criterio de promoción solo comprueba el corte de Isolation Forest, así que **no detecta** que una víctima de DEV haya entrado al entrenamiento del LSTM. Ya figura como pendiente en `docs/analysis/sesion_cierre_modelos_20261008.md`, sección 7.

### D5. Observación menor: escaladores v1 ajustados sobre todos los datos
En v1, `Fase3` ajusta `scaler_isoforest` y `scaler_lstm` con `fit_transform` sobre **todo** el conjunto, incluida la prueba. Es una fuga leve y preexistente. No bloquea, pero conviene corregirla junto con lo anterior, porque la nueva partición ofrece la máscara de entrenamiento para hacerlo (como ya hace v2).

### D6. Volumen y dominio de los datos del agente
- Hay unos 28 usuario-días del agente frente a unos 49 000 pares usuario-día de entrenamiento de CLUE. Su efecto sobre el modelo es despreciable mientras el volumen no crezca.
- Los eventos del sistema operativo se traducen al vocabulario de CLUE (transferencia de dominio, `datos.tex`, sección de mapeo). Mezclarlos en el entrenamiento es coherente con RF-19, pero el benchmark sigue sin medir la detección en el dominio del agente.

---

## 3. Solución propuesta

### 3.1 Principio
La partición se decide **por origen** del dato:

| Origen | Fecha | Isolation Forest | LSTM | Benchmark |
|---|---|---|---|---|
| CLUE-LDS | ≤ `CORTE_TEMPORAL` | train | según la asignación congelada | — |
| CLUE-LDS | > `CORTE_TEMPORAL` | test | según la asignación congelada | DEV/HOLDOUT |
| Agente | cualquiera | train | train | — (no participa) |
| Víctimas DEV/HOLDOUT | > `CORTE_TEMPORAL` | **nunca** train | **nunca** train | sí |

El origen se puede deducir sin cambiar el formato de `clue_combinado.json`: el exportador ya garantiza que todo evento del agente tiene `time > FIN_CLUE_LDS`. Se define `es_agente = date > FIN_CLUE_LDS`.

### 3.2 Cambios por archivo

**`scripts/_score_common.py`**
- Agregar `FIN_CLUE_LDS = "2022-09-29"`, en una sola fuente compartida con `export_clue_combinado.py`.
- Agregar una función pura que todos los notebooks usen, para que la regla viva en un único lugar:
  ```python
  def mascara_train_iso(dates: pd.Series) -> np.ndarray:
      """True para CLUE-LDS hasta el corte y para todo dato del agente."""
      d = pd.to_datetime(dates)
      es_agente = d > pd.Timestamp(FIN_CLUE_LDS)
      return ((d <= pd.Timestamp(CORTE_TEMPORAL)) | es_agente).to_numpy()
  ```

**`scripts/Fase3_engineering.ipynb`**
- Celda 11: reemplazar `quantile(0.8)` y el `assert` por `sc.mascara_train_iso(agg_features['date'])`. Ajustar el escalador de Isolation Forest **solo** sobre esa máscara, en v1 y en v2 (corrige D5).
- Celda 8 (v2): `pre = (fin <= corte) | (fin > FIN_CLUE_LDS)`, es decir, las secuencias del agente van a *train*. En v1, ajustar el escalador del LSTM solo sobre las secuencias de entrenamiento.
- Como control de cordura, conservar un `assert` de que el cuantil 0,8 calculado **solo sobre CLUE** sigue dando `CORTE_TEMPORAL`. Eso detecta un cambio accidental en `clue.json`.

**`scripts/Fase4_forest.ipynb`**
- Celda 2: `train_mask = sc.mascara_train_iso(df_sorted['date'])` y `test_mask = ~train_mask`. La prueba queda formada solo por CLUE posterior al corte.

**`scripts/Fase5_autoencoders.ipynb`**
- Rama v1: no sortear de nuevo. Leer la asignación vigente (`models/lstm_split_users.pkl`), mantener la asignación de cada usuario de CLUE y mandar a *train* a los usuarios nuevos del agente.
- Excluir explícitamente del entrenamiento a las víctimas DEV/HOLDOUT, leídas de `data/benchmark/ampliado/mundos.parquet`, al menos sus secuencias posteriores al corte.
- Si se prefiere no depender del archivo anterior, otra opción es una asignación determinista por *hash* del `uid` (por ejemplo, `sha256(uid) % 100 < 70`). Es estable ante usuarios nuevos, pero **cambia la asignación actual** y, con ella, las métricas de referencia; habría que recalcular la línea de base. Por eso se recomienda congelar la asignación.

**Registro de la partición (nuevo)**
- Al final de `Fase4`/`Fase5`, escribir `scripts/models/particion.json` con este contenido:
  ```json
  {"corte_temporal": "2021-08-02", "fin_clue_lds": "2022-09-29",
   "iso_train_filas": 0, "iso_train_filas_agente": 0, "iso_test_primer_dia": "2021-08-03",
   "lstm_train_usuarios": 0, "lstm_train_usuarios_agente": 0,
   "victimas_benchmark_en_train_iso": 0, "victimas_benchmark_en_train_lstm": 0}
  ```
- Incluirlo en el juego de artefactos que se respalda y restaura (`reentrenamiento_scheduler.py`, lista de artefactos).

**`api/app/scoring/metricas_service.py` (`precondicion`)**
- Reemplazar la comparación del primer día de prueba por la verificación de la propiedad que importa, leyendo `particion.json` del candidato:
  1. existe `particion.json` (si falta, *fail-safe*, como hoy);
  2. `corte_temporal == CORTE_TEMPORAL` y `iso_test_primer_dia == PRIMER_DIA_TEST`, es decir, la prueba de CLUE no se movió;
  3. `victimas_benchmark_en_train_iso == 0` y `victimas_benchmark_en_train_lstm == 0`.
- Ajustar el mensaje de rechazo para que diga cuál de las tres condiciones falló.

**`scripts/export_clue_combinado.py`**
- Importar `FIN_CLUE_LDS` de la fuente común en lugar de duplicarlo.

### 3.3 Fuera de alcance (registrar como decisiones)
- **Peso de los datos del agente:** con el volumen actual no se pondera. Si crece, evaluar ponderación o un mínimo de usuario-días antes de reentrenar (tarea del planificador).
- **Benchmark del dominio del agente:** el criterio sigue midiendo la detección sobre CLUE. Medir en el dominio propio requiere escenarios etiquetados de *endpoints* (trabajo futuro de la tesis).
- **Limitaciones relacionadas del planificador** (registro «*pipeline* en curso», excepciones no registradas, sin tiempo máximo): se corrigen aparte, aunque conviene hacerlo antes de ejercitar la promoción real.

---

## 4. Procedimiento de implementación (orden sugerido)

1. **Rama:** `fix/particion-reentrenamiento`.
2. **Línea de base:** antes de tocar nada, guardar las métricas del gate con los artefactos vigentes (`puntuar.py --run ampliado --tag base`): ROC-AUC medio 0,7726 y FPR 0,0557.
3. **Función de máscara y constantes** en `_score_common.py`, con pruebas unitarias (§5.1).
4. **Fase3 y Fase4:** aplicar la máscara y los escaladores sobre *train*. Ejecutar el *pipeline* **solo con `clue.json`** y comprobar que las salidas coinciden con las vigentes (§5.2). Este es el control de no regresión más importante.
5. **Fase5:** congelar la asignación y excluir a las víctimas. Repetir el control con CLUE solo.
6. **`particion.json`:** generarlo e incluirlo en el respaldo y la restauración.
7. **`precondicion`:** reescribirla y actualizar `api/tests/test_gate_promocion.py`.
8. **Prueba con datos del agente:** sintéticos o los reales filtrados (§5.3).
9. **Corrida real del planificador** en el entorno local, con registro en `reentrenamiento_log`.
10. **Documentación:** actualizar `docs/analysis/` y avisar para actualizar la tesis (§7).

---

## 5. Validación

### 5.1 Pruebas unitarias (nuevas)
- `mascara_train_iso`:
  - fecha ≤ corte → `True`;
  - corte < fecha ≤ fin de CLUE → `False`;
  - fecha > fin de CLUE → `True`;
  - el borde exacto `CORTE_TEMPORAL` → `True`.
- Asignación del LSTM congelada: un usuario de CLUE conserva su conjunto, un usuario nuevo va a *train* y una víctima del benchmark nunca queda en *train*.
- `precondicion`, a partir de distintos `particion.json`:
  - correcto → `None`;
  - falta el archivo → *fail-safe*;
  - el corte cambió → *fail-safe*;
  - hay víctimas en *train* de Isolation Forest → *fail-safe*;
  - hay víctimas en *train* del LSTM → *fail-safe*.

### 5.2 No regresión con CLUE solo
- `isoforest_test_results.parquet`: el primer día es 2021-08-03 y la cantidad de filas es igual a la vigente.
- Métricas del gate dentro del ruido entre semillas: ROC-AUC medio cerca de 0,7726 y FPR cerca de 0,0557. Si D5 cambia los escaladores, documentar la diferencia y comprobar que se mantiene dentro de los márgenes (0,02 / 0,01).
- Las salidas HOLDOUT de la tesis no cambian de manera significativa. En caso contrario, documentarlo antes de seguir.

### 5.3 Con datos del agente
- El *pipeline* termina sin `assert` fallidos, con v1 y con v2.
- `particion.json`: `iso_train_filas_agente > 0`, `lstm_train_usuarios_agente > 0`, víctimas en *train* = 0.
- El criterio de promoción **evalúa las métricas**: el motivo empieza con `promueve:` o `rechaza:`, no con `no promueve (fail-safe)`.
- Con el volumen actual, se espera que el candidato quede dentro de los márgenes y se promueva. Si se rechaza, registrar el motivo: puede ser ruido entre semillas, que es una limitación ya documentada del criterio.
- Comprobar la recarga en caliente (`reload_artifacts`) y el registro en `metricas_modelo`.

### 5.4 Criterio de aceptación
Una corrida del **planificador** (no manual) con datos reales del agente produce un candidato cuyo criterio de promoción se resuelve por métricas, con el registro completo. Con eso queda ejercitada de punta a punta la promoción de RF-21, hoy pendiente.

---

## 6. Riesgos

| Riesgo | Mitigación |
|---|---|
| Congelar la asignación del LSTM depende de un archivo de artefactos | Incluirlo en el respaldo; si falta, *fail-safe* en el *pipeline* en lugar de un sorteo nuevo |
| Corregir D5 (escaladores) mueve las métricas de referencia | Hacerlo en un commit separado y volver a medir la línea de base antes de seguir |
| Los datos del agente en *train* cambian la distribución de referencia de percentiles | `export_train_references.py` ya se ejecuta último; verificar que use la misma máscara de *train* |
| Un evento de agente con fecha errónea (≤ fin de CLUE) se toma como CLUE | El exportador ya lo excluye como reproducción; mantener ese filtro |

---

## 7. Impacto en la tesis (cuando esté implementado)
- `producto.tex`, tabla de limitaciones: quitar o reformular «Fragilidad del corte temporal del criterio de promoción» y «Partición del LSTM sensible a usuarios nuevos».
- `producto.tex`, sección 9.2.4, y `conclusiones.tex`, trabajo futuro: actualizar el estado de RF-21 si se logra una promoción real desde el planificador.
- `datos.tex`, sección de partición: describir la partición por origen (CLUE hasta el corte más los datos del agente en *train*).
- `pruebas.tex`: agregar las pruebas nuevas al inventario y actualizar los conteos.
