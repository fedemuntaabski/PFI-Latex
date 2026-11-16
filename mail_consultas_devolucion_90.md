# Borrador de mail: respuestas a las tres consultas de la devolución del 90 %

Fuente: `correcciones_devolucion_90_latex.md` §9, con las cifras actualizadas al 16/11 (camino por defecto nuevo). Las cifras del etiquetado son **provisionales**: hay un solo etiquetador y ningún analista las confirmó. Todas las cifras están en la memoria (sección "Valor del sistema con la detección actual" y cap. de pruebas).

---

**Asunto:** PFI UMBRAL: respuestas a las consultas de la devolución del 90 %

Estimado profesor:

Le respondemos las tres consultas de la devolución. Las respuestas también están incorporadas en la memoria: en las conclusiones (secciones "Valor del sistema con la detección actual" y "Qué se cambiaría primero") y en el estado del arte (subsección "Conjuntos de datos de referencia").

**1. Con una detección del 13,3 % en el escenario combinado, ¿qué le aporta hoy el sistema a una organización?**

Primero, una aclaración sobre esa cifra. El 13,3 % salía de escenarios de ataque que armamos nosotros sobre historiales reales. En la revisión posterior concluimos que esos escenarios no representaban ataques reales y que estaban orientando las decisiones del modelo: cada ajuste podía mejorar la cifra sin mejorar la detección de un ataque real. Por eso los retiramos. Hoy la detección no está medida, porque ningún conjunto de datos del dominio trae ataques reales etiquetados, y preferimos declararla así antes que sostener una cifra con una referencia inválida. En la memoria dejamos constancia del resultado de la versión 1: cumplía una de cinco metas, con 13,3 % de detección en el escenario combinado y 15,4 % de días sin inyección en nivel alto.

Con eso dicho, el sistema aporta hoy tres cosas verificadas y una acotada:

1. **Cierra el ciclo que el estado del arte deja abierto.** Decide en la API y actúa en el equipo sin un analista de por medio. La respuesta es graduada, configurable por nivel desde el panel y reversible en el caso de la denegación de carpeta (se restaura desde un respaldo de la ACL). Está probada de extremo a extremo contra la instancia en la nube.
2. **La carga de alertas es baja y está medida sobre actividad real.** Llega a nivel alto el 1,81 % de los usuario-días del conjunto de desarrollo y el 1,05 % en una única evaluación sobre el conjunto reservado. Para una PyME sin SOC, es un volumen revisable.
3. **Cada alerta llega explicada:** con las variables de Isolation Forest que más se desvían, con la ubicación nueva o con el recurso que el usuario usa por primera vez.
4. **La acotada: qué detecta.** En una revisión ciega provisional de 403 usuario-días reales, 14 de 162 alertas (8,6 %; IC 95 % de 3,9 % a 15,0 %) merecían que un analista abriera el caso, contra cerca del 1 % de los días sin alerta. Las que aciertan son eventos de alto impacto: descargas masivas, borrados masivos y carpetas expuestas por enlace público.

En síntesis, hoy le sirve a una organización como herramienta de triage y de respuesta rápida ante cambios grandes de volumen o de ubicación. No sirve como detector autónomo de una cuenta robada que imita al usuario. Por eso la configuración por defecto reserva las acciones restrictivas para el nivel crítico. Para que sea un detector confiable hay que entrenarlo con telemetría propia del agente.

**2. ¿Por qué eligieron ese dataset y no uno de referencia para amenazas internas?**

Porque la referencia habitual, CERT (r4.2 a r6.2), es sintética: un simulador genera tanto a los usuarios como a los ataques, y nos habíamos fijado la regla de entrenar y evaluar solo con actividad humana real. Un modelo que rinde bien en CERT demuestra que reconoce los patrones del generador. Buscamos alternativas reales con etiquetas en el dominio de un equipo Windows, y ninguna servía:

- RUU exige un acuerdo firmado y su ataque es guionado.
- TWOS no tiene licencia publicada y su actividad es escenificada.
- En WUIL, los ataques los generan *scripts*.
- LANL 2015 tiene un protocolo de evaluación poco realista.
- OpTC es un ataque externo en una red instrumentada.

Ninguna cumplía a la vez "real", "por usuario" y "accesible". CLUE-LDS sí: actividad real de 920 usuarios durante cinco años, con licencia CC BY 4.0.

Tiene razón en que la elección tuvo costos que un análisis previo habría anticipado. CLUE no tiene etiquetas, viene de una plataforma en la nube y no de un equipo Windows, y su campo de país está casi vacío: falta en el 99,95 % de los eventos de la población de entrenamiento. Este último punto tendría que habernos hecho descartar la variable de país desde el principio; en la versión 1 terminó funcionando como un interruptor de ubicación. Ya la sacamos de Isolation Forest y la reemplazamos por una regla explícita de ubicación. Además, agregamos el relevamiento de conjuntos de datos al estado del arte y medimos la brecha de dominio: sobre telemetría real de equipos Windows (LANL 2017), el modelo entrenado en CLUE marca el 53,66 % de los días, contra el 4,13 % de uno entrenado en ese dominio.

**3. ¿Qué cambiarían primero en el modelo para acercarse a las metas?**

Dos cambios ya están hechos, con criterios fijados antes de medir. La detección de novedad pasó a ser solo informativa, porque ninguna de sus alertas propias merecía revisión, y el país pasó a una regla explícita de ubicación. Los siguientes van en este orden, porque cada paso es condición del siguiente:

1. **Entrenar y calibrar en el dominio correcto.** Un piloto con el agente en modo de simulación: al menos cinco equipos Windows de uso laboral real durante seis semanas, con consentimiento informado. Con esos datos se reentrena y recalibra Isolation Forest. La brecha de 53,66 % frente a 4,13 % muestra que hoy el modelo no está calibrado para el equipo donde corre, y ningún otro ajuste compensa eso.
2. **Tener con qué medir.** Pedir a un analista externo que confirme el etiquetado provisional, y registrar en el piloto las acciones de riesgo reales, para tener por primera vez una medida de detección en el dominio. Esa medida se evalúa una sola vez sobre datos reservados.
3. **Corregir lo que el etiquetado señala:** variables por tipo de operación, en particular la compartición hacia afuera, que fue el punto débil.
4. **Recién después:** variables con granularidad menor al día y una nueva evaluación de un componente de secuencia.

Quedamos a disposición para ampliar cualquiera de los puntos.

Saludos cordiales,

Santiago Mociulsky y Federico Muntaabski
