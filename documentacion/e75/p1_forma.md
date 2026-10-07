# P1 — Correcciones de forma E75

Rama `e75/paquete`. Fuente: `documentacion/e75/textos_e75.md` (T14, T15, T20, T21, T22). Un commit por tanda. Cada tanda compila con 0 errores y sin "??" en el PDF.

## Tanda 1 — Transcripciones (T20)

- Anexo C (`interview_1_pablo.tex`): "permission de night" y "permission the night" → "permission denied" (2 casos).
- Anexo F (`interview_4_pena.tex`): turno de Mociulsky "Okay, en un copy." → "[ininteligible]".
- Anexo G (`interview_5_ruiz.tex`): 10 etiquetas `Ruiz Matías Gabriel:` → `RUIZ MATÍAS GABRIEL:`. El título del anexo y la línea "Entrevistado:" no cambian.
- Anexo E (`interview_3_guillermo.tex`): separación de turnos mezclados, verificada con el audio por el equipo. Se cambió solo la etiqueta del hablante; el texto no cambió, lo que se comprobó por script. Los turnos consecutivos del mismo hablante se fusionaron. Resultado: de 22 a 59 turnos.

| # | Fragmento (inicio) | Antes | Después |
|---|---|---|---|
| E1 | "Mira, nosotros, para lo que es la parte de..." | Pita | Muntaabski |
| E2 | "Sí, cuando vos te conectás a una máquina…" | Pita | Muntaabski |
| E3 | "Es decir, seguridad, ¿verdad?…" | Pita | Muntaabski |
| E4 | "un tema de causa-efecto. No sé si te ayuda todo esto." | Muntaabski | Pita |
| E6 | "Es que este es el tema, o sea, vos me decís un motor de riesgo…" | Muntaabski | Pita |
| E7 | "Guillermo, creo que ahí Santiago mandó…" | Pita | Muntaabski |
| E9 | "Igual está muy bueno lo que mencionás…" | Pita | Muntaabski |
| E10 | "Y está bueno que vos des esa visión…" | Pita | Muntaabski |
| E11 | "¿Qué tal? ¿Cómo andás? Sí, también estoy de compañero…" | Muntaabski | Mociulsky |
| E12 | "No pasa nada." | Muntaabski | Pita |
| E13 | "No, no, decíme, decímelas." | Muntaabski | Pita |
| E14 | "Ok, el mayor desafío y es el enorme…" | Muntaabski | Pita |
| E15 | "Claro. Bueno, paso a la siguiente pregunta…" | Pita | Muntaabski |
| E16 | "A ver, vamos de vuelta…" | Muntaabski | Pita |
| E17 | "A ver, primero," | Mociulsky | Pita |
| E18 | "Ok, pero en caso de actividades como críticas…" | Pita | Mociulsky |
| E19 | "Sí, sí, se entendió perfecto. Ok." | Pita | Mociulsky |
| E20 | "Bueno, sigo yo, Santi…" | Pita | Muntaabski |
| E21 | "Claro, claro, entiendo…", "Sí, no tiene sentido.", "Claro. Sí, nosotros quizás tenemos..." | Pita | Muntaabski |
| E22 | "Correcto." (final del turno) | Muntaabski | Pita |
| E23 | "¿Distinguen ustedes entre los comportamientos inusuales…?" | Pita | Muntaabski |
| E24–E27 | Preguntas e intervenciones del entrevistador dentro del turno ("¿Eso no sería algo parecido a un Exoar…?", "No, es la respuesta automática…", "Busco otra pregunta…", "¿Cuáles son las que no pueden faltar nunca…?") | Pita | Muntaabski |
| E28 | "robándote información o denegándote la actividad…" | Mociulsky | Pita |
| E29 | "No diría que faltó…" | Mociulsky | Pita |
| E30 | "Bueno, con esto yo creo que preguntamos todo…" | Pita | Mociulsky |
| E31 | "así que ya por mi parte esta área. No sé si Fede quiere aportar algo más." | Muntaabski | Mociulsky |
| E32 | "Yo tengo un concepto muy arraigado…" | Muntaabski | Pita |
| E33 | "dos décadas de estar haciendo esto." | Muntaabski | Pita |
| E34 | "No, no, por favor, ningún problema." | Muntaabski | Pita |

E5 y E8 se revisaron y conservan su etiqueta. Las interjecciones breves ("Correcto.", "Claro.", "Sí.") y el intercambio del número de teléfono se dejaron sin separar.

## Tanda 2 — Estado del arte y comparativo (T14, T15, T21)

- 2.2.1 (`chapter02.tex`):
  - Sentinel: "Diversos usuarios señalan que el modelo de costos basado en el volumen de datos procesados puede resultar elevado en organizaciones con grandes cantidades de logs." → "Su modelo de costos se basa en el volumen de datos ingeridos, lo que puede resultar elevado en organizaciones con grandes cantidades de registros."
  - Splunk: "Diversos reportes señalan que su implementación inicial puede resultar compleja y requerir conocimientos especializados para su correcta configuración." → "Su puesta en marcha requiere integrar y normalizar múltiples fuentes de datos, lo que demanda conocimientos especializados para su configuración."
  - Se borraron los 6 comentarios `% REVISAR (E75)` de 2.2.1. Las frases que acompañaban quedan como estaban.
  - **Pendiente fuera de alcance:** el comentario `% REVISAR (E75)` de 2.2.3 (Autenticación adaptativa, remite a documentación de Okta) no se tocó.
- 2.2.6: "El verdadero diferencial radica en que" → "El diferencial del proyecto consiste en que", y se agregó al final el párrafo T14.
- 2.1: las 4 citas narrativas pasan a `\parencite`. La oración se reformuló sin nombrar al autor y la cita va al final.
  - `Artioli2024`: "\textcite{…} destacan que esto…" → "Esto … \parencite{…}."
  - `Kuhn2010`: "Como explica \textcite{…}, este modelo…" → "Este modelo … \parencite{…}."
  - `AlShehari2023`: "Estudios como el de \textcite{…} muestran que este método…" → "Este método … \parencite{…}."
  - `Kuppa2022`: "\textcite{…} advierte además el riesgo…" → "Existe además el riesgo … \parencite{…}."
- 3.1: "dimens iones" → "dimensiones". El origen era un salto de línea dentro de la palabra en el fuente.
- 3.2: "informacion" → "información".
- 3.5: menciones por apellido. "Guillermo" → "Pita" (5 casos), "Pablo" → "Villarino" (1 caso). En el perfil (3.5.1), la primera presentación de cada entrevistado conserva el nombre completo.
- Tablas:
  - 3.1 (Okta): "Es exactamente el ``punto ciego…'' …, Okta…" → "Corresponde al ``punto ciego…'' …: Okta…"
  - 3.3: "sigue exactamente la conclusión" → "sigue la conclusión".
  - 3.3: "adopta literalmente la combinación" → "adopta la combinación".
