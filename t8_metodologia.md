# T8. Cronograma real de los incrementos (a partir de git)

Fuente única: el historial de git de la rama `entrega/limpieza` (561 commits sin merge al 16/11, `git log --no-merges --date=short --format="%ad %h %s"`) y las ramas y tags del repo. **Herramienta de seguimiento: solo git** (decisión del autor, 16/11): no se usaron Issues, Projects ni tableros externos. Las ramas por funcionalidad (`feature/*`, `analysis/*`, `fix/*`, `e75/*`) hicieron de tablero, y cada documento de sesión en `docs/` registró qué se decidió y por qué.

Método de las fechas: el inicio es el primer commit cuyo asunto nombra el incremento y el fin, el último (ver la columna "Fuente"). Casi toda la historia es lineal: hay 10 merges, en su mayoría de la integración E75 del 09/10. Por eso no se pueden reconstruir las ramas por merge. Las fechas son de commit, no de calendario de trabajo.

Commits por mes: abr 4, may 3, jul 17, ago 119, sep 26, oct 359, nov 46 (al 16/11). Primer commit: 16/04/2026 (`abb678e`).

| Incremento | Inicio | Fin | Alcance | Release / hito | Ajustes que salieron de los resultados | Fuente (inicio → fin) |
|---|---|---|---|---|---|---|
| 0. Datos y modelos base | 03/05 | 04/08 | Fase 1 a 6 sobre CLUE-LDS: limpieza, agregado usuario-día, secuencias, IF y autoencoder LSTM | Artefactos v1 del 02/09 | — | `2d2341e` "Procesamiento de datos (INICIO)" → `0206754` "incluir modelos de ml" |
| 1. CU-01 Detección (API + agente) | 17/07 | 12/08 | API FastAPI con score híbrido, agente Windows (PEP) y mitigación local | Demo del 50 % (merge `demo50%`, 12/08) | — | `c2fe8e5` "Comienzo de la API", `ce8424d` "cambios en agente" (31/07) → merge `demo50%` |
| 2. CU-02 Ajuste de umbrales y políticas | 17/07 | 27/08 | Dashboard, umbrales y acciones editables, niveles configurables (RF-13) | — | — | `263d9b5` "Comienzo Dashboard" → ramas `feature/rf13-niveles-configurables` (27/08) |
| 3. CU-03 Reentrenamiento | 20/08 | 25/08 | Captura de eventos crudos (RF-19), scheduler (RF-20), gate y hot-swap (RF-21), log (RF-22) | Primera corrida automática completa, 25/08 | — | `90160dd` "primeros cambios de cu03" → rama `feature/rf21-metricas-hotswap` (25/08) |
| 4. CU-04 Alta de usuario (arranque en frío) | 20/08 | 27/08 | Estado `en_aprendizaje`, acción atenuada y umbral configurable | — | Umbral de aprendizaje configurable (RF-24/25), `70bf9ec`, 27/08 | `260d330` "primer avance coldstart" → `70bf9ec` "rf24" |
| 5. IAM | 31/08 | 20/10 | Patrón adaptador, mock, Keycloak bidireccional (14/10), Entra ID y proveedores administrables | Release EC2 `20261015-143709-b499fa3` | — | `090ada0` "feat(iam): stub AzureADIAMProvider" → `8e70724` |
| 6. Endurecimiento | 28/08 | 20/10 | Resiliencia agente↔API, dedup, key por agente, hash chain, sesión del dashboard, paquete E75 (merges del 09/10) | Entrega E75 (20/10) | — | `3ec1dfb` "diagnostico resiliencia agente" → `f9f5632` "fix(auth): rechazar la clave de administración…" |
| 7. Despliegue en AWS | 10/09 | 14/11 | Terraform, EC2, Caddy y releases | Releases `20261108-175917-5c36b9d`, `20261114-221354-3634c38` y `20261116-103416-4e85d1d` | Empaquetar `iso_calibracion.json` para el camino `iso` (`5c36b9d`, 08/11) | `34acc33` "terraform" → `8ef581f` "demo/README: release vigente en la EC2" |
| 8. Revisión de modelos | 04/10 | 13/11 | Benchmark DEV/HOLDOUT, gate de no inferioridad, tercer modelo, novedad, etiquetado de triage | Tag `pre-limpieza-entrega` (13/11) | Ver la tabla siguiente | `3bb99a2` "benchmark y validaciones" → `89f6f3a` "Etiquetado CLUE DEV: lote 21" (12/11) |
| 9. Limpieza y entrega | 13/11 | 16/11 | Limpieza de documentos de proceso, devolución del 90 % (este goal) | — | — | tag `pre-limpieza-entrega` → `HEAD` |

## Ajustes que salieron de los resultados del modelo

| Ajuste | Resultado que lo motivó | Fecha | Commit |
|---|---|---|---|
| Gate de promoción por no inferioridad (antes: "iguala o mejora") | El criterio viejo decidió dos rechazos por ruido | 10/10 | `1d55caf` |
| Corte temporal fijo (2021-08-02) y pipeline determinista | Con un corte dinámico, el gate comparaba particiones distintas | 28/10 | `2eb574f` |
| Clasificación única de usuarios en Fase 2 y Fase 6 | Fase 2 y Fase 6 clasificaban distinto | 28/10 | `56b0d86` |
| Solo datos reales: se retiran los escenarios S1–S7 y el gate queda solo por FPR real | Escenarios construidos, sin validez como detección | 29/10 | `04413ec` |
| LSTM fuera del camino por defecto | Permutar la secuencia no cambia el ranking (Spearman 0,989) y sin país queda cerca del azar | 30/10 | `5995111`, `fe750e2` |
| Novedad de recurso como tercer modelo | Criterio F1 en CLUE DEV | 30/10 | `42e56f2` |
| Markov fuera del default (camino `iso`, A2b) | El piso de Markov explicaba 177 de 189 días transitorios | 31/10 | `919de73` |
| LANL 2015 retirado como evidencia | Una sola intrusión, casi toda desde un host | 31/10 | `d7572b1` |
| Umbral de aprendizaje configurable | Datos de la población `clean_valid` (orden de magnitud) | 27/08 | `70bf9ec` |
| Regresión del puntaje contra la simulación del default; duplicados de `clean_valid_*` | El oráculo de Fase 6 estaba desactualizado (T1) | 16/11 | este goal |

## Cómo reproducir

```bash
git log entrega/limpieza --no-merges --date=short --format="%ad %h %s" | sort
git log --merges --first-parent --date=short --format="%h %ad %s" entrega/limpieza
git tag -l --format="%(refname:short) %(creatordate:short)"
git branch -a --format="%(refname:short) %(committerdate:short)"
```
