# Devolución de la entrega del 90 %: correcciones en la memoria LaTeX

Rama de referencia: `revision-caps7a13` (16/11/2026). Compañero: `correcciones_devolucion_90_codigo.md`.

> **Estado de aplicación (16/11, cierre):**
> - **Aplicadas:** L1, L2, L3, L4, L5, L7, L8, L9, L10, L12, L13, L14, L15 y L16.
>   - L10: icacls real; la CI sigue sin correr y así se declara.
>   - L15: borrador en `mail_consultas_devolucion_90.md`.
>   - L16: compila limpio sin referencias ni citas indefinidas, 291 páginas.
>     - `hyperref` sin color y con `pdfborder` en 0.
>     - `pdfcomment`, `todonotes`, `\Nico` y `\Fermat` comentados.
>     - El error `\ulp@afterend` venía de un `.aux` viejo y desaparece con `latexmk -C`.
> - **Salteadas por decisión del autor:**
>   - L6, la entrevista PyME: no hay entrevista hecha todavía. La falta queda declarada en el cap. de validación (§ "Síntesis de la validación") y en el trabajo futuro.
>   - L11, usabilidad con usuarios externos: no bloquea la entrega.
> - **Cambios de estructura:**
>   - El cap. 4 pasó a ser "Validación del problema con profesionales y usuarios" (`chap:validacion`).
>   - Las 14 fichas se reemplazaron por `tab:comparacion-comercial` y `tab:comparacion-algoritmos`, en el estado del arte.
>   - La matriz y la síntesis de diferenciadores se movieron al estado del arte.
>   - En `main.tex` se comentaron `todonotes`, `\Nico`, `\Fermat` y `pdfcomment`.

## 0. Antes de empezar: la devolución es anterior a la revisión de modelos

El profe corrigió el PDF **previo** a la revisión de modelos. Desde entonces:

- Las páginas que cita (25–38, 39–56, 13–14, 156, 167) ya no coinciden con el PDF actual. Cada ítem se ubica acá por archivo y línea del `.tex` vigente.
- La tabla de metas que cita (Tabla 10.VIII: E4 13,3 %, promedio 5 %, 15,4 % de días sin inyección) **ya no existe**: se retiró junto con los escenarios S1–S7 (`pruebas.tex:302-327`). La detección figura ahora como "no medible sin ataques etiquetados del dominio".
- Esto **no resuelve** la observación del profe. Sus tres preguntas siguen vigentes, y además hay un riesgo nuevo: que el lector vea que las metas incumplidas desaparecieron y lo interprete como un intento de ocultar el resultado (ver §8).

Estado por ítem: ✅ ya cubierto · 🟡 cubierto en parte · 🔴 pendiente · 🔁 cambió de forma, pero hay que responderlo igual.

| # | Ítem de la rúbrica | Nota | Estado hoy | Sección |
|---|---|---|---|---|
| 1 | Estructura general | Cumple (con observación) | 🔴 | §1 |
| 2 | Formato académico | Parcial | 🔴 | §2 |
| 3 | Redacción académica | Parcial | 🔴 | §3 |
| 4 | Estado del arte | Cumple (2 pedidos) | 🔴 | §4 |
| 5 | Conclusión del estado del arte | Cumple | ✅ (se reubica con §1) | §1 |
| 6 | Entrevistas | Cumple (1 pedido) | 🔴 | §5 |
| 7 | Tendencias | Cumple | ✅ | — |
| 8 | Metodología | Parcial | 🔴 | §6 |
| 9 | Pruebas funcionales | Cumple (2 pedidos) | 🔴 (depende del código) | §7 |
| 10 | Resultados de las pruebas | Cumple | ✅ (cuidar §8) | §8 |
| 11 | Modelo de negocio | Cumple | ✅ (sumar la entrevista PyME, §5) | — |
| 12 | Producto entregado | Parcial | 🔁 | §8 |
| 13 | Bibliografía | Cumple | 🟡 (se agregan entradas en §4) | §4 |
| — | Tres consultas | — | 🔴 | §9 |

---

## 1. Estructura: unificar Antecedentes y Análisis comparativo 🔴 (prioridad alta)

**El profe:** el estado del arte aparece dos veces (sección de Antecedentes y capítulo "Análisis comparativo"). Pide unificarlos en una sola sección de antecedentes.

**Hoy:**
- `chapters/chapter02.tex:181-339`: 2.2 Estado del arte (4 comerciales, académicos, alternativos, limitaciones, tendencias y conclusión).
- `chapters/chapter04.tex` (capítulo 3, `chap:comparativo`) contiene:
  - 3.1, 7 fichas `longtable` Campo/Detalle (`tab:comp-sentinel` … `tab:comp-proyecto`, líneas 5-189);
  - 3.2, la matriz de capacidades (191-225);
  - 3.3, otras 7 fichas de algoritmos (`tab:algo-*`, 227-404);
  - 3.4, la síntesis de diferenciadores (406-417);
  - 3.5, las entrevistas (419-447);
  - 3.6, la encuesta (449-513).

Las fichas de 3.1 y 3.3 repiten casi literalmente lo que ya dice 2.2.

**Decisión:** las tablas comparativas se integran en 2.2. Entrevistas y encuesta pasan a un capítulo propio.

**Estructura propuesta del nuevo 2.2 "Estado del arte":**

| Nuevo | Contenido | De dónde sale |
|---|---|---|
| 2.2.1 Soluciones comerciales | Párrafo común + diferencias por producto (ver §3) + **una** tabla comparativa con columnas Tipo, Dónde se ejecuta la respuesta, Agente propio, Transparencia del modelo, Modelo de costo y Diferencia con el proyecto. Filas: Sentinel, Splunk UBA, Exabeam, Entra ID, Okta, EDR/XDR PyME y proyecto | 2.2.1 actual + `tab:comp-*` (las 7 tablas se reemplazan por 1) |
| 2.2.2 Trabajos académicos | Texto actual (RADAC, UEBA con DL, IF) + **una** tabla con filas por trabajo (Aliyu, Villarreal-Vasquez, Tian, Artioli, Hariri, Landauer, proyecto) y columnas Dataset, Métrica, Limitación y Relación con el diseño | 2.2.2 actual + `tab:algo-*` (7 → 1) |
| 2.2.3 Enfoques alternativos | Okta, biometría, RADAC y EDR/XDR | igual que hoy |
| **2.2.4 Conjuntos de datos de referencia** | **Nuevo** (ver §4b) | — |
| 2.2.5 Matriz de capacidades | `tab:matriz-capacidades` + lectura | 3.2 |
| 2.2.6 Limitaciones reportadas | igual | 2.2 |
| 2.2.7 Tendencias | igual | 2.2 |
| 2.2.8 Conclusión del estado del arte | Texto actual + 3.4 (síntesis de diferenciadores) | 2.2 + 3.4 |

El párrafo de 3.3 "El diseño inicial combinaba Isolation Forest con un LSTM…" (`chapter04.tex:404`) se mueve al final de 2.2.2.

**Capítulo nuevo 3: "Validación del problema con profesionales y usuarios"** (lo que queda de `chapter04.tex`):
- 3.1 Entrevistas (actual 3.5) y la nueva entrevista PyME (§5);
- 3.2 Encuesta (actual 3.6);
- 3.3 Síntesis de la validación (nueva, unas 10 líneas: qué validan las entrevistas, qué la encuesta y qué falta validar, que es la demanda PyME).

**Mecánica:**
- Conservar los labels porque hay referencias desde otros capítulos:
  - `sec:comparacion-general` y `sec:estado-arte-entra` (`e50_mercado.tex:13`);
  - `sec:ea-splunk` (`e50_mercado.tex:18`);
  - `sec:ea-edr` (`e50_mercado.tex:20,101,103`);
  - `sec:encuesta-usuarios` (`negocio.tex:32,39`, `requerimientos.tex:309`);
  - `sec:matriz-capacidades`, `sec:sintesis-diferenciadores`, `sec:validacion-diseno` y `sec:entrevistas-profesionales`.
- Si se fusiona una sección, el label se pone en la sección destino.
- `chap:comparativo` pasa a nombrar el capítulo de validación, o se renombra a `chap:validacion` y se actualiza `chapter01.tex:121`.
- Hay que reescribir `chapter01.tex:116-141` (estructura del documento: cambian la cantidad de secciones y la descripción de la sección 3) y la introducción de `e50_mercado.tex`, que hoy dice "construidos sobre las mismas alternativas".
- `main.tex:275` (`\input{chapters/chapter04}`) se mantiene, pero ahora es el capítulo de validación; opcionalmente, renombrar el archivo a `validacion.tex`.
- Compilar y buscar `??` y `undefined references` en el log.

**Ganancia esperada:** se eliminan 14 `longtable` de una sola columna de datos; la reducción aproximada es de 8 a 12 páginas.

---

## 2. Formato académico: resumen y abstract 🔴 (prioridad alta, es de forma y es barato)

**Hoy:**
- `main.tex:268` y `main.tex:270` tienen comentados `%\input{chapters/summary}` y `%\input{chapters/abstract}`.
- `chapters/summary.tex` es el placeholder de la plantilla, con un `\Fermat{…}`.
- `chapters/abstract.tex` dice "Completar.".
- El README dice "No hacer el resumen ni el abstract hasta la entrega final"; el profe lo pide ahora.

**Qué hacer:**
1. Reemplazar `summary.tex` por el resumen (unas 250–300 palabras, un solo párrafo o dos), con "Palabras clave" al final.
2. `abstract.tex`: la misma versión en inglés, con "Keywords".
3. Descomentar las dos líneas en `main.tex`. Verificar que `\Fermat` no quede en ningún lado (`grep -rn '\\Fermat\|\\Nico' chapters`).
4. Quitar del README la línea "No hacer el resumen…".

**Borrador del resumen.** Todas las cifras salen del `.tex` vigente; revisarlas antes de cerrar.

> UMBRAL es un sistema de vigilancia conductual para pequeñas y medianas empresas argentinas que aborda el punto ciego posterior a la autenticación: un atacante con credenciales válidas opera con los permisos del usuario legítimo sin disparar controles basados en reglas. Siguiendo la separación entre punto de decisión y punto de aplicación de políticas de NIST SP 800-207, un agente liviano para Windows recolecta metadatos de procesos, archivos y conexiones y los envía por TLS a una API central. La API calcula un puntaje de riesgo de 0 a 100 por evento, con continuidad entre sesiones y decaimiento temporal, y devuelve una acción graduada que el agente ejecuta en el equipo: desde una alerta hasta la terminación de procesos o la denegación reversible de acceso a carpetas. Un panel web muestra el riesgo de cada usuario con su explicación y permite ajustar umbrales y acciones en tiempo de ejecución. El modelo combina Isolation Forest sobre la actividad diaria con una detección de novedad de recurso, entrenados con registros reales del conjunto CLUE-LDS. Sobre días reales, la tasa de alertas en nivel alto es del 2,66 %, y la latencia de cómputo tiene un percentil 95 de 13,4 ms. Las 748 pruebas automatizadas superan el 85 % de cobertura de líneas. La capacidad de detección no pudo medirse, porque ningún conjunto de datos del dominio incluye ataques reales etiquetados, y el modelo entrenado en la nube marca el 53,66 % de los días de un dominio de equipos Windows, frente al 4,13 % de uno entrenado en ese dominio. Recolectar telemetría propia y obtener incidentes etiquetados son, por eso, el principal trabajo futuro. El análisis económico muestra viabilidad en un escenario de adopción moderada.
>
> **Palabras clave:** UEBA, Zero Trust, detección de anomalías, Isolation Forest, puntaje de riesgo, respuesta en el *endpoint*, PyME.

El abstract es la traducción fiel (Keywords: *UEBA, Zero Trust, anomaly detection, Isolation Forest, risk scoring, endpoint response, SMB*).

---

## 3. Redacción académica: fichas comerciales con plantilla idéntica 🔴 (prioridad alta, va junto con §1)

**Hoy** (`chapter02.tex:190-233`), las cuatro fichas siguen el mismo esqueleto, casi con las mismas frases:

| Movimiento | Sentinel | Splunk | Exabeam | Entra ID |
|---|---|---|---|---|
| Objetivo | "Su objetivo principal es…" (191) | "El propósito central…" (202) | "Su objetivo principal es…" (213) | "Su objetivo principal es…" (225) |
| Funcionamiento | "Su funcionamiento se basa…" (193) | "Para lograrlo, el sistema analiza…" (204) | "Su funcionamiento combina…" (215) | "Su funcionamiento se basa…" (227) |
| Datos | "Los datos utilizados provienen…" (195) | "Los datos utilizados incluyen…" (206) | "Los datos utilizados incluyen…" (217) | "Los datos utilizados provienen…" (229) |
| Resultados | "Según la documentación pública del fabricante…" (197) | "Según el fabricante…" (208) | "Entre los resultados reportados por el fabricante…" (219) | "Según el fabricante…" (231) |
| Limitaciones | "No obstante, la solución presenta algunas limitaciones." (199) | "Sin embargo, la solución presenta algunas limitaciones." (210) | "No obstante, la plataforma presenta algunas limitaciones." (221) | "No obstante, la solución presenta algunas limitaciones." (233) |

La introducción (`:188`) anuncia la plantilla explícitamente: "Para cada una se describen su objetivo, su funcionamiento, los datos que utiliza, los resultados que reporta y sus limitaciones".

**Qué hacer:**
1. Un **párrafo común** con lo que las cuatro comparten, que hoy se repite cuatro veces: líneas base históricas por usuario o entidad, puntaje de riesgo, ingesta multifuente desde logs ya existentes, resultados reportados solo por el fabricante y modelos no publicados.
2. Por producto, **solo lo que lo distingue** en los ejes que importan al proyecto. Son tres o cuatro oraciones cada uno, con cita al fabricante (§4a):
   - **Sentinel:** incluye entidades de infraestructura; costo por volumen ingerido; la respuesta pasa por *playbooks* (Logic Apps/SOAR); sin agente propio de respuesta.
   - **Splunk UBA:** fuerte correlación temporal entre fuentes; sin respuesta nativa; fin de venta en diciembre de 2025 (ya citado, `Splunk2025UBAEoS`), por eso se conserva como representativo y no como competidor.
   - **Exabeam:** el más cercano en concepto porque integra SOAR, pero responde orquestando herramientas existentes, sin un agente liviano propio.
   - **Entra ID Protection:** riesgo de identidad (inicio de sesión y usuario), acceso condicional y CAE; no observa el uso del equipo.
3. Cerrar con **un párrafo de lectura** que lleve a la tabla comparativa única (§1): la diferencia que importa al proyecto es **dónde se ejecuta la respuesta** (SOAR externo, IAM, nada, o el agente en el equipo) y **qué se observa** (identidad o uso del equipo).
4. Revisar la misma muletilla en Okta (`:264-273`) y en EDR (`:287-292`).

**Borrador del párrafo común:**

> Las cuatro soluciones comparten un núcleo: construyen líneas base de comportamiento a partir del historial de usuarios y entidades, asignan un puntaje de riesgo a las desviaciones y se alimentan de registros que ya existen en la organización (autenticación, red, aplicaciones). En todos los casos, los resultados de detección que se publican provienen del propio fabricante y los modelos no son públicos. Lo que las distingue, y lo que interesa a este proyecto, es dónde termina el ciclo: qué hace cada una cuando el riesgo sube y si dispone de un componente propio en el equipo del usuario.

---

## 4. Estado del arte: citas del fabricante y datasets de referencia 🔴 (prioridad alta)

### 4a. Citar la documentación pública de cada fabricante

**Hoy:** dice "según la documentación pública del fabricante" sin cita (`chapter02.tex:197, 208, 219, 231`). En `biblio.bib` solo existe `Splunk2025UBAEoS` (línea 718).

**Qué hacer:** agregar entradas `@online` con `urldate`, con el mismo formato que `Splunk2025UBAEoS`, y citarlas en cada ficha, tanto en la descripción como en "según el fabricante". Claves sugeridas (**las URL se verifican al cargar**; las de abajo son las páginas de documentación habituales y hay que abrirlas antes de citar):

| Clave | Documento | URL a verificar |
|---|---|---|
| `MicrosoftSentinelUEBA` | Microsoft Learn: *Advanced threat detection with User and Entity Behavior Analytics (UEBA) in Microsoft Sentinel* | learn.microsoft.com/azure/sentinel/identify-threats-with-entity-behavior-analytics |
| `MicrosoftSentinelPricing` | Microsoft Sentinel pricing (respalda "costo por volumen ingerido") | azure.microsoft.com/pricing/details/microsoft-sentinel |
| `SplunkUBADocs` | Splunk UBA documentation: *About Splunk UBA* | docs.splunk.com/Documentation/UBA |
| `ExabeamDocs` | Exabeam: documentación de la plataforma (New-Scale SIEM / UEBA) | docs.exabeam.com |
| `MicrosoftEntraIDProtection` | Microsoft Learn: *What is Microsoft Entra ID Protection?* | learn.microsoft.com/entra/id-protection/overview-identity-protection |
| `MicrosoftCAE` | Microsoft Learn: *Continuous access evaluation* (respalda la frase de `:233`) | learn.microsoft.com/entra/identity/conditional-access/concept-continuous-access-evaluation |
| `OktaAdaptiveMFA` | Okta: *Adaptive MFA* / *Identity Threat Protection* (`:265, :273`) | okta.com / help.okta.com |
| `MicrosoftDefenderBusiness` | Microsoft Learn: *Microsoft Defender for Business* (`:288`) | learn.microsoft.com/defender-business |
| `WazuhActiveResponse` | Wazuh documentation: *Active response* (`:288, :290`) | documentation.wazuh.com |

Regla: si una afirmación de las fichas no aparece en la documentación citada (por ejemplo, "falta de visibilidad en el funcionamiento de sus algoritmos"), se reformula como lectura del equipo ("la documentación no describe los modelos") en lugar de atribuírsela al fabricante.

### 4b. Revisar los datasets públicos de referencia (nueva subsección 2.2.4)

**El profe:** falta revisar los datasets de referencia para UEBA y amenazas internas, por ejemplo CERT. La elección condicionó los resultados (99,95 % de país desconocido), y un análisis previo lo habría anticipado.

**Hoy:**
- CERT aparece solo de paso (`chapter02.tex:249, 253, 295`; `chapter04.tex:295, 320`), como el dataset que usan otros autores.
- `datos.tex:18-42` tiene una tabla de "conjuntos complementarios" (LANL 2017, GUIDE, OpTC y LANL 2015), pero está en el capítulo de datos y es posterior a la elección. No hay una comparación previa ni la justificación de por qué CLUE y no CERT.
- El 99,95 % está en `datos.tex:179`.

**Qué hacer:** subsección nueva en 2.2, antes de la matriz, con:

1. **Criterios** (párrafo corto): actividad humana real y no generada; unidad usuario (no solo *host* o red); dominio cercano al agente (*host* Windows); etiquetas de ataque reales; campos que usa el modelo (tipo, hora, usuario, ubicación); licencia y acceso.
2. **Tabla** (fuente: `DATASETS.md` y `Datasets reales complementarios a CLUE-LDS.md` del repo de código, y las notas de `data/sandbox/20261029/h4/repo/docs/revision_modelos_20261028/{08,20,24}_*.md`, que son una copia de trabajo no versionada; confirmar cada celda):

| Conjunto | Origen de la actividad | Dominio | Etiquetas | Ubicación | Acceso / licencia | Lectura para el proyecto |
|---|---|---|---|---|---|---|
| CERT r4.2–r6.2 | **Sintético**: usuarios y ataques generados | *host* + correo + web (simulado) | Sí, inyectadas | No | Público (CMU SEI / KiltHub) | Referencia de la literatura; descartado como evidencia porque la actividad no es real |
| CLUE-LDS | Real (plataforma de archivos en la nube) | Nube | **No** | Campo presente, **99,95 % desconocido** | CC BY 4.0 | Elegido: real, por usuario, licencia abierta |
| LANL 2015 | Real + *red team* | Red/autenticación | Sí (*red team*) | No | Público | Descartado: protocolo de evaluación poco realista (Larroche, 2026) |
| LANL 2017 | Real | *Host* Windows | Sin ataques | No | Público | Solo para medir FPR en *host* |
| DARPA OpTC | Ejercicio en red instrumentada | *Host* Windows | *Red team* (APT externo) | No | Dominio público | Piloto de transferencia, no de detección *insider* |
| RUU | Real (normales) + *masqueraders* guionados | *Host* Windows | Sí | No | Acuerdo de uso; sitio sin respuesta | No accesible |
| TWOS | Juego con humanos (*masquerader*/traidor) | *Host* + HTTP + SMTP | Sí | No | Sin verificar | No accesible |
| WUIL | Usuarios reales; ataques por *scripts* | *Host* Windows | Sí (simulados) | No | A pedido | Descartado: etiquetas sintéticas |
| GUIDE | Incidentes reales de otro producto | SOC (alertas) | Sí | — | Kaggle CDLA | Solo para validar la acumulación por cuenta |

3. **Justificación de la elección** (borrador):

> Se eligió CLUE-LDS por ser el único conjunto con actividad humana real, a nivel de usuario y con licencia abierta. CERT, la referencia más citada en la detección de amenazas internas, se descartó como fuente de evidencia porque tanto los usuarios como los ataques son generados por un simulador: un modelo que lo detecta bien demuestra que reconoce los patrones del generador, no los de un atacante. La elección tiene costos que este relevamiento permite anticipar: CLUE-LDS no tiene etiquetas, de modo que la detección no puede medirse; pertenece al dominio de una plataforma en la nube y no al de un equipo Windows; y su campo de ubicación está casi vacío (el 99,95 % de los eventos usados tiene el país como desconocido, sección~\ref{…}). La versión 1 del modelo incluyó variables de país igualmente, y en la práctica funcionaron como un interruptor de ubicación (tabla~\ref{tab:limitaciones-producto}); un perfilado de completitud de los campos antes de definir las variables lo habría mostrado.

   Esta última frase reconoce lo que dice el profe; conviene dejarla así.

4. En `datos.tex:6-16`, agregar una remisión a la nueva 2.2.4. La tabla `tab:datos-complementarios` puede quedar (describe el uso real en la revisión), con un "ver criterios en la sección 2.2.4".
5. **Bibliografía nueva:** CERT (Glasser y Lindauer, 2013, *Bridging the Gap: A Pragmatic Approach to Generating Insider Threat Data*, IEEE SPW; verificar la referencia); RUU (Ben Salem y Stolfo, 2011); TWOS (Harilal et al., 2018); WUIL (Camiña et al., 2014). Ya existen: `Kent2015`, `Turcotte2018LANL`, `Freitas2024GUIDE` y `Arantes2021OpTC`. `Larroche2026` ya tiene entrada en `.bib` (verificado).

---

## 5. Entrevistas: sumar un responsable de sistemas de PyME 🔴 (prioridad alta, requiere gestión)

**Hoy:** `chapter04.tex:425` ya declara que ninguno de los cinco trabaja en una PyME (el profe lo valoró). Falta la entrevista.

**Qué hacer:**
1. Conseguir al menos una entrevista con un responsable de sistemas o IT de una PyME (idealmente de 10 a 200 empleados, sin SOC propio), con autorización de publicación como las demás.
2. Transcribirla en un anexo nuevo, con el mismo formato que `interview_*.tex`, y agregarlo a `annex.tex`. Actualizar la lista de anexos en `chapter01.tex:137-141`.
3. Integrarla en:
   - el nuevo cap. 3 (validación), en un párrafo propio "Perspectiva del segmento PyME";
   - el perfil de los especialistas (`chapter04.tex:425`): cambiar "Ninguno de los cinco…" por "Cuatro de los seis…";
   - el modelo de negocio (`negocio.tex`): contrastar los supuestos de precio y demanda con lo que diga el entrevistado;
   - el ítem "Validación comercial" del trabajo futuro (`conclusiones.tex:79-80`).

**Guion propuesto** (semiestructurado, de 30 a 40 minutos):
1. Empresa: rubro, cantidad de empleados y equipos, y cuántas personas hay en IT/seguridad.
2. ¿Qué controles de seguridad usan hoy en los equipos y en las cuentas (antivirus/EDR, MFA, Microsoft 365/Google, SIEM)?
3. ¿Tuvieron incidentes con credenciales robadas, *phishing* o fuga de información? ¿Cómo y cuándo se detectaron?
4. Si hoy alguien usara la cuenta de un empleado desde su propio equipo, ¿cómo se enterarían?
5. ¿Quién atendería una alerta de riesgo? ¿En qué horario? ¿Tercerizan algo con un MSSP o integrador?
6. ¿Aceptarían que el sistema actúe solo (cerrar un proceso, bloquear una carpeta) sin que nadie lo confirme? ¿En qué casos sí y en cuáles no?
7. ¿Cuántas alertas por semana podrían revisar sin que se vuelva ruido?
8. ¿Cómo verían los empleados un agente de monitoreo? ¿Lo informarían y cómo?
9. ¿Qué tendría que demostrar una herramienta así para que la prueben?
10. ¿Cuánto pagan hoy por seguridad por equipo o por usuario? ¿Cuánto pagarían por esto? Contrastar con el precio de `negocio.tex`.
11. ¿Quién decide la compra y por qué canal compran (directo, integrador, MSSP)?
12. De lo que vieron del sistema (demostración o capturas), ¿qué les sirve y qué les sobra?

---

## 6. Metodología en sección propia 🔴 (prioridad alta)

**El profe:** está dentro de la Introducción, los dos incrementos se describen en pocas líneas y la planificación se remite al anexo. Pide una sección propia con el cronograma real de cada incremento, la herramienta de seguimiento y los ajustes que surgieron de los resultados del modelo.

**Hoy:**
- `chapter01.tex:79-114` (`sec:metodologia`): justificación (81-90), dos incrementos en un párrafo (92-97), *pipeline* de entrenamiento (99-108) y gestión del trabajo (110-114).
- Anexo A (`schedule_of_activities.tex`): solo el Gantt **planificado** y la frase "La organización en dos incrementos … surge de la ejecución posterior".
- Nota: `images/gannt.jpg` (sin versionar) tiene exactamente el mismo tamaño que `images/cronograma.jpg` (6 395 682 bytes). Parece una copia del mismo plan, no un Gantt real. Confirmar y borrar si es un duplicado.

**Qué hacer:** capítulo nuevo "Metodología de desarrollo", después de la Introducción (o como el capítulo 2, antes de Antecedentes; lo decide el autor). El label `sec:metodologia` se traslada. En la Introducción queda una oración de remisión.

Estructura propuesta:
1. **Enfoque y justificación:** texto actual de `chapter01.tex:81-90`, sin cambios.
2. **Planificación inicial y desvíos:** Gantt planificado (se mueve aquí o sigue en el Anexo A) y una tabla "Plan contra real" por fase o incremento, con las columnas Fase, Inicio y fin planificados, Inicio y fin reales, Desvío y Causa.
3. **Incrementos ejecutados**, uno por subsección, cada uno con: casos de uso y requerimientos cubiertos, fechas reales, entregable (versión ejecutable o release), cómo se verificó y qué se decidió para el siguiente.
   - Incremento 1: CU-01 y CU-02.
   - Incremento 2: CU-03, CU-04, IAM y endurecimiento.
   - Probable **incremento 3 de hecho**, la revisión de modelos (28/10–14/11). Fue un ciclo completo con objetivo, criterios previos y release, y conviene presentarlo como tal.
4. **Herramienta de seguimiento:** cuál se usó (GitHub Issues o Projects, tablero, planilla), cómo se priorizaba y cada cuánto se revisaba. Se puede agregar una captura en el anexo.
5. **Ajustes derivados de los resultados del modelo:** tabla Resultado → Ajuste → Incremento, que tome las filas de modelo de `tab:decisiones-pruebas` (`pruebas.tex:394-433`) y de la bitácora `revision_modelos_latex.md`:
   - retiro de S1–S7 y evaluación solo con datos reales;
   - LSTM fuera del camino por defecto (no usaba el orden);
   - Markov probado y descartado por oscilación;
   - criterio de promoción redefinido (no inferioridad de la FPR);
   - corte temporal fijo en el reentrenamiento;
   - clasificación por comportamiento como opción;
   - umbral de aprendizaje de 20 eventos configurable.
6. **Pipeline de entrenamiento y gestión del código:** texto actual de 99-114.

**Evidencia disponible en el git del código** (para armar el "real"; los detalles los extrae la tarea 8 del MD de código):

| Mes (2026) | Commits |
|---|---|
| abril | 4 |
| mayo | 3 |
| julio | 17 |
| agosto | 119 |
| septiembre | 26 |
| octubre | 359 |
| noviembre (hasta el 14) | 40 |

Primer commit: 16/04/2026. Hay un tag `pre-limpieza-entrega`.

**Datos a completar por el autor** (no están en el repo): fechas de inicio y fin de cada incremento; herramienta de seguimiento; si hubo reuniones o revisiones periódicas con el tutor y con qué frecuencia; y qué tareas del Gantt planificado no se hicieron o cambiaron.

---

## 7. Pruebas funcionales 🔴 (depende del MD de código)

**El profe:** para la entrega final, resolver al menos la regresión del puntaje y las pruebas del frontend.

**Hoy en el `.tex`:**
- Regresión: `pruebas.tex:417` (fila de decisiones) y `:441` (limitación: "seis diferencias … no como prueba superada").
- Frontend: `pruebas.tex:443` ("no tiene pruebas automatizadas, por declaración").
- icacls simulado: `pruebas.tex:444`.
- Usabilidad sin usuarios: `pruebas.tex:451`.
- Objetivo 9: `conclusiones.tex:32` ("el *frontend*, sin lógica de negocio, queda fuera del umbral").
- Trabajo futuro: `conclusiones.tex:72` ("agregar pruebas al *frontend*…").

**Qué hacer cuando el código esté listo** (tareas 1–3 del MD de código):
1. **Regresión:** reescribir `:441` como prueba superada, con la cifra nueva (diferencias, tolerancia, usuarios y camino evaluado). Actualizar la fila de `:417` (la decisión pasa a ser "se regeneró el oráculo / se agregó la regresión del camino por defecto"). Si la regresión pasa a evaluar el camino por defecto, decirlo explícitamente.
2. **Frontend:**
   - en el inventario (`tab:inventario-pruebas`, cerca de `pruebas.tex:60`), agregar una fila Frontend con su cantidad de pruebas;
   - en la tabla de ejecución (`tab:ejecucion-pruebas`) y en la cobertura (`tab:cobertura-codigo`), agregar la columna o fila del frontend;
   - actualizar los totales (748 → N) en `pruebas.tex:56`, `:147` (total de cobertura), `:456` (síntesis) y `conclusiones.tex:32`;
   - borrar la viñeta de `:443` o reducirla a lo que siga sin probar;
   - en `conclusiones.tex:72`, quitar "agregar pruebas al *frontend*".
3. **icacls:** si se hace la prueba real en el runner Windows, cambiar `:444`.
4. **Integración continua:** si se resuelve el `startup_failure`, volver a afirmar que el *pipeline* aprueba, con fecha y cantidad de trabajos (hoy se reemplazó por "reproducción local", 10.2.3).
5. **Usabilidad con usuarios** (opcional, recomendado): 3 a 5 administradores o personas de IT externas al equipo, 5 tareas guiadas (ver el riesgo de un usuario y su explicación, cambiar un umbral, cambiar una acción, revisar la auditoría, revertir una acción) y un cuestionario SUS. Agregar una subsección en `sec:evaluacion-usabilidad` y actualizar `:451`. La entrevista PyME (§5) puede servir también para esto.

---

## 8. Producto entregado: qué valor tiene con este nivel de detección 🔁 (prioridad máxima)

**El profe:** la detección no alcanza sus metas (1 de 5; E4 13,3 % contra 50 %; 15,4 % de días normales en alto contra ≤ 10 %). Pide discutir en las conclusiones qué valor tiene el producto y qué cambiarían primero.

**Hoy:**
- Esas cifras **ya no están**: la tabla actual (`pruebas.tex:307-324`) tiene otras metas (FPR ≤ 5 %: 2,66 %, cumple) y aclara que las metas de detección "se retiraron junto con esos escenarios" (`:327`).
- `conclusiones.tex:47` dice "El resultado más débil sigue siendo la capacidad de detección, que no puede medirse…", pero **no discute el valor del producto** ni qué cambiar primero (el trabajo futuro, `:55-81`, es una lista sin argumentar).

**Riesgo:** el profe va a buscar las cifras que observó y no las va a encontrar. Si la memoria no explica el cambio, la revisión se lee como si las metas se hubieran cambiado para cumplirlas, cuando en realidad es una decisión metodológica defendible.

**Qué hacer:**

1. **Dejar constancia del resultado v1** (en 10.5, después de la tabla de metas, o en 10.6.1 "Método"). Es un párrafo, o una tabla chica "Metas de la versión 1":
   > En la versión 1, evaluada con escenarios construidos sobre historiales reales, se cumplía una de las cinco metas de comportamiento y detección: la detección atribuible del escenario combinado era del 13,3 % (meta: 50 %), la detección promedio de los cuatro escenarios, del 5,0 %, y el 15,4 % de los días sin inyección terminaba en nivel alto (meta: ≤ 10 %). La revisión de modelos retiró esos escenarios porque no representan ataques reales y orientaban las decisiones de diseño: con ellos, cada ajuste del modelo podía mejorar la cifra sin mejorar la detección de un ataque real. Desde entonces, la detección no se mide en lugar de medirse con una referencia inválida, y el ruido sobre días reales bajó del 5,59 % (versión 1) al 2,66 %.

   Las cifras v1 están en `LIMITACIONES_Y_ESTADO.md` §1 (tabla de metas) y la cifra 5,59 en `pruebas.tex:384`.

2. **Nueva sección en `conclusiones.tex`**, entre "Resultados principales" y "Trabajo futuro": **"Valor del sistema con la detección actual"**. Puntos (texto en §9.1):
   - lo que el sistema demuestra (ciclo cerrado PDP→PEP, respuesta graduada y reversible, latencia, explicación, operación) contra lo que no demuestra (detección);
   - la evidencia de que las alertas no son azar: el etiquetado ciego **provisional** de 403 usuario-días de DEV. Se presenta con todas sus salvedades, como evidencia descriptiva y no como *recall*;
   - para quién sirve hoy: una organización que acepta usarlo como herramienta de triage y de respuesta acotada (los niveles restrictivos solo en crítico, con revisión), no como detector autónomo;
   - con quién no conviene: con acciones restrictivas automáticas en nivel alto.

3. **Convertir el inicio de "Trabajo futuro" en "Qué se cambiaría primero"**, argumentado y en orden (texto en §9.3). El resto de la lista actual puede quedar como "otras líneas".

4. **Objetivo 2** (`conclusiones.tex:25`): agregar media línea con la remisión a la nueva sección.

5. Si se integra el etiquetado provisional:
   - agregar una subsección corta en 10.6 o 10.7 ("Revisión ciega provisional de las alertas"), con método, cifras, intervalos y limitaciones (fuente: `docs/etiquetado/resultado_provisional.md` y `cruce.md` del repo de código);
   - rotularla siempre como **provisional, con un solo etiquetador y sin confirmación de un analista**;
   - **aclarar que DEV ya se usó para elegir el camino por defecto**, así que describe y no confirma;
   - si un analista la confirma antes de la entrega (tarea 4a del MD de código), quitar "provisional".

---

## 9. Respuestas a las tres consultas (borrador para el mail o la defensa, y base de §8)

Las cifras del etiquetado son **provisionales** (un solo etiquetador, sin analista; `docs/etiquetado/resultado_provisional.md`). Citarlas siempre así.

### 9.1 "Con una detección del 13,3 % en el escenario combinado, ¿qué le aporta hoy el sistema a una organización?"

> Primero, una aclaración sobre la cifra. El 13,3 % provenía de escenarios de ataque que construimos nosotros sobre historiales reales. En la revisión posterior concluimos que esos escenarios no representaban ataques reales y que estaban orientando las decisiones del modelo, así que los retiramos: hoy la detección no está medida, porque ningún conjunto de datos del dominio trae ataques reales etiquetados. Preferimos declararla no medida antes que sostener una cifra con una referencia inválida.
>
> Con eso dicho, el sistema aporta hoy tres cosas verificadas y una acotada:
> 1. **Cierra el ciclo que el estado del arte deja abierto**: decide en la API y actúa en el equipo, sin un analista de por medio, con una respuesta graduada y reversible (la denegación de carpeta se restaura desde un respaldo de la ACL) y configurable por nivel desde el panel. Esto está probado de extremo a extremo contra la instancia en la nube.
> 2. **Una carga de alertas baja y medida sobre actividad real**: el 2,66 % de los usuario-días llega a nivel alto y el 1,29 % cierra el día así. Para una PyME sin SOC, es un volumen revisable.
> 3. **Cada alerta llega explicada**: las variables de Isolation Forest que más se desvían, o el recurso nuevo que la disparó.
> 4. **La acotada: qué detecta.** En una revisión ciega provisional de 403 usuario-días reales, 14 de 162 alertas (8,6 %; IC 95 % del 3,9 % al 15,0 %) merecían que un analista abriera el caso. Las que aciertan son todas de Isolation Forest y son eventos de alto impacto: descargas masivas, borrados masivos y carpetas expuestas por link público. Entre los días sin alerta, cerca del 1 % merecía revisión.
>
> En síntesis, hoy le sirve a una organización como herramienta de triage y de respuesta rápida ante cambios grandes de volumen, no como detector autónomo de una cuenta robada que imita al usuario. Por eso la configuración por defecto reserva las acciones restrictivas para el nivel crítico. Que sea un detector confiable depende de entrenarlo con telemetría propia del agente.

### 9.2 "¿Por qué eligieron ese dataset y no uno de referencia para amenazas internas?"

> Porque la referencia habitual, CERT (r4.2 a r6.2), es sintética: tanto los usuarios como los ataques los genera un simulador, y nos fijamos la regla de entrenar y evaluar solo con actividad humana real. Un modelo que rinde bien en CERT demuestra que reconoce los patrones del generador. Buscamos alternativas reales con etiquetas en el dominio de un equipo Windows: RUU (requiere un acuerdo y el sitio no respondía), TWOS (disponibilidad sin verificar), WUIL (ataques generados por *scripts*), LANL 2015 (protocolo de evaluación poco realista) y OpTC (ataque externo en una red instrumentada). Ninguna cumplía a la vez "real", "por usuario" y "accesible". CLUE-LDS sí: actividad real de 920 usuarios durante cinco años, con licencia CC BY 4.0.
>
> Tienen razón en que la elección tuvo costos que un análisis previo habría anticipado: CLUE no tiene etiquetas, es de una plataforma en la nube y no de un equipo Windows, y su campo de país está casi vacío (99,95 % desconocido). Este último punto tendría que habernos hecho descartar las variables de país desde el principio; en la versión 1 terminaron funcionando como un interruptor de ubicación. Agregamos ese relevamiento de conjuntos de datos al estado del arte. Además, medimos la brecha de dominio: sobre telemetría real de equipos Windows (LANL 2017), el modelo entrenado en CLUE marca el 53,66 % de los días, contra el 4,13 % de uno entrenado en ese dominio.

### 9.3 "¿Qué cambiarían primero en el modelo para acercarse a las metas?"

> En este orden, porque cada paso es condición del siguiente:
> 1. **Entrenar y calibrar en el dominio correcto.** Recolectar telemetría propia del agente en un piloto, varias semanas de equipos reales, y reentrenar y recalibrar Isolation Forest con ella. La brecha 53,66 % frente a 4,13 % muestra que hoy el modelo no está calibrado para el equipo donde corre, y ningún otro ajuste compensa eso.
> 2. **Tener con qué medir.** Hacer confirmar por un analista externo el etiquetado provisional, y en el piloto registrar los incidentes que la organización confirme, para tener por primera vez una cifra de *recall* en el dominio. Evaluar una sola vez sobre el HOLDOUT reservado.
> 3. **Corregir lo que el etiquetado ya señala:**
>    - la detección de novedad, tal como está, no aportó (0 de 58 alertas propias merecían revisión), así que la endureceríamos (más recursos nuevos, solo carpetas y destinos de red) o la dejaríamos solo informativa hasta tener evidencia;
>    - agregaríamos variables por tipo de operación, en particular la compartición hacia afuera, que fue el punto flojo;
>    - sacaríamos `n_distinct_countries` del modelo y pondríamos una regla explícita de ubicación en el motor de decisión.
> 4. **Recién después**, variables con granularidad menor al día y volver a evaluar un componente de secuencia.

---

## 10. Otros pendientes detectados al cruzar el `.tex`

- `chapter01.tex:117`: "El documento se organiza en trece secciones". Cambia con §1 y §6.
- `chapter01.tex:137-141`: lista de anexos. Agregar el anexo de la entrevista PyME y, si se crea, el del seguimiento o la metodología.
- `chapter04.tex:229`: "muestra que la elección inicial de Isolation Forest + LSTM no es arbitraria". Con la fusión, reformular en presente (IF + novedad) o como historia de la decisión.
- Pendientes de la bitácora que tocan el estado del arte: los subapartados 2.1.5.3 a 2.1.5.5 ya tienen citas (Bowman, Ho, Kim, Rashid, Siffer) y no quedan `TODO` en `chapters/` (verificado el 16/11).
- README: además del resumen, revisar el resto de la lista "Antes de las entregas" (`hyperref` sin color, comandos `\Nico`/`\Fermat`, `pdfcomment`).

---

## 11. Checklist

| # | Tarea | Bloquea la entrega final | Depende de |
|---|---|---|---|
| L1 | Unificar los caps. 2 y 3; capítulo de validación; labels y referencias (§1) | Sí | — |
| L2 | Resumen y abstract (§2) | Sí | — |
| L3 | Sintetizar las fichas comerciales y una tabla comparativa (§3) | Sí | L1 |
| L4 | Citas del fabricante en `.bib` (§4a) | Sí | — |
| L5 | Subsección de datasets de referencia y bibliografía (§4b) | Sí | Código T5 (confirmar la tabla) |
| L6 | Entrevista PyME: anexo, validación y negocio (§5) | Sí (lo pide el profe) | Gestión del autor |
| L7 | Capítulo de metodología: plan contra real, herramienta y ajustes (§6) | Sí | Código T8 + datos del autor |
| L8 | Regresión del puntaje en el texto (§7.1) | Sí | Código T1 |
| L9 | Pruebas del frontend en tablas y totales (§7.2) | Sí | Código T2 |
| L10 | icacls real / CI en verde (§7.3–7.4) | No | Código T3, T6 |
| L11 | Usabilidad con usuarios externos (§7.5) | No (recomendado) | — |
| L12 | Constancia del resultado v1 (§8.1) | Sí | — |
| L13 | Conclusiones: valor del sistema y qué cambiar primero (§8.2–8.3, §9) | Sí | Código T4a si se quita "provisional" |
| L14 | Etiquetado provisional en el cap. 10 (§8.5) | Sí, si se usa en L13 | — |
| L15 | Mail con las respuestas a las 3 consultas (§9) | — | — |
| L16 | Pendientes de §10 y compilación sin referencias indefinidas | Sí | todo lo anterior |

Cruce rúbrica → tarea:

| Ítem de la rúbrica | Tareas |
|---|---|
| 1 Estructura | L1 |
| 2 Formato | L2 |
| 3 Redacción | L3 |
| 4 Estado del arte | L4, L5 |
| 5 Conclusión del estado del arte | L1 (reubicación) |
| 6 Entrevistas | L6 |
| 7 Tendencias | sin cambios |
| 8 Metodología | L7 |
| 9 Pruebas funcionales | L8–L11 |
| 10 Resultados | L12, L14 |
| 11 Negocio | L6 (contraste) |
| 12 Producto | L12, L13 |
| 13 Bibliografía | L4, L5 |
| Consultas | L13, L15 |
