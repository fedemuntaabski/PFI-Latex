# P8 E75 — Remanentes de la devolución E50

Rama `e75/paquete`. Un commit por tanda, sin push. Compilación tras cada tanda
(`pdflatex`, `biber`, `pdflatex` ×2): 0 errores, 0 referencias o citas indefinidas, ningún `??` en el PDF.

| Tanda | Commit |
|---|---|
| 1. Formato de citas | `088746a` |
| 2. Tablas sin referencia | `91225d2` |
| 3. Tiempo verbal | `136bc1c` |
| 4. Restos | `6cc8575` |
| 5. Transcripciones | sin cambios (ver abajo) |

## Tanda 1 — Formato de citas

Único cambio en el preámbulo (`main.tex:16`): se agrega `uniquelist=false` a las opciones de `biblatex`.

Se compararon las 71 citas parentéticas del PDF antes y después del cambio. Cambiaron solo estas:

| Antes | Después | Apariciones |
|---|---|---|
| (Landauer; Onder et al., 2023) | (Landauer et al., 2023) | 5 |
| (Artioli et al., 2024; Landauer; Onder et al., 2023) | (Artioli et al., 2024; Landauer et al., 2023) | 1 |
| (Landauer; Skopik et al., 2022a; Landauer; Skopik et al., 2022b) | (Landauer et al., 2022a; Landauer et al., 2022b) | 1 |
| (Landauer; Skopik et al., 2022b) | (Landauer et al., 2022b) | 3 |
| Landauer; Onder et al. (2023) (cita textual, tabla 3.XIV) | Landauer et al. (2023) | 1 |

Verificación:

- `Landauer2022` → 2022a, `Landauer2022Dataset` → 2022b, `Landauer2023Survey` → 2023. Las tres obras siguen distinguiéndose.
- En el `.bbl` solo esas dos obras de 2022 llevan `extradate`. No hay otras obras con el mismo primer autor y año.
- El patrón "Autor; Autor et al." aparecía 11 veces en el cuerpo del PDF antes del cambio y no aparece ninguna después.

## Tanda 2 — Tablas y figuras sin referencia por número

Un script contó, para cada `\label{tab:…}` y `\label{fig:…}` de los capítulos 1 a 13, los `\ref`, `\autoref`, `\cref` y `\pageref` fuera del propio float.
Encontró 38 etiquetas sin referencias, más que las 16 señaladas en el PDF. Ninguna es una figura.
Se agregó una oración por serie; no se reescribió ningún párrafo:

| Tablas | Ubicación | Oración agregada |
|---|---|---|
| 3.I a 3.VII | §3.1, párrafo introductorio | Las tablas~\ref{tab:comp-sentinel} a~\ref{tab:comp-proyecto} presentan esa comparación. |
| 3.VIII | §3.2, párrafo introductorio | La tabla~\ref{tab:matriz-capacidades} resume esa verificación. |
| 3.IX a 3.XV | §3.3, párrafo introductorio | Las tablas~\ref{tab:algo-catboost} a~\ref{tab:algo-proyecto} presentan esa comparación. |
| 4.I | §4.2, antes de la tabla | La tabla~\ref{tab:actores} describe los actores del sistema. |
| 4.II a 4.VIII | §4.3, párrafo introductorio | Las tablas~\ref{tab:rf-modulo1} a~\ref{tab:rf-modulo7} presentan los requerimientos de cada módulo. |
| 5.I a 5.VIII | "Catálogo de pantallas" | Las tablas~\ref{tab:mockup-login} a~\ref{tab:mockup-historial} contienen esas justificaciones. |
| 7.II a 7.V | "Frameworks y librerías" | Las tablas~\ref{tab:tec-api} a~\ref{tab:tec-pipeline} detallan cada componente. |
| 7.VI | "Servicios e infraestructura" | La tabla~\ref{tab:servicios} enumera los servicios externos y la infraestructura del sistema. |
| 7.VIII | "Protocolos de comunicación" | La tabla~\ref{tab:protocolos} resume los protocolos entre componentes. |
| 10.VI | §10, consumo de recursos (RNF-02) | La tabla~\ref{tab:rnf02} presenta los resultados. |
| 12.II | §12, supuestos | La tabla~\ref{tab:supuestos-fin} resume los supuestos. |

Al volver a correr el script, solo quedan sin referencia propia las tablas internas de los rangos (3.II a 3.VI, 3.X a 3.XIV, 4.III a 4.VII, 5.II a 5.VII, 7.III a 7.IV). Están cubiertas por la oración con rango; en `main.aux` se verificó que cada serie es consecutiva.

## Tanda 3 — Tiempo verbal

El barrido de los capítulos 1 a 13 encontró 150 formas en pretérito (`se …ó`, `…aron`, `…ieron`, `fue/fueron`) y, después, las irregulares (`reprodujo`, `tradujeron`, `obtuvieron`, `redujo`, etc.).
Se pasaron 79 al presente:

| Capítulo | Cambios |
|---|---|
| 7 Arquitectura | se descartó, se eligió (×2), se prefirió, se realizaron, no se creó → no está creada, se evaluó, se dejó, se reemplazaron, se eligieron |
| 8 Datos | se entrenó (×3), se clasificaron (×2), se descartaron, se excluyeron (×2), se utilizaron, se estandarizaron, se obtuvieron, se particionaron |
| 9 Producto | se utilizó, fue verificado → se verifica, no se observó, se verificó, se aplicó, no se creó, se entrenó, se evaluaron |
| 10 Pruebas | se tomaron (×2), fueron obtenidos → se obtienen, se midió (×4), fueron verificados → se verifican, se realizaron, fue sometido → se somete, se descartaron, se ejecutó (×2), no fue instrumentada → no está instrumentada, se enviaron, se registró (×2), se evaluó (×2), se construyeron, se inyectaron, se seleccionaron, se reprodujo, se tomó, se inyectó, se recalculó, se pudo, no se aislaron, se utilizaron, revisó, se verificaron, se clasificó, se identificaron, no se encontraron, fueron → son, se corrigió, se corrigieron (×2), se unificó, se tradujeron, se mejoró, se evaluaron, lo corrigió, redujo (×2), identificó, se verificó, no fue validada → no está validada |
| 13 Conclusiones | se verificó, se observaron |

Quedan en pretérito, porque no narran trabajo del equipo o porque son ejecuciones fechadas:

- **Capítulo 2:** obras de otros autores y hechos normativos (aprobó, asumió, compararon, mostraron, etc.).
- **Capítulo 3:** citas textuales y respuestas de la encuesta (fue concedido, fue comunicada, fueron detectados).
- **Capítulos 4 y 5:** poscondiciones de casos de uso y semántica de la interfaz (quedó registrado, qué cambió, se cerró ese día).
- **Capítulo 10, ejecuciones fechadas:** demostración de agosto de 2026, configuración de septiembre de 2026 y reentrenamiento de agosto de 2026 (se ejecutaron, generó, quedó, se alcanzó, se verificó, completó, no promovió, empeoró).
- **Capítulo 10, resultados obtenidos:** terminó, fue del 14,6 %, se concentró, elevaron, quedó, provinieron, superó, finalizaron, confirmaron, finalizó.
- **Capítulo 9 (producto:131) y Capítulo 13 (conclusiones:32):** la única corrida real del planificador (produjo, no se promovió).
- **Capítulo 12:** el dato de mercado (osciló).

Los dos ejemplos que cita la devolución ya estaban en presente: "no parte de un wireframe estático, sino que se construye" (cap. 5) y "se releva … mediante una encuesta" (cap. 3).

## Tanda 4 — Restos

| Ítem | Antes | Después |
|---|---|---|
| a. 2.2.3 | `% REVISAR (E75): remite a la documentación de Okta…` + "Según la documentación oficial de Okta, el sistema trabaja con señales en tiempo real…" | Comentario eliminado. "Okta Adaptive MFA trabaja con señales en tiempo real…" |
| b. RNF-02 | "El agente debe ser liviano y no degradar el uso normal del equipo: consumo medio…" | "El agente opera con un consumo acotado que preserva el uso normal del equipo: consumo medio de CPU menor o igual al 5 % de la máquina y memoria residente menor o igual a 150 MB." |
| b. RNF-10 | "El reentrenamiento no debe afectar la disponibilidad ni la latencia del servicio de scoring en producción." | "El reentrenamiento se ejecuta en un proceso aislado que preserva la disponibilidad y la latencia del servicio de scoring en producción." |
| c. 3.6.2 | "percibidos por los usuarios" | "percibidos por los participantes" |
| c. 3.6.5 | "los usuarios valoran" | "los participantes valoran" |
| c. 3.6.9 | "prioridades expresadas por los usuarios" (el texto decía "usuarios", no "población objetivo") | "prioridades expresadas por los participantes" |
| c. 3.6.9 | "Los resultados también respaldan varias decisiones" | "Los resultados también son consistentes con varias decisiones" |
| d. 2.2.6 | "motor de IA en la nube" | "motor de IA de la API central" |
| e. 10.5.1 | `[[DECIDIR: los valores de las metas…]]` | "Las metas se fijan antes de cualquier reentrenamiento posterior del modelo; si este cambia los resultados, se informan contra estas mismas metas." |
| f. 6.x | "Diagrama de clases --- Agente PEP" | "Diagrama de clases --- agente PEP" |

f. Títulos de sección. Se revisaron todos los encabezados de los capítulos 1 a 13. Solo se corrigió el de 6.x. Se mantienen:

- **Productos:** Microsoft Sentinel UEBA, Splunk UBA, Microsoft Entra ID Protection, Okta Adaptive MFA.
- **Técnicas:** Isolation Forest, LSTM Autoencoder, Graph Neural Networks.
- **Marcos:** Zero Trust Architecture, User and Entity Behavior Analytics.
- **Siglas y nombres propios:** RBAC, ABAC, RADAC, XAI, SOAR, FODA, UML, API PDP, Porter, Boston Consulting Group.
- **Rótulos con dos puntos (`Módulo N:`, `CU-0N:`, `HU-NN:`, `Épica N:`):** la mayúscula después del rótulo es la convención para epígrafes de este tipo.

## Tanda 5 — Transcripciones (Anexos C y E)

Ningún turno de los entrevistados tiene oraciones de más de 60 palabras. La puntuación ya se había corregido en el commit `5157d99` ("limpia y puntúa transcripciones (Anexos C-F)").

| Anexo | Archivo | Oración más larga | Oraciones > 60 palabras | Palabras |
|---|---|---|---|---|
| C (Villarino) | `interview_1_pablo.tex` | 49 | 0 | 7513 |
| E (Pita) | `interview_3_guillermo.tex` | 49 | 0 | 6185 |

No se modificó ninguno de los dos archivos (`git diff` vacío), así que la secuencia de palabras es idéntica por construcción. En los demás anexos tampoco hay oraciones de más de 60 palabras; la más larga está en el D, con 59.

## Pendientes fuera de alcance (no se tocaron)

Quedan marcadores `[[…]]` en:

- `chapter01.tex:53`
- `chapter04.tex:438` (`[[COMPLETAR: fechas]]`)
- `requerimientos.tex:79` y la celda de estado de RNF-02 (`[[ESTADO SEGÚN RNF-02]]`)
- `producto.tex:129, 158, 162`
- `pruebas.tex`: valores y la interpretación de RNF-02
- `conclusiones.tex`, líneas 20 a 64

Se imprimen en el PDF.
