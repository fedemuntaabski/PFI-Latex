# Guía para el repo de código: puntos 3 y 5

Esta guía acompaña a `revision_caps7_13_bibliografia.md`. Cubre los dos puntos que se resuelven en el repo de código, no en la memoria LaTeX.

| Punto del resumen | Hallazgo en el informe | Tema |
|---|---|---|
| 3 | A6 | Novedad de carpeta |
| 5 | A9 | Qué camino corren las pruebas y la medición de latencia |

Repo: `G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad`, en adelante `repo/`. Commit revisado: `0f53d62`.

La sección C, al final, deja anotados los otros puntos de código del informe para más adelante.

---

## A. Punto 3: la novedad de carpeta no ve carpetas con la telemetría del agente

### A.1 Qué pasa

1. **El agente manda solo el nombre del archivo.** En `repo/agent/collectors.py:189-191` arma:
   ```python
   {"file": name, **self._extra}   # _extra = {"carpeta": "<etiqueta relativa>"} (línea 128)
   ```
2. **El PDP saca la carpeta del nombre del archivo.** En `repo/api/app/scoring/novedad_service.py`, `recurso_de()` hace:
   ```python
   if tipo in TIPOS_ARCHIVO and params.get("file"):
       return f"carpeta:{posixpath.dirname(...file...) or '.'}"
   ```
   Como `file` no trae ruta, `dirname` devuelve `""`. Entonces el recurso queda **siempre `carpeta:.`**:
   - el primer día con historia aparece una vez como nuevo;
   - después ya está en `vistos` y nunca vuelve a ser nuevo.
3. **El parámetro `carpeta` del agente se usa en otro lado.** Solo entra en `informativos()`, como `carpeta_vigilada:<x>`. Eso va a la explicación, pero **no** a `nuevos`: no cuenta para el nivel ni para el cuantil.
4. **En CLUE la carpeta sí existe.** Sale de `params.path`, primer segmento (la rama del final de `recurso_de`). Por eso la validación en CLUE sí midió carpetas.
5. **Procesos y destinos no se validaron en ningún conjunto de datos.** CLUE no tiene procesos ni destinos de red. Esas dos clases solo existen con la telemetría del agente.

### A.2 Cómo confirmarlo, sin tocar nada (unos 10 minutos)

```powershell
cd G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad
python -c "import sys; sys.path.insert(0,'api'); from app.scoring.novedad_service import recurso_de; print(recurso_de({'type':'file_written','params':{'file':'informe.docx','carpeta':'confidencial'}}))"
# Esperado hoy: carpeta:.
```

Después, revisar en Redis de la instancia (o el local) si el cuantil de novedad llegó a tener datos:

- La clave es `scoring:umbral_movil:novedad_recursos`. La define `NOVEDAD_KEY` en `novedad_service.py`.
- Si tiene menos de 50 muestras en los últimos 30 días, `umbral_nuevos()` devuelve `None`.
- En ese caso **la novedad nunca elevó el nivel** en la instancia.
- Ese dato importa para la tesis: hoy afirma que el camino por defecto es "IF + novedad".

### A.3 Opciones para resolverlo (elegir una)

| Opción | Cambio | Costo | Efecto en la tesis |
|---|---|---|---|
| **1. Usar `carpeta` en el PDP** (recomendada) | En `recurso_de`, para los eventos `file_*`, usar `params.get("carpeta")` cuando `dirname(file)` es vacío. | Una línea, más un test en `api/tests/test_novedad_service.py`. | La clase carpeta pasa a funcionar con el agente. La validación sigue siendo la de CLUE, así que hay que aclararlo. |
| 2. Que el agente mande una ruta relativa | En `collectors.py`, mandar `file = f"{carpeta}/{name}"`. | Cambia el contrato del evento. Afecta `_derivar_detalle`, el dashboard, los tests del agente y la demo. | Igual que la opción 1, pero más invasiva. |
| 3. No tocar el código | Nada. | — | Corregir el texto: "con la telemetría del agente, la novedad cubre procesos y destinos; las carpetas solo en modo informativo". |

Esbozo de la opción 1:

```python
if tipo in TIPOS_ARCHIVO and params.get("file"):
    d = posixpath.dirname(str(params["file"]).replace(chr(92), "/"))
    return f"carpeta:{d or params.get('carpeta') or '.'}"
```

Test mínimo:

```python
def test_carpeta_del_agente_sin_ruta():
    ev = {"type": "file_written", "params": {"file": "a.txt", "carpeta": "confidencial"}}
    assert recurso_de(ev) == "carpeta:confidencial"
```

Riesgos de la opción 1:

- Cambia qué recursos se cuentan, así que puede subir la tasa de novedad en la instancia.
- No altera las cifras de CLUE (2,66 %), porque CLUE entra por `params.path`.
- Después del cambio, correr la suite y `scripts/benchmark/puntuar.py` para confirmar que la tasa de falsos positivos en DEV no se mueve.

### A.4 Qué llevar a la tesis después

Según la opción elegida:

- Con la opción 3: ajustar `datos.tex` §8.3.4 y `pruebas.tex` §10.5.2 ("destinos de red, procesos y carpetas").
- Con cualquier opción: agregar una línea con el estado real del cuantil en la instancia (si llegó o no a 50 muestras).

---

## B. Punto 5: las pruebas y la latencia no corren el camino por defecto

### B.1 Qué pasa

1. **Las pruebas fijan la versión 1.** `repo/api/tests/conftest.py:17` hace `os.environ["SCORING_TERCER_MODELO"] = "lstm"`. Por eso:
   - la mayoría de las 547 pruebas, y el 95,25 % de cobertura, ejercitan la **versión 1**;
   - el camino `iso` solo se prueba en `test_camino_iso.py`, `test_sin_lstm.py`, `test_novedad_service.py` y `test_markov_service.py`.
2. **El `.env` local fija Markov.** `repo/.env:43` tiene `SCORING_TERCER_MODELO=markov`.
3. **La API lee ese `.env` al arrancar.** `repo/api/app/scoring/main.py:32` hace `load_dotenv(_ROOT_ENV)`. No pisa variables que ya estén en el entorno, pero si el proceso no trae `SCORING_TERCER_MODELO`, toma `markov` del `.env`.
4. **El benchmark de latencia no fija el camino.** `repo/scripts/evidencia/bench_rnf01_latencia.py:53-64` (`spawn_api`) define el entorno de la API, pero **no** fija `SCORING_TERCER_MODELO`. Si se corrió sin exportarla, la medición del 15/11 que la tesis llama "con el camino por defecto" (`pruebas.tex:190`) corrió con **Markov**.
5. **La medición del 15/11 no está guardada en el repo.** `scripts/evidencia/bench_rnf01_resultado.json` es del 6/10 (versión 1: p95 de 14,91 ms y p99 de 148,87 ms). Los valores 13,71 / 18,24 ms del texto no figuran en el repo. Además, `health.detalle` no dice qué camino estaba activo.

### B.2 Cómo confirmarlo

```powershell
cd G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad
Select-String -Path .env -Pattern TERCER_MODELO
# ¿Dónde quedó la salida de la corrida del 15/11? Buscar un JSON nuevo o un log:
Get-ChildItem -Recurse -Filter *rnf01* | Sort-Object LastWriteTime | Select-Object -Last 5 FullName,LastWriteTime
```

Si no aparece el resultado del 15/11, o no se sabe con qué variable corrió, hay que volver a medir (B.3).

### B.3 Cómo resolverlo

**1. Fijar el camino en el benchmark.** Es una línea en `spawn_api`; conviene permitir que se pase por parámetro:

```python
env["SCORING_TERCER_MODELO"] = a.camino  # nuevo argumento --camino, por defecto "iso"
```

Y registrar el camino en el JSON de salida: `"camino": env["SCORING_TERCER_MODELO"]`.

**2. Volver a medir y guardar la evidencia:**

```powershell
python scripts/evidencia/bench_rnf01_latencia.py --camino iso
```

Guardar el resultado como `bench_rnf01_resultado_iso_20261115.json` y actualizar `pruebas.tex` (tabla `tab:rnf01`) si cambian los valores.

**3. El `.env` local.** Tiene que estar alineado con el camino por defecto:
- dejar `SCORING_TERCER_MODELO=` vacío o `iso`;
- o documentar que el desarrollo local usa Markov a propósito.

**4. Las pruebas.** Hay dos opciones:
- **(a) Mínima:** declararlo en la tesis (§10.2.4 y la tabla de cobertura). Por ejemplo: "la suite corre la versión 1; el camino por defecto lo cubren N pruebas específicas".
- **(b) Mejor:** parametrizar las pruebas de extremo a extremo de *scoring* para correr con `lstm` e `iso`. Es un `pytest.mark.parametrize` sobre la variable de entorno, más `reload_artifacts()`. Así la cobertura y la E2E reflejan el camino vigente.

  Con la opción (b), volver a medir la cobertura con `scripts/cobertura_local.ps1` y actualizar `tab:cobertura-codigo`.

**5. Contar las pruebas del camino `iso`** para poner la cifra en la tesis:

```powershell
cd api; python -m pytest --collect-only -q tests/test_camino_iso.py tests/test_sin_lstm.py tests/test_novedad_service.py | Select-Object -Last 3
```

### B.4 Qué llevar a la tesis después

- La latencia RNF-01 medida con el camino declarado, y la fecha del JSON.
- Una frase en §10.2.1 o §10.2.4 que diga con qué camino corren la suite y la cobertura.

---

## C. Otros puntos de código del informe, para más adelante

| Id | Qué mirar | Dónde |
|---|---|---|
| A1 | El *blend* personal (`W_PERSONAL_MAX=0,7`) no está en la simulación. ¿Qué comparó la reproducción de 462.024 eventos? | `hybrid_service.py:376-403`, `scripts/benchmark/puntuar.py:17`, `scripts/export_iso_calibracion.py`, `scripts/evidencia/gap_5a_replay.py` |
| A5 | El país lo autodeclara el agente; la demo llega a crítico con `--vpn` | `agent/collectors.py:566`, `scripts/ensayo_demo_pep.py:25`, `scripts/demo_exfil.py` |
| M1 | 51 frente a 63 usuarios de DEV; definición de la tasa de falsos positivos frente a "algún evento en alto" | `scripts/benchmark/puntuar.py`, `scripts/benchmark/generar_split.py` |
| M2 | Las 6 acciones válidas (incluye `notificar_admin`) | `api/app/scoring/config_store.py:174` |
| M6 | `hour > 20`: fuera de horario desde las 21:00 | `api/app/scoring/features.py:194` (y el notebook de la Fase 3) |
| M8 | Verificar el control de acceso en la release del 14/11 | Instancia |
| M10 | Cobertura «En calibración»: `routes.get_score` usa `determine_coverage` (bloques del LSTM) | `api/app/scoring/routes.py`, `coverage.py` |
| M12 | Correr HOLDOUT una vez con el camino `iso` | `puntuar.py --holdout` |
| M14 | 547 frente a 508 + 30: identificar las 9 restantes | `pytest --collect-only` con y sin artefactos |
| — | Texto obsoleto de `regla_piso.condicion` | `models/score_hibrido/config_score_hibrido.json` |
