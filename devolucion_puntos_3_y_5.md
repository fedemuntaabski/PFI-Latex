# Devolución: puntos 3 y 5 de la guía de código

Responde a `guia_codigo_puntos_3_y_5.md`. Trabajo hecho el 15/11/2026 en la rama `entrega/limpieza`, sobre el commit revisado `0f53d62`. Commit con los cambios: `f74fed8` (pusheado a `origin/entrega/limpieza`).

Resumen en una línea por punto:

- **Punto 3 (A6):** confirmado. Se corrigió en el PDP con la opción 1 de la guía. La novedad de carpeta ahora funciona con la telemetría del agente. No cambia nada en CLUE.
- **Punto 5 (A9):** confirmado. La suite ahora corre el camino por defecto (`iso`). El benchmark fija el camino y lo registra. Se volvió a medir la latencia con evidencia guardada en el repo.

Al final hay una lista de los cambios para la tesis, con el texto propuesto.

---

## 1. Punto 3: novedad de carpeta con la telemetría del agente

### 1.1 Qué se confirmó

| Afirmación de la guía | Resultado |
|---|---|
| Con el agente, `recurso_de` devolvía siempre `carpeta:.` | Confirmado. `{'file': 'informe.docx', 'carpeta': 'confidencial'}` daba `carpeta:.`. |
| `carpeta` solo entraba como `carpeta_vigilada:` informativo | Confirmado. Iba a la explicación y a la cola por cuenta, pero no a `nuevos`: no contaba para el nivel ni para el cuantil. |
| En CLUE la carpeta sale de `params.path` | Confirmado. Además, `data/clue.json` no tiene ningún campo `file` ni `carpeta`. Por eso el cambio **no puede mover** las cifras de CLUE. |
| Procesos y destinos no se validaron con ningún conjunto de datos | Confirmado. CLUE no los tiene. |

**Hallazgo nuevo, importante para el texto.** El agente no recorre subcarpetas. `FileSystemCollector` usa `os.scandir` sin recursión y solo mira archivos. `carpeta` es la etiqueta fija de cada carpeta vigilada (`AGENT_WATCH_DIRS`). Entonces, con el agente, el conjunto de carpetas posibles es la lista de carpetas vigiladas, no el árbol de directorios que el usuario recorre. La novedad de carpeta solo dice "primer acceso de este usuario a una carpeta vigilada", y eso importa justamente para una carpeta sensible como `Sueldos 2026` en la demo.

### 1.2 Estado real del cuantil de novedad (Redis de producción)

Lectura de solo lectura sobre el Redis de Upstash, el mismo que usa la EC2 (`infra/README.md`, `infra/secrets.tf`). La clave es `scoring:umbral_movil:novedad_recursos`:

| Dato | Valor |
|---|---|
| Muestras totales | 133 (del 20/09 al 09/11/2026) |
| Muestras en los 30 días previos al 15/11 | **7** (mínimo exigido: 50) |
| Muestras con valor > 0 en esa ventana | 1 |
| Clave de la variante con decaimiento | vacía |

**Conclusión:** `umbral_nuevos()` devuelve `None` (arranque en frío). **En la instancia, la novedad nunca elevó el nivel.** Solo aparece en la explicación. Esto vale para los tres tipos de recurso, no solo para las carpetas.

### 1.3 Qué se cambió

- `api/app/scoring/novedad_service.py`, en `recurso_de`: para los eventos `file_*`, si `file` no trae ruta, se usa `params.carpeta`. Si tampoco viene, queda `"."` como antes. Si `file` trae ruta, sigue mandando la ruta.
- `api/app/scoring/hybrid_service.py`: un mismo primer acceso ya no aparece dos veces en la explicación (una como `carpeta:<x>` y otra como `carpeta_vigilada:<x> (informativo)`). La cola por cuenta sigue recibiendo `carpeta_vigilada`, igual que antes.
- Pruebas nuevas en `api/tests/test_novedad_service.py`:
  - casos unitarios de `recurso_de` con el contrato del agente;
  - una prueba de extremo a extremo (`POST /eventos`). En ella, tres días en `Administracion/Proveedores` y después un acceso a `Administracion/Sueldos` producen `carpeta:Administracion/Sueldos` en `nuevos`, con una sola línea en la explicación.

### 1.4 Efectos y riesgos

- **CLUE (2,66 %, FPR DEV):** sin cambios. La entrada es `params.path`, y CLUE no trae ni `file` ni `carpeta`. No hizo falta volver a correr `puntuar.py`.
- **Instancia:** no cambia mientras no se despliegue una release nueva (ver §3). Cuando se despliegue, el texto del dashboard cambia:
  - antes: «primer acceso a carpeta_vigilada:Administracion/Sueldos 2026 (informativo)»;
  - después: «primer acceso a carpeta:Administracion/Sueldos 2026».

  El nivel no cambia mientras el cuantil siga en arranque en frío. El guion de la demo (`demo/guion_demo.md:25`) sigue valiendo en lo que narra.
- **Tasa de novedad:** puede subir un poco, porque cada carpeta vigilada cuenta como recurso. El efecto es acotado: son pocas por agente y fijas por configuración.

---

## 2. Punto 5: con qué camino corren las pruebas y la latencia

### 2.1 Qué se confirmó

| Afirmación de la guía | Resultado |
|---|---|
| `conftest.py` fijaba `SCORING_TERCER_MODELO=lstm` | Confirmado: la suite corría la versión 1. |
| `.env:43` tiene `SCORING_TERCER_MODELO=markov` | Confirmado (es una decisión del 29/10, anterior al cambio de default a `iso`). |
| `bench_rnf01_latencia.py` no fijaba el camino | Confirmado. Sin la variable exportada, la API toma `markov` del `.env`. |
| La medición del 15/11 de la tesis no está en el repo | Confirmado. Solo existía `bench_rnf01_resultado.json`, del 06/10 (v1). `health.detalle` no dice qué camino estaba activo. |

**Hallazgo adicional sobre el benchmark.** Los eventos `file_*` del benchmark mandaban `params.path = "C:/demo/docs/..."`. Ese no es el contrato del agente, que manda `file` y `carpeta`. Ahora los manda como el agente.

### 2.2 Qué se cambió

**Suite de la API.**
- `conftest.py` fija `SCORING_TERCER_MODELO=iso`, el camino por defecto.
- Las 18 pruebas propias de la versión 1 piden la fixture nueva `camino_v1`. La fixture fija `lstm`, recarga los artefactos y al final deja los anteriores. Son estas:
  - 2 de `test_artifacts_carga.py`;
  - 6 funciones de `test_gate_promocion.py`, 7 casos contando los parametrizados;
  - 4 funciones de `test_markov_service.py`, 5 casos;
  - 2 de `test_novedad_service.py`;
  - 1 de `test_reentrenamiento_backup.py`;
  - 1 de `test_reentrenamiento_scheduler_decision.py`.
- Antes de cambiar nada se midió cuánto de la suite ya funcionaba con `iso`: **529 de 547 pasaban**. Las 18 que fallaban son exactamente las que suponen la versión 1: el criterio de promoción del LSTM, la carga de los artefactos del LSTM, los perfiles Markov parcheados sobre los artefactos de v1 y el "flag apagado por defecto" de la novedad.
- TensorFlow se sigue importando temprano en `conftest.py` si está instalado, por el orden de DLL en Windows.

**Benchmark (`scripts/evidencia/bench_rnf01_latencia.py`).**
- Argumento nuevo `--camino {iso,markov,lstm}`, por defecto `iso`. Se pasa a la API que levanta el script.
- El JSON de salida registra `condiciones.camino` y `condiciones.fecha`.

**`docs/contexto/testing.md`:** conteos y cobertura actualizados.

**Sin tocar:** `.env`. Es local y no está versionado, y `demo/README.md:135` ya documenta que trae `markov` y que hay que exportar `iso` para replicar la EC2. Si se quiere alinear, basta con cambiar la línea 43 a `SCORING_TERCER_MODELO=iso`.

### 2.3 Resultados

**Suite de la API con artefactos, en el camino por defecto:** 548 aprobadas, 0 fallidas y 0 omitidas. Son las 547 de antes más la prueba nueva de carpeta.

**Cobertura** (`scripts/cobertura_local.ps1`, 15/11/2026, con el mismo alcance que la tesis):

| Componente | Pruebas | Sentencias | % líneas | % líneas y ramas |
|---|---|---|---|---|
| API (PDP) | 548 | 3 289 | **95,29** | 94,01 |
| Agente (PEP) | 200 | 1 124 | **91,90** | 91,20 |
| Total | 748 | 4 413 | **94,43** | 93,28 |

Como comparación, con `pytest --cov=app` (sin los módulos de `scripts`), la API daba 95,91 % de líneas en v1 y 94,07 % con `iso` antes de los cambios. Con la suite nueva, que corre `iso` y además las 18 pruebas de v1, da 95,95 %.

**Latencia RNF-01.** Las condiciones son las del texto: 1000 eventos y 50 de calentamiento, 5 usuarios, Redis en memoria, sin PostgreSQL y el mismo equipo. La medición fue el 15/11/2026, cerca de las 23 h ART.

| Corrida | Camino | Media | Mediana | p95 | p99 | Máx. | ev/s |
|---|---|---|---|---|---|---|---|
| Evidencia (seed 42) | `iso` | 12,58 | 12,41 | **13,40** | **15,15** | 56,92 | 79,5 |
| Repetición (seed 43) | `iso` | 12,45 | 12,28 | 13,26 | 14,25 | 56,06 | 80,3 |
| Repetición (seed 44) | `iso` | 12,50 | 12,33 | 13,33 | 14,08 | 55,04 | 80,0 |
| Control (seed 42) | `markov` | 12,67 | 12,51 | 13,42 | 14,64 | 58,52 | 79,0 |
| Tesis actual (15/11, camino no registrado) | ¿`markov`? | 12,83 | 12,59 | 13,71 | 18,24 | 55,28 | 78 |

Los valores están en ms. Hay dos archivos de evidencia versionados: `scripts/evidencia/bench_rnf01_resultado_iso_20261115.json` y `scripts/evidencia/bench_rnf01_resultado_markov_20261115.json`. Las repeticiones con seeds 43 y 44 quedaron fuera del repo.

Lectura de los resultados:
- `iso` y `markov` no se distinguen en latencia. La cifra de la tesis queda dentro de la variación entre corridas, así que la conclusión (cumple con amplio margen) no cambia.
- Lo que cambia es la trazabilidad. Ahora hay un JSON con el camino declarado.
- En la corrida de evidencia, los cinco eventos más lentos fueron de 56,9, 21,1, 19,5, 19,4 y 18,2 ms. Son aislados y de tipos `file_*` distintos.

---

## 3. EC2

- **No se pudo consultar la instancia.** No hay credenciales de AWS en esta máquina: tanto `aws sts get-caller-identity` como el servidor MCP de AWS devuelven `NoCredentials`, y renovarlas requiere un `aws login` interactivo. No se prendió nada y no hay nada que apagar.
- **Camino de la EC2:** `iso`, según `demo/README.md:135` (release `20261114-221354-3634c38`). El punto 5 no afecta a la instancia.
- **Redis de la EC2:** es Upstash, el mismo que se leyó en §1.2. El dato "la novedad nunca elevó el nivel" vale para la instancia.
- **El cambio del punto 3 todavía no está en la EC2.** Hace falta una release nueva para que la novedad de carpeta funcione allí. Recomendación: desplegarla solo si se va a grabar o regrabar la demo con ella; antes, ensayar el texto del detalle de Lucía (§1.4). Después, apagar con `apagar.ps1`.

---

## 4. Otros hallazgos (sección C de la guía)

- **M14 (547 frente a 508 + 30).** En una copia limpia del repositorio en Windows, sin artefactos, el resultado es 508 aprobadas, 30 omitidas y **9 fallidas**. Era lo mismo en `0f53d62`, antes de estos cambios, así que no lo introdujeron ellos. Ahora son 31 omitidas, por la prueba nueva, que también se omite sin artefactos.
  - Las 9 son 3 de `test_health_ready.py`, 4 de `test_reload_artifacts_endpoint.py`, 1 de `test_hybrid_service_backdated.py` y 1 de `test_historial_scores_explicacion.py`.
  - Causa: arrancan la API sin `artefactos_stub` y el lifespan corta porque falta `scripts/models/isolation_forest.joblib`.
  - La tabla de resultados de `pruebas.tex` dice "508 aprobadas, 30 omitidas, **0 fallidas**" para la configuración de CI. Hay que verificarlo en Linux o corregirlo (en Windows no da 0).
- **Pruebas de `test_markov_service.py`:** parchean `artifacts.markov` sobre artefactos ya cargados. Si los artefactos cargados son los de `iso`, el scoring entra a la rama de Markov y después a la de `iso`, y falla con `UnboundLocalError: con_historia` (`hybrid_service.py:403`). En producción no puede pasar, porque `load_artifacts` deja `markov` o `nudos_iso`, nunca los dos. Por eso esas pruebas usan `camino_v1`.
- **Regresión del score** (`run_regression_test.py`, camino v1 por diseño): **falla, pero ya fallaba antes**. Se corrió con los cambios y sobre `0f53d62`, en un worktree limpio, y las dos salidas son **idénticas al dígito**.
  - Hay 6 discrepancias de cobertura «parcial», todas en `digital-harlequin-possum-procuratorfiscal`: diferencias de 0,055 a 4,47 puntos. La peor es la del 2020-11-19 (esperado 13,68, obtenido 9,21).
  - La convergencia del historial completo pasa: `big-maroon-lynx-radiocontroller`, 0,31 frente a una tolerancia de 0,5.
  - Los cambios no la causan: el de `hybrid_service.py` solo filtra la lista `explicacion`.
  - El script dice que la cobertura «parcial» se validó con 8 de 8 fechas y diferencia 0 «pre-Fase 2a». Esa referencia offline quedó desactualizada frente a algún cambio posterior del scoring. Queda como pendiente aparte.

---

## 5. Cambios para la tesis (texto propuesto)

Los números de línea son de `G:\Latex\PFI-Latex\chapters\` al 15/11. Las cifras nuevas salen de §2.3.

### 5.1 `pruebas.tex`: latencia RNF-01 (líneas 189-222)

**Línea 190.** Agregar el camino declarado y la evidencia al final del párrafo:

> … sin base de datos y con el camino por defecto (Isolation Forest y novedad, fijado explícitamente en la prueba). La tabla~\ref{tab:rnf01} presenta los resultados, medidos el 15 de noviembre de 2026; la medición queda registrada en el repositorio junto con el camino evaluado.

**Tabla `tab:rnf01`:**

| Métrica | Antes | Después |
|---|---|---|
| Media | 12,83~ms | 12,58~ms |
| Mediana | 12,59~ms | 12,41~ms |
| Percentil 95 | 13,71~ms | 13,40~ms |
| Percentil 99 | 18,24~ms | 15,15~ms |
| Máximo | 55,28~ms | 56,92~ms |
| Errores | 0 de 1000 | 0 de 1000 |
| Rendimiento secuencial | 78 eventos por segundo | 80 eventos por segundo |

**Línea 222.** Reemplazar «los valores más altos (entre 20,7 y 55,3~ms) son aislados» por:

> los valores más altos (entre 18,2 y 56,9~ms) son aislados

Opcionalmente, agregar después de esa oración:

> Dos repeticiones con otras semillas dieron percentiles 95 de 13,26 y 13,33~ms y percentiles 99 de 14,25 y 14,08~ms; el perfil de Markov, medido en las mismas condiciones como control, no se distingue del camino por defecto (13,42 y 14,64~ms).

### 5.2 `requerimientos.tex:245` y `conclusiones.tex:26` y `:43`

- `p95 de 13,7~ms y p99 de 18,2~ms` → `p95 de 13,4~ms y p99 de 15,2~ms`.
- `conclusiones.tex:43`: `13,7\,ms` → `13,4\,ms`.

### 5.3 `pruebas.tex`: inventario, resultados y cobertura

- **Línea 56:** `747 pruebas automatizadas, 547 de la API y 200 del agente` → `748 pruebas automatizadas, 548 de la API y 200 del agente`. Agregar a continuación:

  > La suite de la API se ejecuta con el camino por defecto; las 18 pruebas propias de la versión~1 (carga de artefactos del LSTM, criterio de promoción y caminos alternativos) fijan ese camino de forma explícita.

- **Línea 92:** `547 aprobadas, 0 fallidas, 0 omitidas` → `548 aprobadas, 0 fallidas, 0 omitidas`.
- **Línea 94 (CI):** verificar antes de dejar «0 fallidas» (ver §4, M14). En Windows, en una copia limpia, da 508 aprobadas, 31 omitidas y 9 fallidas.
- **Tabla `tab:cobertura-codigo`:**
  - API: `547 & 3\,287 & \textbf{95,25} & 93,86` → `548 & 3\,289 & \textbf{95,29} & 94,01`
  - Total: `\textbf{747} & 4\,411 & \textbf{94,40} & 93,17` → `\textbf{748} & 4\,413 & \textbf{94,43} & 93,28`
  - Agente: sin cambios.
- **Después de la tabla**, una frase sobre el camino:

  > La medición corresponde a la suite ejecutada con el camino por defecto; las pruebas de la versión~1 y de los caminos alternativos se incluyen con su camino fijado explícitamente.

- **`conclusiones.tex:32`:** `747 … 547 … 95,25 %` → `748 … 548 … 95,29 %`.

### 5.4 `datos.tex:132` (`sec:novedad-recurso`) y `pruebas.tex:338`

Agregar después de «a partir de los parámetros que el agente ya envía con cada evento»:

> Con la telemetría del agente, la carpeta es la carpeta vigilada en la que ocurre el evento, porque el agente no recorre subcarpetas; en CLUE-LDS, el primer nivel de la ruta del archivo. Los destinos de red y los procesos solo existen en la telemetría del agente y no se validaron sobre ningún conjunto de datos.

Y, en la misma sección o en las limitaciones, el estado real:

> En la instancia desplegada, el cuantil poblacional de recursos nuevos no alcanzó el mínimo de 50 muestras en la ventana de 30 días (7 muestras al 15 de noviembre de 2026), por lo que la detección de novedad no elevó el nivel de ningún usuario: su efecto observable fue la explicación «primer acceso a…».

Revisar también, por coherencia con este último dato:
- `datos.tex:128` («eleva el nivel a alto por medio de la regla de piso»);
- `pruebas.tex:289` y `:338`.

El mecanismo está bien descrito, pero en la instancia no llegó a activarse.

---

## 6. Pendientes

1. Confirmar el resultado de CI en Linux (M14), o corregir «0 fallidas» en `pruebas.tex:94`.
2. Desplegar en la EC2 si se quiere la novedad de carpeta en la demo (§3).
3. Opcional: alinear `.env:43` con `iso`.
4. La regresión de la Fase 7 (`run_regression_test.py`) falla desde antes de estos cambios, con 6 discrepancias en cobertura parcial (§4). Si la tesis dice que esa regresión pasa, hay que revisarlo.
5. Fuera de alcance, siguen abiertos de la sección C de la guía: A1, A5, M1, M2, M6, M8, M10, M12, y el texto obsoleto de `regla_piso.condicion`.
