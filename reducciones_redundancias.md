# Reducciones de redundancias aplicadas

Rama `e75/correcciones-e50-v2`, commits `6f97c91..HEAD` (22 commits, sin push).
Criterio: cada tema queda desarrollado en una **sección dueña**; en las demás pasa a una mención breve con "(sección X)". Cuando el texto recortado tenía un dato que no estaba en otro lado, ese dato se **movió** a la dueña (marcado con ➜).

Resultado: 263 → 260 páginas (el pie de página pasa de "de 261" a "de 258").
Palabras netas quitadas: ronda 1 ≈ 620, ronda 2 ≈ 280. Compilación sin errores, sin "??".

Para ver el detalle exacto de cada cambio: `git show <commit>`.

---

## Ronda 1: redundancias graves (🔴)

### 1. Diferencial "cierra el ciclo detección → decisión → acción" · dueña 2.2.6 · `b8cb276`
| Archivo · sección | Antes | Después |
|---|---|---|
| `chapter04.tex` · 3.4 Síntesis de diferenciadores | 4 párrafos casi iguales a 2.2.6 (enfoque pasivo/reactivo, PEP/PDP, "monitoreo y alerta → respuesta adaptativa", sin re-login) | Síntesis por competidor apoyada en la matriz 3.VIII: Sentinel/Splunk, Exabeam, Entra ID/Okta y ad-RACs, más un cierre que remite a 2.2.6 |
| `requerimientos.tex` · 4.5.1 (CU-01) | 2 oraciones: valor diferencial + "Esto contrasta con las soluciones… que delegan la respuesta" | 1 oración + (sección 2.2.6) |
| `e50_mercado.tex` · 11.1.1 Producto | 5 oraciones sobre el punto ciego, la ventana del atacante y "además de avisar, reacciona" | 1 oración + (sección 2.2.6). Las viñetas con citas literales no se tocaron |
| `e50_mercado.tex` · 11.2.1 Fortalezas | Viñeta 1 sin referencia | Se agrega (sección 2.2.6) |

### 2. Verificación en la nube del 10/10/2026 · dueña 9.4 · `25fd9fb`
| Archivo · sección | Antes | Después |
|---|---|---|
| `chapter01.tex` · 1.3 Descripción | "API central desplegada en la nube (verificada el 10 de octubre de 2026)" | Sin el paréntesis |
| `producto.tex` · 9.3 Cumplimiento | "el 10 de octubre de 2026 se verifica de punta a punta… la API rechaza con 403…" | "se verifica de punta a punta con un agente real contra la instancia (sección 9.4)". ➜ El resultado de los 403 pasa a 9.4 |
| `producto.tex` · 9.5, tabla 9.III, fila Seguridad | "…se verifican en la instancia el 10 de octubre de 2026" | "…se verifican en la instancia (sección 9.4)" |
| `producto.tex` · 9.6.1, fila "Canal HTTP en loopback" | "La verificación… se realiza el 10 de octubre de 2026" | "Verificado de extremo a extremo con un agente real (sección 9.4)" |

### 3. "Todavía no se ejecuta una promoción con un modelo genuinamente nuevo" · dueña 9.2.4 · `538a83d`
| Archivo · sección | Antes | Después |
|---|---|---|
| `producto.tex` · 9.2.4 | Solo mencionaba la corrida del 2/9 | ➜ Recibe las tres corridas (25/8, 23/8 y 2/9) y "por diferencias del orden del ruido" |
| `producto.tex` · 9.3 | Párrafo de RF-21 con las corridas, la adopción y "Por lo tanto, todavía no…" | 1 oración + (sección 9.2.4) |
| `producto.tex` · 9.7 Síntesis | Sin referencia | Se agrega (sección 9.2.4) |
| `pruebas.tex` · 10.3, viñeta Reentrenamiento | Remitía al criterio vigente | Se mantiene (datos que solo están ahí: 1 h 50 min, 0,1155 → 0,1175); cambia la referencia |
| `pruebas.tex` · 10.5 intro | "La regla anterior rechaza ese juego…; se adopta porque es el único juego completo y coherente…" | "Ese juego se adopta como vigente por consistencia y no por una promoción (sección 9.2.4)" |
| `pruebas.tex` · 10.9, fila corrida del 25/8 | Incluía la oración sobre el juego del 2/9 adoptado por consistencia | "…sin una promoción real (sección 9.2.4)" |

### 4. Detección 12–30 % / 91–99 % / FP 4–5 % · dueña 10.7.4 · `afc86e6`
| Archivo · sección | Antes | Después |
|---|---|---|
| `chapter04.tex` · 3.3.7, tabla 3.XV, Métrica | ROC-AUC + "detecta entre el 12 % y el 30 %… 91 % y 99 %… 4 % al 5 %" | ROC-AUC + "la detección operativa… se presenta en la sección 10.7.4" |
| `producto.tex` · 9.6.1, fila 1 | "lo confirma: sin país, el nivel alto detecta entre el 12 % y el 30 %…" | "lo confirma (sección 10.7.4)" |
| `pruebas.tex` · 10.7.5 Contraste con las metas | Repetía "(4 % a 5 %)" y "(12 % a 30 %…)" | Sin porcentajes, con (sección 10.7.4) |

### 5 y 6. Explicación con 3 variables de IF / período de aprendizaje · dueñas 5.4.4 y RF-24/25 + 9.2.5 · `43c7208`
| Archivo · sección | Antes | Después |
|---|---|---|
| `e50_diseno_ux.tex` · 5.4.4, párrafo "Las tarjetas…" | "la explicación se basa solo en el modelo diario, ya que el LSTM no ofrece explicaciones; … durante el aprendizaje la acción se atenúa…" | Solo la limitación poblacional/individual. La explicación sin LSTM y la atenuación quedan dichas una vez cada una |
| `chapter04.tex` · 3.2 Lectura de la matriz | "(las 3 de mayor z-score, calculadas en cada evento) pero no tiene un mecanismo propio para el LSTM…" + oración sobre el período de aprendizaje | "cubre solo el componente Isolation Forest (sección 5.4.4)". Se elimina la oración del período de aprendizaje |
| `chapter04.tex` · 3.6.6 Privacidad | "con las tres variables de IF que más se apartan de la población de entrenamiento" | "(sección 5.4.4)" |

### 7. Variables de Isolation Forest · dueña 8.3.1 · `adbf63d`
| Archivo · sección | Antes | Después |
|---|---|---|
| `producto.tex` · 9.2.2, paso 1 | Lista de las 8 variables | "ocho variables agregadas (sección 8.3.1)" |

### 8. Reversión con icacls · dueña 9.6.1 · `e214bc6`
| Archivo · sección | Antes | Después |
|---|---|---|
| `conclusiones.tex` · 13.1, objetivo 4 | "…porque icacls /restore requiere… SeRestorePrivilege; sin elevación… /remove:d…" | "…con el agente ejecutado como administrador (sección 9.6.1)" |
| `pruebas.tex` · 10.9, fila reversión | "(icacls /save y /restore)" | "(icacls /save)" + (sección 9.6.1) |

### 9. mTLS y firma de respuestas · dueña 13.4, ítem 9 · `a945c7d`
| Archivo · sección | Antes | Después |
|---|---|---|
| `producto.tex` · 9.6.1, fila mTLS, Tratamiento | Diseño completo (segundo sitio del proxy, autoridad propia, huella) + oración sobre la firma | "Trabajo futuro: autenticación mutua y firma de las respuestas (sección 13.4)". ➜ La oración sobre el proxy de inspección pasa a 13.4 |
| `arquitectura.tex` · 7.6 | "queda diseñada como trabajo futuro (sección 9.6)" | "(sección 9.6) … (sección 13.4)" |

### 10. RADAC / ad-RACs · dueña 2.2.2.1 · `3792438`
| Archivo · sección | Antes | Después |
|---|---|---|
| `chapter04.tex` · 3.1.6, tabla ad-RACs | "validado con métricas fuertes (Recall 100 %, F1 98 %)" | "validado frente a reglas estáticas (sección 2.2.2.1)" |
| `chapter02.tex` · 2.2.3.3 | 2 párrafos de definición que repetían 2.1.4.3 | 1 oración que remite a 2.1.4.3. Se mantiene el párrafo de ventajas y limitaciones |
| `chapter04.tex` · 3.3.1 CatBoost | — | Sin cambio (decisión tuya) |

### 11. Gemini en la tabla 9.III, fila Transferencia internacional · dueña 9.6.2 · `5c68286`
| Archivo · sección | Antes | Después |
|---|---|---|
| `producto.tex` · 9.5, tabla 9.III | API REST, modelos, error 429, cabecera, delimitado, validación, 6 s y controles contra inyección | Solo qué datos salen, hacia quién y qué queda a cargo de la organización, + (sección 9.6.2). La fila ya no corta página |
| `producto.tex` · 9.6.2 | No tenía los nombres de modelo | ➜ Recibe `generateContent`, `gemini-3.1-flash-lite` / `gemini-2.5-flash` (429) y el texto de respaldo |

### 12. Métricas de pruebas en 13.2 · dueñas 10.2/10.4 · `d9056d0`
| Archivo · sección | Antes | Después |
|---|---|---|
| `conclusiones.tex` · 13.2 | p95 + 0,09 % CPU, 33 MB, 530 pruebas, 93,9 % / 89,3 % | p95 de 14,9 ms frente a 500 ms + "consumo y cobertura dentro de sus umbrales (tabla 13.I)" |

### 13. Ausencia de etiquetas en CLUE-LDS · dueña 10.5.1 · `befca40`
| Archivo · sección | Antes | Después |
|---|---|---|
| `pruebas.tex` · 10.5.2 | "Como el conjunto no incluye etiquetas… no es posible calcular precisión, recall, F1 ni curvas ROC…" | "Por la ausencia de etiquetas señalada en la sección 10.5.1, tampoco es posible trazar curvas ROC…" |

---

## Ronda 2: redundancias menores + PEP/PDP

| # | Commit | Archivo · sección | Antes | Después |
|---|---|---|---|---|
| R1 | `af24131` | `chapter02.tex` · 2.1.8 Estándares | Repetía los principios de NIST (verificación continua, separación entre quien decide y quien ejecuta) | Remite a 2.1.2; conserva los niveles de respuesta y 800-207A |
| R1 | `af24131` | `requerimientos.tex` · 4.1 | Rol completo del agente PEP y de la API PDP + oración de NIST | "agente local (PEP), API central (PDP)…" + remite a 4.2 y 7.1 |
| R1 | `af24131` | `e50_diseno_ux.tex` · 5.4.4 | "la ausencia de controles… respeta la separación entre PEP y PDP" (repetido en el mismo apartado) | Se quita (queda el párrafo de RNF-04) |
| R2 | `8bc73ef` | `chapter02.tex` · 2.2.5.4 | "no existe un único algoritmo…" (casi igual a 2.2.2.2) | "En línea con lo que concluyen Artioli y Landauer, presentadas en las secciones 2.2.2.2 y 2.2.2.3…" |
| R3 | `8bc73ef` | `chapter02.tex` · 2.2.5.1 | Repetía la conclusión de Landauer ("LSTM/autoencoders entre los más utilizados") | "La revisión presentada en la sección 2.2.2.3 señala…" |
| R4 | `8bc73ef` | `chapter02.tex` · 2.2.4 | Explicación completa del attacker-induced drift | "(attacker-induced drift, sección 2.1.7.2)" |
| R5 | `764302c` | `pruebas.tex` · 10.5.1 | "no aplica técnicas de sobremuestreo ni de balanceo de clases" | "…no aplica técnicas de balanceo de clases (sección 8.1)" |
| R6 | `26205e8` | `arquitectura.tex` · 7.6 | Dos párrafos que repetían TLS / HTTPS fuera de loopback / HTTP en loopback | Un párrafo |
| R7 | `26205e8` | `producto.tex` · 9.4 | Caddy, ACME, /api, interfaz local, SSM sin SSH, CDN no usada | "con el proxy inverso y los controles descritos en la sección 7.5.2" |
| R8 | `db22546` | `producto.tex` · 9.5.1 | "El borrado de la API alcanza al estado… herramienta de limpieza, no supresión completa" (igual a la tabla 9.III) | "…no es un mecanismo de supresión completo (tabla 9.III)" |
| R9 | `db22546` | `producto.tex` · 9.2.4 | "idéntica byte a byte… comparación A/B sobre 800 eventos" | "la salida del puntaje no cambia (sección 10.7.3)" |
| R10 | `db22546` | `pruebas.tex` · 10.2.3 | "…74 % … funciona como protección contra regresiones" | "…74 % (sección 10.2.4)" |
| R11 | `bf75c03` | `e50_diseno_ux.tex` · 5.4.2, 5.4.3, 5.4.6 | Lista de colores repetida; "evita confundir los últimos 30 eventos…" dicho dos veces; justificación de los botones de guardado | Sin la lista de colores; los 30 eventos una sola vez; botones → (sección 5.2) |
| R12 | `1744313` | `pruebas.tex` · 10.5 intro | "(50 522 931 eventos; 8 494 589 válidos…)" | "(sección 8.2)" |
| R13 | `bfa8336` | `chapter01.tex` · objetivos 1 y 7 | Obj. 1 con "credencial individual y revocable…, ligada a su identidad y a los usuarios" (igual que el 7) | Obj. 1: "credencial individual por agente". El 7 conserva el detalle y suma "revocable" |

---

## Etiquetas nuevas
`sec:pantalla-porque` (5.4.4), `sec:if-variables` (8.3.1), `sec:radac-marco` (2.1.4.3), `sec:ea-radac` (2.2.2.1), `sec:zero-trust` (2.1.2), `sec:ea-ueba-dl` (2.2.2.2), `sec:ea-if` (2.2.2.3), `sec:estrategias-drift` (2.1.7.2), `sec:despliegue-nube` (7.5.2), `sec:resultados-holdout` (10.7.3).

## Sin cambios a propósito
- Tablas RF/RNF/HU del cap. 4 y Anexos C–G.
- Cifras clave de 13.1 y 13.2 (detección, latencia).
- 3.3.1 CatBoost (decisión tuya).
- 11.1.3, 12.2, 12.5.3 y 9.5 (mTLS): ya eran menciones breves.
- El par 9.6.1 ↔ 13.4, las síntesis de capítulo y la presentación de los tres componentes en cada capítulo: hilo conductor (detalle en la sección "No se cambian" del plan).
