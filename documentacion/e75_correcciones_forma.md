# Correcciones de forma E50 → E75

Rama `e75/correcciones-forma` (base `87af6b0`). Solo contenido: no se modificó el preámbulo, la clase, los paquetes ni la configuración de formato de `main.tex`. Después de cada tanda se compiló con `latexmk -pdf main.tex`: 0 errores, 0 referencias o citas indefinidas en `main.log`, 0 `??` en el texto del PDF.

| Tanda | Commit | Contenido |
|---|---|---|
| 1 | `5157d99` | Transcripciones (Anexos C a F) |
| 2 | `28ed9e3` | Erratas, tiempo verbal, lenguaje de cursada, nombres de código, referencias |
| 3 | `c78f57a` | Títulos, párrafos introductorios, Plaza |
| 4 | `d48e971` | Figuras, citas, bibliografía |
| 5 | — | Encabezado (solo localización, sin cambios) |

---

## Tanda 1: Transcripciones

### 1. Etiquetas del entrevistado (formato APELLIDO NOMBRE)

| Anexo | Antes → después |
|---|---|
| C (`interview_1_pablo.tex`) | `PABLO:` → `VILLARINO PABLO RODOLFO:` (todos los turnos); línea "Entrevistado: Pablo (…)" → "Entrevistado: Villarino Pablo Rodolfo (…)" |
| E (`interview_3_guillermo.tex`) | `GUILLERMO:` → `PITA GUILLERMO:` (todos los turnos); línea "Entrevistado: Guillermo (…)" → "Entrevistado: Pita Guillermo (…)" |
| D, F | Ya estaban en el formato pedido. |

Las etiquetas de los entrevistadores (`MUNTAABSKI FEDERICO:`, `MOCIULSKY SANTIAGO BERNARDO:`) ya eran consistentes en C a F.

### 2. Restos de transcripción automática eliminados

Anexo C: `Perfect.`, `Yeah.` (×3), `It.`, `Okay, here you.`, `Okay, thank you.`, `The win.`.
Anexo F: `Yeah.` (×4), `Dizzy.`, `Perfect.`, `Belly.`, `That.`, `But...` (×2), `Thank you.`, `Think. So. Yeah.`, `Say it. La milandia.`.
Los turnos que quedaron vacíos se eliminaron completos.

### 3. Partición de oraciones largas

116 cortes, cambiando solo puntuación y mayúscula inicial: 41 en C, 21 en D, 36 en E y 18 en F. Se cortó en comas existentes o antes de conectores ("Entonces", "Pero", "Y", "Porque"…).

### Salida del script de verificación

`python documentacion/scripts/verificar_transcripciones.py` compara, por anexo, el cuerpo de la transcripción en `87af6b0` con el actual. Primero quita las etiquetas de los interlocutores, pasa todo a minúsculas y elimina la puntuación. Exige que no haya inserciones ni reemplazos, que todo borrado esté en la lista aprobada y que cada cambio de mayúscula ocurra al inicio de una oración.

```
Anexo C (chapters/appendix/interview_1_pablo.tex)
  palabras antes: 7237  después: 7224  diferencia: 13
  bloques borrados (8): ['perfect', 'yeah', 'it', 'okay here you', 'yeah', 'okay thank you', 'yeah', 'the win']
  RESULTADO: IDÉNTICO salvo restos aprobados

Anexo D (chapters/appendix/interview_2_jacubovich.tex)
  palabras antes: 4755  después: 4755  diferencia: 0
  bloques borrados (0): []
  RESULTADO: IDÉNTICO salvo restos aprobados

Anexo E (chapters/appendix/interview_3_guillermo.tex)
  palabras antes: 5958  después: 5958  diferencia: 0
  bloques borrados (0): []
  RESULTADO: IDÉNTICO salvo restos aprobados

Anexo F (chapters/appendix/interview_4_pena.tex)
  palabras antes: 4354  después: 4335  diferencia: 19
  bloques borrados (13): ['yeah', 'dizzy', 'perfect', 'belly', 'yeah', 'that', 'but', 'thank you', 'yeah', 'yeah', 'think so yeah', 'but', 'say it la milandia']
  RESULTADO: IDÉNTICO salvo restos aprobados
```

---

## Tanda 2: Erratas, tiempo verbal y lenguaje de cursada

### 4. Erratas
- `chapter02.tex` (2.2.4): "Un estudios realizado" → "Un estudio realizado".
- `e50_diseno_ux.tex` (5.1): "fromato" → "formato"; "validada(" → "validada (".
- Villarreal-Vasquez: ya figuraba sin tilde en el `.bib`, en el texto y en el PDF. Sin cambios.

### 5. Pretérito → presente (voz propia)

| Ubicación | Antes → después |
|---|---|
| 5.1 | "no partió… se construyó" → "no parte… se construye"; "Se dibujaron" → "Se dibujan" |
| 5.3.6 | "se eligió" → "se elige" |
| 5.3.7 | "se decidió incluirla" → "se incluye" |
| 3.3.3 (tabla GNN) | "evaluó… priorizó" → "evalúa… prioriza" |
| 3.5 | "se realizó un relevamiento" → "se realiza un relevamiento" |
| 3.6 | "se relevó", "Se obtuvieron", "indicaron", "no respondieron" → "se releva", "Se obtienen", "indican", "no responden" |
| 3.6.5 | "fueron relativamente equilibrados" → "son relativamente equilibrados" |
| 3.6.6 | "se ubicaron", "indicó", "fue seleccionada" → "se ubican", "indica", "es seleccionada" |
| 3.6.7 | "se identificó" → "se identifica" |
| 2.2.6 | "pudimos evidenciar" → "se evidencia" |

Lo que se dejó en pasado, a propósito:
- 3.6.8 ("la detección ocurrió"): relata hechos informados por los encuestados.
- Precondiciones y postcondiciones de los casos de uso e historias de usuario en el capítulo 4.
- 9.4 ("se verificó") y 10.2 a 10.7: describen ejecuciones concretas.

### 6. Lenguaje de cursada
- 1.2: "se implementará un motor… entrenado por los alumnos para detectar… contará… permitirá" → "se implementa un motor… que detecta… cuenta… permite".
- 3.5 / 3.5.3: "para etapas posteriores del desarrollo", "a profundizar en etapas posteriores del proyecto" y "a desarrollar en profundidad en las próximas etapas del proyecto" → "líneas de evolución del sistema".
- 10.7: "conviene corregirlo antes de la entrega" → "conviene corregirlo con prioridad alta".
- 10.8 (tabla): "Corregir los cuatro antes de la entrega" → "Corregir los cuatro".
- 11.4: "citada en anteriores entregas" → "citada".
- 3.3.3 / 3.6.5 / 3.6.9: "PFI" → "el proyecto" / "el sistema".

### 7. Nombres de código en la prosa
- 3.2: "(condición OR entre `is_anomaly_iso` e `is_anomaly_lstm_user`)" → "(basta con que uno de los dos modelos marque el evento como anómalo)".
- 3.6.6: "la explicabilidad proporcionada por `explicar_features`" → "la explicación que acompaña a cada evento, con las tres variables de Isolation Forest que más se apartan de lo habitual,".
- 3.6.5 (agregado): `ProcessCollector`, `FileSystemCollector`, `avg_hour`/`off_hours_ratio`, `denegar_carpeta`, `historial_scores` y `notificar_admin` se describen en palabras.

### 8. Referencias
- 5.1 y tabla de 5.3.2: "Capítulo~\ref{sec:decisiones-transversales-mockups}" → "Sección~\ref{…}".
- Anexo B: "Capítulo 4, Sección~\ref{sec:encuesta-usuarios}" → "Sección~\ref{…}". El número estaba además desactualizado: hoy es el capítulo 3.
- 3.6.7: "la sección de Competencias" → "el Capítulo~\ref{chap:mercado}". Se agregó `\label{chap:mercado}`.

---

## Tanda 3: Títulos y estructura

### 9. Mayúscula de oración
Marco teórico; Gestión de identidad y acceso: …; Introducción a los datasets: datos reales vs. datos sintéticos; Estado del arte; Soluciones comerciales vigentes; Trabajos académicos: modelos de detección de anomalías; Control de acceso adaptativo basado en riesgo (RADAC) y su homónimo en 2.2.3; Autenticación continua basada en biometría conductual; Tendencias emergentes; Conclusión del estado del arte; Análisis comparativo del estado del arte; Contraste con la práctica profesional… / …percepción de los usuarios finales…; Requerimientos, casos de uso e historias de usuario; Requerimientos funcionales; Requerimientos no funcionales; Casos de uso; Historias de usuario; Justificación de diseño y mockups; Análisis de mercado y competitividad; Marketing mix: producto, precio y plaza; Cruz de Porter: 5 fuerzas; Anexo A: Cronograma de actividades.

En el cuerpo, "Estado del Arte" pasa a "Estado del arte" en los capítulos 3 y 11.

Se mantuvieron con mayúsculas los nombres propios y términos técnicos: Zero Trust Architecture, User and Entity Behavior Analytics, Graph Neural Networks, Boston Consulting Group, Isolation Forest y LSTM Autoencoder. También los rótulos con identificador ("Módulo 1: …", "CU-01: …", "HU-01: …", "Épica 1: …").

### 10. Párrafos introductorios
Se agregaron en el capítulo 1, el capítulo 2, 2.1, 2.2, 2.2.1, 2.2.2, 2.2.3, 2.2.5, el capítulo 3, el capítulo 4, 4.5, las épicas 4.6.1 a 4.6.5 (una oración cada una), el capítulo 6, 7.3, 8.3, 9.2, 10.2, 10.4, 10.6, el capítulo 11 y 11.1. Solo describen lo que contienen las subsecciones. También hay una oración introductoria antes de las listas de Fortalezas, Debilidades, Oportunidades y Amenazas.

### 11. Plaza (11.1.3)
Se reorganizó en canales de distribución (directo self-service; integradores y MSSP), modalidad de despliegue (API y bases como servicios gestionados en la nube, agente en cada equipo Windows) y alcance geográfico. Este último no figura en ninguna parte del documento: queda con un `\todo[inline]` visible en el PDF (ver revisión manual).

---

## Tanda 4: Figuras, tablas y citas

### 12. Fuente de las figuras
Como no se usa el paquete `caption`, se agregó `{\small Fuente: …\par}` dentro de cada `figure`, después del `\label`. El caption y la Lista de Figuras no cambian. Son 48 figuras:
- Wireframes, diagramas, FODA, BCG, Gantt y la curva de 10.1: "Fuente: elaboración propia."
- Pantallas reales (5.2, 5.4, 5.6, 5.8, 5.10, 5.11, 5.13, 5.15, 5.17): "Fuente: elaboración propia, captura del sistema."
- Encuesta (B.1 a B.18): "Fuente: elaboración propia a partir de los resultados de la encuesta."

### 13. Referencias a figuras
Ahora se referencian las figuras 5.1 a 5.17 (una oración por pantalla), 6.1 a 6.5, 11.1, 11.2 y A.1 (Gantt, que tampoco tenía referencia). La figura 8.2 ya estaba referenciada en 8.5.1. Se comprobó que toda figura con `\label` tiene al menos un `\ref`.

### 14. Citas narrativas en el Estado del arte
Las 14 oraciones con `\textcite` de la sección 2.2 se reescribieron en forma parentética con `\parencite`. Las 4 del Marco teórico (2.1) no se tocaron, porque el pedido era solo sobre el Estado del arte (ver revisión manual).

### 15. Bibliografía
- Se quitaron Splunk2025, MicrosoftSentinelUEBA, MicrosoftEntraIDProtection, MicrosoftEntraRisks, OktaAdaptiveMFA, OktaRiskScoring, ExabeamUEBA y CortexXSOAR, junto con sus citas.
- También se quitaron ExabeamPlatform y SplunkSOAR, que eran documentación de proveedores sin citar.
- "SplunkSOAR" en el texto se corrigió a "Splunk SOAR".
- Al-Shehari ahora se ordena bajo A (se agregó `SORTKEY` en la entrada). Verificado en el PDF.

### 16. Citas de los marcos de análisis
- Porter, M. E. (1979). How Competitive Forces Shape Strategy. *Harvard Business Review*, 57(2), 137–145. Datos verificados.
- Henderson, B. D. (1970). *The Product Portfolio*. BCG Perspectives, The Boston Consulting Group. Autor, año y título verificados; el número de la serie no.
- Weihrich, H. (1982). The TOWS Matrix—A Tool for Situational Analysis. *Long Range Planning*, 15(2), 54–66. Datos verificados; no se cargó DOI.

---

## Tanda 5: Encabezado

El texto "AGENTE INTELIGENTE DE RIESGO DE IDENTIDAD" está definido en `main.tex:55`, dentro de `\newpagestyle{ruled}` → `\sethead{…}{\parbox[b]{0.43\textwidth}{\raggedright\MakeUppercase{Agente Inteligente de Riesgo de Identidad}}}{…}`. No se modificó.

---

## Puntos marcados para revisión manual

1. **Plaza, alcance geográfico** (`e50_mercado.tex:36`): `\todo[inline]` visible en el PDF; hay que completarlo.
2. **Afirmaciones sin respaldo tras quitar las citas de proveedores** (comentarios `% REVISAR (E75)` en `chapter02.tex`):
   - "Entre los resultados reportados, Microsoft destaca…" (l. 120).
   - "Diversos usuarios señalan…" (l. 123).
   - "Entre los resultados reportados, Splunk UBA destaca…" (l. 133).
   - "Diversos reportes señalan…" (l. 136).
   - "Entre los resultados reportados por el fabricante, Exabeam…" (l. 146).
   - "Entre los resultados reportados por Microsoft…" (l. 158).
   - "Según la documentación oficial de Okta…" (l. 197).
3. **`e50_mercado.tex:112` (BCG, crecimiento del mercado)**:
   - "toda la bibliografía citada es de 2025 en adelante" es falso (hay fuentes de 1979 a 2024).
   - Remite a una "sección de Conocimientos del proyecto" y a una cita ("el perímetro ha desaparecido…") que no existen en el documento.
4. **Henderson (1970)**: completar el número de BCG Perspective si se requiere. Opcional: DOI de Weihrich (1982).
5. **`chapter04.tex:176`**: la celda "Diferenciador del proyecto propuesto" de la tabla del proyecto está vacía.
6. **`\textcite` del Marco teórico** (`chapter02.tex:14, 39, 71, 93`): sin convertir. Decidir si también pasan a forma parentética.
7. **Transcripciones**:
   - Se mantuvieron `Ok/Okay` (uso real en el habla).
   - Quedan sin tocar `permission de night` (Anexo C, probable "permission denied") y `en un copy` (Anexo F).
   - En el Anexo E hay turnos mezclados: preguntas del entrevistador dentro del turno de Guillermo y viceversa. Separarlos implica cambiar etiquetas.
   - Quedan 6 oraciones de 46 a 59 palabras sin un punto de corte natural.
   - El Anexo G (cuestionario escrito) conserva la etiqueta `Ruiz Matías Gabriel:`.
