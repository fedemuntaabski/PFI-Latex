# E75 — Transcripciones de entrevistas (Anexos C a F)

Corrección del profesor: quitar restos de transcripción automática y partir las oraciones larguísimas solo con puntuación.

Archivos tocados:

| Anexo | Archivo | Entrevistado |
|---|---|---|
| C | `chapters/appendix/interview_1_pablo.tex` | Villarino Pablo Rodolfo |
| D | `chapters/appendix/interview_2_jacubovich.tex` | Jacubovich Luciana |
| E | `chapters/appendix/interview_3_guillermo.tex` | Pita Guillermo |
| F | `chapters/appendix/interview_4_pena.tex` | Peña Alejandro Francisco |

El Anexo G (`interview_5_ruiz.tex`) es un cuestionario escrito: no se tocó. Sus etiquetas `Pregunta N:` son las que corresponden a ese formato.

## Criterio aplicado

1. **Eliminado**: fragmentos que son basura del reconocimiento de voz y cuya eliminación no cambia el sentido ("Done.", "BM.", "O.", "Easy.", "Y." sueltos entre otros fragmentos, turnos de una sola sílaba sin contenido).
2. **[inaudible]**: palabras mal transcriptas, aunque la forma correcta parezca evidente. No se adivinó ninguna; la hipótesis va en la tabla. Esto incluye nombres técnicos y marcas mal escritos (Gira, Sonarcube, Telegraph, Trelix, Jenkin, etc.), como se acordó.
3. Se unificó la marca: el `[ininteligible]` que ya existía en el Anexo F pasó a `[inaudible]`.
4. Muletillas y repeticiones del habla ("bueno", "o sea", "¿no?", "este", "como como", "de de", "otros otros", "una de una", "Mhm", "Hmm", "Ehm") se dejaron. El único falso arranque que se quitó fue "las" de "las los objetivos", porque lo marcaste vos.
5. **Puntuación**: se partieron todas las oraciones de más de 45 palabras. Solo se agregaron puntos, comas, dos puntos o signos de pregunta, y se puso en mayúscula la primera letra de la oración nueva. No se cambió ninguna palabra.
6. Etiquetas de hablante: todas tienen el formato `APELLIDO NOMBRE:` (verificado con grep en C a F). No había ninguna distinta.

Después de los cambios, ninguna oración de los Anexos C a F supera las 45 palabras (contadas con un script que corta en `.`, `?` y `!`).

## Cambios

La línea es la del `.tex` **antes** de editar. Si el texto aparece más de una vez, se indica en la columna "Texto original" y la línea es la de la primera aparición.

| Anexo | Línea | Texto original | Acción | Hipótesis (solo [inaudible]) |
|---|---|---|---|---|
| C | 14 | Bueno, , como | puntuación |  |
| C | 16 | Valora. Es Sandy. | [inaudible] | "Dale. ¿Santi?" (pase de palabra a Santiago) |
| C | 20 | DeepBops | [inaudible] | "DevOps" |
| C | 20 | Divos | [inaudible] | "DevOps" |
| C | 20 | testerqua | [inaudible] | "tester QA" / "testers QA" |
| C | 24 | ingenios DevSecOps | [inaudible] | "ingenieros" |
| C | 24 | on premis | [inaudible] | "on premise" |
| C | 32 | agentes de Telegraph (2 veces) | [inaudible] | "Telegraf" (agente de recolección de métricas) |
| C | 32 | un premise | [inaudible] | "on premise" |
| C | 36 | One premise | [inaudible] | "on premise" |
| C | 42 | no o k | [inaudible] | "¿no? Ok" |
| C | 48 | Alexander su usuario. | [inaudible] | Fragmento de la frase de Villarino que sigue en el turno siguiente ("…un servidor que está en AWS") |
| C | 50 | WS, yo hago la integración… | [inaudible] | "AWS" (final de "un servidor que está en AWS") |
| C | 54 | Gira | [inaudible] | "Jira" |
| C | 54 | Shyle | [inaudible] | "Agile" |
| C | 66 | En 2:03 horas | [inaudible] | "2 o 3 horas" |
| C | 72 | de Jenkin tengo | [inaudible] | "Jenkins" |
| C | 76 | VILLARINO PABLO RODOLFO: Done. (turno completo) | eliminado |  |
| C | 78 | Si vos pudieses… (48 palabras) | puntuación |  |
| C | 80 | BM. Bien, buena pregunta. | eliminado |  |
| C | 80 | Jenkin también | [inaudible] | "Jenkins" |
| C | 80 | las los objetivos del ingeniero DevOps | eliminado |  |
| C | 80 | nuestros COP | [inaudible] | "nuestro scope" |
| C | 80 | Sonarcube | [inaudible] | "SonarQube" |
| C | 92 | BDI | [inaudible] | "VDI" |
| C | 92 | ejaz. | eliminado |  |
| C | 96 | yam | [inaudible] | "IAM" |
| C | 102 | algunos son premis | [inaudible] | "on premise" |
| C | 102 | Sé cómo hacerlo… (49 palabras) | puntuación |  |
| C | 122 | el uso de la guía | [inaudible] | "la IA" |
| D | 22 | supervisación | [inaudible] | "supervisión" |
| D | 24 | lo intenia | [inaudible] | "lo tenga" o "lo contemple" (dudoso) |
| D | 34 | medio APL | [inaudible] | "a pulmón" (dudoso) |
| D | 36 | se destipula | [inaudible] | "se estipula" / "se determina" |
| D | 38 | La pregunta original era… (59 palabras) | puntuación |  |
| D | 38 | te splashes | [inaudible] | "te explayes" |
| D | 40 | o sea, el equipo ya está reunido… (46 palabras) | puntuación |  |
| D | 48 | tiempo de CTO | [inaudible] | Sigla sin sentido; quizá "de esto" o "de FTE" (dudoso) |
| D | 52 | valor abrigado | [inaudible] | "valor agregado" |
| D | 64 | Cosas de la gente | [inaudible] | "agentes" |
| E | 8 | cueto | [inaudible] | "cohete" |
| E | 8 | lleva de un corante | [inaudible] | Dudoso; quizá "llevá un cortado" (sigue la ironía del café) |
| E | 16 | el cabucho marca | [inaudible] | "el que mucho abarca" (refrán) |
| E | 20 | se lo goñó (2 veces) | [inaudible] | "se logueó" |
| E | 44 | la hipera | [inaudible] | Dudoso; quizá "la cámara" |
| E | 52 | lo más paciente posible | [inaudible] | "fehaciente" |
| E | 54 | un guión | [inaudible] | "IAM" |
| E | 56 | se lo ganean | [inaudible] | "se loguean" |
| E | 60 | se lo goñaron (2 veces) | [inaudible] | "se loguearon" |
| E | 86 | Exoar | [inaudible] | "SOAR" |
| E | 104 | microsigmentación | [inaudible] | "microsegmentación" |
| E | 104 | Un 100 puede faltar | [inaudible] | "Un SIEM" |
| E | 104 | Una herramienta de microsegmentación… (49 palabras) | puntuación |  |
| E | 110 | por mi parte esta área | [inaudible] | "estaría" |
| E | 122 | en la GR … chete | [inaudible] | "la jerga"; "che, te" (dudoso) |
| F | 16 | pasear controles | [inaudible] | "saltear" / "bypassear" |
| F | 16 | pólisis | [inaudible] | "policies" (políticas de Chrome) |
| F | 16 | titanular | [inaudible] | "granular" |
| F | 20 | Hola. | eliminado |  |
| F | 20 | la paso del compañero | [inaudible] | "password" |
| F | 24 | ¿A qué tipos de guía? | [inaudible] | "IA" |
| F | 26 | le vas al montado | [inaudible] | Dudoso; quizá "le paso el mando a" |
| F | 28 | con un tallo | [inaudible] | Dudoso; quizá "Sí, vengo ahora con una" |
| F | 30 | del diam | [inaudible] | "del IAM" |
| F | 32 | Pasqui | [inaudible] | "KeePass" |
| F | 36 | password 6 … Centify | [inaudible] | "Password Safe"; "Centrify" o "CyberArk" |
| F | 52 | se logra | [inaudible] | "se loguea" |
| F | 54 | O K. | [inaudible] | "OK" |
| F | 56 | Y. Easy. (eliminado) + "la lista de soc" → [inaudible], hip. "el analista de SOC" | eliminado |  |
| F | 60 | de live | [inaudible] | "OneDrive" |
| F | 60 | HGPT | [inaudible] | "a ChatGPT" |
| F | 60 | Sinterin | [inaudible] | "ese ínterin" |
| F | 70 | Y. Claro. Y. | eliminado |  |
| F | 80 | cero trans | [inaudible] | "zero trust" |
| F | 80 | deflectivo | [inaudible] | "en definitiva" o "en efectivo" |
| F | 80 | el sitio | [inaudible] | "el CEO" |
| F | 82 | escasez | [inaudible] | "es acerca del" |
| F | 86 | del LP | [inaudible] | "de DLP" |
| F | 86 | no vio una respuesta | [inaudible] | "hay" |
| F | 86 | o k … y cara. partido … niñas generales | [inaudible] | "OK"; "a partir de ahí" (dudoso); "líneas generales" |
| F | 86 | una reina ínfima | [inaudible] | "una regla" o "una variable" |
| F | 90 | He hecho lo más importante. | [inaudible] | "Es de" / "Eso es" lo más importante |
| F | 96 | plaza Lucero | [inaudible] | "traza el usuario" / "traza Fulano" |
| F | 98 | MOCIULSKY SANTIAGO BERNARDO: Y. (turno completo) | eliminado |  |
| F | 100 | plazas | [inaudible] | "trazas" |
| F | 106 | cenpoint | [inaudible] | "endpoints" |
| F | 106 | la mente | [inaudible] | "Linux" |
| F | 106 | lleva a gente | [inaudible] | "agente" |
| F | 108 | [ininteligible] | [inaudible] | Turno completo ininteligible (marca unificada) |
| F | 110 | cuartos | [inaudible] | "costos" |
| F | 110 | es un Es un plus | puntuación |  |
| F | 110 | hace una match | [inaudible] | "le das una Mac" |
| F | 110 | Trelix | [inaudible] | "Trellix" |
| F | 110 | Y y ahí te ganaste… (54 palabras) | puntuación |  |
| F | 114 | Somos atentos. O. Okay. | [inaudible] | "O." y "Okay." eliminados; "Somos atentos" → hip. "Estamos atentos" |
| F | 120 | Otra de cuenta. | [inaudible] | "Tenelo en cuenta" |
| F | 122 | Ninuts | [inaudible] | "Linux" |
| F | 126 | imbestiable … juegos exploratorio | [inaudible] | "es entendible" (dudoso); "es exploratorio" |
| F | 132 | Sí. Sí. Y. Sí. | eliminado |  |
| F | 136 | reváleos | [inaudible] | "relevantes" o "válidos" |
| F | 138 | de la gente | [inaudible] | "del agente" |
| F | 138 | ustedes elevado | [inaudible] | "¿lo evaluaron?" |
| F | 140 | MUNTAABSKI FEDERICO: En. (turno completo) | eliminado |  |
| F | 142 | cacharla de café | [inaudible] | "charla" |
| F | 142 | cayendo | [inaudible] | "haciendo" / "creando" |
| F | 142 | periodos elevados | [inaudible] | "privilegios" |
| F | 142 | que todo allá | [inaudible] | "de Troya" |
| F | 142 | tiki, tiki, tiki | [inaudible] | Posible muletilla real "tiqui, tiqui" (= etcétera); confirmar |
| F | 148 | Muy varios. | [inaudible] | "válidas" |
| F | 86 | …sí, [inaudible] es un poco [inaudible] generales no va a depender… (51 palabras después de los reemplazos) | puntuación | |

## Sin cambios: para que decidas

1. **Anexo E, l. 10 (turno de MUNTAABSKI FEDERICO)**: "Ahora nosotros, en la siguiente entrega, que es el 18 de agosto, nosotros tenemos que mostrar, por así decirlo, el 50\% del avance." **No se modificó.** Habla del calendario de la materia y deja ver que la entrevista se hizo con el proyecto a mitad de camino. Decidí si queda así, si se recorta con `[…]` o si se aclara en el texto del capítulo.
2. **Anexo D: turnos con varios hablantes mezclados.** La transcripción automática separó mal los turnos y varias intervenciones tienen dentro frases de otra persona. Ejemplos: l. 10 ("Tranquilo, disparen" es de Jacubovich), l. 12 ("Para nada, chicos, graben"), l. 30 (la respuesta sobre el SIEM Sentinel está dentro del turno de Mociulsky), l. 34 ("Sí. Chiquito, pero sí. Todavía somos medio…"), l. 38, l. 62 ("Tienen otra idea, tírenla y le respondo" es de Jacubovich) y l. 72 (despedida con varias voces). Sin el audio no moví nada entre turnos, porque eso sería atribuir palabras.
3. **"logonean", "logoneaste", "logoneando", "logonea" (Anexo E, varias líneas).** Los dejé porque "logonear" (de *logon*) puede ser jerga real del entrevistado. En cambio, "se lo goñó", "se lo goñaron" y "se lo ganean" sí van como `[inaudible]`.
4. **Palabras existentes que probablemente no son las que se dijeron.** Las dejé porque no son basura evidente: D l. 16 "tenemos que hablar por la información" (¿velar?) y "ahí está la acción entre medir" (¿la tensión?); D l. 20 "inintencionadamente"; D l. 36 "traqueo"; C l. 102 "ejecutar tal cosa a todo el usuario" (¿como root?); F l. 16 "principios privilegios"; F l. 32 "para borrar las contraseñas" (¿guardar?); F l. 80 "se me asusta"; F l. 86 "del tiempo organizacional" (¿clima?).
5. **"Y." al principio de una oración** (por ejemplo C l. 42 "generalmente Y. Si el usuario", C l. 80 "Y. En mi equipo", F l. 72 "Y. Entonces", F l. 84 "Y. La pregunta") quedó, porque es el "y…" del habla seguido de una pausa. Solo eliminé los "Y." que estaban sueltos entre otros fragmentos (F l. 56, 70, 98 y 132).
6. **"Okay"/"Ok" usados como acuse de recibo al principio de un turno** (C l. 56, 88, 100, 108; F l. 48, 50, 58, 102, 134, 144) quedaron: tienen sentido en la conversación. Solo salió el "Okay." aislado de F l. 114.
7. **"tiki, tiki, tiki" (F l. 142)**: lo marqué `[inaudible]` porque lo señalaste como resto. Pero "tiqui, tiqui" existe en el habla rioplatense con el sentido de "etcétera". Si lo reconocés como dicho, se puede restituir.

## Preguntas para vos

1. C l. 16, "Valora. Es Sandy.": ¿era tu "Dale. ¿Santi?" para pasarle la palabra a Santiago?
2. C l. 46-50: ¿la frase de Villarino terminaba en "un servidor que está en AWS" ("Alexander su usuario." + "WS")? Si es así, se podría juntar el fin de la frase y sacar tu interjección "Claro."
3. C l. 66, "En 2:03 horas": ¿"2 o 3 horas"?
4. D l. 24, "lo intenia": ¿"lo tenga" o "lo contemple"?
5. D l. 34, "medio APL": ¿"a pulmón"?
6. D l. 48, "tiempo de CTO": ¿qué dijo Jacubovich?
7. E l. 8, "lleva de un corante": ¿"llevá un cortado"?
8. E l. 44, "siempre la hipera la misma": ¿"la cámara"?
9. E l. 54, "utilizan un guión": ¿"un IAM"?
10. E l. 110, "por mi parte esta área": ¿"estaría"?
11. E l. 122, "en la GR … chete": ¿"en la jerga" y "che, te"?
12. F l. 26-28, "le vas al montado" / "con un tallo": ¿qué se dijo en el pase de palabra entre ustedes?
13. F l. 36, "password 6" / "Centify": ¿"Password Safe" y "Centrify" o "CyberArk"?
14. F l. 86, "y cara. partido … niñas generales": ¿"a partir de ahí, en líneas generales"?
15. F l. 90, "He hecho lo más importante": ¿"Es de lo más importante"?
16. F l. 96, "plaza Lucero Pepito": ¿"la traza de Fulano/Pepito"?
17. F l. 114, "Somos atentos": ¿"Estamos atentos"?
18. F l. 126, "imbestiable" / "juegos exploratorio": ¿"es entendible" / "es exploratorio"?
19. F l. 142, "tiki, tiki, tiki": ¿lo restituyo como "tiqui, tiqui, tiqui"?
20. Para todos los `[inaudible]` con hipótesis evidente (DevOps, Jira, SonarQube, IAM, SIEM, SOAR, Linux, endpoints, etc.): si tenés el audio o recordás la palabra, ¿querés que ponga la forma correcta entre corchetes, por ejemplo `[Jira]`, en lugar de `[inaudible]`?
21. Frase del 18 de agosto (E l. 10): ¿queda, se recorta o se comenta?
22. Turnos mezclados del Anexo D: ¿querés que se separen? Habría que hacerlo con el audio.

## Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex`: compila sin errores (`build/main.pdf`, 244 páginas).
