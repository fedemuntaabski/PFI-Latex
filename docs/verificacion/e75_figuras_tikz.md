# Verificación e75 — figuras TikZ y ajustes de texto

Rama `e75/cap7-8-11-12`. Commits nuevos: `e0fe7ce` (texto: cap. 8, cap. 11 y biblio) y `b789198` (figuras en TikZ). Sin push, sin trailers.

## 0. Chequeos de solo lectura (repo de código, `e75/entrega`)

### 0a. Clave `session:` de Redis
Se escribe **sin expiración nativa**: `get_redis_client().set(clave, json.dumps({"role": role, "expira_epoch": time.time() + SESION_TTL_SECONDS}))` (`api/app/scoring/auth.py:114-116`), con `SESION_TTL_SECONDS = 8 * 3600` (`auth.py:100`). El comentario de `auth.py:110-112` lo confirma («Epoch-en-valor… sin TTL nativo»). La clave se valida comparando `time.time() >= data["expira_epoch"]` (`auth.py:129`). → Se aplican las ediciones 2a y 2b.

### 0b. SQL 001–010 (`api/app/scoring/sql/`)
Todas las tablas: `id BIGSERIAL PRIMARY KEY`, `created_at TIMESTAMPTZ NOT NULL DEFAULT now()`. Todas tienen `ENABLE ROW LEVEL SECURITY` salvo `historial_scores`.

| Tabla | Columnas (tipo, nulidad, default) | Restricciones / otros |
|---|---|---|
| `historial_scores` (001, 009) | uid TEXT NN; fecha DATE NN; risk_score_hibrido DOUBLE PRECISION; nivel_sugerido TEXT; cobertura TEXT NN; accion_sugerida TEXT NN; cierre_de_dia BOOLEAN NN DEFAULT TRUE; explicacion JSONB; motivo TEXT | UNIQUE(uid, fecha); índice (uid, fecha DESC) |
| `eventos_crudos` (005, 007) | uid TEXT NN; ts TIMESTAMPTZ NN; tipo_evento TEXT NN; payload JSONB NN; row_hash TEXT; prev_hash TEXT | disparador `trg_eventos_crudos_hash_chain` (BEFORE INSERT, por fila) fija row_hash y prev_hash; cadena por uid, hash génesis de 64 ceros |
| `drift_alerts` (004) | uid TEXT NN; fecha DATE NN; lado TEXT NN ('iso' \| 'lstm'); features JSONB NN; corrimiento_max DOUBLE PRECISION NN | — |
| `historial_politicas` (002) | form TEXT NN ('umbrales' \| 'acciones' \| 'reentrenamiento'); actor TEXT; before_json JSONB; after_json JSONB NN | — |
| `historial_reentrenamientos` (003) | fecha DATE NN; cantidad_eventos INTEGER NN; variacion_metrica TEXT NN; actor TEXT | — |
| `historial_agent_keys` (008) | agent_id TEXT NN; key_hash TEXT NN (sha256 hex); accion TEXT NN ('alta' \| 'revocacion'); actor TEXT | — |
| `metricas_modelo` (006, 010) | modelo TEXT NN ('iso' \| 'lstm'; 010 agrega 'benchmark_dev'); metrica_valor DOUBLE PRECISION (010: nullable); cantidad_muestras INTEGER (010: nullable); es_vigente BOOLEAN NN DEFAULT false; rol TEXT; metricas JSONB; motivo TEXT | índice (modelo, es_vigente) |

Comentarios de 010 sobre las columnas nuevas:
- `rol`: `'candidato' | 'vigente'` (NULL en filas viejas).
- `metricas`: detalle de la decisión (AUC por escenario, FPR ≥ alto, n).
- `motivo`: texto de la decisión del criterio de promoción; en un fail-safe se inserta solo la fila del candidato con `metrica_valor`/`cantidad_muestras` NULL y el motivo.
- Las filas viejas (`iso`, `lstm`) quedan como historial sin migrar.

## 1. Figuras en TikZ
Un archivo por figura en `images/diagramas/tikz/` (`despliegue_local.tex`, `despliegue_aws.tex`, `er_scoring_eventos.tex`, `er_config_modelos.tex`) más `estilos.tex` compartido. Cada `\includegraphics` se reemplazó por `\input` dentro del mismo `figure`; `\caption`, `\label` y «Fuente: elaboración propia.» no se tocaron. Los PDF/PNG viejos siguen en `images/diagramas/v75/` sin referenciarse. Preámbulo (`config/symbols.tex`): se agregaron `\usetikzlibrary{positioning,arrows.meta,shapes.geometric,fit,calc,backgrounds}` y `adjustbox` (ya instalado en MiKTeX) para limitar cada figura a `\textwidth` y 0,6 de la altura de la página.

- 7.1: recuadro «Equipo Windows» (agente PEP, API uvicorn, dashboard Vite); «POST /eventos (loopback)» y «consulta cada 2 s»; Redis (Upstash) y PostgreSQL (Supabase) como cilindros; Gemini, SMTP e «IAM simulado / Keycloak» punteados con «opcional».
- 7.2: agente y navegador → HTTPS → Caddy dentro de la instancia EC2 (t3.small) dentro de «AWS us-east-2»; almacén de parámetros y S3 (con «despliegue por SSM») hacia la instancia; Redis, PostgreSQL (São Paulo) y Gemini (opcional) a la derecha; GitHub Actions («integración continua (no despliega)») aparte, punteado. Sin CloudFront.
- 8.1 y 8.2: columnas y anotaciones tomadas literalmente de 0b (incluye `rol`, `metricas`, `motivo`, `alta | revocacion`, `disparador`, `iso|lstm|benchmark_dev`, `candidato|vigente`). Relaciones punteadas «uid (lógica)» y «lógica». Sin números de migración.

## 2. Ediciones de texto
| Ed. | Archivo | Estado |
|---|---|---|
| 2a «quince tipos de clave» | `chapters/datos.tex:196` | Aplicada |
| 2b fila «Sesiones del panel» tras «Claves de agentes» (8 horas, o hasta el cierre de sesión) | `chapters/datos.tex` (tabla 8.V) | Aplicada |
| 2c fila `metricas_modelo` (tabla 8.IV) | `chapters/datos.tex:169` | Aplicada (010 lo confirma: resultado y motivo del criterio de promoción) |
| 2d `(sección~\ref{sec:benchmark})` | `chapters/e50_mercado.tex` (debilidad 11m) | Aplicada; `sec:benchmark` es la sección «Evaluación con escenarios etiquetados» (`pruebas.tex:406`) |
| 2e `year = {2026}` en `FRED2026DGS10` | `biblio.bib` | Aplicada |

## 3. Compilación y verificación
`pdflatex`, `biber`, `pdflatex`, `pdflatex` sin errores (`^!` = 0). `main.pdf`: 262 páginas físicas, pie «Página N de **260**».

| Verificación | Resultado |
|---|---|
| Páginas impresas de las figuras | 7.1 → p. 104; 7.2 → p. 105; 8.1 y 8.2 → p. 115 (las dos en la misma página; páginas físicas 106, 107 y 117) |
| «evidencia», «verificado», «CloudFront», «unico», «009», «007», «logica» en esas páginas | 0 |
| «desplegado» en la p. 106 física | 1, **no es de la figura**: es el texto «La tabla 7.VII contrasta lo diseñado con lo desplegado.» (párrafo siguiente) |
| «revocacion» en la 8.2 | Presente |
| «rol», «metricas», «motivo» en `metricas_modelo` | Presentes |
| «[s.f.]» en todo el documento | 0 |
| «quince tipos de clave» | 1 |
| «Sesiones del panel» | 1 |
| «??» | 0 |
| Páginas con texto debajo de «Página N de M» | 0 |
| Total «de N» | 260 |

PNG para revisar: `docs/verificacion/figuras_tikz/p106-106.png` (7.1), `p107-107.png` (7.2), `p117-117.png` (8.1 y 8.2).

## Observaciones para el autor
1. El pie de la figura 7.2 conserva el título «Arquitectura de despliegue en la nube, con el estado de cada recurso» (se pidió no tocar el `\caption`). Ahora la figura ya no muestra estados; conviene quitar «, con el estado de cada recurso». Lo mismo cabría revisar en el texto que la introduce.
2. Las tablas de 8.1/8.2 quedan escaladas al ancho de página (~0,85): el texto es legible pero chico. Si se prefiere más grande, hay que separar cada figura en dos filas.
3. Pendientes de la tanda anterior (sin cambios): fuente del EMBI, y el «291 usuarios» de `datos.tex:62` frente a los 908 de la síntesis.
