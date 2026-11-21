# Relevamiento de datasets de referencia (consolidado, 2026-11-16)

Reúne en un solo archivo versionado lo que estaba disperso en `DATASETS.md`, `Datasets reales complementarios a CLUE-LDS.md` (23/10) y las notas `08_`, `20_` y `24_` de la revisión de modelos del 28/10. Estas últimas solo estaban en la copia de trabajo no versionada `data/sandbox/20261029/h4/repo/docs/revision_modelos_20261028/`. Es la tabla de la §4b del LaTeX, con la fuente de cada celda.

Criterio de selección (decisión del autor, 28 y 29/10):
1. Datos **reales**, con actividad de personas u organizaciones en su trabajo normal.
2. Etiquetas de ataque, si las hay, que vengan de personas (red team o incidentes), no de inyecciones ni guiones.
3. Licencia de dominio público, CC0, CC BY o equivalente, sin acuerdo firmado ni suscripción.

Columna "Ubicación": si el dataset trae un dato de ubicación (país o IP) por evento, que es lo que usaría la variable `n_distinct_countries`.

Marcas de verificación: [V] verificado en la fuente primaria; [I] inferido o no verificado; [R] medido en el repo.

| Dataset | Origen | Dominio | Etiquetas | Ubicación | Acceso / licencia | Decisión | Fuente |
|---|---|---|---|---|---|---|---|
| **CLUE-LDS** (Landauer et al., 2022) | Real: plataforma hBOX de Huemer Group (Viena), 2017-07-07 a 2022-09-29, ~50 M de eventos, seudonimizado [V] | Colaboración de archivos en la nube (44 tipos de evento) | No tiene | El campo existe, pero no trae país el **99,76 %** de los 50,5 M de eventos crudos, y el **99,95 %** de los de la población de entrenamiento (`clean_valid`) [R, `reports/perfilado_clue/`] | CC BY 4.0, Zenodo 10.5281/zenodo.7119953 [V] | **Usado**: entrenamiento, benchmark DEV/HOLDOUT, FPR y etiquetado de triage | `DATASETS.md`; Zenodo 7119953 |
| **CERT Insider Threat r4.2–r6.2** (Glasser y Lindauer, 2013) | **Sintético**: usuarios, organización y escenarios de ataque generados por un simulador [V] | Host + correo + web + dispositivos | Escenarios insider generados | Sintética | Libre (KiltHub, CMU SEI) | **Descartado: sintético.** Es el benchmark más citado de insider threat, pero sus métricas no hablan de comportamiento real | Glasser, J. y Lindauer, B. (2013), *Bridging the Gap: A Pragmatic Approach to Generating Insider Threat Data*, IEEE S&P Workshops; notas `08_` y `20_` |
| **DARPA OpTC** (Arantes et al., 2021) | Telemetría de ~500 hosts Windows 10 (2019). El origen del tráfico benigno de fondo no está documentado [I] | Host Windows (archivo, proceso, red, sesión), cerca del agente | Red team humano (APT externo), ground truth en PDF [V] | IP de flujos; sin país | Dominio público ("Distribution A"), DataPort 10.21227/edq8-nk52 [V] | **Usado solo para evaluación** (piloto de transferencia, `docs/piloto_optc.md`); rotulado como ejercicio de red team | `DATASETS.md`; `Datasets reales…` §ficha; nota `24_` |
| **LANL 2017** "Unified Host and Network" (Turcotte, Kent y Hash, 2018) | Real: 90 días de la red corporativa de LANL [V] | Host Windows (logon 4624/4625, proceso 4688) + netflow | No tiene | Sin país (equipos anonimizados) | Renuncia de derechos, estilo CC0 [V] | **Usado** para medir la brecha de dominio (ISO de CLUE en host: 53,66 % contra 4,13 %) | nota `24_`; `docs/contexto/estado_modelos.md` |
| **LANL 2015** "Multi-Source" (Kent, 2015) | Real: 58 días de LANL [V] | Autenticación, procesos, DNS, flujos | Red team real (solo autenticación) [V] | Sin país | CC0 1.0, doi 10.17021/1179829 [V] | **Descartado como evidencia** (P-80): una sola intrusión, casi toda desde un host (Larroche, 2026) | notas `20_` y `24_`; `docs/contexto/estado_modelos.md` |
| **RUU** "Are You You?" (Ben Salem y Stolfo, 2011) | Usuarios normales reales; masqueraders voluntarios con guion en un equipo de laboratorio [V] | Host Windows (procesos, registro, archivos) | Masquerade guionado | No | Acuerdo de uso firmado; sitio sin respuesta [V] | **Descartado**: exige acuerdo y el masquerade es guionado | `Datasets reales…` §ficha |
| **TWOS** (Harilal et al., 2018) | Estudiantes en un juego de 5 días [V] | Teclado, mouse, host, HTTP, logon | Masqueraders e insiders del juego | No | Sin licencia publicada; sitio no verificado [I] | **Descartado**: comportamiento escenificado y disponibilidad sin confirmar | `Datasets reales…` §ficha; nota `24_` |
| **WUIL** (Camiña et al., 2014) | Usuarios reales; masquerade simulado con scripts [V] | Host Windows (archivos) | Por scripts | No | A pedido de los autores | **Descartado**: etiquetas sintéticas | `Datasets reales…` §descartados |
| **DARPA TC E3/E5** | Trazas de procedencia con red team y fondo guionado [V] | Grafos de procedencia (CDM), sin usuario humano | Red team | No | Dominio público [V] | **Descartado**: otro dominio y formato | `Datasets reales…` §ficha |
| **OTRF Security Datasets** (ex Mordor) | Ataques reproducidos en laboratorio, capturas cortas [V] | Host Windows | Ataques de laboratorio | No | MIT [V] | **Descartado**: sin línea base de usuario | `Datasets reales…` §descartados |
| **SEA** (Schonlau et al., 2001) | Comandos UNIX reales de 50 usuarios; masquerade por inserción [V] | Línea de comandos | Por inserción | No | Sin licencia publicada [I] | **Descartado**: etiquetas construidas | nota `24_` |
| **IBM Cloud Console** (Zenodo 14062900) | Telemetría operativa real [V] | Servicio (requests, códigos HTTP), sin usuarios | Por herramientas internas | No | CC BY 4.0 [V] | **Descartado**: no hay usuarios | `Datasets reales…` §descartados |
| **Splunk BOTS, CIC-IDS, UNSW-NB15** | Laboratorio [V] | Red / SIEM | De laboratorio | IP | Varias | **Descartados**: laboratorio | nota `24_` |
| **GH Archive** | Real: eventos públicos de GitHub [V] | Colaboración en la nube | No | No | Archivo de eventos sin licencia declarada [V] | **Condicional**, no usado | nota `24_` |

## Lo que el perfilado previo habría anticipado

El perfilado de completitud de `data/clue.json` está en `reports/perfilado_clue/perfilado.md` (`scripts/evidencia/perfilado_clue.py`, una pasada en streaming sobre todo el archivo). Muestra que `location.countryCode` casi nunca viene: falta en el 99,7579 % de los 50.522.931 eventos (52 países distintos en el resto). En la población de entrenamiento (`data/processed/clean_valid_*`, 8,49 M de eventos) el valor es `unknown` en el 99,9463 %, el 99,95 % que cita el LaTeX. Tampoco vienen `role` (87,8 %) ni `isLocalIP` (99,5 %), y `params` está vacío en el 0,49 % de los eventos. Por eso `n_distinct_countries` es constante en casi todos los usuario-días y solo se mueve en los pocos eventos con país: funciona como interruptor, que es justo lo que pasa en la demo. Ese perfilado no se hizo antes de elegir las variables. Es la observación del profesor y vuelve al LaTeX como lección (`datos.tex:179`).

## Pendientes y sin verificar

Siguen sin verificar:
- el sitio y las condiciones de TWOS y RUU;
- cómo se generó el tráfico benigno de OpTC;
- los términos propios de IEEE DataPort.

Ninguno cambia la decisión.
