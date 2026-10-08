# P4 — Desarrollo del negocio (T16, T17, T18, T22)

Fecha: 08/10/2026. Rama `e75/paquete`. Sin push.

## 1. Ubicación y commits

- Capítulo nuevo `chapters/negocio.tex`, `\label{chap:negocio}`, incluido en `main.tex` con
  `\input{chapters/negocio}` inmediatamente después de `\input{chapters/e50_mercado}`. Queda como
  **capítulo 12** (12.1 Cliente, usuario y pagador; 12.2 Lienzo; 12.3 Monetización; 12.4 Viabilidad
  económico-financiera, `sec:viabilidad-fin`; 12.5 Identidad de marca).
- `biblio.bib`: `@book{Osterwalder2010}` agregado después de `Henderson1970`, mismo formato.
- 11.1.2 (Precio): remisión a la sección~12.4 al final.

| Commit | Bloque |
|---|---|
| `53a9ace` | T16 + `Osterwalder2010` + `\input` |
| `61f38f5` | T17 + cuatro tablas del modelo |
| `f670825` | T18 + figura del logo |
| `31e5bcf` | Remisión en 11.1.2 |
| (este) | Informe |

Compilación tras cada bloque (pdflatex, biber, pdflatex ×2): 0 errores, 0 referencias o citas
indefinidas, sin "??" en el PDF, 0 `Overfull \hbox` en todo el documento. Los `Overfull \vbox
(36.8594pt too high)` son del encabezado de página y aparecen en todas las páginas desde antes.
Queda un `Underfull \hbox` (badness 7613) en `negocio.tex:41` (celda "Fuentes de ingresos" del
lienzo, justificación de la columna `p{}`); no afecta la lectura.

## 2. Ajustes aplicados respecto de textos_e75.md

- T16: 1a (47 % / 112 participantes), 1b (frase del canal, 20 %), 1d (`Osterwalder2010`);
  `sec:encuesta` → `sec:encuesta-usuarios`; `cap:negocio` → `chap:negocio`; `\fuente{...}` →
  `{\small Fuente: ...\par}`.
  Nota de redacción (sin cambio, el texto pedido es literal): la celda queda "en la encuesta, el
  47 % de la base efectiva de la encuesta (...)"; "encuesta" se repite.
- T17: `\label{sec:viabilidad-fin}`; celda de tasa reemplazada completa (sin `[[VERIFICAR]]`);
  párrafo de acumulación después de la tabla de supuestos.
- Encabezados de las tablas nuevas (incluidos los dos `longtable` de T16/T17) en `\textbf{}`, como
  en el resto del documento.
- Signo menos de los flujos como `$-$` (los números son los del script, sin cambios).
- Referencias a las tablas: en "Escenarios" (`tablas~\ref{tab:clientes-fin} y~\ref{tab:flujos-fin}`,
  en la primera oración). Las de `tab:indicadores-fin` y `tab:sensibilidad-fin` quedaron en
  "Interpretación", porque la subsección "Indicadores" solo tiene el párrafo del punto de equilibrio,
  que no usa esas tablas; "Interpretación" es donde se citan el VAN, la TIR y el VAN al 35 %.
- T18: `[H]` → `[h]` + `\FloatBarrier`; `figuras/` → `images/`; se antepuso "La
  figura~\ref{fig:logo} presenta el logotipo del producto." al párrafo del logotipo.

## 3. Tablas insertadas

| N.º | Etiqueta | Título | Formato |
|---|---|---|---|
| 12.I | `tab:canvas` | Lienzo del modelo de negocio | `longtable` (T16) |
| 12.II | `tab:supuestos-fin` | Supuestos del análisis económico-financiero | `longtable` (T17) |
| 12.III | `tab:clientes-fin` | Clientes activos al cierre de cada año por escenario | `table[h]`, `lrrrrr` |
| 12.IV | `tab:flujos-fin` | Flujo neto de fondos por escenario (USD) | `table[h]`, `lrrrrrr` |
| 12.V | `tab:indicadores-fin` | Indicadores económico-financieros por escenario | `table[h]`, seis columnas `p{}` alineadas a la derecha, encabezados en dos o tres líneas |
| 12.VI | `tab:sensibilidad-fin` | Sensibilidad del VAN a la tasa de descuento (USD) | `table[h]`, `lrrr` |
| Fig. 12.1 | `fig:logo` | Logotipo del producto | `figure[h]`, `images/logo_umbral.png` |

Las tablas III a VI salen de `python -I documentacion/e75/modelo_financiero.py --latex`; todas
llevan "Fuente: elaboración propia a partir del modelo financiero." y `\FloatBarrier`.
Después de `\end{tabular}` se agregó `\par`: sin él, en una tabla más angosta que la caja de
texto, la línea de fuente queda en el mismo renglón que la tabla.
**Aviso (fuera de alcance, sin cambios):** `tab:metas-modelo` (`chapters/pruebas.tex:224`) tiene
la misma estructura sin `\par`; hoy no se ve porque la tabla ocupa todo el ancho.

## 4. Verificación de números (salida de `modelo_financiero.py` sin `--latex`)

| Dato | Texto (cap. 12) | Script / cálculo | Estado |
|---|---|---|---|
| Inversión inicial | USD 23.000 | 23.000 | ✓ |
| Ingreso por cliente | USD 390 (USD 5,20 × 75) | 390 (5,20 por equipo) | ✓ |
| Margen de contribución | USD 283 | 283 (282,6) | ✓ |
| LTV | 283 / 0,02 = 14.150 | 14.150 | ✓ |
| LTV/CAC | 9,4 | 14.150 / 1.500 = 9,43 | ✓ |
| Recupero del CAC | 5,3 meses | 1.500 / 283 = 5,30 | ✓ |
| Punto de equilibrio año 1 | 13 clientes | 13,3 | ✓ |
| Punto de equilibrio año 5 | 43 clientes | 43,3 | ✓ |
| Clientes por USD 1.000 de fijo | "entre tres y cuatro" | 1.000 / 282,6 = 3,5 | ✓ |
| Base: VAN al 25 % | USD 35.084 | 35.084 | ✓ |
| Base: TIR | 38,8 % | 38,8 % | ✓ |
| Base: payback simple | 3,8 años | 3,8 | ✓ |
| Base: payback descontado | 4,5 años | 4,5 | ✓ |
| Base: VAN al 35 % | USD 7.456 | 7.456 | ✓ |
| Base: dos primeros años negativos | sí | −42.496; −35.398 | ✓ |
| Base: necesidad de fondos | USD 100.894 | 100.894 (= 23.000 + 42.496 + 35.398) | ✓ |
| Pesimista: no recupera | sí | payback "no recupera" | ✓ |
| Pesimista: necesidad de fondos | USD 360.837 | 360.837 | ✓ |
| Optimista: VAN | USD 336.532 | 336.532 | ✓ |
| Optimista: payback | 2,2 años | 2,2 | ✓ |
| Supuestos de escenarios (altas, abandono, CAC) | texto de 12.4.2 | `escenarios` del script | ✓ |

No hay inconsistencias entre el script y el texto. No se modificó ningún supuesto.

Porcentajes de la encuesta contra el capítulo 3:

| Dato | Cap. 12 | Cap. 3 | Estado |
|---|---|---|---|
| Base efectiva | 112 participantes | 112 respuestas (3.6, `chapter04.tex:445`) | ✓ |
| Criticidad media-alta o alta | 47 % | 47 % (3.6) | ✓ |
| Recomendación de proveedores | 20 %, factor más mencionado | 20 %, el mayor (3.6.6, `chapter04.tex:485`) | ✓ |
| Costo como factor de adopción | 17 % | 17 % (3.6.6) | ✓ |
| Adopción improbable | 41 % | 41 % (3.6.7, `chapter04.tex:489`) | ✓ |

Observación: los seis factores de adopción del 3.6.6 suman 101 %; el cap. 3 los presenta como
porcentaje de participantes y el cap. 12 sigue ese criterio. Conviene confirmar en el formulario si
la pregunta era de opción única (redondeo) o múltiple (porcentaje sobre selecciones).

## 5. Tasa de descuento: DGS10

Consulta a FRED (`fredgraph.csv?id=DGS10`) el 08/10/2026:

| Fecha | DGS10 |
|---|---|
| 01/10/2026 | 5,24 |
| 02/10/2026 | 5,28 |
| 05/10/2026 | 5,31 |
| 06/10/2026 | 5,27 |
| 07/10/2026 | sin publicar todavía |

El valor del 07/10 no estaba disponible. Contra el último publicado (5,27), el texto (5,35)
difiere en 0,08 puntos, por debajo del umbral de 0,1: **no se ajustó**. Ningún día de octubre
llegó a 5,35 (máximo 5,31); si al publicarse el 07/10 la diferencia supera 0,1, cambiar
"5,35" por el valor publicado. Con EMBI de 573 a 650 pb, la suma da 11,0 % a 11,8 %, coherente con
"entre el 11 % y el 12 %". El EMBI no se verificó.

## 6. Color del logo

| Dato | Resultado |
|---|---|
| a. Capítulo 5 (paleta del panel) | `e50_diseno_ux.tex:84` y `:324` (5.x "Decisiones de diseño transversales") solo dicen que el nivel de riesgo se codifica con un *badge* de color por nivel (bajo/medio/alto/crítico) y que la paleta es consistente entre pantallas. **No nombra ningún color** ni dice cuál corresponde al nivel intermedio. |
| b. Colores dominantes de `images/logo_umbral.png` (píxeles opacos) | `#0F2A44` azul oscuro (71.045 px), `#FFFFFF` blanco (4.088), `#4A5B6C` gris azulado (3.008), `#F2B233` amarillo ámbar (2.101). Coincide con los `fill`/`stroke` de `logo_umbral.svg`. |
| c. Decisión | El documento no lo dice: **se dejó el `[[VERIFICAR]]`**. Para cerrarlo, describir en el cap. 5 los colores reales de los *badges* (o sacarlos del código del *dashboard*) y, si el nivel medio es amarillo/ámbar, borrar el marcador. |

## 7. Coherencia del capítulo 11 (solo informe, sin cambios)

| Ubicación (cap. 11) | Frase | Contradice | Detalle |
|---|---|---|---|
| 11.1.3 Plaza, "Modalidad de despliegue" | "Despliegue 100\% *cloud-native*: la API y las bases de datos (...) funcionan como servicios gestionados en la nube" | 7.5, 9.4 | Solo se verificó el despliegue local (agente, API y panel en un equipo Windows). La nube está aplicada en forma parcial, sin red de distribución ni TLS ni acceso operativo para usuarios finales (7.5.2, `arquitectura.tex:249`). La API no corre como servicio gestionado en el camino verificado. |
| 11.1.1 Producto, "Diferencial" | "bloquear el acceso, aislar el proceso" y, en el ítem de Splunk, "ejecuta la acción (restricción de permisos, aislamiento del proceso)" | 9.2.1 | Las acciones implementadas son `alertar`, `terminar_procesos`, `denegar_carpeta`, `terminar_y_denegar` y `suspender_proceso` (`producto.tex:52-56`). No hay aislamiento de procesos ni bloqueo del acceso a la sesión. |
| 11.1.1, ítem Sentinel | "el sistema puede exponer la razón concreta de cada alerta en la notificación generada por IA" | 7.4, 9.2, 9.6 | La explicación cubre solo las tres variables de Isolation Forest; un puntaje impulsado por el LSTM no identifica la causa (limitación en 9.6, `producto.tex:199`). Gemini es opcional y tiene un texto predefinido de respaldo (`arquitectura.tex:183`). Afecta también al lienzo del cap. 12 ("con explicación de cada alerta"). |
| 11.2.1 Fortalezas | "Notificaciones con explicación generada por IA en el momento de la alerta" | 7.4, 9.6 | Igual que la fila anterior. |
| 11.2.1 Fortalezas | "Arquitectura Zero Trust real (PDP/PEP, NIST SP 800-207)" | 7.6, 9.6 | En el entorno verificado el canal agente-API es HTTP sin TLS y sin autenticación mutua (RNF-13 no implementado, `arquitectura.tex:296`); la API acepta solicitudes sin autenticar si no hay claves configuradas (`producto.tex:217`). "Real" es más fuerte que lo verificado. |
| 11.2.3 Oportunidades | "integrarse como complemento de soluciones IAM existentes" | 9.6 | El adaptador de Keycloak está probado solo con un proveedor simulado (`producto.tex:221`). Es una oportunidad, no una afirmación de estado, pero conviene no presentarla como capacidad disponible. |
| 11.1.3 Plaza, "Canales" | "Distribución digital directa, con alta *self-service*" | 12.4.1 | El cap. 12 incluye en la inversión inicial el "pasaje del prototipo a producto (instalador, firma de código, endurecimiento)": hoy el alta autogestionada no existe. Si se redacta en presente, contradice el estado actual; en futuro, es consistente. |

No se encontraron contradicciones numéricas entre el cap. 11 y el 12: los rangos de precio
(Business USD 2-5, Enterprise USD 6-10) contienen los precios del modelo (USD 4 y USD 8), y el
segmento de 50 a 100 equipos contiene el cliente de referencia de 75.
