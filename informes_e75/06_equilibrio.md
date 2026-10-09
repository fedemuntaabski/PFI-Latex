# E75 — Punto de equilibrio frente a la adopción proyectada (sección 12.4)

## Datos usados y origen

Fuente principal: `documentacion/e75/modelo_financiero.py`, el diccionario `SUPUESTOS`. Es el script que genera las tablas 12.III a 12.VI. Lo volví a correr (`python modelo_financiero.py --latex`) y su salida coincide exactamente con las tablas del capítulo.

| Dato | Valor | Origen |
|---|---|---|
| Costo fijo mensual del equipo, años 1 a 5 | USD 3.500, 6.000, 9.000, 11.000 y 12.000 | `fijo_mensual_por_anio` |
| Infraestructura base de nube | USD 250 por mes, todos los años | `infra_fija_mensual` |
| Margen de contribución por cliente | USD 282,60 por mes (el texto lo redondea a USD 283) | `margen_contribucion_cliente()`: ingreso de USD 390 × (1 − 0,03 − 0,03 − 0,5 × 0,20) − 75 × 0,60 |
| Clientes activos al cierre de cada año | Pesimista 5/14/30/41/49; base 11/41/86/132/168; optimista 22/74/150/236/307 | Tabla 12.III (`tab:clientes-fin`), igual a la salida del script |

El costo fijo de los años 2 a 4 **sí existe** en el script, así que no hizo falta omitir ningún año. La tabla 12.II del texto solo nombra los extremos (USD 3.500 y USD 12.000).

## Cálculos

Punto de equilibrio = ⌈(costo fijo del equipo + 250) / margen de contribución⌉. Da el mismo entero con 282,60 que con 283.

| Año | Costo fijo total (USD/mes) | / 282,60 | / 283 | Equilibrio (hacia arriba) |
|---|---|---|---|---|
| 1 | 3.750 | 13,27 | 13,25 | 14 |
| 2 | 6.250 | 22,12 | 22,08 | 23 |
| 3 | 9.250 | 32,73 | 32,69 | 33 |
| 4 | 11.250 | 39,81 | 39,75 | 40 |
| 5 | 12.250 | 43,35 | 43,29 | 44 |

Clientes al cierre frente al equilibrio (✔ = lo alcanza o lo supera):

| Año | Equilibrio | Pesimista | Base | Optimista |
|---|---|---|---|---|
| 1 | 14 | 5 | 11 | 22 ✔ |
| 2 | 23 | 14 | 41 ✔ | 74 ✔ |
| 3 | 33 | 30 | 86 ✔ | 150 ✔ |
| 4 | 40 | 41 ✔ | 132 ✔ | 236 ✔ |
| 5 | 44 | 49 ✔ | 168 ✔ | 307 ✔ |

**Mes en que se llega al equilibrio.** Simulé mes a mes con la misma lógica que `simular()`: clientes = clientes × (1 − abandono) + altas. Comparé los clientes de cada mes con el equilibrio de ese año:

- **Optimista:** mes 8 (año 1). Desde ahí se mantiene por encima en todo el horizonte.
- **Base:** mes 17 (quinto mes del año 2). Desde ahí se mantiene por encima.
- **Pesimista:** mes 47 (año 4). En el mes 49 vuelve a caer por debajo, porque el equilibrio sube de 40 a 44 con el costo fijo del año 5, y recién lo recupera en el mes 52.

Promedio de clientes activos en el año, que es la base que usa el flujo: pesimista 2,9 / 10,0 / 23,0 / 36,4 / 45,6; base 6,0 / 27,6 / 66,0 / 111,7 / 152,2; optimista 12,3 / 50,9 / 116,2 / 197,7 / 275,5.

Costo de adquisición anual: base año 2 = 3 × 12 × 1.500 = USD 54.000; pesimista años 4 y 5 = 2 × 12 × 2.500 = USD 60.000.

## Texto agregado o modificado (`chapters/negocio.tex`)

**12.4.3 (Indicadores).** Cambié la frase existente de 13 y 43 a 14 y 44, con tu OK (ver "Inconsistencias"), y agregué:

> La tabla 12.VII calcula el equilibrio de cada año como el costo fijo mensual dividido por el margen de contribución, redondeado hacia arriba, y lo compara con los clientes activos al cierre del año en cada escenario. En negrita figuran los valores que alcanzan o superan el equilibrio.

**Tabla 12.VII.** Etiqueta `tab:equilibrio-fin`; epígrafe "Punto de equilibrio operativo frente a los clientes activos al cierre de cada año".
- Columnas: Año, Costo fijo mensual (USD), Equilibrio, Pesimista, Base y Optimista.
- Lleva "Fuente: elaboración propia a partir del modelo financiero.".
- Aparece en la lista de tablas (`build/main.lot`, página 164).
- Va después de la 12.VI, así que no renumera las tablas 12.III a 12.VI.

**12.4.4 (Interpretación).** Párrafo nuevo, entre el párrafo de los indicadores y el de la regla de decisión:

> La comparación con la adopción proyectada (tabla 12.VII) muestra en cuánto tiempo se llega al equilibrio. En el escenario optimista se alcanza en el octavo mes y el primer año cierra con 22 clientes frente a 14. En el base se alcanza en el mes 17, es decir, a mitad del segundo año, que cierra con 41 clientes frente a 23. En el pesimista recién se alcanza en el cuarto año (41 frente a 40) y en el quinto queda apenas por encima (49 frente a 44). Que los flujos sigan negativos después de superar el equilibrio es coherente con el modelo, por dos razones. Primero, el equilibrio es operativo: no incluye el costo de adquisición ni el impuesto a las ganancias. Segundo, la tabla compara los clientes al cierre del año, mientras que el flujo se calcula con la base de clientes de cada mes. En el escenario base, el segundo año tiene en promedio 28 clientes activos y USD 54.000 de costo de adquisición, por lo que el flujo todavía es negativo y la necesidad de fondos llega a USD 100.894; desde el tercer año, la base supera con holgura el equilibrio y el flujo pasa a ser positivo. En el pesimista, aun por encima del equilibrio, los USD 60.000 anuales de adquisición de los años 4 y 5 no se cubren, y por eso la inversión no se recupera y la necesidad de fondos acumula USD 360.837. Llegar al equilibrio en algo menos de un año y medio, como en el escenario base, es razonable para una suscripción que depende de un canal de MSSP que recién empieza a aportar clientes en el segundo año; llegar recién en el cuarto año, como en el pesimista, no lo es, y es el caso que la regla de decisión del párrafo siguiente busca detectar a tiempo.

## Verificación de coherencia con las tablas 12.III, 12.IV y 12.V

- **12.III (clientes):** los clientes de la tabla 12.VII son los mismos de la 12.III.
- **12.IV (flujos):**
  - Base: el año 2 sigue negativo (−35.398) aunque cierra por encima del equilibrio, y el año 3 es positivo (17.228). Coincide con la explicación del párrafo (promedio del año 2 de 27,6 clientes, más USD 54.000 de adquisición).
  - Optimista: el año 1 es negativo (−27.251) aunque cierra por encima, porque su promedio es de 12,3 clientes, por debajo de 14. El año 2 ya es positivo.
  - Pesimista: los 5 años son negativos, porque el margen sobre el equilibrio en los años 4 y 5 (como mucho 1 a 5 clientes, unos USD 17.000 al año) no cubre los USD 60.000 de adquisición.
- **12.V (indicadores):**
  - Necesidad base: 23.000 + 42.496 + 35.398 = 100.894 ✔.
  - Necesidad optimista: 23.000 + 27.251 = 50.251 ✔.
  - Necesidad pesimista: la suma de los valores redondeados da 360.838 y la tabla dice 360.837. Es una diferencia de redondeo, porque el script suma los valores sin redondear; no es un error.
  - El payback base de 3,8 años y el optimista de 2,2 años son compatibles con los años en que se supera el equilibrio.
- Compilación: `latexmk` sin errores; `build/main.pdf` tiene 245 páginas. Rasterizado de la página 164: la tabla entra en el ancho de texto, con las negritas y la fuente bien.

## Inconsistencias encontradas

1. **"13 clientes" y "43 clientes" en 12.4.3.** El modelo da 13,3 y 43,3: el texto truncaba en lugar de redondear hacia arriba, y con 13 clientes no se cubren los USD 3.750 de costo fijo (13 × 282,60 = 3.674). **Corregido a 14 y 44 con tu aprobación.**
2. **Expectativa sobre el escenario pesimista.** El pedido sugería que el pesimista quizás nunca alcanza el equilibrio, pero lo alcanza en el año 4 (41 clientes frente a 40, al cierre). No es un error del documento; el párrafo lo explica y aclara por qué los flujos siguen negativos.
3. **Costo fijo de los años 2 a 4.** La tabla 12.II solo da los extremos (USD 3.500 y USD 12.000). Los valores intermedios (6.000, 9.000 y 11.000) ahora se ven en la tabla 12.VII, sumados los USD 250 de nube, y salen del script. No hay contradicción, pero si querés que la 12.II los detalle, hay que agregarlos ahí.
4. **Necesidad de fondos pesimista:** 360.837 frente a 360.838, por redondeo (ver arriba). No se tocó.
