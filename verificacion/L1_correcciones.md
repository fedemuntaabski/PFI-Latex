# L1 — Correcciones críticas (solo texto LaTeX)

Rama: `e75/correcciones-e50-v2` (creada desde el commit base `6c0d408`).

| N.º | Archivo:línea | Antes (resumido) | Después (resumido) | Estado |
|---|---|---|---|---|
| 1a | chapters/chapter04.tex:370 | `IsolationForest + LSTM Autoencoder (proyecto propuesto)` | `Isolation Forest + LSTM Autoencoder (proyecto propuesto)` | Aplicado |
| 1b | chapters/chapter04.tex (tab:algo-proyecto, Dataset) | ~50M eventos anonimizados, 5.000+ usuarios, Huemer Group | 50 522 931 eventos seudonimizados de 920 usuarios, jul 2017–sep 2022, con \ref a 8.1, 10.6 y 10.7 | Aplicado |
| 1c | chapters/chapter04.tex (Métrica) | `run_regression_test.py` como test de no-regresión | ROC-AUC híbrido HOLDOUT 0,58–0,80 sin país; recall 12 %–30 % sin país, 91 %–99 % con país; FPR 4 %–5 % | Aplicado |
| 1d | chapters/chapter04.tex (Limitación) | Cold-start compartido con la literatura | Detección baja sin cambio de país; LSTM cerca del azar; brecha de dominio (\ref a 10.7.4 y 10.10) | Aplicado |
| 1e | chapters/chapter04.tex (Relación) | "sobre un dataset de producción real en vez de sintético/simulado como..." | "sobre registros reales en lugar de datos sintéticos, a diferencia de..." | Aplicado |
| 2 | chapters/chapter04.tex:215 | Cold-start: usuario nuevo escala a alto sin warm-up | Período de aprendizaje (RF-24 y RF-25): nivel normal, acción limitada a alertar, salvo eventos de archivo | Aplicado |
| 3 | chapters/chapter02.tex:29 | `...: fundamentos y dataset de referencia` | `...: fundamentos` (sin `\label` asociado) | Aplicado |
| 4 | chapters/chapter04.tex:217–220 | Párrafo "Las valoraciones del proyecto propuesto..." repetido | Se borra la segunda aparición; queda la primera (L179) | Aplicado |
| 5 | chapters/pruebas.tex:265–271 | "Una versión preliminar del trabajo planteaba..." | "Como alternativa se evalúa..." (cita `\parencite{Kent2015}` conservada) | Aplicado |
| 6a | chapters/chapter04.tex:~430 | Primer párrafo de 3.6 comenzaba "La encuesta se elabora en Google Forms..." | Comienza "Como complemento al contraste con la práctica profesional... encuesta, elaborada en Google Forms y difundida..." | Aplicado |
| 6b | chapters/chapter04.tex:~437 | Segundo párrafo con la oración "Como complemento..." | Oración borrada; empieza en "Se obtienen 135 respuestas..." | Aplicado |

## Origen de las cifras (1c, de chapters/pruebas.tex, 10.7.3)
- ROC-AUC 0,58 a 0,80: columna Híbrido de `tab:bench-auc` (mínimo 0,58 en S1 similar; máximo 0,80 en S2 k=10 y S3).
- 12 % a 30 %: columna "Alto o superior, sin país" de `tab:bench-recall` (mín. 0,12 en S1 similar; máx. 0,30 en S2 k=10). Coincide con el texto de "Lectura de los resultados". La fila "S2 solo archivos" (0,11) queda fuera, igual que en ese texto.
- 91 % a 99 %: columna "Alto o superior, con país" de `tab:bench-recall` (S2 k=2 a k=10); coincide con el prompt y con el texto.
- FPR 4 % a 5 %: `tab:bench-fpr`, híbrido alto o superior, HOLDOUT 0,04 y período de test de IF 0,05.
- 50 522 931 eventos y 920 usuarios: chapters/datos.tex:16 (coincide con el prompt).

## Notas y diferencias con el prompt
- 10.7.4 ("Lectura de los resultados") no tenía `\label`. Se agregó `\label{sec:lectura-benchmark}` en pruebas.tex para poder usar `\ref`. Sin cambio de formato.
- Las fechas "julio de 2017 a septiembre de 2022" se tomaron del prompt; no se contrastaron con datos.tex.
- RF-24/RF-25 (chapters/requerimientos.tex:183 y 185) coinciden con el texto pedido (umbral configurable, por defecto 20; acción atenuada a `alertar`, nivel informado sin cambio; eventos de archivo con política normal). Sin ajustes.
- 5: el prompt pedía "(Kent, 2015)"; se conservó `\parencite{Kent2015}`.
- `chapters/archivo/obsoleto_e50.tex` aún contiene algunos patrones del grep, pero no se incluye desde `main.tex`; no se tocó.

## Compilación
Receta del README: `pdflatex` → `biber` → `pdflatex` (más una pasada extra).
- Errores: 0. Referencias o citas indefinidas ("??", "Undefined"): 0. Warnings de biber: 0.
- PDF: 278 páginas.

## Verificación final
- grep en los .tex incluidos por main.tex de `5.000+`, `Huemer`, `run_regression_test`, `warm-up`, `Una versión preliminar`, `dataset de referencia`: sin resultados (solo aparecen en `chapters/archivo/obsoleto_e50.tex`, fuera del documento).
- "Las valoraciones del proyecto propuesto": 1 aparición.
