# Revisión crítica: capítulos 7 a 13 y bibliografía

Fecha: 15/11/2026. Rama: `revision-modelos-latex`. No se modificó ningún `.tex` ni el `.bib`.

Alcance:

| Cap. | Archivo |
|---|---|
| 7 Arquitectura | `chapters/arquitectura.tex` |
| 8 Datos | `chapters/datos.tex` |
| 9 Producto | `chapters/producto.tex` |
| 10 Pruebas | `chapters/pruebas.tex` |
| 11 Mercado | `chapters/e50_mercado.tex` |
| 12 Negocio | `chapters/negocio.tex` |
| 13 Conclusiones | `chapters/conclusiones.tex` |

Código contrastado: `G:\pfi\Agente-...\` (abreviado `repo/`). Commit: `0f53d62`.

**Qué está bien (verificado).**

- Cuentas financieras recalculadas a mano: VAN de los tres escenarios, TIR base del 56 %, recuperos, necesidad de fondos, equilibrio por año, margen de USD 320, LTV/CAC, tramos de nube y punto de corte de USD 2.370.
- Cuentas de latencia: 20 × 124 ms y 78 ev/s.
- Cobertura ponderada del 94,40 %.
- Particiones: 49.048 + 12.236 y 291 + 617 + 12 = 920.
- Endpoints: 4 + 16 + 12 + 2 = 34.
- Versiones de librerías, Python, Node, Terraform y región `us-east-2`.
- TTL (8 h, 6 h, 30 min / 60 s) y 20 reintentos en Redis.
- Los 49 DOIs del `.bib` resuelven.
- No hay citas indefinidas.

---

## 1. Prioridad ALTA: problemas de fondo (método o veracidad)

### A1. Las cifras del modelo no describen el sistema que corre: falta el *blend* personal

- **Producción.** `api/app/scoring/hybrid_service.py:376-403` mezcla el riesgo de Isolation Forest con el percentil personal. El peso llega hasta `W_PERSONAL_MAX = 0,7` (línea 129) una vez que el usuario tiene 20 eventos. **Después** aplica la calibración por cuantiles.
- **Simulación.** `scripts/benchmark/puntuar.py:17` dice textualmente: *"El blend personal NO se reproduce"*.
- **Cifras afectadas.** Esa simulación produce 2,66 % / 4,95 %, 15,17 %, el criterio de promoción (gate) y el sandbox 2,95 % frente a 2,66 %. Todas miden un sistema sin el componente que pesa 70 % en producción.
- **Calibración.** `scripts/export_iso_calibracion.py` calcula los nudos (80,8 / 95,0 / 99,0) sobre el puntaje ISO **crudo**. En producción se aplican al puntaje **mezclado**. La promesa "medio, alto y crítico ≈ 20 %, 5 % y 1 % de los días" (`datos.tex:126`, `pruebas.tex:334`) no vale para lo que ve el usuario.
- **Texto.** `datos.tex:128` ("el puntaje del usuario es el de Isolation Forest calibrado...") omite el *blend*. `producto.tex:56` sí lo menciona. Son inconsistentes entre sí.
- **Reproducción.** `pruebas.tex:364` dice: "Una reproducción completa de 462.024 eventos reales a través de la API coincidió sin diferencias con la simulación". Según `corregir_en_latex/revision_modelos.md:125`, esa reproducción es de la **Etapa 8 (31/10)**, con el camino ISO + Markov + novedad. El camino por defecto actual se adoptó después (Etapa 9). Hoy la frase está bajo "Resultado del camino por defecto" y sugiere que valida las cifras vigentes.

**Revisar en código:**

- ¿Cómo dio 0 diferencias si la API mezcla y la simulación no? Quizá la reproducción comparó el nivel, el puntaje de un usuario nuevo o algo con el *blend* desactivado.
- Rehacer la reproducción con `SCORING_TERCER_MODELO=iso`, o declarar el alcance.
- Decidir entre dos caminos: (a) incorporar el *blend* a `puntuar.py`, o (b) declarar en 8.3 y 10.4 que las métricas excluyen el componente personal.

### A2. "15,17 % → 2,66 %" atribuye la mejora a la novedad, pero la novedad solo puede subir el nivel

`pruebas.tex:289` dice: "Usado solo, el detector marcaría demasiados días; en el camino completo la tasa baja al 2,66 %".

- La novedad solo eleva al piso (`hybrid_service.py:449-453`). Agregarla **no puede bajar** la tasa de falsos positivos.
- La baja viene de la **calibración** por cuantiles. El 15,17 % es ISO sin calibrar: `docs/contexto/estado_modelos.md:56`.
- **Acción:** reescribir la frase atribuyendo la baja a la calibración.

### A3. "Falsos positivos" sin etiquetas, y una meta que se cumple casi por construcción

- Sin etiquetas, toda alerta sobre días reales se cuenta como falso positivo. Eso supone que CLUE DEV no contiene ataques. Hay que declararlo en 10.4, o llamar a la métrica "tasa de alertas en nivel alto".
- La meta "≤ 5 % en alto" (`pruebas.tex:312`) coincide con el nudo 0,95 de la calibración, que fija alto ≈ 5 % de los días de entrenamiento. Cumplirla no es evidencia independiente; es casi una consecuencia del diseño. Conviene decirlo, sobre todo junto con A1.

### A4. La comparación con la versión 1 mezcla particiones y usa un lenguaje ya retirado

`pruebas.tex:380` compara el 2,66 % en DEV con "la versión 1, sobre HOLDOUT, ... 4 % en los negativos".

- "Negativos" remite a los escenarios construidos, que ya se retiraron.
- HOLDOUT es otra partición.
- La cifra comparable existe: **v1 en DEV, 5,59 % / 10,09 %** (`docs/contexto/estado_modelos.md:24`). Usar esa.

### A5. La demo y la verificación llegan a crítico por el país simulado, justo la limitación declarada

- `scripts/ensayo_demo_pep.py:25` dice: *"El país simulado lleva a 'critico' (~98): dos países distintos"*. Lo mismo pasa con `scripts/demo_exfil.py --vpn RU`.
- La prueba E2E usa "6 eventos desde un país simulado" (`pruebas.tex:161`).
- La tesis presenta la escalada a crítico (prueba E2E, agente real a los 36 s, `pruebas.tex:240`) como validación de la cadena. Por otro lado, `producto.tex:208` declara "El país actúa como interruptor".
- **Hay que decir explícitamente que el nivel crítico de la demo lo dispara el cambio de país.**
- El país **lo autodeclara el agente**: lo lee de la configuración o de un archivo de *override* (`agent/collectors.py:566-577`). No se deriva de la IP. La tesis no lo menciona, y es relevante para el modelo de amenaza.

### A6. La novedad de carpeta no funciona con la telemetría real del agente

- El agente envía solo el **nombre** del archivo: `agent/collectors.py:189-191`, `{"file": name, "carpeta": ...}`.
- `novedad_service.recurso_de` toma `posixpath.dirname(params["file"])`. Con un nombre sin ruta, el resultado es siempre `carpeta:.`. El parámetro `carpeta` que manda el agente no se usa para el recurso.
- Consecuencia: hay una sola "carpeta" por usuario y nunca aparece una nueva.
- La validación en CLUE usó `params.path` (carpetas). CLUE **no tiene** procesos ni destinos de red. Por lo tanto, los recursos "proceso" y "destino" del agente nunca se validaron, y la clase carpeta queda degenerada en producción.
- El cuantil poblacional exige 50 muestras en 30 días. Con 1 a 7 usuarios desplegados, ¿llegó a activarse alguna vez en la instancia? Verificarlo en Redis o en los logs.
- **Texto afectado:** `datos.tex:132` y `pruebas.tex:336` ("destinos de red, procesos y carpetas").

### A7. El etiquetado propio contradice la justificación de la novedad

`docs/contexto/estado_modelos.md` (etiquetado provisional) registra **0 de 58** alertas "solo novedad" que merecían revisión, frente al 13,5 % de las de origen ISO.

Se decidió no integrar el etiquetado; es una decisión del autor. Aun así, la tesis afirma que la novedad "cubre lo que Isolation Forest no ve" (`pruebas.tex:336`) sin evidencia a favor y con evidencia propia en contra. Como mínimo, suavizar la afirmación.

### A8. Una decisión de modelo tomada en función de la demo

`pruebas.tex:368` dice: calibrar en arranque en frío "no se adoptó ... porque dejaba la demostración sin nivel crítico". También `markov_service.py:63` (comentario "11i_ enmienda 2").

Ante un evaluador, elegir la configuración por su efecto en la demo es un punto débil. Opciones: quitar ese motivo, justificarlo en términos de sensibilidad (por ejemplo, "ceguera ante un ataque en los primeros días"), o asumirlo explícitamente.

### A9. Las pruebas y la medición local no corren el camino por defecto

- **Pruebas.** `api/tests/conftest.py` fija `SCORING_TERCER_MODELO=lstm` (`docs/contexto/testing.md:5`). Las 547 pruebas y el 95,25 % de cobertura ejercitan sobre todo la **versión 1**. El camino por defecto se prueba solo en `test_camino_iso.py`, `test_sin_lstm.py` y `test_novedad_service.py`. La tesis solo aclara que la E2E fija `lstm` (`pruebas.tex:161`).
- **Medición local.** El `.env` local tiene `SCORING_TERCER_MODELO=markov` (`.env:43`). La latencia RNF-01 del 15/11 dice "con el camino por defecto" (`pruebas.tex:190`). Verificar que esa corrida desactivó la variable. Si no, la medición es del camino Markov.

---

## 2. Prioridad MEDIA: inconsistencias entre capítulos o con el código

| # | Dónde | Problema | Qué revisar o corregir |
|---|---|---|---|
| M1 | `pruebas.tex:357` frente a `datos.tex:126` y `pruebas.tex:444` | DEV tiene 63 usuarios, pero la tabla dice "51 usuarios". Para el camino por defecto, la tasa de falsos positivos (2,66 %) es idéntica a "días con algún evento en alto" (2,66 %); para Markov difieren (5,37 % frente a 14,04 %). | Definir cada métrica: ¿es por día cerrado o por evento? ¿Por qué 51? Revisar en `puntuar.py` si es casualidad o la misma métrica. |
| M1b | `pruebas.tex:454`, `conclusiones.tex:47` | Se llama "oscilación dentro del día" al porcentaje de días con algún evento en alto. Eso no es oscilación. | Oscilación sería, por ejemplo, la diferencia entre "algún evento" y "al cierre" (2,66 − 1,29). Renombrar. |
| M2 | `producto.tex:28-49` frente a `conclusiones.tex:27` | La tabla tiene 5 acciones y las conclusiones dicen "seis acciones". El código tiene 6: `config_store.py:174` incluye `notificar_admin`. | Agregar `notificar_admin` a la tabla 9.I. |
| M3 | `arquitectura.tex:42`; `e50_mercado.tex:19,66`; `negocio.tex:35` | Se habla de "variables que más influyen o contribuyen" al puntaje de Isolation Forest. El código (`explainability.py`) usa el z-score frente a la población, no una contribución al puntaje. `producto.tex:56` lo describe bien. | Cambiar a "variables que más se desvían de la población". |
| M4 | `datos.tex:179` | "No identifica directamente procesos inusuales o destinos de red". La detección de novedad (8.3.4) lo contradice. | Restringir la frase a Isolation Forest. Lo mismo en `chapter04.tex:504` (cap. 3, de la otra sesión). |
| M5 | `producto.tex:204` (Arranque en frío) | El tratamiento declarado es el "período de aprendizaje". Pero el aprendizaje dura 20 eventos (p25 = 35 min) y el arranque en frío, 3 días. Además, los eventos de archivo **no** se atenúan (`hybrid_service.py:184-191`). | Reformular: la atenuación cubre una fracción del período de 3 días. |
| M6 | `datos.tex:79` | Dice "después de las 20:00", pero el código usa `hour > 20` (`features.py:194`): cuenta como fuera de horario desde las 21:00. | Elegir: corregir el texto ("a partir de las 21:00") o el código. |
| M7 | `pruebas.tex:227` frente a `negocio.tex:68` | Latencia: 16–17 comandos a Redis y 4 viajes a PostgreSQL. Negocio: "17 comandos y **una** escritura en PostgreSQL". | Unificar (afecta poco al costo). |
| M8 | `producto.tex:123,129` frente a `pruebas.tex:241` | El rechazo de la clave de administración se da como parte de la release vigente, pero el control de acceso se verificó en la "release anterior". | Verificar en la release del 14/11 o decirlo. |
| M9 | `conclusiones.tex:26` | El objetivo 3 (latencia ≤ 500 ms) figura como cumplido, aunque en la configuración de referencia (nube) el p95 es 3,1 s. | Justificar en una línea por qué la meta aplica al cómputo, o marcarlo como parcial. |
| M10 | `producto.tex:246` (Nota «En calibración») | En el camino `iso`, `hybrid_service.py:360` fija la cobertura según 3 días de historia, no según el LSTM. Pero `coverage.py` (vía `routes.get_score`) usa bloques (`chunks`) del LSTM. | Ver cuál alimenta el dashboard. Puede ser un bug de pocas líneas, más fácil de corregir que de declarar. |
| M11 | `producto.tex:90` | El Isolation Forest vigente fue **rechazado** por la regla de entonces y quedó cargado por accidente. Se adopta "por consistencia". Nunca pasó un criterio de promoción. | Explicitarlo como decisión manual, o pasarlo por el criterio actual (el sandbox ya lo hizo con un candidato). |
| M12 | `datos.tex:126` frente a `pruebas.tex:444` | HOLDOUT "reservada para la evaluación final", pero el camino vigente nunca se evaluó en HOLDOUT. | Correr HOLDOUT una vez con el camino por defecto, o decir que la evaluación final está pendiente. |
| M13 | `pruebas.tex:111` frente a `pruebas.tex:130` | "Umbral del 85 % de cobertura combinada" (integración continua de la API) frente a "el umbral se fija sobre la cobertura de líneas". `ci.yml:94` usa `--fail-under=85` combinado; el agente, por líneas. | Aclarar qué umbral aplica a cada componente. La frase "admite una diferencia de hasta dos puntos" no se entiende. |
| M14 | `pruebas.tex:56,94` | 547 pruebas en total, pero en integración continua 508 + 30 = 538. No se explican las 9 restantes. Además, la integración continua corre 4 archivos del agente, ¿se cuentan en las 508? | Explicar la diferencia. |
| M15 | `conclusiones.tex:64,70` | El "límite de intentos en el inicio de sesión" no figura en la tabla de limitaciones. Los ítems 4 y 6 repiten la seudonimización. | Unificar. |
| M16 | `negocio.tex:350` | "Mes 16, a mitad del segundo año": el mes 16 es el cuarto mes del año 2. | Corregir la expresión. |
| M17 | `negocio.tex:166` | Riesgo país "650 pb, su máximo del año". Al 2/10 era cierto; a la fecha de entrega el máximo de 2026 ya es de unos 790 pb (cierre de octubre). | Fecharlo: "al 2 de octubre de 2026". |
| M18 | `datos.tex:39` | La fila de LANL 2015 cita a Larroche pero no al conjunto. `Kent2015` está definida y no se usa. | Agregar `\parencite{Kent2015}`. |
| M19 | `datos.tex:72` | "Tasa de falsos positivos en personas 5,1 % frente a 0,9 %" sin indicar camino, partición ni nivel. | Completar. |
| M20 | `arquitectura.tex:127` | "Autenticación mutua a nivel de aplicación", pero el servidor se autentica por TLS, en la capa de transporte. | Reformular como "autenticación de ambas partes". |
| M21 | `pruebas.tex:372` | La cola por cuenta es "la única cifra confirmatoria", pero está apagada por defecto, sin explicar por qué. | Una línea de justificación. |
| M22 | `e50_mercado.tex:97` | El título "Cruz de Porter" es poco usual. | "Cinco fuerzas de Porter". |
| M23 | `e50_mercado.tex:90,103` | Los beneficios de Sentinel en E5 y la inclusión de Defender en Business Premium no tienen fuente. | Citar la documentación de Microsoft o remitir a la sección del estado del arte. |

**Código (cosmético o menor, no afecta al texto):**

- `models/score_hibrido/config_score_hibrido.json`: `regla_piso.condicion` describe la regla de la v1 (con LSTM).
- `drift_alerts.lado` y `metricas_modelo.modelo` siguen como `iso | lstm`. Ya figuran como pendientes en la bitácora.
- `.env` local: contraseñas triviales (`ADMIN_PASSWORD=asd`). Está ignorado por git. Verificar que el modo estricto también las rechace, no solo las "por defecto o de ejemplo".

---

## 3. Bibliografía

### 3.1 Método

- Cruce de claves citadas frente a definidas: **0 citas indefinidas**. Hay **13 entradas definidas sin citar**; no se imprimen porque no hay `\nocite`.
- Los 49 DOIs se consultaron en `doi.org`: **todos resuelven**. Los títulos, años y autores se compararon con Crossref.
- Fuentes web verificadas una por una: Larroche (arXiv), GUIDE (arXiv), Disposición 60-E/2016, UCEMA, DGS10 y riesgo país.

### 3.2 Citadas en los capítulos 7 a 13

| Clave | Estado | Observación |
|---|---|---|
| Rose2020 | ✅ | — |
| Landauer2022 | ✅ | Faltan las páginas 4285–4294. |
| Landauer2022Dataset | ✅ | Zenodo 7119953. |
| Landauer2023Survey | ✅ | — |
| Turcotte2018LANL | ✅ | Crossref coincide (capítulo 1, pp. 1–22). |
| Freitas2024GUIDE | ⚠️ | El artículo existe y los autores coinciden. La licencia "CDLA-2.0" no figura en arXiv: verificarla en Kaggle (probablemente sea CDLA-Permissive-2.0). |
| Arantes2021OpTC | ✅ | El DOI resuelve. |
| Larroche2026 | ⚠️ | Existe: arXiv 2607.29390, del 31/07/2026, "Accepted at ANUBIS '26". La página no confirma la asociación con ESORICS ni la licencia CC BY 4.0. El resumen no nombra LANL 2015: confirmar en el PDF que sostiene "protocolo poco realista" para ese conjunto. |
| Welford1962 | ✅ | — |
| OWASP2025LLM | ✅ | year = 2024 es correcto (publicado en noviembre de 2024). |
| NIST_AI100_2_2025 | ✅ | — |
| Nielsen1994 | ⚠️ | Sirve para las heurísticas. La escala de severidad de 0 a 4 tiene como fuente canónica a Nielsen, *Severity Ratings for Usability Problems* (1994/95), o *Usability Engineering* (1993). |
| Salerno2025 | ⚠️ | Las cifras coinciden (523.207 empresas, agosto de 2025). La autora aparece como "Ana Salerno" en la web y como "Anatilde" en el `.bib`: verificar. Existe un informe posterior (mayo de 2026, datos a diciembre de 2025, caída del 1,6 %): decidir si se actualiza. |
| Weihrich1982, Porter1979, Osterwalder2010 | ✅ | — |
| Henderson1970 | ⚠️ | Es un ensayo de *BCG Perspectives*, no un libro. El tipo `@book` es discutible: usar `@article` o `@online`. |
| FRED2026DGS10 | ✅ | El 5,3 % coincide con octubre de 2026 (entre 5,2 % y 5,3 %, máximo desde 2002). |
| MDZ2026RiesgoPais | ⚠️ | El sitio devuelve 403 y no se pudo leer la nota. El valor de 650 pb a comienzos de octubre se confirma con otras fuentes. **Está duplicada** con `MENDEZ2026RiesgoPais` (misma URL, con autora). Citar la de Méndez y borrar esta. Ver M17. |

### 3.3 Problemas en el resto del `.bib`

**Errores:**

- **Hanif2024:** el DOI `10.3390/electronics13010175` corresponde a *Stassin et al., "Explainability and Evaluation of Vision Transformers"*. **El DOI es incorrecto.** No está citada.
- **Mangla2025:** el DOI `10.56127/ijst.v4i1` es del número de la revista, no del artículo. Además, la revista es de calidad dudosa. No está citada.
- **Mohammed2023:**
  - la clave no corresponde a los autores (Almansoori y Telek);
  - `Mikl{'o}s` está mal escrito: debe ser `Mikl{\'o}s`, si no se imprime una comilla. No está citada.
- **SAJS2025:** el autor es el nombre de la revista; faltan los autores reales. No está citada.
- **Ley20744:** el título dice "t.o. Decreto 390/1976", pero la fecha y el número de Boletín Oficial son los de la ley original (27/09/1974). El texto ordenado se publicó el 21/05/1976. Elegir uno de los dos.

**Formato o campos faltantes:**

- **Verizon2025:** es `@TechReport` y le falta el campo `institution`. No está citada.
- **Elbasheer2025:** es `@Article` con `journal = arXiv preprint`. Debería ser `@online` con `eprint`. No está citada.
- **Fahrmann2022:** falta `number = 8`.
- **Rashid2016HMM:** faltan las páginas 47–56.
- **Sharma2020:** faltan las páginas 1–9.
- **Ho2021Hopper:** faltan las páginas.
- **Kim2018Markov:** Crossref no devuelve autores. Verificar los autores a mano.

**Calidad de las fuentes:**

- **Ansari2025 (IJIREEICE) y Mangla2025 (IJST):** revistas de bajo prestigio. Si se citan en los capítulos 1 a 6, conviene reemplazarlas.

**Correcto o menor:**

- **DNPDP2016:** ✅ fecha del 18/11/2016 y Boletín Oficial n.º 33.507. La lista de países adecuados también la actualiza la Resolución AAIP 34/2019, y la Resolución AAIP 198/2023 suma las cláusulas de la Red Iberoamericana de Protección de Datos (RIPD). Considerar citarlas en `producto.tex:156`.
- Claves con año distinto del campo (Glockler2023→2024, Hariri2019→2021, VillarrealVasquez2021→2023, JNSM2025→2026): es correcto, porque el año de la versión en línea difiere del de la revista. Nada que corregir.
- **13 entradas sin citar:** Elbasheer2025, Fahrmann2022, Hamarsheh2025, Hanif2024, Hassan2025, JNSM2025, Kent2015, Mangla2025, MENDEZ2026RiesgoPais, Mohammed2023, Parimalla2025, SAJS2025 y Verizon2025. Kent2015 y MENDEZ deberían usarse (M18 y fila MDZ). El resto se puede borrar o dejar.

---

## 4. Cómo proceder (orden sugerido)

1. **Decidir A1 primero**, porque condiciona todas las cifras del modelo. Revisar en el código cómo dio 0 diferencias la reproducción, y elegir entre agregar el *blend* a `puntuar.py` o declararlo.
2. **Correcciones de texto que no requieren medir de nuevo:** A2, A3, A4 (usar 5,59 % / 10,09 %), A5 (país en la demo), A8, M1b, M2, M3, M4, M5, M6, M16, M17 y M18.
3. **Verificaciones de código cortas:**
   - A6: novedad de carpeta con `params.file` sin ruta; ¿se activó alguna vez en la instancia?
   - A9: ¿qué `SCORING_TERCER_MODELO` usó la medición de latencia del 15/11?
   - M1: 51 frente a 63 usuarios.
   - M10: cobertura en el dashboard.
   - M14: las 9 pruebas restantes.
4. **Corridas opcionales que cierran huecos:** HOLDOUT con el camino por defecto (M12); reproducción con el camino `iso` (A1); verificar el control de acceso en la release vigente (M8).
5. **Bibliografía:** corregir la duplicada MDZ/MENDEZ y citar `Kent2015`. Verificar Larroche, la licencia de GUIDE y el nombre de Salerno. El resto es limpieza de entradas no citadas.

---

## 5. Estado de aplicación (rama `revision-caps7a13`, 15/11/2026)

Aplicado en LaTeX (sin tocar el repo de código):

| Id | Cambio | Archivo |
|---|---|---|
| A1 (texto) | La calibración se calcula sin la línea base personal; el puntaje por defecto incluye el *blend* (peso máx. 0,7); la simulación no reproduce la línea base; la reproducción de 462.024 eventos corresponde a la configuración anterior | `datos.tex`, `pruebas.tex` |
| A2 | La baja del 15,17 % al 2,66 % se atribuye a la calibración | `pruebas.tex` |
| A3 | Supuesto "días reales = negativos" y meta de ruido esperable por construcción | `pruebas.tex` |
| A4 | Comparación con la v1 en DEV (5,59 % / 10,09 %) en lugar de HOLDOUT | `pruebas.tex` |
| A5 | La demo y el agente real llegan a crítico con el país simulado; el país lo autodeclara el agente | `pruebas.tex`, `producto.tex` |
| A7 | Aporte de la novedad declarado como no medido | `pruebas.tex` |
| A8 | Motivo de no calibrar en frío reformulado en términos de sensibilidad | `pruebas.tex` |
| M1b | "Oscilación" → "días con algún evento en nivel alto" | `pruebas.tex`, `conclusiones.tex` |
| M2 | Fila `notificar_admin` en la tabla de acciones (ahora 6, coincide con conclusiones) | `producto.tex` |
| M3 | "Variables que más contribuyen" → "que más se desvían" | `arquitectura.tex`, `e50_mercado.tex`, `negocio.tex` |
| M4 | La limitación sobre procesos y destinos se restringe a Isolation Forest | `datos.tex` |
| M5 | Arranque en frío: alcance real del período de aprendizaje | `producto.tex` |
| M6 | Fuera de horario: "a partir de las 21:00" (coincide con `hour > 20`) | `datos.tex` |
| M7 | 4 operaciones en PostgreSQL por evento | `negocio.tex` |
| M9 | Objetivo 3: la meta no se cumple de extremo a extremo en la nube | `conclusiones.tex` |
| M11 | El IF vigente no superó ningún criterio de promoción: decisión manual | `producto.tex` |
| M12 | HOLDOUT del camino por defecto: pendiente | `datos.tex` |
| M13 | Umbral de cobertura por componente en integración continua | `pruebas.tex` |
| M15 | Fila nueva "sin límite de intentos" en limitaciones; trabajo futuro sin duplicar la seudonimización | `producto.tex`, `conclusiones.tex` |
| M16 | Mes 16 = cuarto mes del segundo año | `negocio.tex` |
| M17 | Riesgo país fechado al 2/10/2026 | `negocio.tex` |
| M18 | Cita `Kent2015` para LANL 2015 | `datos.tex` |
| M20 | Autenticación "de ambas partes, en capas distintas" | `arquitectura.tex` |
| M21 | Justificación de la cola por cuenta apagada | `pruebas.tex` |
| M22 | "Cinco fuerzas de Porter" | `e50_mercado.tex` |
| LCT art. 71 | Art. 70 (dignidad) y art. 71 (conocimiento de la autoridad de aplicación), alineado con el cap. 2 | `producto.tex` |
| Bib | `Landauer2022` con páginas; `Ley20744` con fecha de la ley y del texto ordenado por separado | `biblio.bib` |

Ya resuelto por la sesión de los caps. 1 a 6: MDZ/MENDEZ duplicada, `Mohammed2023`, páginas de `Rashid2016HMM` y `Sharma2020`.

Pendiente, depende del repo de código (ver `guia_codigo_puntos_3_y_5.md`): A6, A9, M1 (51 frente a 63), M8, M10, M14, M19 y la decisión de fondo de A1 (agregar el *blend* a la simulación o mantener la declaración).

Pendiente sin código, por falta de fuente: M23 (licencias Microsoft), el texto completo de Larroche sobre LANL 2015 y el DOI correcto de `Hanif2024` (no citada).

Compilación: 282 páginas, 0 errores, sin citas ni referencias indefinidas.
