# Textos listos para insertar — E75

Cada bloque `T#` está escrito para pegarse en el `.tex`. Los prompts de `prompts_latex_e75.md` le indican a Claude Code dónde va cada uno.

**Convenciones**
- `[[DECIDIR: ...]]`: lo tiene que decidir el equipo antes de compilar la versión final.
- `[[VERIFICAR: ...]]`: dato que hay que confirmar contra una fuente.
- `[[CODIGO: ...]]`: dato que depende del trabajo del repo de código (cobertura, seguridad, RNF-02, reentrenamiento). Se completa en L3.
- Las citas usan `\parencite{clave}`. Las claves nuevas están en el bloque T22.
- Todo lo numérico sale del propio documento (capítulos 8, 9 y 10) o del modelo financiero (`modelo_financiero.py`).

---

## T1 — Título y encabezado

Propuestas. Cumplen 10 a 20 palabras y responden qué, quién, dónde y cuándo, con nombre de producto.

1. **UMBRAL: agente inteligente de vigilancia conductual y mitigación de riesgo de identidad para PyMEs argentinas (2026)** — 15 palabras.
2. **UMBRAL: agente de detección conductual y respuesta automática ante el uso indebido de credenciales en PyMEs argentinas, 2026** — 17 palabras.
3. **UMBRAL: monitoreo conductual continuo y mitigación automática del riesgo de identidad en endpoints de PyMEs de Argentina (2026)** — 17 palabras.

Encabezado de página (versión corta, consistente con la carátula): `UMBRAL: AGENTE DE VIGILANCIA CONDUCTUAL Y MITIGACIÓN DE RIESGO DE IDENTIDAD`. Si no entra en dos líneas: `UMBRAL — VIGILANCIA CONDUCTUAL Y RIESGO DE IDENTIDAD`.

`[[DECIDIR: nombre del producto. "UMBRAL" es una propuesta (ver T18). Si se cambia, cambia en T1, T16 y T18. Verificar que no esté registrado como marca en la clase 9/42 del INPI.]]`

---

## T2 — Objetivos (reemplaza 1.1)

```latex
\section{Objetivos}

\subsection{Objetivo general}
Desarrollar un sistema de seguridad conductual que evalúe de forma continua, durante toda la
sesión, la desviación del comportamiento de cada usuario respecto de su conducta habitual mediante
un puntaje de riesgo dinámico, y que ejecute en el propio equipo una respuesta proporcional a ese
riesgo, siguiendo la separación entre punto de decisión y punto de aplicación de políticas
propuesta por la arquitectura Zero Trust \parencite{rose2020}.

\subsection{Objetivos específicos}
\begin{enumerate}
  \item Implementar un agente para equipos Windows que recolecte únicamente metadatos de actividad
        (procesos, archivos y conexiones de red), los envíe a una API central por un canal cifrado
        y autenticado, y consuma como máximo el 5\,\% de la CPU y 150\,MB de memoria residente.
  \item Entrenar un modelo híbrido de detección de anomalías (Isolation Forest y LSTM Autoencoder)
        sobre un conjunto de datos público de comportamiento de usuarios, y evaluarlo contra las metas
        de detección y de alertas sobre actividad normal definidas en la sección \ref{sec:metas-modelo}.
  \item Calcular un puntaje de riesgo de 0 a 100 por evento, con continuidad entre sesiones y
        decaimiento temporal, con una latencia de evaluación de percentil 95 menor o igual a 500\,ms.
  \item Ejecutar en el equipo una respuesta graduada según el nivel de riesgo, desde una alerta hasta
        la terminación de procesos y la denegación de acceso a carpetas, reversible cuando el sistema
        operativo lo permita.
  \item Proveer un panel de administración que muestre el estado de riesgo de cada usuario con su
        explicación y permita modificar umbrales, acciones y notificaciones sin reiniciar componentes.
  \item Mantener la vigencia del modelo mediante un reentrenamiento periódico aislado del servicio de
        producción, y tratar a los usuarios nuevos con un período de aprendizaje.
  \item Proteger las credenciales del sistema y el canal entre sus componentes mediante cifrado en
        tránsito y autenticación mutua entre el agente y la API.
  \item Analizar el tratamiento de datos personales que realiza el sistema a la luz de la Ley 25.326
        y de la normativa laboral argentina, e identificar los controles que lo hacen viable.
  \item Verificar el sistema con pruebas automatizadas que alcancen una cobertura de código mínima
        del 85\,\%, pruebas de extremo a extremo y una evaluación de usabilidad del panel.
\end{enumerate}
```

Notas:
- La etiqueta `\label{sec:metas-modelo}` la crea T9.
- Si el objetivo 7 no queda cumplido en el código, no se borra: se informa como "parcial" en las conclusiones (T19).

---

## T3 — Metodología de desarrollo (nueva 1.4)

```latex
\section{Metodología de desarrollo}
El proyecto se desarrolla mediante un proceso iterativo e incremental guiado por casos de uso
\parencite{larman2003}. Cada incremento toma un conjunto de casos de uso, lo lleva a través de
análisis, diseño, implementación y prueba, y entrega una versión ejecutable del sistema completo
sobre la que se planifica el incremento siguiente. Se elige este enfoque por tres motivos. Primero,
el comportamiento del modelo de detección no puede conocerse antes de entrenarlo y probarlo
contra la telemetría real del agente, de modo que los requerimientos se ajustan a partir de los
resultados de cada iteración. Segundo, el sistema tiene tres componentes desplegados en forma
independiente (agente, API y panel), y un incremento vertical que atraviesa los tres permite
verificar la integración temprano. Tercero, un equipo de dos personas no justifica los roles y
ceremonias de un marco como Scrum, pero sí la entrega frecuente de versiones verificables.

Se organizan dos incrementos principales. El primero cubre la detección y la mitigación en el
equipo (CU-01) y el ajuste de políticas desde el panel (CU-02). El segundo incorpora el
reentrenamiento periódico del modelo (CU-03), el alta de usuarios nuevos con período de
aprendizaje (CU-04), la integración con sistemas de gestión de identidad y el endurecimiento de la
ingesta, la autenticación y el canal. El cronograma de ambos incrementos se presenta en el
Anexo~A.

El pipeline de entrenamiento del modelo se organiza en seis fases sucesivas, desde la
preparación del conjunto de datos hasta la exportación de los artefactos que consume la API,
y se ejecuta en forma separada del ciclo de desarrollo del software. [[VERIFICAR: nombrar las seis
fases tal como están en los notebooks.]]

La gestión del trabajo se apoya en el control de versiones con ramas por funcionalidad, la
revisión de cada cambio antes de integrarlo y un pipeline de integración continua que ejecuta el
análisis estático, la compilación y las pruebas automatizadas en cada cambio (sección
\ref{sec:integracion-continua}). La división de tareas responde a la especialización de cada
integrante: uno concentra el entrenamiento del modelo y el otro el agente, la API y el panel.
[[VERIFICAR: que la división de tareas descripta sea la real; ajustar si no.]]
```

`[[VERIFICAR: la etiqueta de la sección de integración continua (10.2.3) — crearla si no existe.]]`

---

## T4 — Estructura del documento (nueva 1.5)

> Se inserta al final, cuando ya existen todos los capítulos nuevos. Ajustar números si cambian.

```latex
\section{Estructura del documento}
El documento se organiza en trece capítulos. El capítulo~\ref{cap:antecedentes} presenta el marco
teórico (el punto ciego posterior a la autenticación, la arquitectura Zero Trust, el análisis de
comportamiento de usuarios y entidades, los modelos de control de acceso, los algoritmos de detección
de anomalías y el marco legal de protección de datos personales) y el estado del arte en soluciones
comerciales y trabajos académicos. El capítulo~\ref{cap:comparativo} compara el proyecto con esas
alternativas y contrasta el diseño con entrevistas a profesionales de seguridad y con una encuesta a
usuarios finales. El capítulo~\ref{cap:requerimientos} define los actores, los requerimientos
funcionales y no funcionales, los casos de uso y las historias de usuario. El
capítulo~\ref{cap:diseno} justifica el diseño del panel de administración con sus wireframes y
pantallas, y el capítulo~\ref{cap:uml} presenta los diagramas UML.
El capítulo~\ref{cap:arquitectura} describe la arquitectura, las tecnologías elegidas, el despliegue y
los protocolos de comunicación. El capítulo~\ref{cap:datos} presenta el conjunto de datos, la
preparación, los modelos y el modelo de datos del sistema. El capítulo~\ref{cap:producto} describe
el producto implementado, el cumplimiento de los requerimientos, el tratamiento de datos personales y
las limitaciones conocidas. El capítulo~\ref{cap:pruebas} reúne las pruebas automatizadas, funcionales,
de rendimiento, la evaluación del modelo y la evaluación de usabilidad. El
capítulo~\ref{cap:mercado} analiza el mercado y la competencia, el capítulo~\ref{cap:negocio}
presenta el modelo de negocio, la viabilidad económico-financiera y la identidad de marca, y el
capítulo~\ref{cap:conclusiones} expone las conclusiones y el trabajo futuro.

Los anexos complementan el cuerpo del documento. El Anexo~A presenta el cronograma de
actividades; el Anexo~B, los resultados completos de la encuesta; y los Anexos~C a G, las
transcripciones de las entrevistas a los cinco profesionales consultados.
```

Nota: si el equipo prefiere no crear un capítulo 12 aparte para negocio (ver T16), sacar la referencia a `cap:negocio` y nombrar las secciones dentro del capítulo de mercado.

---

## T5 — Alcance (agregar al final de 1.2, y corregir el tiempo verbal)

Reemplazo completo de 1.2 (hoy dice "se implementará" y "entrenado por los alumnos"):

```latex
El proyecto consiste en el desarrollo de un agente UEBA que trabaja en conjunto con una API central.
La API incorpora un modelo de inteligencia artificial entrenado por el equipo para detectar
anomalías en el comportamiento de los usuarios, y el sistema incluye un panel de administración
para visualizar el nivel de riesgo de cada usuario y modificar los umbrales que definen las acciones
a ejecutar. El agente se desarrolla para equipos con Windows y el producto se orienta a pequeñas y
medianas empresas de Argentina. El alcance incluye el análisis del tratamiento de datos personales
que realiza el sistema según la normativa argentina, pero no la implementación de los procesos
organizacionales que esa normativa exige a la empresa que lo adopte (por ejemplo, la información a
los empleados o la inscripción de la base de datos).
```

---

## T6 — Requerimientos en forma positiva

**RNF-04**
> La decisión de riesgo se origina siempre en el motor de scoring central (PDP); el agente (PEP) ejecuta únicamente la acción que el PDP indica para cada evento, conforme a la separación entre PEP y PDP de NIST SP 800-207.

**RNF-05**
> Ante una caída de la API o un error de autenticación, el agente continúa el monitoreo y conserva los eventos no enviados en un buffer local acotado (vigencia de 3 horas y tope de 20 000 eventos), que reenvía al restablecerse la conexión, con reintentos y un mecanismo de circuit breaker.

**RNF-08**
> El agente recolecta exclusivamente metadatos de actividad: nombres de archivo y de proceso, dirección y puerto remotos, marca temporal e identificador del par equipo-usuario.

**RF-04** (agregar al final)
> El decaimiento tiene una vida media de 3 días. [[VERIFICAR: si la vida media es configurable, agregar su rango; si no, decir "fija".]]

---

## T7 — Encuesta: muestreo y alcance de los resultados (inicio de 3.6)

```latex
La encuesta se difunde [[COMPLETAR: canal, por ejemplo redes sociales y contactos personales y
laborales del equipo]] entre [[COMPLETAR: fechas]]. Se trata de una muestra no probabilística por
conveniencia: los participantes no se seleccionan al azar de una población definida, sino entre las
personas que el equipo puede alcanzar y que deciden responder. Por lo tanto, los porcentajes que
siguen describen a los participantes y no pueden generalizarse a la población de empleados de
empresas argentinas; se utilizan como indicio del problema y como insumo de diseño, no como
estimación estadística. La muestra tampoco se estratifica por tamaño de empresa ni por sector.
```

Además, en 3.6.1 a 3.6.9 reemplazar las generalizaciones por referencias a la muestra: "los empleados" → "los participantes"; "para una parte importante de los empleados" → "para una parte importante de los participantes"; "la encuesta respalda la premisa" → "los resultados de la encuesta son consistentes con la premisa".

---

## T8 — Nota de autoevaluación (después de la tabla 3.VII y en 3.2)

```latex
Las valoraciones del proyecto propuesto en esta tabla y en la matriz de capacidades son una
autoevaluación del equipo basada en lo implementado y verificado en los capítulos de producto y
de pruebas, y no una medición externa. Las valoraciones de los competidores se basan en lo que
describe el estado del arte; cuando una fuente no se pronuncia sobre una capacidad, se marca N/D.
```

Celda vacía de la tabla 3.VII ("Diferenciador del proyecto propuesto"): `No aplica (fila de referencia). La síntesis de diferenciadores se presenta en la Sección~\ref{sec:sintesis-diferenciadores}.`

---

## T9 — Metas de evaluación del modelo y aclaración sobre etiquetas

> Va en el capítulo de pruebas, al comienzo de 10.5 (antes de la tabla 10.VII). Las metas tienen que quedar **fijadas antes de reentrenar** el modelo: si se reentrena, se informan los resultados nuevos contra estas mismas metas, sin moverlas.

```latex
\subsection{Metas de evaluación}\label{sec:metas-modelo}
El conjunto de datos CLUE-LDS no incluye etiquetas de actividad maliciosa
\parencite{landauer2022b}, por lo que la evaluación no puede expresarse en exactitud, precisión,
exhaustividad o F1. [[COMPLETAR: una oración que explique por qué versiones anteriores del trabajo
mencionaban sesiones etiquetadas y balanceo de clases, y por qué ese enfoque se descarta. No
inventar.]] En su lugar, se fijan las metas de la tabla~\ref{tab:metas-modelo}, que combinan el
comportamiento del modelo sobre datos sin etiquetar con la detección de escenarios de ataque
inyectados (sección~\ref{sec:escenarios}).

\begin{table}[H]
\centering
\caption{Metas de evaluación del modelo y resultado obtenido}
\label{tab:metas-modelo}
\begin{tabular}{p{5.2cm}p{3.2cm}p{3cm}p{1.8cm}}
\hline
Métrica & Meta & Resultado & Cumple \\
\hline
Tasa de anomalías de Isolation Forest en prueba & entre 1\,\% y 3\,\% (contaminación del 2\,\%) & 0,79\,\% & No \\
Tasa de anomalías del LSTM en prueba & entre 3\,\% y 7\,\% (umbral en el percentil 95) & 3,99\,\% & Sí \\
Detección atribuible del escenario combinado (E4) con el umbral del nivel alto (70) & $\geq$ 50\,\% de los usuarios & 13,3\,\% (2 de 15) & No \\
Detección atribuible promedio de los cuatro escenarios con umbral 70 & $\geq$ 33\,\% & 6,7\,\% (4 de 60) & No \\
Usuario-días sin inyección que terminan en nivel alto o crítico & $\leq$ 10\,\% & 16,8\,\% & No \\
Latencia de evaluación, percentil 95 (RNF-01) & $\leq$ 500\,ms & 14,9\,ms & Sí \\
\hline
\end{tabular}
\fuente{Elaboración propia.}
\end{table}
```

`[[DECIDIR: los valores de las metas. Son una propuesta razonable; lo importante es que queden fijos y se justifiquen. Si el reentrenamiento cambia los resultados, se actualiza solo la columna "Resultado" ([[CODIGO]]).]]`
`[[VERIFICAR: el comando del caption de fuente que usa el documento — reemplazar \fuente por el que corresponda.]]`

Justificación breve (párrafo debajo de la tabla):

```latex
Las tasas de anomalías se comparan con el parámetro que cada modelo usa para fijar su umbral: una
tasa muy por debajo indica que el umbral es más estricto en prueba que en entrenamiento. La meta
de detección exige que al menos la mitad de los ataques combinados, que son los más evidentes,
lleven al usuario al nivel alto, y la meta de alertas acota la carga de revisión sobre actividad
normal a uno de cada diez usuario-días. Los resultados muestran que el sistema cumple las metas de
rendimiento y de comportamiento del LSTM, pero no las de detección ni de alertas: es la principal
limitación técnica del proyecto, cuyas causas se analizan en la sección~\ref{sec:interpretacion}.
```

---

## T10 — Aporte diferencial del Anexo G (al final de 3.5.1)

```latex
A diferencia de las otras cuatro, la consulta a Ruiz se realiza mediante un cuestionario escrito. Su
inclusión se justifica por el rol operativo que aporta: la atención de alertas en herramientas de
tipo SIEM/XDR y la ejecución de procedimientos de respuesta (playbooks), que es la perspectiva de
quien recibiría las alertas del sistema propuesto. Sus respuestas sobre factores de riesgo coinciden
con las del resto de los entrevistados; su aporte específico está en la secuencia de respuesta ante
un incidente, que se contrasta con el catálogo de acciones del proyecto en la sección~\ref{sec:validacion-diseno}.
```

Además, en 3.5 los entrevistados se nombran por apellido en todo el texto (hoy alterna "Guillermo", "Pablo" con "Peña", "Ruiz"): Jacubovich, Pita, Peña, Ruiz, Villarino.

---

## T11 — Marco legal (nueva subsección en el marco teórico, después de "Estándares y marcos normativos")

> Verificar cada artículo contra el texto oficial antes de compilar. Lo escrito acá es fiel a lo que dice cada artículo según mi conocimiento, pero no lo pude contrastar con InfoLEG desde esta sesión.

```latex
\subsection{Marco legal: protección de datos personales}\label{sec:marco-legal}
Un sistema que registra la actividad de los empleados en sus equipos de trabajo trata datos
personales, por lo que su viabilidad depende del marco normativo de protección de datos y del
derecho laboral. En Argentina, la norma principal es la Ley 25.326 de Protección de los Datos
Personales \parencite{ley25326}, reglamentada por el Decreto 1558/2001.

La ley define como dato personal a la información de cualquier tipo referida a personas humanas
o de existencia ideal determinadas o determinables (art.~2). Los registros de actividad que
recolecta el agente están asociados a un identificador de equipo y de usuario, por lo que
constituyen datos personales aunque no incluyan el contenido de archivos ni de comunicaciones.

Los principios relevantes para el proyecto son los siguientes:
\begin{itemize}
  \item \textbf{Calidad y finalidad} (art.~4): los datos deben ser ciertos, adecuados, pertinentes
        y no excesivos en relación con la finalidad para la que se obtienen, y no pueden utilizarse
        para finalidades distintas o incompatibles con ella.
  \item \textbf{Consentimiento} (art.~5): el tratamiento requiere el consentimiento libre, expreso
        e informado del titular, salvo excepciones, entre ellas que los datos deriven de una relación
        contractual del titular y resulten necesarios para su desarrollo o cumplimiento.
  \item \textbf{Información al titular} (art.~6): al recabar los datos se debe informar la
        finalidad, los destinatarios, la existencia del archivo y su responsable, y la posibilidad de
        ejercer los derechos de acceso, rectificación y supresión.
  \item \textbf{Seguridad y confidencialidad} (arts.~9 y 10): el responsable debe adoptar las
        medidas técnicas y organizativas necesarias para garantizar la seguridad y confidencialidad
        de los datos, y quienes intervienen en el tratamiento están obligados al secreto.
  \item \textbf{Transferencia internacional} (art.~12): se prohíbe la transferencia de datos
        personales a países u organismos que no proporcionen niveles de protección adecuados, salvo
        las excepciones previstas.
  \item \textbf{Derechos del titular} (arts.~14 a 16): acceso, rectificación, actualización y
        supresión de sus datos.
  \item \textbf{Registro} (art.~21): las bases de datos privadas destinadas a proporcionar
        informes deben inscribirse en el registro que lleva el órgano de control.
\end{itemize}

El órgano de control es la Agencia de Acceso a la Información Pública (AAIP), que dicta normas
complementarias, entre ellas las medidas de seguridad recomendadas para el tratamiento de datos
personales \parencite{aaip2018} y los criterios sobre países con protección adecuada y cláusulas
contractuales modelo para la transferencia internacional \parencite{dnpdp2016}. Argentina adhiere
además al Convenio 108 del Consejo de Europa para la protección de las personas con respecto al
tratamiento automatizado de datos de carácter personal \parencite{ley27483}.
[[VERIFICAR: Ley 27.483 (aprobación del Convenio 108) y si corresponde citar también la ley que aprueba
el Protocolo modificatorio (Convenio 108+).]]

En el ámbito laboral, la Ley de Contrato de Trabajo \parencite{ley20744} admite que el empleador
establezca sistemas de control personal destinados a la protección de sus bienes, siempre que
salvaguarden la dignidad del trabajador, se practiquen con discreción y mediante medios de
selección automática, y sean puestos en conocimiento de la autoridad de aplicación (arts.~70 a 72).
El monitoreo de la actividad en equipos provistos por la empresa se analiza en este marco: su
legitimidad depende de que los empleados conozcan la existencia del control, su finalidad y su
alcance.
```

---

## T12 — Tratamiento de datos personales y viabilidad legal (nueva sección en el capítulo de producto, antes de "Limitaciones conocidas")

```latex
\section{Tratamiento de datos personales y viabilidad legal}\label{sec:tratamiento-datos}
El sistema actúa como herramienta de una organización que monitorea los equipos que provee a sus
empleados. En un despliegue real, la organización cliente es la responsable del tratamiento en los
términos de la Ley 25.326, y el proveedor del sistema actúa como prestador de servicios de
tratamiento por cuenta de ella. La tabla~\ref{tab:tratamiento-datos} relaciona cada principio del
marco legal (sección~\ref{sec:marco-legal}) con la forma en que el sistema lo contempla y con lo que
queda a cargo de la organización.

\begin{longtable}{p{3cm}p{6cm}p{5cm}}
\caption{Principios de la Ley 25.326 y su tratamiento en el sistema}\label{tab:tratamiento-datos}\\
\hline
Principio & Cómo lo contempla el sistema & A cargo de la organización / pendiente \\
\hline
\endfirsthead
\hline
Principio & Cómo lo contempla el sistema & A cargo de la organización / pendiente \\
\hline
\endhead
Finalidad (art.~4) & Finalidad única y declarada: detectar el uso indebido de credenciales y
responder ante él. Los datos no se usan para medir productividad ni para otros fines. &
Declarar la finalidad en la política interna y no reutilizar los datos para otros fines. \\
Datos no excesivos (art.~4) & El agente recolecta solo metadatos de actividad (RNF-08): no captura
contenido de archivos, mensajes, pantallas ni pulsaciones de teclado. Las direcciones IP y las
cuentas de volumen muy alto quedan sin puntaje. & Configurar las carpetas y aplicaciones vigiladas
de forma acotada. \\
Consentimiento e información (arts.~5 y 6) & El panel muestra, para cada puntaje, las variables
que lo explican, lo que permite informar al empleado por qué se tomó una acción. & Informar a los
empleados la existencia del control, su finalidad y sus derechos (política de uso aceptable o
cláusula contractual), y comunicarlo a la autoridad de aplicación laboral (LCT, art.~71). \\
Seguridad (art.~9) & [[CODIGO: cifrado TLS entre agente, panel y API; autenticación mutua entre
agente y API; credenciales del panel fuera del navegador; claves de agente ligadas a su
identificador]]. Cadena de hashes sobre los eventos crudos, seguridad a nivel de fila en la base de
datos y secretos en un almacén de parámetros. & Gestionar los accesos al panel y rotar las claves. \\
Confidencialidad (art.~10) & Acceso al panel con inicio de sesión y roles diferenciados de consulta
y administración; registro de auditoría de los cambios de configuración. & Limitar el acceso al
personal de seguridad. \\
Transferencia internacional (art.~12) & Los servicios gestionados que usa el sistema procesan
datos fuera de Argentina: la API corre en una instancia de AWS en Estados Unidos (us-east-2), y el
estado y el historial se guardan en Redis (Upstash) y PostgreSQL (Supabase)
[[VERIFICAR: región de Upstash y de Supabase]]. El servicio opcional de redacción de correos (Gemini)
recibe el puntaje y los eventos recientes de la alerta. & Formalizar la transferencia con cláusulas
contractuales modelo, o desplegar en una región con protección adecuada; desactivar o minimizar lo
que se envía al servicio de redacción. \\
Acceso, rectificación y supresión (arts.~14 a 16) & El panel permite consultar el historial de un
usuario y eliminarlo. & Pendiente: definir un plazo de conservación. La cadena de hashes por
usuario entra en tensión con la supresión, porque borrar una fila impide verificar las siguientes. \\
Registro (art.~21) & No aplica al proveedor. & Evaluar la inscripción de la base según el uso que
la organización haga de ella. \\
\hline
\end{longtable}
\fuente{Elaboración propia a partir de la Ley 25.326 y la Ley de Contrato de Trabajo.}

\subsection{Conservación de los datos y cadena de hashes}
Hoy los eventos crudos y el historial de puntajes no tienen un plazo de conservación definido. La
cadena de hashes que protege la integridad de los eventos (sección~\ref{sec:modelo-relacional})
dificulta la supresión: eliminar una fila rompe la verificación de las siguientes del mismo
usuario. Se identifican tres alternativas: cerrar la cadena por período (por ejemplo, mensual),
conservar el último hash de cada período y eliminar los períodos vencidos; reemplazar el
identificador del usuario por un seudónimo calculado con una clave secreta, de modo que destruir la
clave anonimice los registros sin modificarlos; o eliminar el contenido de la fila y conservar solo
su hash. Se adopta como trabajo futuro la primera, por ser la que preserva la verificación de los
períodos vigentes con el menor cambio en el modelo de datos.

\subsection{Datos de entrenamiento}
El modelo se entrena con CLUE-LDS, un conjunto público de registros reales seudonimizados mediante
identificadores descriptivos y distribuido bajo licencia CC BY 4.0 (sección~\ref{sec:conjunto-datos}).
El uso del conjunto respeta la licencia mediante la atribución a sus autores y no requiere el
tratamiento de datos de personas identificables.

\subsection{Descargo de responsabilidad}
El sistema es una herramienta de apoyo a la seguridad de la información y no reemplaza el criterio
del personal de seguridad. Las acciones automáticas que ejecuta (terminación de procesos,
denegación de acceso a carpetas) pueden afectar el trabajo legítimo de un empleado ante un falso
positivo; por eso las acciones más severas se reservan para el nivel crítico y pueden revertirse
cuando el sistema operativo lo permite. La organización que lo adopte es responsable de
configurar las políticas de respuesta, de informar a sus empleados y de cumplir la normativa de
protección de datos y laboral aplicable.
```

`[[VERIFICAR: etiquetas \ref existentes (sec:modelo-relacional, sec:conjunto-datos); crearlas si no existen.]]`

---

## T13 — Viabilidad técnica (al final del capítulo de arquitectura, o en el de producto)

```latex
\subsection{Viabilidad técnica}
El sistema no requiere hardware específico. El agente se ejecuta como un proceso nativo en equipos
con Windows que la organización ya posee, con un consumo de recursos acotado por RNF-02, y la API
y el almacenamiento corren sobre servicios de nube de uso general (cómputo, Redis y PostgreSQL
gestionados) contratables bajo demanda. La viabilidad técnica depende, por lo tanto, de la
disponibilidad de esos servicios y no de la producción o adquisición de dispositivos.
```

---

## T14 — Cierre de la conclusión del estado del arte (al final de 2.2.6)

Además, cambiar "El verdadero diferencial radica en que" por "El diferencial del proyecto consiste en que".

```latex
La relevancia del problema excede a las grandes organizaciones. El robo de credenciales afecta
también a pequeñas y medianas empresas que no cuentan con un centro de operaciones de seguridad
ni con presupuesto para las plataformas relevadas, que están dimensionadas y tarifadas para el
segmento corporativo. Un sistema que detecta el uso indebido de una sesión válida y responde sin
depender de un analista disponible acerca a ese segmento una capacidad que hoy queda fuera de su
alcance, y reduce el daño que un incidente puede causar a la organización, a sus empleados y a los
datos de terceros que esta administra.
```

---

## T15 — Correcciones puntuales del capítulo de mercado

**Plaza, alcance geográfico** (reemplaza el `\todo`):
> *Alcance geográfico.* Argentina, con foco inicial en las PyMEs del Área Metropolitana de Buenos Aires, donde se concentran los integradores y proveedores de servicios de seguridad gestionados del canal de reventa. La comercialización en otros países de América Latina se plantea como una expansión posterior, sujeta a adecuar el tratamiento de datos a la normativa de cada país.

**Frases sin cita en 2.2.1** (las otras cinco quedan como están: nombrar al fabricante en el texto es lo que pide la cátedra):
- Sentinel, "Diversos usuarios señalan que el modelo de costos…" → *"Su modelo de costos se basa en el volumen de datos ingeridos, lo que puede resultar elevado en organizaciones con grandes cantidades de registros."*
- Splunk, "Diversos reportes señalan que su implementación inicial…" → *"Su puesta en marcha requiere integrar y normalizar múltiples fuentes de datos, lo que demanda conocimientos especializados para su configuración."*

**Matriz BCG, eje de crecimiento** (reemplaza el párrafo completo):
> *Eje crecimiento del mercado: alto.* Se ubica en el extremo alto por dos motivos. Primero, un cambio estructural: el trabajo remoto y la migración a servicios en la nube reducen la eficacia de la seguridad perimetral, premisa de la que parte el enfoque Zero Trust \parencite{rose2020}, y obligan a controlar la actividad posterior al inicio de sesión (sección~\ref{sec:punto-ciego}). Segundo, la literatura sobre UEBA y control de acceso adaptativo relevada en el estado del arte es en su mayoría reciente, lo que indica un campo en desarrollo activo. La valoración es cualitativa: el proyecto no cuenta con datos propios sobre el tamaño ni la tasa de crecimiento del mercado.

**Matriz BCG, eje de participación** (reescritura en registro académico):
> *Eje participación relativa de mercado: baja.* La participación relativa se mide contra el líder del segmento. Las tres soluciones relevadas tienen una posición consolidada: Sentinel se distribuye integrado al ecosistema de Microsoft, Splunk tiene una trayectoria extensa en el mercado de SIEM y Exabeam combina capacidades de SIEM, UEBA y SOAR. El producto, en cambio, no tiene clientes, marca reconocida ni implementaciones previas, por lo que su participación inicial es nula. La participación se construye con tiempo de operación en el mercado y no depende solo de la calidad técnica del producto.

**Henderson en la bibliografía**: sin número de serie → ver T22.

**Pasada de registro en todo el capítulo 11** (sin cambiar contenido): eliminar "acá", "ahí", "literalmente", "por definición", "exactamente", "no tendría sentido, invalidaría todo…"; sacar las frases entre comillas que imitan diálogo ("detecté algo raro", "hice algo al respecto", "No es 'una alerta más clara'…") y reemplazarlas por la idea en tercera persona. Mismo criterio para "literalmente" (tabla de 3.3) y "exactamente" (tablas de 3.1 y 3.3).

---

## T16 — Modelo de negocio (nuevo)

> Ubicación recomendada: nuevo capítulo "Modelo de negocio y viabilidad económico-financiera" después de "Análisis de mercado y competitividad". Alternativa: secciones 11.5 a 11.7 dentro de ese capítulo.

```latex
\chapter{Modelo de negocio y viabilidad económico-financiera}\label{cap:negocio}
Este capítulo describe cómo el producto crea, entrega y captura valor \parencite{osterwalder2010},
y evalúa si puede sostenerse y ser rentable en el tiempo. Los supuestos parten del análisis de
mercado del capítulo anterior (segmento, precio y canales) y de los costos reales de la
infraestructura del prototipo.

\section{Cliente, usuario y pagador}
El producto es un servicio B2B. El \textbf{usuario} del panel es el responsable de seguridad o de
tecnología de la organización, que revisa los niveles de riesgo y configura las políticas. Los
empleados cuyos equipos ejecutan el agente no son usuarios del producto, sino titulares de los
datos que este trata (sección~\ref{sec:tratamiento-datos}). El \textbf{cliente} que decide la
compra es el responsable de tecnología o, en las empresas más chicas, la dirección. El
\textbf{pagador} es la organización, en forma directa o a través del proveedor de servicios de
seguridad gestionados (MSSP) que le revende el producto.

\section{Lienzo del modelo de negocio}
La tabla~\ref{tab:canvas} resume el modelo en los nueve bloques del lienzo de
\textcite{osterwalder2010}.

\begin{longtable}{p{3.4cm}p{11cm}}
\caption{Lienzo del modelo de negocio}\label{tab:canvas}\\
\hline
Bloque & Contenido \\
\hline
\endfirsthead
\hline
Bloque & Contenido \\
\hline
\endhead
Segmentos de clientes & PyMEs argentinas de 50 a 100 equipos con información sensible y sin
centro de operaciones de seguridad propio; en la encuesta, el 47\,\% de los participantes accede a
datos o sistemas de criticidad media-alta o alta (sección~\ref{sec:encuesta}). \\
Propuesta de valor & Detección del uso indebido de una sesión válida y respuesta automática en el
propio equipo, sin depender de un analista ni de una plataforma de orquestación externa, con
explicación de cada alerta y a un precio acorde al presupuesto de una PyME. \\
Canales & Venta directa con alta autogestionada y reventa a través de integradores y MSSP que ya
atienden PyMEs. \\
Relación con los clientes & Alta autogestionada con período de aprendizaje automático;
soporte por correo; acompañamiento del MSSP en los clientes que llegan por ese canal. \\
Fuentes de ingresos & Suscripción mensual por equipo monitoreado en dos planes: Business (USD 2 a 5)
y Enterprise, con reentrenamiento periódico configurable (USD 6 a 10). \\
Recursos clave & Modelo de detección entrenado y su pipeline de reentrenamiento; agente, API y
panel; equipo de desarrollo; infraestructura de nube. \\
Actividades clave & Desarrollo y mantenimiento del producto; reentrenamiento y evaluación del
modelo; soporte; gestión del canal de reventa. \\
Socios clave & Integradores y MSSP; proveedores de nube (AWS, Upstash, Supabase); proveedores de
identidad (Keycloak u otros) para la integración IAM. \\
Estructura de costos & Equipo (costo fijo principal); infraestructura de nube base (fija) y por
equipo monitoreado (variable); comisiones del canal y del procesador de pagos (variables);
costo de adquisición de clientes; certificado de firma de código y asesoramiento legal. \\
\hline
\end{longtable}
\fuente{Elaboración propia con el esquema de \textcite{osterwalder2010}.}

\section{Monetización y economía unitaria}
El esquema de suscripción por equipo se elige porque el costo variable del producto crece con
la cantidad de equipos monitoreados (eventos procesados, almacenamiento y cómputo de la API), de
modo que el ingreso escala con el mismo factor que el costo. Con una mezcla supuesta de 70\,\% de
equipos en el plan Business a USD 4 y 30\,\% en Enterprise a USD 8, el ingreso promedio es de USD 5,20
por equipo y de USD 390 por mes para un cliente de 75 equipos. Descontados el costo de nube por
equipo (USD 0,60), las comisiones de pago e impuestos sobre ventas (6\,\%) y la comisión del canal
(20\,\% sobre la mitad de las ventas), el margen de contribución es de USD 283 por cliente y por mes.

Con un costo de adquisición de USD 1.500 y una tasa de abandono del 2\,\% mensual (escenario base),
el valor de vida de un cliente es de USD 283 / 0,02 = USD 14.150, la relación entre el valor de vida
y el costo de adquisición es de 9,4 y el costo de adquisición se recupera en 5,3 meses.

\textbf{Disposición a pagar.} El proyecto no cuenta con una medición directa de la disposición a
pagar. El precio se fija por debajo del de las soluciones del segmento corporativo, que se
tarifan por volumen de datos o por usuario con montos dimensionados para grandes empresas, y se
contrasta con la encuesta, donde el costo aparece como factor determinante de adopción para el
17\,\% de los participantes. Validar el precio con clientes potenciales es la primera acción
comercial prevista.
```

---

## T17 — Viabilidad económico-financiera (nuevo, continúa T16)

> Las tablas salen de `python modelo_financiero.py --latex`. Si se cambia algún supuesto, se vuelve a correr y se reemplazan las tablas y los números del texto.

```latex
\section{Viabilidad económico-financiera}

\subsection{Supuestos}
El análisis se realiza sobre el flujo de fondos anual, en dólares estadounidenses constantes para
aislarlo de la inflación local, con un horizonte de cinco años. El horizonte se justifica porque
el ingreso es recurrente y el costo de adquirir cada cliente se recupera a lo largo de varios meses:
en tres años los escenarios todavía reflejan sobre todo la etapa de adquisición. No se considera
valor residual al final del horizonte, lo que hace que la evaluación sea conservadora.

\begin{longtable}{p{6cm}p{8.3cm}}
\caption{Supuestos del análisis económico-financiero}\label{tab:supuestos-fin}\\
\hline
Supuesto & Valor y fundamento \\
\hline
\endfirsthead
\hline
Supuesto & Valor y fundamento \\
\hline
\endhead
Inversión inicial & USD 23.000: horas del equipo valorizadas (1.000 h a USD 15/h, USD 15.000),
pasaje del prototipo a producto (instalador, firma de código, endurecimiento; USD 6.000),
constitución de la sociedad y asesoramiento legal (USD 1.500) y certificado de firma de código
(USD 500). \\
Precio y mezcla de planes & USD 5,20 por equipo y por mes (70\,\% Business a USD 4, 30\,\% Enterprise a
USD 8), dentro de los rangos de la sección de precio. \\
Tamaño del cliente & 75 equipos, punto medio del segmento de 50 a 100. \\
Costo variable & Nube: USD 0,60 por equipo y por mes; procesador de pagos 3\,\%; impuesto sobre los
ingresos brutos 3\,\% (supuesto conservador); comisión del 20\,\% al MSSP sobre la mitad de las
ventas. \\
Costo fijo & Equipo y soporte: USD 3.500 por mes el primer año (dos integrantes a tiempo parcial),
que crece hasta USD 12.000 en el quinto; infraestructura base de nube: USD 250 por mes. \\
Impuesto a las ganancias & 25\,\% sobre el resultado positivo de cada año (supuesto simplificado,
sin quebrantos trasladables). \\
Tasa de descuento & 25\,\% anual en dólares, con sensibilidad entre 20\,\% y 35\,\%.
[[VERIFICAR: justificar con el rendimiento de un bono del Tesoro de EE.\,UU. a 10 años, el riesgo
país de Argentina a la fecha y una prima por riesgo de emprendimiento; citar la fuente de cada
dato.]] \\
\hline
\end{longtable}
\fuente{Elaboración propia.}

\subsection{Escenarios}
Los tres escenarios difieren en la velocidad de adopción, la tasa de abandono y el costo de
adquisición, y cada uno responde a una hipótesis sobre el mercado:
\begin{itemize}
  \item \textbf{Pesimista}: la resistencia a la adopción observada en la encuesta (el 41\,\% de los
        participantes considera improbable que su empresa adopte el sistema) se traduce en un ciclo
        de venta largo y caro. Se incorpora un cliente cada dos meses el primer año y dos por mes desde
        el tercero, con un abandono del 3\,\% mensual y un costo de adquisición de USD 2.500.
  \item \textbf{Base}: el canal de MSSP empieza a aportar clientes desde el segundo año. Se
        incorporan 1, 3, 5, 6 y 6 clientes por mes en cada año, con un abandono del 2\,\% mensual y
        un costo de adquisición de USD 1.500.
  \item \textbf{Optimista}: el canal se activa desde el primer año y el producto se recomienda entre
        clientes. Se incorporan 2, 5, 8, 10 y 10 clientes por mes, con un abandono del 1,5\,\% mensual
        y un costo de adquisición de USD 1.000.
\end{itemize}

[TABLA: clientes activos al cierre de cada año — salida de modelo_financiero.py --latex]

[TABLA: flujos netos por escenario — salida de modelo_financiero.py --latex]

\subsection{Indicadores}

[TABLA: VAN, TIR, payback simple y descontado, necesidad máxima de fondos]

[TABLA: sensibilidad del VAN a la tasa de descuento]

El punto de equilibrio operativo es de 13 clientes activos el primer año y crece hasta 43 en el
quinto, a medida que aumenta el costo fijo del equipo: con un margen de contribución de USD 283 por
cliente, cada USD 1.000 de costo fijo mensual adicional exige entre tres y cuatro clientes más.

\subsection{Interpretación}
En el escenario base, el proyecto genera valor: el VAN al 25\,\% es de USD 35.084, la TIR de
38,8\,\% supera la tasa de descuento y la inversión se recupera en 3,8 años (4,5 años con flujos
descontados). Sin embargo, el resultado es sensible a la tasa: al 35\,\% el VAN se reduce a
USD 7.456. Además, los dos primeros años tienen flujos negativos, por lo que el proyecto requiere
financiar hasta USD 100.894 acumulados antes de generar caja. En el escenario optimista el VAN es
de USD 336.532 y la inversión se recupera en 2,2 años. En el pesimista el proyecto no recupera la
inversión en el horizonte y acumula una necesidad de fondos de USD 360.837: con una adopción tan
lenta, el costo fijo crece más rápido que la base de clientes.

La viabilidad depende, por lo tanto, de la velocidad de adopción y del costo de adquirir cada
cliente, más que del precio o del costo de infraestructura. Esto define qué validar primero: la
disposición a pagar de las PyMEs y la capacidad de los MSSP de aportar clientes a un costo menor
que la venta directa. Como regla de decisión, si al cabo del primer año la base de clientes queda
por debajo del punto de equilibrio y el costo de adquisición observado supera los USD 2.000, se
replantea el canal o el segmento antes de aumentar el costo fijo.
```

> **Ojo:** los números del texto (VAN, TIR, payback, necesidad de fondos, punto de equilibrio, LTV/CAC) están sincronizados con la versión actual del script. Si cambian los supuestos, hay que actualizarlos también en el texto, no solo en las tablas.

---

## T18 — Identidad de marca (nuevo, al final del capítulo de negocio)

```latex
\section{Identidad de marca}
\subsection{Nombre}
El producto se denomina \textbf{UMBRAL}. El nombre remite al concepto central del sistema: los
umbrales de riesgo que separan el comportamiento habitual de un usuario de una desviación que
requiere respuesta, y el límite que un atacante con credenciales válidas no debería poder cruzar
después del inicio de sesión. Es una palabra corta, en español y fácil de pronunciar para el
segmento local, y no describe una tecnología puntual, lo que permite que la marca acompañe la
evolución del producto.

\subsection{Logotipo}
El isotipo es un escudo, símbolo convencional de la protección, que contiene una línea de
actividad que cruza una línea horizontal: la línea representa la actividad del usuario a lo largo
de la sesión, la horizontal representa el umbral, y el punto en el pico marca el momento en que el
sistema interviene. El logotipo acompaña el isotipo con el nombre en mayúsculas y una tipografía
sin serifa de peso alto, que transmite solidez y se lee bien en tamaños chicos, como el ícono del
agente en la barra de tareas. La paleta combina un azul oscuro, asociado a la confianza y habitual en
productos de seguridad, con un amarillo de acento que remite a una señal de advertencia y coincide
con el color que el panel usa para los niveles de riesgo intermedios.
[[VERIFICAR: que el amarillo coincida con la paleta del dashboard; si no, ajustar el color del logo o
la frase.]]

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth]{figuras/logo_umbral.png}
\caption{Logotipo del producto.}\label{fig:logo}
\fuente{Elaboración propia.}
\end{figure}

\subsection{Posicionamiento y mensaje}
El eslogan \emph{``confianza continua, después del login''} resume la propuesta de valor frente a
las soluciones que concentran el control en el inicio de sesión. El posicionamiento busca
diferenciar al producto en dos ejes que surgen del análisis de mercado: un sistema que actúa y no
solo alerta, y un precio y una puesta en marcha pensados para PyMEs. La comunicación evita
presentar el producto como una herramienta de vigilancia de empleados y lo presenta como una
protección de sus credenciales, en línea con la sensibilidad sobre la privacidad que muestran la
encuesta y el marco legal.
```

---

## T19 — Conclusiones y trabajo futuro (nuevo capítulo final, antes de la bibliografía)

```latex
\chapter{Conclusiones y trabajo futuro}\label{cap:conclusiones}

\section{Cumplimiento de los objetivos}
El objetivo general se cumple en su alcance funcional: el sistema evalúa cada evento durante toda
la sesión, mantiene un puntaje de riesgo con continuidad entre sesiones y ejecuta en el equipo una
respuesta graduada, con la decisión centralizada en la API y la aplicación distribuida en los
agentes. La tabla~\ref{tab:cumplimiento-objetivos} detalla cada objetivo específico.

\begin{longtable}{p{5.6cm}p{6.2cm}p{2.2cm}}
\caption{Cumplimiento de los objetivos específicos}\label{tab:cumplimiento-objetivos}\\
\hline
Objetivo & Evidencia & Estado \\
\hline
\endfirsthead
\hline
Objetivo & Evidencia & Estado \\
\hline
\endhead
1. Agente liviano con canal cifrado y autenticado & Recolección de metadatos implementada (RF-01,
RNF-08); canal [[CODIGO: TLS y autenticación mutua]]; consumo [[CODIGO: RNF-02]] & [[CODIGO]] \\
2. Modelo híbrido evaluado contra metas & Modelo entrenado sobre CLUE-LDS; cumple 1 de las 5 metas de
comportamiento y detección, y la de latencia (tabla~\ref{tab:metas-modelo}) [[CODIGO: actualizar si se reentrena]] & Parcial \\
3. Puntaje con continuidad y latencia $\leq$ 500\,ms & Continuidad y decaimiento implementados
(RF-03, RF-04); percentil 95 de 14,9\,ms y percentil 99 de 148,9\,ms en entorno local & Cumplido \\
4. Respuesta graduada y reversible & Seis acciones configurables por nivel (RF-07, RF-08) verificadas
en el equipo; la terminación de procesos no es reversible por limitación del sistema operativo
(RNF-06) & Cumplido con limitación \\
5. Panel con explicación y configuración en tiempo de ejecución & CU-02 implementado (RF-12 a
RF-17, RNF-07); evaluación heurística con cuatro problemas mayores corregidos & Cumplido \\
6. Reentrenamiento aislado y período de aprendizaje & CU-03 y CU-04 implementados; la única
corrida real del reentrenamiento produjo un modelo peor que el vigente, que no se promovió (RF-21)
& Cumplido; promoción no observada \\
7. Credenciales y canal protegidos & [[CODIGO: resultado de seguridad]] & [[CODIGO]] \\
8. Análisis de la normativa de datos personales & Marco legal (sección~\ref{sec:marco-legal}) y
análisis del tratamiento (sección~\ref{sec:tratamiento-datos}); queda pendiente el plazo de
conservación & Cumplido \\
9. Pruebas con cobertura $\geq$ 85\,\% & [[CODIGO: cantidad de pruebas y cobertura]]; pruebas de extremo
a extremo y evaluación heurística realizadas & [[CODIGO]] \\
\hline
\end{longtable}
\fuente{Elaboración propia.}

De los 30 requerimientos funcionales, 28 están implementados y 2 en estado parcial, y de los 15 no
funcionales, [[CODIGO: actualizar conteo con RNF-02, RNF-03 y RNF-13]] (sección~\ref{sec:cumplimiento-requerimientos}).

\section{Resultados principales}
El resultado técnico más relevante es la arquitectura: el sistema cierra el ciclo de detección,
decisión y respuesta en el equipo, que es el hueco que el estado del arte identifica en las
soluciones comerciales, y lo hace con una latencia muy por debajo de la que exige una respuesta en
tiempo casi real. La separación entre el punto de decisión y el de aplicación permite cambiar
umbrales y acciones sin modificar los agentes.

El resultado más débil es la capacidad de detección. Sobre escenarios de ataque inyectados en el
historial de 15 usuarios, la detección atribuible nunca supera un tercio de los usuarios en ningún
umbral, y con el umbral vigente del nivel alto llega al 13,3\,\% en el escenario combinado, mientras
que el 16,8\,\% de los días sin ataque termina en nivel alto. Las causas identificadas son la
granularidad diaria de las variables de Isolation Forest, que diluye una ráfaga corta de eventos;
la longitud de las secuencias del LSTM; y un conjunto de entrenamiento en el que casi todos los
eventos tienen el país sin registrar, lo que impide detectar el cambio de país. Estos resultados
se basan en una muestra chica y en escenarios diseñados por el propio equipo, pero alcanzan para
concluir que el modelo, tal como está entrenado, no detecta de forma confiable ataques de corta
duración. [[CODIGO: actualizar si el reentrenamiento cambia los resultados.]]

El análisis económico muestra que el producto puede ser rentable en un escenario de adopción
moderada, con un VAN de USD 35.084 al 25\,\%, pero que su viabilidad depende de la velocidad de
adopción y del costo de adquirir clientes. El marco legal no impide el uso del sistema, pero exige
que la organización que lo adopte informe a sus empleados y formalice la transferencia
internacional de los datos.

\section{Lecciones aprendidas}
\begin{itemize}
  \item Un conjunto de datos público resuelve la falta de datos reales, pero impone su vocabulario
        y sus limitaciones: traducir la telemetría de un equipo Windows al vocabulario de una
        plataforma de archivos compartidos hace que algunos eventos no aporten a las variables del
        modelo, y la falta de etiquetas obliga a construir una evaluación propia.
  \item Sin etiquetas, la evaluación del modelo necesita metas definidas de antemano y escenarios
        controlados; las métricas no supervisadas por sí solas no dicen si el sistema detecta.
  \item Las limitaciones de seguridad del propio sistema (credenciales y canal) son parte del
        producto y no un detalle de despliegue: un sistema de seguridad se evalúa también por
        cómo se protege a sí mismo.
  \item Verificar en el destino real (la base de datos, el correo recibido, el equipo donde se
        ejecuta la acción) evita dar por cumplidas funciones que solo se observaron en un registro.
\end{itemize}

\section{Trabajo futuro}
El trabajo futuro se prioriza según el impacto sobre la principal limitación del sistema:
\begin{enumerate}
  \item \textbf{Capacidad de detección}: incorporar variables con granularidad menor al día,
        evaluar secuencias más cortas o solapadas en el LSTM, y calibrar umbrales y pesos con
        escenarios etiquetados más amplios (sección~\ref{sec:interpretacion}).
  \item \textbf{Datos propios}: reentrenar el modelo con telemetría de equipos Windows, para
        eliminar la traducción de vocabulario y la variable de país sin información.
  \item \textbf{Explicabilidad del LSTM}: hoy un puntaje impulsado por ese componente no identifica
        qué lo causó.
  \item \textbf{Conservación de datos}: implementar el cierre de la cadena de hashes por período y
        un plazo de conservación configurable (sección~\ref{sec:tratamiento-datos}).
  \item \textbf{Validación comercial}: medir la disposición a pagar y el costo de adquisición a
        través del canal de MSSP, que son las variables que más influyen en la viabilidad.
  \item [[CODIGO: limitaciones de seguridad que queden abiertas después del trabajo del repo de
        código; integración con un proveedor de identidad real.]]
\end{enumerate}
```

`[[VERIFICAR: etiquetas sec:interpretacion (10.6.4) y sec:cumplimiento-requerimientos (9.3); crearlas si no existen.]]`

---

## T20 — Transcripciones (pendientes de L1)

- "permission de night" y "permission the night" → **"permission denied"** (es el cartel de acceso denegado que describe el entrevistado; error del reconocimiento de voz).
- "Okay, en un copy." → `[ininteligible]` salvo que el audio permita reconstruirlo.
- Anexo E: separar los turnos mezclados entre entrevistador y entrevistado, cambiando solo la etiqueta del hablante (verificar con el audio).
- Anexo G: etiqueta en mayúsculas, `RUIZ MATÍAS GABRIEL:`, para que sea uniforme con el resto.

---

## T21 — Otras correcciones de forma detectadas en el PDF actual

- 3.1: "dimens iones" → "dimensiones". 3.2: "informacion" → "información".
- Marco teórico: convertir a cita parentética las 4 citas narrativas de 2.1 (el criterio vale para todo el documento).
- Figuras 5.11 y 8.2: no se mencionan por número en el cuerpo.
- Anexo A: el diagrama de Gantt es ilegible a ese tamaño. Opciones: página apaisada (`landscape`) a página completa, o dividirlo en dos figuras (incremento 1 e incremento 2). Revisar que refleje lo realizado y no solo lo planificado.
- Figura 7.2 (despliegue en la nube): tiene notas internas ("[a verificar] state running", "estado\_producto dice apagada/t3.micro", "EC2 sin evidencia") y muestra CloudFront. Se rehace en L3 con el despliegue real; mientras tanto, no dejarla así en ninguna versión que se entregue.
- Figura 7.1: quitar de las etiquetas "[solo local]", "sin envio real", "EC2 sin evidencia".

---

## T22 — Entradas bibliográficas nuevas (biblatex)

```bibtex
@book{osterwalder2010,
  author    = {Osterwalder, Alexander and Pigneur, Yves},
  title     = {Business Model Generation: A Handbook for Visionaries, Game Changers, and Challengers},
  publisher = {John Wiley \& Sons},
  location  = {Hoboken, NJ},
  year      = {2010},
  isbn      = {978-0-470-87641-1}
}

@article{larman2003,
  author  = {Larman, Craig and Basili, Victor R.},
  title   = {Iterative and Incremental Development: A Brief History},
  journal = {Computer},
  volume  = {36},
  number  = {6},
  pages   = {47--56},
  year    = {2003},
  doi     = {10.1109/MC.2003.1204375}
}

@book{henderson1970,
  author    = {Henderson, Bruce D.},
  title     = {The Product Portfolio},
  publisher = {The Boston Consulting Group},
  location  = {Boston},
  year      = {1970}
}

@misc{ley25326,
  author       = {{República Argentina}},
  title        = {Ley 25.326 de Protección de los Datos Personales},
  howpublished = {Boletín Oficial de la República Argentina},
  year         = {2000},
  note         = {[[VERIFICAR: fecha de publicación y URL de InfoLEG]]}
}

@misc{ley20744,
  author       = {{República Argentina}},
  title        = {Ley 20.744 de Contrato de Trabajo (texto ordenado por Decreto 390/1976)},
  howpublished = {Boletín Oficial de la República Argentina},
  year         = {1976},
  note         = {[[VERIFICAR]]}
}

@misc{ley27483,
  author       = {{República Argentina}},
  title        = {Ley 27.483. Aprobación del Convenio para la Protección de las Personas con Respecto al Tratamiento Automatizado de Datos de Carácter Personal},
  howpublished = {Boletín Oficial de la República Argentina},
  year         = {2019},
  note         = {[[VERIFICAR: año de sanción/publicación y si corresponde agregar la ley del Protocolo 108+]]}
}

@misc{aaip2018,
  author       = {{Agencia de Acceso a la Información Pública}},
  title        = {Resolución 47/2018. Medidas de seguridad recomendadas para el tratamiento y conservación de los datos personales},
  howpublished = {Boletín Oficial de la República Argentina},
  year         = {2018},
  note         = {[[VERIFICAR]]}
}

@misc{dnpdp2016,
  author       = {{Dirección Nacional de Protección de Datos Personales}},
  title        = {Disposición 60-E/2016. Transferencia internacional de datos personales},
  howpublished = {Boletín Oficial de la República Argentina},
  year         = {2016},
  note         = {[[VERIFICAR]]}
}
```

Ajustar las claves si el `.bib` del proyecto usa otro formato (por ejemplo, `rose2020` puede llamarse distinto).
