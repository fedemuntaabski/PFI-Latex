# Redundancias del documento PFI (UMBRAL)

Revisión de `main.tex`, capítulos 1 a 13. Numeración según el `main.toc` compilado.
No se revisan las transcripciones (Anexos C–G), que son fuente primaria.

**Leyenda de tipo**
- **Directa**: mismo dato, cifra o frase (casi) textual en más de un lugar.
- **Indirecta**: mismo tema/idea explicado de nuevo con otras palabras.
- 🔴 alta (3+ lugares con el mismo detalle) · 🟡 media · 🟢 baja / probablemente aceptable.

---

## Resumen: las 15 más fuertes

| # | Tema | Tipo | Secciones |
|---|------|------|-----------|
| 1 | Diferencial "cierra el ciclo detección→decisión→acción en el endpoint, sin re-login" | Directa | 2.2.6, 3.4, 4.5.1, 11.1.1, 11.2.1, 12.2, 12.5.3, 13.2 |
| 2 | 2.2.6 y 3.4 son casi el mismo texto | Directa | 2.2.6 ↔ 3.4 |
| 3 | Credencial del agente ligada a identidad/usuarios, 403 | Directa | 1.1.2 (obj. 1 y 7), 7.1, 7.6, 9.2.6, 9.3, 9.5, 9.6.1, 10.9, 13.1 |
| 4 | Verificación en la nube del 10/10/2026 | Directa | 1.3, 7.7, 9.3, 9.4, 9.5, 9.6.1, 11.1.3, 13.1 |
| 5 | "Todavía no se ejecuta una promoción con un modelo genuinamente nuevo" + corridas 25/8, 23/8, 2/9 | Directa | 9.2.4, 9.3, 9.7, 10.3, 10.5, 10.9, 13.1 |
| 6 | Detección 12–30 % sin país / 91–99 % con país / FP 4–5 % | Directa | 3.3.7, 9.6.1, 10.7.4, 10.7.5, 10.11, 13.1, 13.2 |
| 7 | Explicación = 3 variables de Isolation Forest; LSTM sin explicación | Directa | 3.2, 3.6.6, RNF-11, 5.4.4, 9.2.2, 9.6.1, 11.1.1, 11.2.1, 12.2, 13.1 |
| 8 | Período de aprendizaje (20 eventos, atenúa a `alertar` salvo archivos) | Directa | 3.2, RF-24/25, 4.5.4, HU-11, 5.4.4, 9.2.5, 10.9 |
| 9 | Redacción asistida con Gemini / inyección de instrucciones | Directa | RF-31, 7.4, 9.2.2, 9.5 (tabla), 9.6.1, 9.6.2, 10.9, 13.4 |
| 10 | Pipeline de scoring (8 variables IF, 50 eventos LSTM, 0,5/0,5, vida media 3 d, 40/70/90, regla de piso) | Directa | RF-03 a RF-07, 4.5.1, HU-02, 8.3, 9.2.2, 10.7.3 |
| 11 | Reversión de ACL con `icacls /restore`, `SeRestorePrivilege`, `/remove:d` | Directa | 1.1.2, RF-11, HU-04, 9.2.1, 9.6.1, 10.9, 13.1 |
| 12 | mTLS y firma de respuestas como trabajo futuro | Directa | 1.1.2, 7.6, 9.5, 9.6.1, 9.7, 13.1, 13.4 |
| 13 | RADAC / ad-RACs con Recall 100 %, precisión 95 %, F1 98 % | Directa | 2.1.4.3, 2.2.2.1, 2.2.3.3, 3.1.6, 3.3.1 |
| 14 | Brecha / transferencia de dominio (nube → Windows) | Directa | 3.3.7, 8.4, 8.6, 9.6.1, 10.10, 11.2.2, 13.3, 13.4 |
| 15 | Métricas de pruebas (530 pruebas, 93,9/89,3 %, p95 14,9 ms, 0,09 % CPU, 33 MB) | Directa | RNF-01/02, 10.2, 10.4, 10.11, 13.1, 13.2 |

---

## A. Problema, marco teórico y estado del arte

### A1. Punto ciego post-autenticación / robo de credenciales / movimiento lateral 🔴 Indirecta
- **Dónde**: 1.3 (párr. 1), 2.1.1, 2.2.3.1 (limitación de Okta), 2.2.6, 3.1.5 (tabla Okta), 3.4, 3.6.1, 3.6.2, 3.6.9, 11.1.1 (Diferencial), 11.4, 12.5.1 (Nombre), 12.5.3.
- **Qué**: se re-explica que la seguridad confía solo en el login y que un atacante con credenciales válidas se mueve sin ser detectado. 2.1.1 es la definición; el resto lo vuelve a contar.

### A2. NIST SP 800-207 y separación PEP/PDP 🔴 Directa + indirecta
- **Dónde**: 1.1.1, 2.1.2 (PEP/PDP/PIP), 2.1.8 (Estándares), 2.2.6, 3.1.7, 3.4, 3.5.2 (Modelo de confianza cero), 4.1, RNF-04 (4.4), 5.4.4, 7.1, 7.7, 11.1.1, 11.2.1, 13.1, 13.2.
- **Qué**: 2.1.2 y 2.1.8 presentan el mismo estándar dos veces dentro del marco teórico ("verificación continua", "separación entre componentes que deciden y que ejecutan"). Luego cada capítulo vuelve a decir "siguiendo NIST SP 800-207, el agente es PEP y la API es PDP".

### A3. RADAC tratado tres veces dentro del capítulo 2 🔴 Directa
- **Dónde**: 2.1.4.3 (RADAC en IAM), 2.2.2.1 (ad-RACs, trabajos académicos), 2.2.3.3 (RAdAC, enfoques alternativos); y de nuevo en 3.1.6 y 3.3.1.
- **Qué**: misma definición (decisión de acceso ajustada dinámicamente al riesgo) en tres subsecciones. Las métricas de Aliyu2024 (Recall 100 %, precisión 95 %, F1 98 %) aparecen en 2.2.2.1, 3.1.6 y 3.3.1.

### A4. "No existe un único algoritmo" → modelos híbridos 🟡 Directa
- **Dónde**: 2.2.2.2 (Artioli), 2.2.5.4 (Ensambles), 3.3.4, 3.3.6, 3.3.7.
- **Qué**: la frase "no existe un único algoritmo capaz de ofrecer el mejor rendimiento en todos los escenarios" está casi igual en 2.2.2.2 y 2.2.5.4.

### A5. Conclusión de la revisión de Landauer2023Survey 🟡 Directa
- **Dónde**: 2.2.2.3 (párr. 2), 2.2.5.1 (XAI), 3.3.6.
- **Qué**: "LSTM/Autoencoders dominan en anomalías secuenciales; Isolation Forest es eficiente en baja latencia" tres veces.

### A6. Explicabilidad / "caja negra" en la literatura 🟡 Indirecta
- **Dónde**: 2.2.4 (párr. 3), 2.2.5.1, 3.2 (columna XAI).
- **Qué**: limitación y tendencia cuentan lo mismo (modelos profundos poco interpretables, XAI como respuesta).

### A7. Cold-start 🟡 Indirecta
- **Dónde**: 2.2.2.2 (LADOHD), 2.2.4 (párr. 2), 3.3.2, 4.5.4 (aporte de CU-04).

### A8. Concept drift y attacker-induced drift 🟡 Directa
- **Dónde**: 2.1.7.2 (Kuppa2022), 2.2.4 (párr. 4), 4.5.3 (aporte de CU-03).
- **Qué**: el envenenamiento gradual del reentrenamiento se explica completo en 2.1.7 y otra vez en 2.2.4.

### A9. Desbalance / ausencia de ataques etiquetados 🔴 Directa
- **Dónde**: 2.1.5 (intro), 2.2.4 (párr. 1), 8.1, 10.5.1, 10.5.2.
- **Qué**: 10.5.1 y 10.5.2 repiten casi igual "CLUE-LDS no incluye etiquetas, por lo que no se puede calcular precisión/recall/F1" (ambas citan Landauer2022Dataset). 8.1 y 10.5.1 repiten "sin técnicas de balanceo de clases".

### A10. Datos reales vs sintéticos 🟢 Indirecta
- **Dónde**: 2.1.6, 3.3.7, 8.4 (párr. "decisión de diseño"), 9.5.2.

### A11. Descripción y limitaciones de los competidores 🔴 Directa
- **Dónde**: 2.2.1 → re-tabulado en 3.1.1–3.1.5 → 3.2 (matriz) → 3.4 (último párr.) → 11.1.1 (bullets con "citas textuales del estado del arte") → 11.2.1, 11.2.2, 11.2.4 → 11.3 → 11.4.
- **Qué**: las mismas limitaciones (Sentinel opaco y caro por volumen; Splunk sin respuesta nativa; Exabeam sin agente propio) se citan hasta cinco veces. El cap. 11 se cita a sí mismo como "según el propio estado del arte".

### A12. Segmento PyME desatendido 🟡 Indirecta
- **Dónde**: 2.2.6 (último párr.), 11.1.2, 11.2.3, 11.3 (fuerzas 1 y 4), 11.4, 12.1, 12.2.

---

## B. Arquitectura y producto

### B1. Los tres componentes (agente / API / dashboard) 🔴 Indirecta
- **Dónde**: 1.2, 1.3, 3.1.7, 4.1, intro del cap. 5, 7.1, 9.1 (tabla), 11.1.1 (Producto).
- **Qué**: cada capítulo vuelve a presentar el sistema desde cero.

### B2. Flujo de un evento 🟡 Directa
- **Dónde**: 4.5.1 (CU-01), 6.1 (texto del diagrama de flujo), 7.1 (párr. 3), 9.2.2 (lista de pasos).
- **Qué**: agente captura → API valida/deduplica → Redis/PostgreSQL → puntaje → nivel/acción → confirmación.

### B3. Pipeline de scoring 🔴 Directa
- **Dónde**: RF-03 a RF-07 (4.3.2), 4.5.1, HU-02, 3.1.7, 8.3.1–8.3.3 (+ párrafo tras la tabla), 9.2.2 (pasos 1–7), 10.7.3.
- **Qué**: las 8 variables de Isolation Forest están listadas en 8.3.1 y otra vez en 9.2.2 paso 1. Vida media de 3 días: RF-04, 8.3.3, 9.2.2, 10.9. Umbrales 40/70/90: RF-05, 8.3.3, 10.7.3, 10.9. Regla de piso: RF-06, HU-02, 5.4.4, 9.2.2.

### B4. Período de aprendizaje 🔴 Directa
- **Dónde**: 3.2 ("Lectura de la matriz", fuera de lugar), RF-24 a RF-27, 4.5.4, HU-11/12/13, 5.4.4 (dos párrafos), 9.2.5, 10.9 (tabla), 12.2.
- **Qué**: "20 eventos (1 a 1000), el nivel no cambia, la acción se atenúa a `alertar` salvo eventos de archivo" casi textual en RF-25, HU-11, 5.4.4 y 9.2.5.

### B5. Catálogo de acciones y mapeo nivel → acción 🔴 Directa
- **Dónde**: 1.1.2 (obj. 4), RF-07, RF-08, RF-10, HU-03, 3.5.2, 9.2.1 (lista), 9.5.3, 9.6.1 (terminación irreversible; mapeo de respaldo del agente), 13.1 (obj. 4).
- **Qué**: RF-08 y 9.2.1 listan las mismas seis/cinco acciones.

### B6. Reversibilidad (ACL, `icacls`, terminación no reversible) 🔴 Directa
- **Dónde**: 1.1.2 (obj. 4), RF-11, RNF-06, HU-04, 9.2.1, 9.6.1 (intro + fila "Reversión… con privilegios"), 10.9 (fila reversión), 13.1 (obj. 4).
- **Qué**: el detalle técnico `icacls /restore` + `SeRestorePrivilege` + respaldo `/remove:d` aparece completo en 9.6.1, 10.9 y 13.1.

### B7. Buffer local (3 h, 20 000 eventos) y circuit breaker (5 min) 🟡 Directa
- **Dónde**: RF-02, RNF-05, 4.5.1 (alternativas), HU-01, 9.2.1, 9.6.1, 10.2.5, 13.4 (ítem 6).

### B8. Solo metadatos (sin contenido, pantallas ni teclado) 🔴 Directa
- **Dónde**: 1.1.2 (obj. 1), RF-01, RNF-08, HU-01, 9.2.1, 9.5 (fila "Datos no excesivos"), 13.1 (obj. 1).

### B9. Credencial individual del agente ligada a identidad y usuarios 🔴 Directa
- **Dónde**: 1.1.2 (obj. 1 **y** obj. 7: repetido dentro de la misma lista), 7.1 (bullet Agente), 7.6 (párr. 3), 9.2.6, 9.3 (párr. de RF-02), 9.5 (fila Seguridad), 9.6.1 (intro), 10.9 (tabla), 13.1 (obj. 1 y 7).

### B10. Clave de administración aceptada en el nivel de agente 🟡 Directa
- **Dónde**: 9.2.6, 9.3, 9.6.1 (fila), 13.4 (ítem 9).

### B11. Token de sesión del panel (opaco, rol, 8 h, sin claves en el navegador) 🔴 Directa
- **Dónde**: 1.1.2 (obj. 7), 7.5.2, 7.6, 8.5.2 (tabla Redis), 9.2.6, 9.4, 9.5, 9.6.1 (fila CSP), 10.9, 13.1 (obj. 7).

### B12. TLS / HTTPS, HTTP en loopback, agente exige HTTPS fuera de loopback 🔴 Directa
- **Dónde**: RNF-13, 7.5.2, 7.6 (párr. 6 y 7), 9.3, 9.5, 9.6.1 (fila), 10.2.5, 13.1 (obj. 1 y 7).
- **Qué**: el último párrafo de 7.6 y la fila de 9.6.1 dicen lo mismo.

### B13. mTLS y firma de respuestas como trabajo futuro 🔴 Directa
- **Dónde**: 1.1.2 (obj. 7), 7.6 (párr. 1 y último), 9.5, 9.6.1, 9.7, 13.1 (obj. 7), 13.4 (ítem 9).
- **Qué**: el diseño propuesto (segundo sitio del proxy, CA propia, huella del certificado) está en 9.6.1 y 13.4 casi igual.

### B14. Despliegue en la nube (Caddy, ACME, API solo en interfaz local, SSM sin SSH, IP fija) 🟡 Directa
- **Dónde**: 7.4, 7.5.2, 9.4.
- **Qué**: 9.4 repite 7.5.2 y agrega fechas de verificación.

### B15. Verificación del 10/10/2026 (y del 6/10) 🔴 Directa
- **Dónde**: 1.3 (paréntesis "verificada el 10 de octubre de 2026"), 7.7, 9.3, 9.4, 9.5 (fila Seguridad), 9.6.1 (fila HTTP en loopback), 11.1.3, 13.1 (obj. 1 y 7).

### B16. Redis (estado) vs PostgreSQL (historial) y servicios gestionados 🔴 Indirecta
- **Dónde**: RF-09, 5.4.9, 7.1, 7.3.1, 7.4, 7.5.3, 8.5 (intro), 8.6, 9.1 (tabla), 9.2.2 (último párr.), 11.1.3.

### B17. Transacciones optimistas en Redis con 20 reintentos (RNF-14) 🟡 Directa
- **Dónde**: 7.3.1, 7.6, 8.5.2, 10.3 (Concurrencia sobre Redis).

### B18. Cadena de hashes 🟡 Indirecta
- **Dónde**: RNF-09, 7.4, 8.5.1, 8.6, 9.2.2, 9.5 (filas Seguridad y Supresión), 9.5.1, 9.6.1, 10.3, 10.9, 13.4 (ítems 5 y 8).
- **Qué**: la tensión "suprimir rompe la cadena" está tres veces: tabla 9.5, 9.5.1 y 9.6.1.

### B19. Seguridad a nivel de fila en 6 de 7 tablas (`historial_scores` pendiente) 🟢 Directa
- **Dónde**: 7.4, 8.5.1, 9.5.

### B20. Dashboard: 8 pantallas, sondeo cada 2 s, sin WebSockets 🟡 Directa
- **Dónde**: intro del cap. 5 y 5.3, 7.3.3, 7.6, 9.2.3, 10.4.1, 10.8.
- **Qué**: 9.2.3 vuelve a describir las pantallas que ya se describen en 5.4.

### B21. 32 endpoints y 4 niveles de acceso 🟡 Directa
- **Dónde**: 7.1 (lista de consumidores), 7.3.1, 9.2.6.

### B22. Explicabilidad del sistema (3 variables de IF por z-score; LSTM sin explicación) 🔴 Directa
- **Dónde**: 3.2 (matriz + lectura), 3.6.6, RNF-11, HU-15, 5.4.3, 5.4.4 (dos veces dentro de la misma subsección), 9.2.2 (paso 7), 9.6.1, 10.6.2, 11.1.1, 11.2.1, 12.2, 13.1 (obj. 5), 13.4 (ítem 2).

### B23. Notificación por correo (intervalo 10 min) y redacción asistida con Gemini 🔴 Directa
- **Dónde**: RF-15, RF-31, 4.5.1, HU-07, 7.4, 7.6, 8.5.2, 9.2.2, 9.5 (fila Transferencia internacional), 9.6.1, 9.6.2, 10.9, 11.1.1, 11.2.1, 13.4 (ítem 7).
- **Qué**: la fila de transferencia internacional de 9.5 incluye todo el detalle técnico de Gemini (modelos, 6 s, 10 eventos, delimitado, validación) que después se explica entero en 9.6.2 y se resume en 9.6.1 y 10.9.

### B24. Integración IAM (rol/departamento, caché 30 min, mock/Keycloak, desactivada, sin validación real) 🟡 Directa
- **Dónde**: RF-28/29/30, 4.5.1, HU-16, 7.4, 7.5.1, 7.6, 8.5.2, 9.2.2, 9.6.1, 10.10, 11.2.3, 13.4 (ítem 9).

---

## C. Reentrenamiento

### C1. Reentrenamiento aislado, planificador, ventana horaria, promoción sin reinicio 🔴 Directa
- **Dónde**: 1.1.2 (obj. 6), 1.3 (último párr.), RF-18 a RF-22, RNF-10, 4.5.3, HU-08/09/10, 7.3.4, 9.1, 9.2.4, 10.3, 10.9, 13.1 (obj. 6).
- **Qué**: los márgenes 0,02 / 0,01 de no inferioridad están en RF-21 y 9.2.4.

### C2. "No se promovió ningún modelo genuinamente nuevo" + corridas del 25/8, 23/8 y 2/9 + adopción "por consistencia" 🔴 Directa
- **Dónde**: 9.2.4, 9.3, 9.7, 10.3 (bullet reentrenamiento), 10.5 (intro), 10.9 (tabla), 13.1 (obj. 6).
- **Qué**: la misma salvedad casi palabra por palabra en 4 a 7 lugares.

### C3. El criterio anterior favorecía a un modelo que no marca nada 🟢 Directa
- **Dónde**: 9.2.4, 13.3 (lección 3).

### C4. Fallos del planificador ("pipeline en curso", excepción reintenta a los 5 min) 🟡 Directa
- **Dónde**: 4.5.3, 9.6.1, 13.4 (ítem 6).

### C5. Fragilidad del corte temporal (2/8/2021) que rechaza reentrenamientos con datos del agente 🟡 Directa
- **Dónde**: 8.4 (último párr.), 9.6.1, 13.4 (ítem 4).

### C6. Comparación A/B "byte a byte" sobre 800 eventos con el conjunto de variables versionado 🟡 Directa
- **Dónde**: 9.2.4, 10.7.3. Texto casi idéntico.

### C7. Modelos v2 rechazados por falsos positivos (0,0734 vs 0,0657) 🟢 Directa
- **Dónde**: 9.2.4, 10.9 (Modelos v2), 13.1 (obj. 6).

---

## D. Datos y resultados del modelo

### D1. Ficha de CLUE-LDS (50 522 931 eventos, 920 usuarios, 2017–2022, CC BY 4.0, seudonimizado) 🟡 Directa
- **Dónde**: 3.3.7, 8.1, 8.2, 9.5.2, 10.5 (intro), 11.3 (fuerza 5).

### D2. Cuentas de servicio (>500 000) e IP sin puntaje 🟢 Directa
- **Dónde**: RF-03, 8.2, 9.5 (fila Datos no excesivos).

### D3. Transferencia / brecha de dominio 🔴 Directa
- **Dónde**: 3.3.7, 8.4 (lista + párr.), 8.6, 9.6.1, 10.10, 11.2.2, 13.3 (lección 1), 13.4 (ítem 3).

### D4. País desconocido en el 99,95 %, el país como "interruptor", el LSTM no aprovecha el orden (Spearman 0,989) 🔴 Directa
- **Dónde**: 3.3.7, 8.4 (bullet), 9.6.1 (filas país y LSTM), 10.6.4, 10.7.4, 10.11, 13.2, 13.4 (ítems 1 y 2).

### D5. Particiones distintas (IF temporal / LSTM por usuario): solo 15 usuarios en común; 47 de 57 víctimas vistas por el LSTM 🟡 Directa
- **Dónde**: 8.3.3, 10.5.2, 10.7.2, 10.7.4, 10.10.

### D6. Detección con escenarios etiquetados: 12–30 % sin país, 91–99 % con país, FP 4–5 % 🔴 Directa
- **Dónde**: 3.3.7, 9.6.1 (fila 1), 10.7.4, 10.7.5, 10.11, 13.1 (obj. 2), 13.2; versión cualitativa en 11.2.2.

### D7. Escenarios inyectados: 13,3 % en E4, 15,4 % de días normales en alto, ninguno crítico, "nunca supera un tercio" 🔴 Directa
- **Dónde**: 9.6.1, 10.5.1 (tabla de metas), 10.6.2, 10.6.3, 10.6.4, 13.1 (obj. 2), 13.2.

### D8. "Es la principal limitación técnica del proyecto" 🟡 Directa
- **Dónde**: 9.7, 10.5.1 (párr. final), 10.11, intro del cap. 13, 13.2, 13.4 (intro).

### D9. Sesgo de la línea base personal en usuarios con poco historial (5 alternativas evaluadas) 🟡 Directa
- **Dónde**: 9.6.1, 10.6.4, 10.9, 13.4 (ítem 1).

### D10. Cobertura parcial: el 19,6 % nunca completa 50 eventos 🟡 Directa
- **Dónde**: 3.3.2, RF-03, 4.5.4, 8.3.2, 9.6.1, 10.9.

### D11. Salto al cerrar la primera secuencia del LSTM 🟢 Directa
- **Dónde**: 9.6.1, 10.9 (Recalibración), 13.4 (ítem 1).

### D12. Peso 0,5 / calibración sin datos independientes 🟢 Indirecta
- **Dónde**: 9.6.1, 10.5.2, 10.9 (Recalibración, Agregación del LSTM).

### D13. Metas fijadas después de la evaluación exploratoria 🟢 Directa
- **Dónde**: 10.5.1, 13.3 (lección 2).

---

## E. Pruebas y cifras de cumplimiento

### E1. Latencia p95 14,9 ms / p99 148,9 ms 🔴 Directa
- **Dónde**: RNF-01 (columna Estado), 10.4.1, 10.5.1 (tabla de metas), 13.1 (obj. 3), 13.2.

### E2. Consumo del agente: 0,09 % CPU, 33 MB 🟡 Directa
- **Dónde**: RNF-02 (columna Estado), 10.4.2, 13.1 (obj. 1), 13.2.

### E3. 530 pruebas (353 + 177) y cobertura 93,9 % / 89,3 % 🔴 Directa
- **Dónde**: 10.2.1, 10.2.4, 10.11, 13.1 (obj. 9), 13.2.

### E4. Frontend sin pruebas / fuera del umbral / "sin lógica de negocio" 🔴 Directa (dentro del cap. 10)
- **Dónde**: 10.2.1 (tabla), 10.2.3, 10.2.4 (párr. Frontend), 10.10, 13.1 (obj. 9), 13.4 (ítem 8).

### E5. CI: 18 pruebas omitidas por artefactos no versionados; la e2e PDP→PEP no corre en CI 🟡 Directa (intra-cap. 10)
- **Dónde**: 10.2.2, 10.2.3, 10.3, 10.9.

### E6. Umbral del 74 % "como protección contra regresiones, no como evidencia" 🟢 Directa
- **Dónde**: 10.2.3, 10.2.4.

### E7. Cobertura previa 84,2 % / 69,4 % 🟢 Directa
- **Dónde**: 10.2.4, 10.9.

### E8. 31/31 RF implementados; 15 RNF = 12 + 3 parciales (RNF-05, 09, 11) 🟡 Directa
- **Dónde**: 4.3 (intro), 9.3, 9.7, 13.1 (párr. tras la tabla).

### E9. Evaluación heurística: 4 problemas mayores corregidos 🟢 Directa
- **Dónde**: RNF-15, 10.8, 10.9, 13.1 (obj. 5).

---

## F. Legal

### F1. Informar a los empleados (LCT arts. 70–72) 🟡 Indirecta
- **Dónde**: 1.2, 2.1.9, 9.5 (fila Consentimiento), 9.5.3, 12.5.3, 13.2.

### F2. Transferencia internacional (EE. UU., Brasil, cláusulas tipo) 🟢 Indirecta
- **Dónde**: 2.1.9, 9.5, 13.2. (Aceptable: marco → aplicación → conclusión.)

### F3. Telemetría sin seudonimizar en el reentrenamiento 🟡 Directa
- **Dónde**: 9.5.2, 9.6.1, 13.4 (ítem 5).

### F4. Conservación y supresión de datos 🟡 Directa
- **Dónde**: 9.5 (fila Acceso, rectificación y supresión), 9.5.1, 9.6.1, 13.1 (obj. 8), 13.4 (ítem 5).

---

## G. Encuesta y entrevistas

### G1. Cifras de la encuesta reutilizadas en negocio 🟢 Directa (uso legítimo como referencia)
- 47 % criticidad media-alta: 3.6 (intro) ↔ 12.2.
- 41 % adopción improbable: 3.6.7 ↔ 12.4.2.
- 20 % recomendación de proveedores: 3.6.6 ↔ 12.2.
- 17 % costo: 3.6.6 ↔ 12.3.

### G2. "La autenticación se percibe como un evento puntual" 🟡 Directa (dentro de 3.6)
- **Dónde**: 3.6.1, 3.6.2, 3.6.9.

### G3. Respuesta graduada respaldada por la encuesta 🟢 Indirecta
- **Dónde**: 3.6.4, 3.6.9, 4.5.2 (aporte de CU-02).

### G4. Funcionalidades priorizadas = implementadas 🟢 Directa
- **Dónde**: 3.6.5, 3.6.9.

---

## H. Patrones estructurales (redundancia por la forma del documento)

1. **Intro de capítulo + 1.5 "Estructura del documento"**: cada capítulo abre con "Esta sección describe…" y 1.5 ya resume los 13 capítulos. Hay además intros de sección que repiten la del capítulo (p. ej. 2.1 y 2.2 repiten la intro del cap. 2; 10.2 repite la de 10).
2. **Síntesis encadenadas**: 7.7, 8.6, 9.7, 10.11 resumen su capítulo y 13.1/13.2 vuelven a resumir las mismas cifras.
3. **Triple formulación RF → CU → HU**: cada comportamiento aparece como requerimiento (4.3), dentro del flujo del caso de uso (4.5) y como criterio de aceptación (4.6) con el mismo nivel de detalle. Ejemplo: RF-25 ≈ párrafo de 4.5.4 ≈ HU-11.
4. **9.2 vs 4.3**: "Funcionalidades" reescribe en prosa los RF ya tabulados en el cap. 4.
5. **9.6.1 vs 13.4**: casi todas las filas de la tabla de limitaciones reaparecen como ítems de trabajo futuro.
6. **Cap. 5, cada pantalla en dos párrafos**: uno que describe y otro que justifica con RF/RNF; se repite el mismo dato. Ejemplos: los 30 eventos recientes (5.4.3, dos veces); los botones de guardado independientes (5.2, 5.4.6 párr. 1 y 5.4.6 párr. 4); la paleta semafórica y los badges consistentes (5.2, 5.4.2, 5.4.3, 5.4.4, 5.4.5, 5.4.6, 5.4.8 y 10.8.1).
7. **Punto "Actual" provisional / día cerrado**: RF-04, 5.4.3, 9.2.2 (paso 5).

---

## Observaciones colaterales (no son redundancias, pero aparecieron al revisar)

- **"Tres" vs "cuatro" soluciones comerciales**: 11.1.1, 11.2, 11.3 y 11.4 hablan de "las tres soluciones relevadas (Sentinel, Splunk UBA, Exabeam)", pero 2.2.1 y 3.1 relevan cuatro (también Entra ID Protection).
- **Cantidad de niveles**: 4.5.2 (CU-02) dice que la API valida "que la cantidad de niveles sean 4", y RF-13 y HU-06 dicen "entre 3 y 6".
- **Datos de LADOHD**: 2.2.2.2 lo describe sobre 38,9 M eventos de una red comercial de 30 equipos, y 3.3.2 indica el dataset "CMU-CERT r4.2" con detección del 93 % y FP del 4,1 %. Conviene verificarlo contra la fuente.
- **Hariri2019**: 3.3.5 le atribuye "logs NGINX / e-commerce" y métricas concretas que 2.2.2.3 no menciona. Conviene verificarlo.
- **3.2 "Lectura de la matriz"**: cierra con un párrafo sobre el período de aprendizaje (RF-24/25) que no tiene relación con la matriz.
