# P5 — Conclusiones y trabajo futuro (T19)

Fecha: 08/10/2026. Rama `e75/paquete`.

## 1. Cambios aplicados

- `chapters/conclusiones.tex` (nuevo): bloque T19 como capítulo 13 (`\label{chap:conclusiones}`).
  Adaptaciones: `cap:conclusiones` → `chap:conclusiones`; `sec:cumplimiento-requerimientos` →
  `sec:cumplimiento`; `\fuente{Elaboración propia.}` → `{\small Fuente: elaboración propia.\par}`
  inmediatamente después de `\end{longtable}`. Los `[[CODIGO]]` quedan visibles.
- `main.tex`: `\input{chapters/conclusiones}` después de `chapters/negocio` y antes de la
  bibliografía. El `%\input{chapters/conclusion}` de la plantilla queda como estaba.
- `chapters/producto.tex` (síntesis 9.7) y `chapters/pruebas.tex` (síntesis 10.10): se agrega
  "(capítulo~\ref{chap:conclusiones})" al final de la frase que menciona el trabajo futuro.
- Dos redacciones de T19 ajustadas porque el documento no las respaldaba tal como estaban (sección 3).

Compilación: `pdflatex`, `biber`, `pdflatex` ×2, sin errores ni referencias indefinidas.
Numeración en `main.aux`: `chap:conclusiones` = 13, `tab:cumplimiento-objetivos` = 13.I.

## 2. Tabla de verificación

| Número o afirmación en T19 | Sección y tabla donde aparece | Coincide |
|---|---|---|
| p95 de 14,9 ms y p99 de 148,9 ms (RNF-01) | 10.4.1, tabla 10.V (`tab:rnf01`): 14,91 / 148,87 ms; tabla 10.VII (14,9 ms); tabla de RNF del cap. 4 (RNF-01: 14,9 / 148,9 ms) | Sí (redondeo a un decimal) |
| 13,3 % (2 de 15) en el escenario combinado con umbral 70 | Tabla 10.VII (`tab:metas-modelo`); tabla 10.IX (`tab:escenarios`), E4: 2 atribuibles | Sí |
| 16,8 % de días sin ataque en nivel alto | 10.6.2 (texto) y tabla 10.VII | Sí |
| "15 usuarios" | 10.6.1 (método) y título de la tabla 10.IX | Sí |
| "la detección atribuible nunca supera un tercio de los usuarios en ningún umbral" | 10.6.3: "nunca supera un tercio de los usuarios", máximo de 33,3 % (E4, umbral 55) | Sí |
| "cumple 1 de las 5 metas de comportamiento y detección, y la de latencia" | Tabla 10.VII: 6 metas; de las 5 que no son de latencia solo cumple la tasa del LSTM (3,99 %); la de latencia cumple | Sí |
| 30 RF: 28 implementados y 2 parciales | 9.3, tabla 9.II (`tab:cumplimiento-cu`), fila Total; también `requerimientos.tex` (síntesis del cap. 4) | Sí |
| 15 RNF | 9.3: "De los 15 requerimientos no funcionales" (8 + 5 + 1 + RNF-02 pendiente) | Sí |
| "seis acciones configurables por nivel" | RF-08 (cap. 4): 6 acciones, pero `notificar_admin` no se ejecuta en el agente; 9.2.1 lista 5 acciones del agente | **Parcial**: ver 3.1 |
| "cuatro problemas mayores corregidos" | 10.7.1 (4 mayores, todos "Corregido" en la tabla 10.X) y 10.7.2 | Sí |
| "la única corrida real del reentrenamiento produjo un modelo peor que el vigente, que no se promovió" | **No está en 9.2.4** (solo describe el mecanismo). Sí en 9.3 ("la única corrida real del planificador produjo un modelo peor que el vigente"), 10.3 (LSTM 0,1155 → 0,1175, no promovió), tabla 10.XI y RF-21 (cap. 4) | Sí (respaldo en 9.3 y 10.3) |
| "casi todos los eventos tienen el país sin registrar" | 10.6.4: el 99,946 % de los eventos tiene el país "registrado como desconocido" | Sí en cifra; se ajusta la redacción (3.2) |
| VAN de USD 35.084 al 25 % | 12.4, tabla 12.V (`tab:indicadores-fin`), escenario base; `modelo_financiero.py` (p0) | Sí |
| Metas $\leq$ 500 ms y cobertura $\geq$ 85 % (objetivos 3 y 9) | RNF-01; T2, objetivo 9. La cobertura no se midió (10.2.2), por eso el objetivo 9 queda `[[CODIGO]]` | Sí (son metas, no resultados) |

## 3. Afirmaciones sin respaldo y redacción aplicada

### 3.1 Objetivo 4: seis acciones

- T19: "Seis acciones configurables por nivel (RF-07, RF-08) verificadas en el equipo".
- Problema: RF-08 define 6, pero `notificar_admin` "no ejecuta ninguna acción en el agente", por
  lo que no se pueden verificar seis en el equipo.
- Aplicado: "Catálogo de seis acciones configurables por nivel (RF-07, RF-08); la ejecución real de
  las mitigaciones en el equipo se verificó en forma manual (sección 10.3)". Respaldo: tabla 10.IV
  (RF-08, verificación manual) y 10.9.

### 3.2 Causas de la baja detección

- T19: "Las causas identificadas son la granularidad diaria…; la longitud de las secuencias…; y un
  conjunto de entrenamiento en el que casi todos los eventos tienen el país sin registrar".
- Problema: 10.6.4 dice que solo la del país está verificada y que las demás son inferidas.
- Aplicado: "Entre las causas, la única verificada es que casi todos los eventos del conjunto de
  entrenamiento tienen el país registrado como desconocido, lo que impide detectar el cambio de
  país; las demás son inferidas: la granularidad diaria…, y la longitud de las secuencias del LSTM."

## 4. Limitaciones (9.6 y 10.9) frente al trabajo futuro de T19

### 4.1 Cubiertas

| Limitación | Origen | Ítem de trabajo futuro |
|---|---|---|
| Sensibilidad baja ante ataques cortos | 9.6 | 1 (detección) |
| Evaluación sin etiquetas; 15 usuarios y escenarios propios | 10.9 | 1 (escenarios etiquetados más amplios) |
| Transferencia de dominio del conjunto de datos | 9.6 | 2 (datos propios) |
| Explicación solo de Isolation Forest | 9.6 | 3 (explicabilidad del LSTM) |
| Sin plazo de conservación de datos | 9.6 | 4 (conservación) |
| Canal sin cifrar; clave de agente no ligada; clave de administración en el navegador | 9.6 | 6 (`[[CODIGO]]` de seguridad) |
| Keycloak sin validación real | 9.6 y 10.9 | 6 (`[[CODIGO]]`, proveedor de identidad real) |

### 4.2 Sin ítem y no resueltas: propuestas (no insertadas)

| Limitación | Origen | Propuesta de ítem |
|---|---|---|
| Reversión de permisos amplia | 9.6, que la declara **"Trabajo futuro"**: es la única contradicción directa | **Reversión acotada**: registrar las entradas de denegación que crea el agente y revertir solo esas. |
| Suspensión fallida informada como ejecutada; envío con el circuit breaker abierto | 9.6 ("corrección prevista en el agente") | **Correcciones del agente**: informar como fallida la suspensión que no se pudo registrar y no intentar envíos nuevos con el circuit breaker abierto. |
| Sesgo de la línea base personal en usuarios con poco historial | 9.6 (solo se documenta); tabla 10.XI | Agregar al ítem 1: "y revisar el componente personal en usuarios con historial escaso". |
| Regresión con una sexta diferencia sin causa; sin cobertura de código; frontend sin pruebas; RF-18, RF-19, RF-22 y RF-26 sin prueba; mitigaciones sin prueba automatizada | 10.9 | **Pruebas**: medir la cobertura de código, agregar pruebas al frontend y a los cuatro RF sin prueba, automatizar la verificación de mitigaciones y atribuir la sexta diferencia de la regresión. |
| Latencia medida con Redis en memoria y sin concurrencia | 10.9 | Agregar a Pruebas: medir la latencia con el Redis gestionado y varios agentes concurrentes. |

### 4.3 Aceptadas por diseño (sin ítem)

- Cobertura parcial prolongada (19,6 % de usuarios): comportamiento previsto (RF-03); el ítem 1
  ("secuencias más cortas o solapadas") la toca en parte.
- Terminación de procesos irreversible y repetida: reservada para el nivel crítico por política.
- Captura por sondeo: inherente al diseño sin controladores del sistema operativo.

### 4.4 Otras diferencias

- Objetivo 6, estado "Cumplido; promoción no observada", contra RF-21 "Parcial" en 9.3 y en el
  cap. 4. No se cambió; decidir si pasa a "Parcial".
- Objetivo 4 "Cumplido con limitación" y RNF-06 "Parcial": coherentes (misma causa).
- 9.6 trata el canal sin cifrar como "previsto mediante la red de distribución con TLS"; T19
  (objetivos 1 y 7) lo deja en `[[CODIGO]]`. Unificar cuando cierre el trabajo de código.

## 5. Marcadores pendientes en `chapters/conclusiones.tex`

1. Obj. 1: `[[CODIGO: TLS y autenticación mutua]]`, `[[CODIGO: RNF-02]]`, estado `[[CODIGO]]`.
2. Obj. 2: `[[CODIGO: actualizar si se reentrena]]`.
3. Obj. 7: `[[CODIGO: resultado de seguridad]]`, estado `[[CODIGO]]`.
4. Obj. 9: `[[CODIGO: cantidad de pruebas y cobertura]]`, estado `[[CODIGO]]`.
5. Conteo de RNF: `[[CODIGO: actualizar conteo con RNF-02, RNF-03 y RNF-13]]`.
6. Resultados: `[[CODIGO: actualizar si el reentrenamiento cambia los resultados.]]`
7. Trabajo futuro, ítem 6: `[[CODIGO: limitaciones de seguridad … proveedor de identidad real.]]`

Dependencias en otros capítulos: RNF-02 (`[[ESTADO SEGÚN RNF-02]]` en 9.3 y cap. 4; tabla 10.VI),
`[[DECIDIR]]` sobre las metas de la tabla 10.VII (si cambian, revisar "1 de las 5 metas").
