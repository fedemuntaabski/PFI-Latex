# E75 — Estructura: niveles, hijo único, mayúsculas y residuo de 13.4

Rama `correcciones-e75-latex`. Fecha: 2026-10-09. Los números de línea corresponden al estado posterior al cambio.

## Cómo se buscaron los casos
- **Niveles sin texto intermedio e hijos únicos**: un script recorre los 17 `.tex` compilados (capítulos 1 a 13, `requerimientos.tex` y anexos), arma el árbol de `\chapter`/`\section`/`\subsection`/`\subsubsection`/`\paragraph`/`\anexo` y marca (a) cada heading seguido de un nivel inferior sin texto en el medio (sin contar comentarios ni `\label`) y (b) cada heading con un único hijo directo.
- **Mayúsculas y referencias**: `grep` sobre los fuentes y `pdftotext` del PDF compilado (índice, lista de figuras, lista de tablas y cuerpo).
- `chapters/archivo/`, `abstract.tex`, `acknowledgments.tex`, `summary.tex`, `conclusion.tex` y `appendix/interviews.tex` no se compilan y no se tocaron.

## A. Párrafos introductorios

El script encontró **solo los cuatro casos señalados**. No hay otros en el documento: después del cambio el script no marca ningún caso.

| Archivo:línea | Antes | Después |
|---|---|---|
| `chapters/chapter01.tex:7-11` | `\section{Objetivos}` seguido de `\subsection{Objetivo general}` | párrafo nuevo (1) entre ambos |
| `chapters/negocio.tex:79-83` | `\section{Viabilidad económico-financiera}` seguido de `\subsection{Supuestos}` | párrafo nuevo (2) entre ambos |
| `chapters/negocio.tex:245-247` | `\section{Identidad de marca}` seguido de `\subsection{Nombre}` | párrafo nuevo (3) entre ambos |
| `chapters/conclusiones.tex:3-6` | `\chapter{Conclusiones y trabajo futuro}` seguido de `\section{Cumplimiento de los objetivos}` | párrafo nuevo (4), con el patrón "Este capítulo …" de los demás capítulos |
| `chapters/conclusiones.tex:8` | `\section{Cumplimiento de los objetivos}` | `\section{Cumplimiento de los objetivos}\label{sec:cumplimiento-objetivos}` (label nuevo, usado por el párrafo 1) |

Párrafos nuevos:

1. **1.1 Objetivos**
   > Los objetivos del proyecto se organizan en dos niveles. El objetivo general enuncia el propósito del sistema en su conjunto, y los objetivos específicos lo descomponen en metas verificables sobre el agente, el modelo de detección, la respuesta en el equipo, el panel de administración, la protección del propio sistema, el marco legal y las pruebas. El grado de cumplimiento de cada uno se analiza en la sección~\ref{sec:cumplimiento-objetivos}.

   (En el PDF: "… se analiza en la sección 13.1.")

2. **12.4 Viabilidad económico-financiera**
   > La viabilidad económico-financiera se evalúa en cuatro pasos. Primero se fijan los supuestos del análisis; luego se plantean tres escenarios de adopción (pesimista, base y optimista) y se calculan para cada uno el valor actual neto, la tasa interna de retorno, el período de recupero y la necesidad máxima de fondos; por último, se interpretan esos indicadores y su sensibilidad a la tasa de descuento.

   (Los escenarios y los indicadores son los de las tablas `tab:clientes-fin`, `tab:indicadores-fin` y `tab:sensibilidad-fin`.)

3. **12.5 Identidad de marca**
   > La identidad de marca reúne los elementos con los que el producto se presenta ante el mercado. Esta sección justifica el nombre elegido, describe el logotipo y define el posicionamiento y el mensaje con los que se comunica la propuesta de valor.

4. **Capítulo 13 Conclusiones y trabajo futuro**
   > Este capítulo cierra el documento. Analiza el grado de cumplimiento del objetivo general y de cada objetivo específico, resume los resultados principales del proyecto en sus aspectos técnicos, económicos y legales, reúne las lecciones aprendidas durante el desarrollo y propone las líneas de trabajo futuro, priorizadas según su impacto sobre la principal limitación del sistema.

## B. Subsección con un solo hijo

El script encontró **un solo caso**: 10.5 → 10.5.1. No hay otros.

Se optó por partir la sección en **dos subsecciones**, porque su contenido ya tenía dos bloques con sentido propio: las metas de evaluación con su resultado (tabla 10.VII) y las métricas no supervisadas del modelo híbrido (tabla 10.VIII). Así 10.5.1 conserva `\label{sec:metas-modelo}` y **no cambia ninguna referencia**: el objetivo específico 2 (`chapter01.tex:27`) sigue citando "la sección 10.5.1", igual que la sección 10.7 ("Las metas de la sección 10.5.1 se mantienen…").

| Archivo:línea | Antes | Después |
|---|---|---|
| `chapters/pruebas.tex:217` | párrafo inicial de 10.5 terminado en "…se realiza sobre él." | se agrega al final la oración (5) |
| `chapters/pruebas.tex:262` | (sin heading) | `\subsection{Métricas no supervisadas}\label{sec:metricas-no-supervisadas}` (10.5.2) |
| `chapters/pruebas.tex:263` | "El conjunto de datos utilizado no incluye etiquetas de actividad maliciosa \parencite{Landauer2022Dataset}. Por lo tanto, no es posible calcular precisión, …" | "Como el conjunto de datos no incluye etiquetas de actividad maliciosa \parencite{Landauer2022Dataset}, no es posible calcular precisión, …" (el resto del párrafo queda igual) |

La reformulación de la l. 263 evita que 10.5.2 abra con la misma oración que 10.5.1.

5. **Oración nueva en 10.5**
   > La sección se organiza en dos partes: primero se fijan las metas de evaluación y se contrasta con ellas el resultado obtenido, y luego se presentan las métricas no supervisadas que describen el comportamiento del modelo híbrido y el acuerdo entre sus dos componentes.

## C. Mayúscula de oración

| Archivo:línea | Antes | Después |
|---|---|---|
| `main.tex:137` | `\renewcommand{\listfigurename}{Lista de Figuras}` | `…{Lista de figuras}` |
| `main.tex:138` | `\renewcommand{\listtablename}{Lista de Tablas}` | `…{Lista de tablas}` |
| `chapters/appendix/schedule_of_activities.tex:15` | `\caption{Diagrama de Gantt del Proyecto --- Planificación de Hitos y Distribución de Tareas.}` | `\caption{Diagrama de Gantt del proyecto: planificación de hitos y distribución de tareas}` |
| `chapters/e50_uml.tex:36` | `\caption{Diagrama de clases del Agente PEP.}` | `\caption{Diagrama de clases del agente PEP.}` **(caso extra)** |
| `chapters/chapter04.tex:215` | "según lo que el propio Estado del arte documenta" | "…el propio estado del arte documenta" |
| `chapters/chapter04.tex:394` | "A partir de la propia Conclusión del estado del arte" | "…la propia conclusión del estado del arte" **(caso extra)** |
| `chapters/e50_mercado.tex:13` | "relevadas en el Estado del arte" | "…en el estado del arte" |
| `chapters/e50_mercado.tex:17` | "según el propio Estado del arte" | "…el propio estado del arte" |
| `chapters/e50_mercado.tex:18` | "(cita textual del Estado del arte)" | "(cita textual del estado del arte)" |
| `chapters/e50_mercado.tex:19` | "que el Estado del arte describe" | "que el estado del arte describe" (caso citado por el profesor, cap. 11) |
| `chapters/e50_mercado.tex:37` | "el propio Estado del arte describe" | "el propio estado del arte describe" |
| `chapters/e50_mercado.tex:42` | "relevado en el Estado del arte" | "relevado en el estado del arte" |
| `chapters/e50_mercado.tex:56` | "que el propio Estado del arte identifica" | "…estado del arte identifica" |
| `chapters/e50_mercado.tex:60` | "que el Estado del arte señala" | "que el estado del arte señala" |
| `chapters/e50_mercado.tex:96` | "que señala el propio Estado del arte" | "…el propio estado del arte" |

Revisados y **sin cambio** (todos los títulos de capítulo, sección, subsección, subsubsección, anexo y los epígrafes de figuras y tablas):
- Nombres propios y términos técnicos establecidos: Microsoft Sentinel UEBA, Splunk UBA, Exabeam, Microsoft Entra ID Protection, Okta Adaptive MFA, Zero Trust Architecture, User and Entity Behavior Analytics, Graph Neural Networks (GNN), Isolation Forest, LSTM Autoencoder, Matriz Boston Consulting Group (BCG), Cruz de Porter, HOLDOUT (nombre de la partición) y los nombres de los entrevistados en los anexos C a G.
- Rótulos con código antes de los dos puntos ("Módulo 1: Agente local…", "CU-01: …", "Épica 1: …", "HU-01: …"): son identificadores con su título y se mantienen con el criterio de todo el capítulo 4.
- Epígrafes de los wireframes y las tablas de justificación del capítulo 5 ("Wireframe de baja fidelidad: Acceso (Login)", "…: Usuarios (listado)", "…: Alertas", etc.): lo que sigue a los dos puntos es el nombre de la pantalla del panel, igual que el título de cada subsección.
- Figura B.13 ("…te parece MENOS disruptivo…"): transcribe literalmente la pregunta de la encuesta.
- `\tablename` = "TABLA": convención de formato del documento, no es Title Case.
- `\section{Estado del arte}` (`chapter02.tex:159`) y `\subsection{Conclusión del estado del arte}`: ya están en mayúscula de oración.

## D. Texto suelto "dor de identidad real. ]" al final de 13.4

- **Origen**: `chapters/conclusiones.tex:131`, último ítem de la enumeración de trabajo futuro: `\item [[CODIGO: limitaciones de seguridad … proveedor de identidad real.]]`. `\item` interpreta el primer `[` como inicio de su argumento opcional (la etiqueta del ítem). La etiqueta tomaba `[CODIGO: … real.` hasta el primer `]`; como no entra en la caja de la etiqueta, se veía solo el final ("dor de identidad real.") y el segundo `]` quedaba como texto del ítem.
- **Cambio**: `\item [[CODIGO: …` → `\item{} [[CODIGO: …`. El grupo vacío impide que `\item` lea el corchete como argumento opcional. El texto del marcador no cambia.
- **Texto perdido**: no hubo. El ítem solo contenía el marcador, que ahora se compone completo. En el PDF el ítem 10 queda: "10. [[CODIGO: limitaciones de seguridad que queden abiertas después del trabajo del repo de código; integración con un proveedor de identidad real.]]". El fragmento "real. ]" ya no aparece en el PDF.

## E. Referencias "Capítulo X.Y"

- En los archivos compilados **no hay ningún caso** de "capítulo"/"Capítulo" seguido de un número de sección ni de un `\ref` a una sección. Todos los `capítulo~\ref{…}` apuntan a labels `chap:` y en el PDF se leen como "capítulo N". El único `Capítulo~\ref{sec:…}` está en `chapters/archivo/obsoleto_e50.tex`, que no se compila.
- **Casos extra**: referencias con mayúscula en medio de oración. El resto del documento usa "la sección~\ref" y "el capítulo~\ref" en minúscula, así que se pasaron a minúscula:

| Archivo:línea | Antes | Después |
|---|---|---|
| `chapters/chapter04.tex:175` | "se presenta en la Sección~\ref{sec:sintesis-diferenciadores}" | "…en la sección~\ref{…}" |
| `chapters/chapter04.tex:186` | "lo que la Sección~\ref{sec:estado-del-arte} documenta" | "lo que la sección~\ref{…} documenta" |
| `chapters/chapter04.tex:224` | "(Sección~\ref{sec:comparacion-general})" | "(sección~\ref{…})" |
| `chapters/chapter04.tex:394` | "(Sección~\ref{sec:estado-del-arte})" | "(sección~\ref{…})" |
| `chapters/chapter04.tex:491` | "(Sección~\ref{sec:entrevistas-profesionales}) y con el análisis FODA/Porter del Capítulo~\ref{chap:mercado}" | "(sección~\ref{…}) … del capítulo~\ref{chap:mercado}" |
| `chapters/e50_diseno_ux.tex:9` | "en la Sección~\ref{sec:decisiones-transversales-mockups}" | "en la sección~\ref{…}" |
| `chapters/e50_diseno_ux.tex:84` | "(ver Sección~\ref{sec:decisiones-transversales-mockups} …)" | "(ver sección~\ref{…} …)" |
| `chapters/appendix/surveys.tex:3` | "se encuentra en la Sección~\ref{sec:encuesta-usuarios}" | "…en la sección~\ref{…}" |

- **Pendiente, fuera de alcance**: "Figura~\ref" aparece con mayúscula en medio de oración o entre paréntesis (por ejemplo, `chapter04.tex:451-495` "(Figura~\ref{…}, Anexo B)" y `schedule_of_activities.tex:3`), mientras que otros capítulos usan "la figura~\ref". No se modificó porque la consigna se refiere a "sección"/"capítulo"; conviene unificarlo en otra pasada.

## Marcadores
`git diff` sobre `[[CODIGO`: la única línea modificada es la del `\item{}` de `conclusiones.tex:131`, y el texto del marcador queda idéntico. No se tocó ningún otro marcador.

## Compilación
`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`:
- Compila sin errores. `build/main.pdf`: **244 páginas** (antes 243; la página extra viene de los párrafos nuevos).
- **Referencias y citas sin definir: 0. Labels con definición múltiple: 0.** `pdftotext` del PDF no encuentra "??".
- Warnings de LaTeX: 2 `'h' float specifier changed to 'ht'` (antes 4; bajan por el cambio de paginación). Warnings de paquetes: los 3 de siempre (xcolor, microtype, soulutf8).
- Overfull: 246 (antes 245). Underfull: 64 (sin cambios). Ninguno de los overfull cae en las líneas de los párrafos nuevos; el adicional no se pudo atribuir a un cambio concreto.
- Verificado en el PDF: "Lista de figuras" y "Lista de tablas" como títulos; Figura A.1 con el epígrafe nuevo, también en la lista de figuras; Figura 6.3 "Diagrama de clases del agente PEP."; 10.5.1 "Metas de evaluación" y 10.5.2 "Métricas no supervisadas" en el índice; objetivo específico 2 citando la sección 10.5.1; ítem 10 de 13.4 completo.
