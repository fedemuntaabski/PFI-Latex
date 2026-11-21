# Devolución de la entrega del 90 %: tareas en el repo de código

Repo: `G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad`, rama `entrega/limpieza` (último commit `f74fed8`).
Compañero: `correcciones_devolucion_90_latex.md`, donde las tareas Lx refieren a su checklist (§11).

Formato de cada tarea: **por qué** (ítem del profe) → **estado actual** → **qué hacer** → **hecho cuando** → **qué vuelve al LaTeX**.

Reglas que siguen vigentes de la revisión de modelos: no usar HOLDOUT para elegir; fijar por escrito el criterio de decisión **antes** de medir; ninguna métrica con datos sintéticos o inyectados; verificar por SHA-256 que los artefactos de producción no cambien en los experimentos.

| # | Tarea | Prioridad | Destraba en LaTeX |
|---|---|---|---|
| T1 | Regresión del puntaje en verde | **Obligatoria** (lo pide el profe) | L8 |
| T2 | Pruebas del frontend | **Obligatoria** (lo pide el profe) | L9 |
| T3 | `icacls` real en el runner Windows | Opcional | L10 |
| T4 | Cambios de modelo ("qué cambiarían primero") | Alta (4a y 4b); el resto es trabajo futuro | L13, L14 |
| T5 | Tabla de datasets y perfilado de campos de CLUE | Alta | L5 |
| T6 | CI con `startup_failure` | Alta | L10 y los "en verde" del cap. 10 |
| T7 | Cifras pendientes para el cap. 10 | Media | L8, L9, L16 |
| T8 | Datos reales para el capítulo de metodología | Alta | L7 |

---

## T1. Regresión del puntaje en verde (obligatoria)

**Por qué:** el profe pide que para la entrega final esté resuelta "al menos la regresión del puntaje". Hoy el LaTeX la declara "limitación conocida y no prueba superada" (`pruebas.tex:441`).

**Estado actual:**
- `scripts/run_regression_test.py` reproduce el historial real de tres usuarios por `POST /eventos` y compara contra el valor fuera de línea de Fase 6.
- `run_regression_test.py:64-65` fuerza `SCORING_TERCER_MODELO=lstm`, es decir, **prueba el camino v1 y no el camino por defecto vigente** (IF + novedad).
- El oráculo (Fase 6) se generó **antes** de corregir el tratamiento de los eventos duplicados, y por eso quedan 6 diferencias, todas de un mismo usuario en días de cobertura parcial (entre 0,06 y 4,47 puntos).
- Requisitos previos: `scripts/export_train_references.py` y `scripts/extract_user_events.py`. Hay que correrlo con `SCORING_API_KEY` y `SCORING_ADMIN_KEY` vacías (ver el docstring).

**Qué hacer** (las dos partes; la (b) es la que importa para la memoria):

- **(a) Regenerar el oráculo v1** con los duplicados corregidos (`export_train_references.py`, `extract_user_events.py` y la parte de Fase 6 que produce `risk_score_hibrido` offline) y volver a correr `run_regression_test.py`. Así se cierra la limitación tal como está escrita. Ojo: regenerar el oráculo **no** debe tocar los artefactos de producción (verificar por SHA-256 antes y después).
- **(b) Regresión del camino por defecto.** Un script o test hermano (por ejemplo `scripts/run_regression_default.py` o un test marcado `slow`) que reproduzca el mismo historial con `SCORING_TERCER_MODELO` sin setear y compare el puntaje y el nivel por evento, o por usuario-día cerrado, contra la **simulación fuera de línea del camino por defecto**, la misma que dio el 2,66 % (`scripts/fase6_sin_lstm.py`, confirmar). La línea base personal debe apagarse igual que hoy (`W_PERSONAL_MAX=0`), porque la simulación no la reproduce.
  - Tolerancia escrita antes de correr: por ejemplo, 0 diferencias de nivel y |Δpuntaje| ≤ 0,5.
  - Si aparecen diferencias, investigar y corregir la causa; no ajustar la tolerancia para que pase.
- Documentar el comando exacto en `docs/` (o en el README de scripts). Si el tiempo de ejecución lo permite, sumarlo al job `api` de `.github/workflows/ci.yml`; si no, dejarlo como verificación local documentada (y decirlo así en la memoria).

**Hecho cuando:** (b) da 0 diferencias fuera de tolerancia y (a) da 0 diferencias o las que queden tienen una causa explicada, con salida guardada en `reports/`.

**Vuelve al LaTeX:** usuarios, eventos, diferencias y tolerancia de (a) y (b); qué camino evalúa cada una; y si corre en CI o en local. Se usa en `pruebas.tex:417, 441` y en la fila 9 de `tab:cumplimiento-objetivos`.

---

## T2. Pruebas automatizadas del frontend (obligatoria)

**Por qué:** el profe pide resolver "las pruebas del frontend". Hoy la memoria dice que no las tiene "por declaración" (`pruebas.tex:443`).

**Estado actual:**
- `frontend/package.json` solo tiene los scripts `dev`, `build`, `lint` y `preview`; no hay *runner* de pruebas.
- El job `frontend` de `ci.yml` (líneas 23-40) corre `npm ci`, `lint` y `build`.
- Hay lógica comprobable aunque "no haya lógica de negocio":
  - `src/api/client.ts` (117 líneas): `ApiError`, `get`, `put`, `post`, `del`, `logout` y `postWithKey`, con validación zod;
  - `src/api/*.ts`: esquemas zod de cada respuesta;
  - componentes de mapeo (`RiskBadge`, `CoverageBadge`, `LearningProgressBadge`);
  - formularios con validación (`AccionesForm`, `AprendizajeThresholdForm`, `RetrainingPeriodForm`, umbrales).

**Qué hacer** (lo mínimo que convierte "sin pruebas" en una suite real; Vite ya está, así que vitest no agrega otra herramienta de build):
1. devDependencies: `vitest`, `@testing-library/react`, `@testing-library/jest-dom`, `jsdom` y `@vitest/coverage-v8`. Script `"test": "vitest run --coverage"` y un bloque `test` en `vite.config.ts` (`environment: 'jsdom'`).
2. Pruebas, en orden de valor:
   - **`client.ts`:** envía la cabecera o el *token* esperado; un 401 limpia la sesión o redirige; un error HTTP produce `ApiError` con el código; una respuesta que no cumple el esquema zod falla (mockear `fetch`).
   - **Esquemas zod** de `scoring`, `usuarios` y `umbrales`: aceptan un payload real de la API (tomarlo de una respuesta guardada) y rechazan uno con campos faltantes.
   - **Badges:** cada nivel (bajo/medio/alto/crítico) y cada cobertura (completa/parcial/sin score) muestra el texto y la clase correctos, incluida la nota «En calibración».
   - **Formulario de umbrales/acciones:** rechaza umbrales no crecientes o fuera de 0–100 y no llama a `put` si la validación falla.
   - **Guardia de sesión en `App.tsx`:** sin sesión redirige al *login*.
3. Agregar `- run: npm test` al job `frontend` de `ci.yml` y subir la cobertura como artifact, igual que el agente.
4. No hace falta llegar al 85 % en el frontend (el objetivo 9 se mide en la API y el agente), pero hay que reportar la cifra.

**Hecho cuando:** `npm test` pasa en local y en CI, con N pruebas y la cobertura de líneas reportada.

**Vuelve al LaTeX:** N pruebas, archivos, cobertura de líneas y si corre en CI. Se usa en `tab:inventario-pruebas`, `tab:ejecucion-pruebas`, `tab:cobertura-codigo`, los totales "748" (`pruebas.tex:56, 147, 456`, `conclusiones.tex:32`) y la viñeta de `pruebas.tex:443`.

---

## T3. `icacls` real en Windows (opcional)

**Por qué:** el profe lo lista entre las limitaciones declaradas (`pruebas.tex:444`: las pruebas de mitigación usan un `icacls` simulado).

**Estado actual:** `agent/enforcement.py` y `agent/tests/test_enforcement_revert.py`. El job `agent-windows` de `ci.yml` (líneas 113-141) ya corre en `windows-latest`.

**Qué hacer:** una prueba marcada (por ejemplo `@pytest.mark.windows_real`, que se omita fuera de Windows) que:
- cree una carpeta temporal;
- aplique la denegación real con el código del agente;
- verifique que el acceso falla;
- revierta y compare la ACL contra la copia previa (`icacls <dir> /save` antes y después).

Probar los dos caminos: con `SeRestorePrivilege` (restauración exacta) y sin él (`/remove:d`), si el runner lo permite. Si el runner no corre como administrador, cubrir solo el camino sin privilegio y declararlo.

**Hecho cuando:** la prueba pasa en el job `agent-windows`.

**Vuelve al LaTeX:** cambiar `pruebas.tex:444` y la fila 4 de `tab:cumplimiento-objetivos`.

---

## T4. Modelo: lo que "cambiarían primero"

**Por qué:** el profe pide discutir qué cambiarían primero para acercarse a las metas. La memoria debe responderlo argumentado (LaTeX §9.3); cuanto de esto se ejecute antes de la entrega, más fuerte la respuesta.

### T4a. Confirmar el etiquetado con un analista (alta)
- **Estado:** `docs/etiquetado/` contiene `protocolo_etiquetado.md`, `etiquetas_provisionales.csv`, `planilla_analista.csv`, `cruce.md` y `resultado_provisional.md`. Un solo etiquetador; precisión de alertas del 8,6 % (IC 3,9–15,0 %); 0 de 58 alertas de solo-novedad merecían revisión.
- **Qué hacer:** enviar la planilla al analista, recibirla y recalcular `cruce.md` con la etiqueta confirmada. Registrar el acuerdo con la etiqueta provisional (kappa) y los casos corregidos (por ejemplo C282 y C352, que `resultado_provisional.md` §4 ya marca como candidatos).
- **Hecho cuando:** existe `resultado_confirmado.md` con las cifras finales, o la decisión explícita de citarlo como provisional.
- **Vuelve al LaTeX:** quitar "provisional" en §8.5 y §9.1, o mantenerlo.

### T4b. Detección de novedad: endurecer o dejarla informativa (alta)
- **Estado:** `api/app/scoring/novedad_service.py:158-162`; el umbral es el cuantil móvil poblacional (`SCORING_NOVEDAD_NIVEL_FPR=0.05`, `_VENTANA=30`, `_MIN=50`). Si lo supera, eleva el nivel a alto por la regla de piso. En el etiquetado, ninguna de sus 58 alertas propias merecía revisión, y casi todas eran archivos o carpetas que el usuario crea en su raíz.
- **Qué hacer**, con el criterio escrito antes:
  - opción 1: no contar como "nuevo" lo que el propio usuario creó ese día;
  - opción 2: restringir la elevación a carpetas preexistentes y destinos de red;
  - opción 3: FPR de 0,01;
  - opción 4: novedad solo informativa (en la explicación, sin elevar el nivel).
  - Medir en DEV: FPR ≥ alto, días al cierre y alertas de novedad que merecían revisión según las etiquetas congeladas. **Aviso de sobreajuste:** las etiquetas se hicieron sobre DEV, así que elegir con ellas es optimista. Declararlo, y si hay presupuesto, confirmar una sola vez en HOLDOUT (T4f).
- **Hecho cuando:** hay una decisión documentada (en `docs/`), con la tabla de opciones y el criterio.
- **Vuelve al LaTeX:** 9.2.2/8.3.4 (descripción de la novedad), `tab:efecto-default` y §9.3.

### T4c. Quitar el país del modelo y poner una regla explícita (media)
- **Estado:** `n_distinct_countries` es una de las 8 variables (`api/app/scoring/features.py:28, 232`). El 99,95 % de los eventos de CLUE tiene el país desconocido. En la demostración, el nivel crítico se alcanza al activar un país simulado (`producto.tex:210`).
- **Qué hacer:** reentrenar IF sin esa variable (con el *pipeline* de Fase 4 y el corte fijo), medir el efecto en la FPR de DEV y agregar en el motor de decisión una regla de ubicación configurable (país nuevo para el usuario → nivel mínimo X, con explicación). Ajustar `scripts/demo_exfil.py` y el test e2e si el guion dependía del país.
- **Hecho cuando:** el modelo nuevo pasa el criterio de promoción (no inferioridad de la FPR), la regla está probada y la demo sigue alcanzando el nivel crítico por un motivo explicado.
- **Vuelve al LaTeX:** 8.3.1, la fila "El país actúa como interruptor" de `tab:limitaciones-producto` y el trabajo futuro.

### T4d. Variable de compartición externa / tipo de operación (media, trabajo futuro si no llega)
- **Estado:** el etiquetado sugiere que compartir hacia afuera es el punto flojo (2 de 5 casos revisables sin alerta; hipótesis con 5 casos).
- **Qué hacer:** agregar al agregado diario la cantidad de eventos de compartición o link público (los tipos CLUE correspondientes) y evaluar como en T4c.

### T4e. Piloto de telemetría propia de *host* (alta para el trabajo futuro, no llega a la entrega)
- **Estado:** brecha de dominio de 53,66 % frente a 4,13 % (LANL 2017). Es la limitación más grave.
- **Qué hacer:** definir el protocolo de un piloto (cuántos equipos, cuántas semanas, consentimiento según la Ley 25.326 y la LCT, y cómo se registran los incidentes confirmados). Escribirlo en `docs/` aunque no se ejecute, porque la memoria lo cita como primer paso.

### T4f. Evaluación única del camino por defecto en HOLDOUT (media)
- **Estado:** HOLDOUT se usó una sola vez, con la v1; el camino por defecto solo se midió en DEV (`pruebas.tex:448`).
- **Qué hacer:** **una** corrida del camino por defecto final (después de T4b y T4c, si se hacen), con el criterio fijado antes. No iterar sobre el resultado.
- **Vuelve al LaTeX:** 10.7 y la viñeta de `pruebas.tex:448`.

---

## T5. Tabla de datasets y perfilado de CLUE (alta)

**Por qué:** el profe pide revisar los datasets de referencia (CERT) y dice que un análisis previo habría anticipado el 99,95 % de país desconocido.

**Estado:** el relevamiento ya existe, pero disperso:
- `DATASETS.md`;
- `Datasets reales complementarios a CLUE-LDS.md` (23/10);
- las notas `08_datasets_reales.md`, `20_datasets_alternativos_livianos.md` y `24_datasets_reales_licencias.md`, que **solo** están en la copia de trabajo `data/sandbox/20261029/h4/repo/docs/revision_modelos_20261028/` (no versionada; `docs/revision_modelos_20261028/` del repo solo tiene `etiquetado`).

**Qué hacer:**
1. Consolidar en un solo archivo versionado (por ejemplo `docs/data/relevamiento_datasets.md`) la tabla de LaTeX §4b, con las columnas Origen, Dominio, Etiquetas, Ubicación, Acceso/licencia y Decisión, más la fuente de cada celda. Incluir CERT r4.2–r6.2 con su motivo de descarte (sintético) y su referencia (Glasser y Lindauer, 2013).
2. Script corto de perfilado de completitud sobre `data/clue.json` (o el procesado): % de nulos o desconocidos por campo (`location.countryCode`, `uidType`, etc.), cardinalidad por campo y distribución de eventos por tipo. Salida en `reports/`. Esto confirma el 99,95 % y deja el perfilado que el profe dice que faltó.
3. `docs/data/arquitectura_data.md` ya no describe `clue.json` como sintético (verificado el 16/11), así que no hay nada que corregir ahí.

**Hecho cuando:** existe la tabla con su fuente y el reporte de completitud.

**Vuelve al LaTeX:** la tabla de 2.2.4 y la cifra del perfilado (`datos.tex:179`).

---

## T6. Integración continua con `startup_failure` (alta)

**Por qué:** sin CI verde, la memoria no puede decir "en verde" ni sumar los jobs nuevos (T1–T3).

**Estado:** desde el 08/11 todas las ramas terminan en `startup_failure` sin crear jobs. Se descartaron `ci.yml`, los permisos y la facturación; hay una consulta abierta con el soporte de GitHub (`LIMITACIONES_Y_ESTADO.md` §0.3). En `G:\pfi\` hay `audit-ci-preflight.md` y `ci.yml.borrador`.

**Qué hacer:**
- seguir la consulta de soporte;
- probar un workflow mínimo (`hello.yml` con un solo `echo`) en una rama, para aislar si falla la cuenta o el archivo;
- revisar si alguna action pinneada (`actions/checkout@v4`, `setup-node@v4`, `setup-python@v5`, `upload-artifact@v4`) o un `uses:` de terceros quedó bloqueado por una política de la organización o del repo (Settings → Actions → "Allow actions…");
- revisar que el YAML no use una feature nueva no soportada.

**Hecho cuando:** una corrida completa con los 4 jobs (más los nuevos) termina aprobada.

**Vuelve al LaTeX:** 10.2.3 (fecha, jobs y resultado) y la síntesis.

---

## T7. Cifras pendientes para el capítulo 10

De `revision_modelos_latex.md` (pendientes para el autor), todavía sin resolver:
- **Desglose de las 30 pruebas omitidas:** `pytest -rs` en la configuración de CI. Hoy el texto dice 25 por modelos, 3 por datos v2 y 2 por Markov (`LIMITACIONES_Y_ESTADO.md` §0.3); confirmarlo.
- **Cantidad de archivos** (44 y 15) y **sentencias** (2 808, 1 107 y 3 915) del inventario y la cobertura: re-medir con la suite actual (`scripts/cobertura_local.ps1`).
- **Verificación del despliegue sobre la release del 14/11:** SHA-256 de los artefactos, TLS, códigos HTTP y agente real. Hoy esos detalles son de la release anterior.
- **Latencia en local:** el texto dice 13,4 ms; en `LIMITACIONES_Y_ESTADO.md` figura 13,71 ms. Confirmar cuál es la medición vigente del camino por defecto.

**Vuelve al LaTeX:** 10.2.1, 10.2.4, 10.4.1 y 10.4.3.

---

## T8. Datos reales para el capítulo de metodología

**Por qué:** el profe pide el cronograma real de cada incremento, la herramienta de seguimiento y los ajustes que surgieron de los resultados del modelo.

**Qué hacer** (solo lectura del git más lo que sepa el autor):
1. `git log --date=short --format="%ad %s"` y `git log --merges` → fechas de inicio y fin de cada incremento, por los primeros y últimos commits de CU-01/02 y CU-03/04, IAM, endurecimiento y revisión de modelos.
   - Ya relevado: primer commit el 16/04/2026; commits por mes: abr 4, may 3, jul 17, ago 119, sep 26, oct 359, nov 40.
   - Falta ubicar cada incremento en esa línea.
2. `git branch -a` y `git tag` → ramas por funcionalidad y releases (tag `pre-limpieza-entrega`; releases desplegadas en la EC2, por ejemplo la del 14/11).
3. Herramienta de seguimiento: si se usó GitHub Issues o Projects, `gh issue list --state all --limit 500` y `gh project list` dan cantidades y fechas. Si fue otra (Notion, Trello, planilla), exportar una captura.
4. Lista de "ajustes derivados de resultados" con la fecha del commit de cada uno: retiro de S1–S7, LSTM fuera del camino por defecto, Markov, criterio de promoción, corte fijo, clasificación por comportamiento y umbral de aprendizaje configurable.

**Hecho cuando:** existe una tabla Incremento | Inicio | Fin | Alcance | Release | Ajustes, con la fuente de cada fecha.

**Vuelve al LaTeX:** el capítulo nuevo de metodología (L7).

---

## Fuera de este MD

- La entrevista PyME y la usabilidad con usuarios son gestión, no código (LaTeX §5 y §7.5).
- Nada de lo de acá toca los artefactos de producción sin pasar por el criterio de promoción; los experimentos van en `data/sandbox/`.
