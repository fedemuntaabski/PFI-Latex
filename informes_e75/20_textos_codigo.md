# E75 / 20: textos del repo de código llevados a la tesis

- Rama: `e75/textos-codigo`, desde `correcciones-e75-latex` (HEAD `71352de`).
- Plan: `documentacion/e75/plan_textos_codigo.md`. Fuentes (solo lectura): informes 02, 04, 05, 11 a 16 del repo de código. Se usaron las cifras del 16 §2 donde difieren del 15 (API 91,56 %, agente 89,34 %, 335 + 177 = 512 pruebas).
- Además del plan, se usó el informe 17 (pegado por el autor durante la sesión) para tres datos: HSTS configurado en el proxy pero sin validar (`[[EN_VIVO]]`), CI verificado en GitHub con los umbrales 75 y 85 sin ajustes, y el CSV de la regresión ya versionado (la regresión no se volvió a correr: sigue con 6 discrepancias).
- Los textos de RF-21 y del gate (CU-03, épica 3, 9.2.4, 10.9) no se tocaron.

## 1. Cambios por capítulo (antes → después)

### Cap. 1, `chapters/chapter01.tex`
- :27 a :55, objetivos específicos 1, 2, 3, 4, 6, 7, 8 y 9 reformulados con los textos de 05 §1, 11 §6 y 13 §7. Objetivo 1: "canal cifrado y autenticado" → TLS, credencial individual y revocable ligada a su identidad, sin respaldo en la admin key. Objetivo 7: "autenticación mutua" → TLS verificado, credencial ligada a identidad y usuarios, sesiones revocables; mTLS como extensión. Objetivo 9: 85 % "de las líneas, medida en la API y en el agente".
- :73, dos `[[CODIGO]]` → `[[EN_VIVO]]`.

### Cap. 4, `chapters/requerimientos.tex`
- :63 RF-02: Parcial → Implementado (texto 11 §6) + `[[EN_VIVO]]`.
- :137 RF-31: estado ampliado con los controles (12 §4).
- :228 RNF-03: Parcial → Implementado (token opaco de 256 bits, 8 h, logout, rol operador 403). La CSP no se implementa: va como limitación.
- :234 RNF-06: Parcial → Implementado (13 §7) + `[[EN_VIVO: prueba manual de revert]]`.
- :248 RNF-13: No implementado → Implementado en el despliegue + `[[EN_VIVO]]`.
- :314 CU-02 flujo 3a y HU-14 (:508): "clave de administrador / control de la interfaz" → token de sesión con rol y vencimiento.
- :575 conteos (ver §2).

### Cap. 7, `chapters/arquitectura.tex`
- :12 (consumidor agente), 211 (decisiones de seguridad del despliegue), :250 y :256 (tabla de despliegue y texto), :290 (claves en encabezados: ya no "expuestas al navegador"), :299 y :305 (HTTPS y "HTTP sin TLS"): alineados con el token de sesión y con el rechazo de `http` fuera de loopback; `[[CODIGO: Prompt C]]` → `[[EN_VIVO]]`.

### Cap. 9, `chapters/producto.tex`
- :122 y :133-138 (tabla 9.II y 9.7): conteos y causa del único parcial (RF-21).
- :142 estado del despliegue: marcador → `[[EN_VIVO]]`.
- Control de acceso (9.2): claves ligadas con identidad y usuarios, token de sesión, roles.
- :165 tabla 9.III, art. 9: marcador reemplazado por los controles del 11 + `[[EN_VIVO]]`. :169 fila de Gemini (12 §5) y se quita el "Pendiente" de prompt injection.
- Tabla 9.IV: actualizadas "Canal sin cifrar" (:229), "Autenticación permisiva" y "Prompt injection" (:245); resueltas y retiradas "Clave de agente no ligada" y "Reversión de permisos amplia" (se mencionan en 9.6.1 y en 10.9); agregadas "Sin mTLS" (:247) y "Sin CSP" (:249, con HSTS como `[[EN_VIVO]]`).
- 9.6.2: reemplazo completo con 12 §5. 9.6 mantiene dos hijos (9.6.1 y 9.6.2).

### Cap. 10, `chapters/pruebas.tex`
- 10.1: dos filas nuevas (E2E PDP→PEP y cobertura).
- 10.2 (:55-115): inventario 306 → 512 pruebas (335 + 177; 32 y 14 archivos, contados en `e75/cobertura`); tabla de resultados con las cifras del 16 §2 (sin columna de duración, que no figura en los informes); se saca "No se mide la cobertura de código…"; CI con cuatro jobs; subsección nueva "Cobertura de código" (:115) con tabla 91,6 % / 89,3 % / 90,9 % de líneas.
- 10.2.4 (:168): RF-18, RF-19, RF-22 y RF-31 a "Prueba automatizada"; RF-26 a "Prueba parcial"; RNF-13 deja de ser "No implementado"; se elimina la fila "Sin prueba registrada".
- 10.3: texto del 14 §9 de la prueba E2E automatizada.
- 10.5 (:259, :326): "92 eventos reales" → CLUE-LDS con 27 duplicados (04 §5 aviso 1); Pearson −0,22 (234 usuarios, p < 0,001) más la nota de los 15 usuarios.
- 10.6 (:376-389): las 3 detecciones (04 §3), aclaración de que 14,3 % / 21,6 % son por nivel con regla de piso (14,2 % por puntaje), curva completa (04 §4) y figura reemplazada.
- 10.9 (:607): cuatro filas nuevas (seguridad B, reversión precisa, controles de Gemini, cobertura).
- 10.10: la regresión sigue con 6 discrepancias (14 §5); se saca la limitación de cobertura no medida y la de requerimientos sin prueba; se mantiene la del frontend como declaración; se agregan RF-26 y RNF-13 sin prueba automatizada.
- Síntesis: 306 → 512 pruebas con cobertura.

### Cap. 13, `chapters/conclusiones.tex`
- Tabla 13.I (:24-65): estado y evidencia de los 9 objetivos, coherentes con el cap. 1. 1 y 7: Cumplido con la verificación en la nube pendiente; 2: Parcial con cifras del 04; 3: aclaración de medición; 4 y 9: Cumplido; 6: Parcial con `[[GATE]]`; 5 y 8 sin cambio.
- Conteo (:69) y 13.4: se sacan "reversión acotada" y "requerimientos sin prueba"; se actualiza "Pruebas" (frontend, métricas de la promoción, latencia con Redis real); nuevo ítem "Seguridad" (mTLS con el diseño del 02 §5, CSP, IdP real); ítem de la redacción asistida actualizado.

### Bibliografía y figura
- `biblio.bib`: `Rose2020` y `Hu2014` pasan a `@TechReport` (sin `JOURNAL`, `institution` con llaves dobles, `number` SP 800-207 / SP 800-162).
- `images/pruebas/curva_umbral.pdf` reemplazada por `curva_umbral_completa.pdf` del repo de código (MD5 `1479a47ee9488a1b012f4da07d729ff1` en ambos).

## 2. Conteos de requerimientos

| Dónde | Antes | Después |
|---|---|---|
| RF (cap. 4 :575, tabla 9.II, 9.7, 13.1) | 29 implementados, 2 parciales (RF-02, RF-21) | 30 implementados, 1 parcial (RF-21) |
| RNF (cap. 4, 9.7, 13.1) | 9 implementados, 5 parciales (RNF-03, 05, 06, 09, 11), 1 no implementado (RNF-13) | 12 implementados, 3 parciales (RNF-05, 09, 11), 0 no implementados |

## 3. Marcadores que quedan

Todos los `[[CODIGO…]]` se reemplazaron por texto o pasaron a `[[EN_VIVO…]]`.

| Marcador | Dónde | Dato que falta |
|---|---|---|
| `[[EN_VIVO: estado del despliegue de la instancia]]` | cap. 1 :73 | Estado final de la instancia el día de la demo |
| `[[EN_VIVO: verificación de punta a punta con un agente real]]` | cap. 1 :73, cap. 7 :299 y :305, 9.6.1 :229 | Evento de un agente real contra la EC2 por HTTPS con key con `--uid` |
| `[[EN_VIVO: evento de un agente en la instancia e inicio de sesión…]]` | cap. 7 :250 y :256, 9.5 :142 | Evento recibido en la instancia y login en el dashboard desplegado |
| `[[EN_VIVO: verificación con un agente real contra la instancia (en la nube)]]` | cap. 4 :63, 9.7 :138 | RF-02: ídem |
| `[[EN_VIVO: verificación de punta a punta con un agente real]]` | cap. 4 :248 | RNF-13 |
| `[[EN_VIVO: prueba manual de revert]]` | cap. 4 :234, 13.1 :42 | Resultado PASS de la prueba manual de icacls (13 §5) |
| `[[EN_VIVO: verificación de TLS, inicio de sesión y claves de agente…]]` | 9.3 :165, 13.1 :55 | Login admin/operador, token de 43 caracteres, logout 401, rechazos 403 |
| `[[EN_VIVO: HSTS activo en la instancia]]` | 9.6.1 :249 | Despliegue y validación del Caddyfile con HSTS |
| `[[GATE: estado según el criterio de promoción que se entregue]]` | 13.1 :48 (objetivo 6) | Decisión sobre qué gate se entrega (depende de otro merge) |

## 4. BLOQUEOS (decisiones del autor)

1. **Objetivo 6 / gate.** La fila de la tabla 13.I queda "Parcial" con `[[GATE]]`; el estado final depende del gate de RF-21, que no se tocó.
2. **Objetivo 4 "Cumplido".** El informe 13 lo supedita a la prueba manual de icacls (`[[EN_VIVO]]`). Si la prueba no da PASS, hay que volver a "Parcial".
3. **Total combinado de la tabla de cobertura.** Los informes 15 y 16 no dan el total combinado de líneas y ramas con las cifras finales; la celda queda en "--" para no inventarlo.
4. **Inventario.** Se contaron los archivos de test en la rama `e75/cobertura` (solo lectura); los informes no los informan. Se quitó la cifra de 204 funciones de prueba por no tener equivalente actualizado.
5. **Tabla de resultados 10.2.2.** Se quitó la columna de duración (no figura en los informes).
6. **Fecha de la ejecución** de la tabla de resultados: 9 de octubre de 2026 (fecha del informe 16).
7. **Cifra de la API.** El informe 17 mide 326 pruebas con el comando del CI en una máquina con artefactos; se usó la del 16 §2 (311 + 15 omitidas, sin artefactos).

## 5. Compilación

`latexmk -pdf -interaction=nonstopmode -outdir=build main.tex` termina sin errores (rc=0); `grep -c undefined build/main.log` = 0; `pdftotext` sin "??", sin "92 eventos reales", "No se mide la cobertura" ni "control de la interfaz". Los marcadores se escriben `[[EN\_VIVO…]]` en el fuente (el guion bajo hay que escaparlo en LaTeX).
