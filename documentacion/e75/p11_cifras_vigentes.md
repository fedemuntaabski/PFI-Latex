# P11 E75 — Cifras del juego de modelos vigente, RNF-02, gate y despliegue

**Fuente:** diagnóstico X2b (las cifras del modelo de los capítulos 8, 9, 10 y 13 provenían del candidato del 23/08, rechazado) y medición X3 (RNF-02), transcriptos en el prompt de P11. **Juego vigente:** corrida del 02/09/2026, referencias de percentil regeneradas el 06/10/2026; queda fijo para la entrega.
**Rama:** `e75/paquete`, sin push.
**Compilación de cada tanda** (pdflatex, biber, pdflatex ×2): 0 errores, 0 `Overfull \hbox` (línea base: 0), 0 referencias indefinidas.

## Commits

| tanda | commit | archivos |
|---|---|---|
| T1 | `23d3a5b` P11 E75 T1 | pruebas.tex, datos.tex, producto.tex, conclusiones.tex |
| T2 | `c9b1c01` P11 E75 T2 | pruebas.tex |
| T3 | `6e523f9` P11 E75 T3 | pruebas.tex, requerimientos.tex, producto.tex, conclusiones.tex |
| T4 | `e2cf52e` P11 E75 T4 | arquitectura.tex, producto.tex, requerimientos.tex |
| T5 | `f85f9f2` P11 E75 T5 | conclusiones.tex |
| entregable | (este archivo) | documentacion/e75/p11_cifras_vigentes.md |

Las líneas son las del estado final (después de T5).

## T1. Cifras del modelo vigente

| Archivo:línea | Antes | Después |
|---|---|---|
| pruebas.tex:240 (metas, IF) | 0,79 % · No | 0,81 % · No |
| pruebas.tex:241 (metas, LSTM) | 3,99 % · Sí | 4,18 % · Sí |
| pruebas.tex:242 (metas, E4 con 70) | 13,3 % (2 de 15) · No | sin cambio |
| pruebas.tex:243 (metas, promedio) | 6,7 % (4 de 60) · No | 5,0 % (3 de 60) · No |
| pruebas.tex:244 (metas, alertas) | 16,8 % · No | 15,4 % · No |
| pruebas.tex:275 | 0,79 % (97 de 12.235 usuario-días) | 0,81 % (99 de 12.236 usuario-días) |
| pruebas.tex:277 | 3,99 % (1.487 de 37.254 secuencias) | 4,18 % (1.558 de 37.254 secuencias) |
| pruebas.tex:279 | Media 0,1248; umbral 0,1368 | Media 0,1225; umbral 0,1180 |
| pruebas.tex:281 | Mediana 41,6; p95 70,2; p99 82,6 | Mediana 42,0; p95 69,3; p99 82,8 |
| pruebas.tex:283 | Pearson −0,20 (234 usuarios) | `[[CODIGO: Pearson con el modelo vigente]]`; la lectura "capturan aspectos distintos" se conserva |
| pruebas.tex:285 | Jaccard 0,111 (15 usuarios) | sin cambio |
| pruebas.tex:289 | "La correlación negativa y la baja coincidencia indican" | "La baja coincidencia indica" (el signo depende del valor) |
| pruebas.tex:321 (tab. escenarios) | E1: 3 / 2 / 1 / 0 | E1: 2 / 2 / 0 / 0 (E2, E3, E4 sin cambio) |
| pruebas.tex:331 | 16,8 %; 14,6 % (cobertura completa); 28,9 % (parcial) | 15,4 % (100 de 650); 14,3 % (79 de 553); 21,6 % (21 de 97) |
| pruebas.tex:333 | "Las cuatro detecciones atribuibles corresponden a dos usuarios con cobertura completa." | "Las tres detecciones atribuibles corresponden a `[[CODIGO: usuarios y cobertura de las detecciones con el modelo vigente]]`." |
| pruebas.tex:346 | 33,3 % en E4 "en el umbral de 55" | "en los umbrales de 55 y de 65"; al final del párrafo, `[[CODIGO: curva completa con el modelo vigente]]` |
| datos.tex:82 | 12.235 de prueba | 12.236 de prueba |
| datos.tex:88 | percentil 95 del entrenamiento (0,1368) | (0,1180) |
| conclusiones.tex:59 | 16,8 % de los días sin ataque | 15,4 % |

**Agregados en T1**
- pruebas.tex:217: párrafo inicial de 10.5 con la aclaración del juego vigente (texto del prompt, literal).
- producto.tex:97 (9.2.4): el juego vigente proviene de la corrida del 2 de septiembre, que la regla anterior rechazó, y se adoptó por consistencia del juego, no por promoción.
- producto.tex:138 (9.3, RF-21): misma aclaración; se conserva "todavía no se observa una promoción con un modelo genuinamente nuevo".
- conclusiones.tex:34 (objetivo 6): misma aclaración. No figuraba en el pedido, pero contradecía la aclaración.

**Revisado sin cambios:** "cumple 1 de las 5 metas" (cap. 13, solo LSTM); síntesis del cap. 10 (l. 601); interpretación 10.6.4 (ninguno en crítico, 0 de 60); l. 260 ("cumple las metas de rendimiento y de comportamiento del LSTM"); l. 359 "6,7 puntos porcentuales" (equivale a 1 de 15, no es la meta); l. 459 ya decía 12.236; 13,3 % en conclusiones:58 y pruebas:346 (2 de 15, sin cambio).

## T2. Latencia (RNF-01)
- pruebas.tex:188: párrafo nuevo con la segunda medición (p95 13,0 ms; p99 108,9 ms; 1000 de 1000 sin error). Tipografía ajustada al documento (`~ms`, `Windows~11`, `1000`).
- Tabla 10.V y fila de latencia de las metas: sin cambio.

## T3. RNF-02

| Archivo:línea | Antes | Después |
|---|---|---|
| pruebas.tex:191 | — | agregado: fecha (08/10/2026), equipo (Windows 11 Pro, 16 núcleos lógicos), 360 muestras sin pérdidas, unos 112 eventos respondidos |
| pruebas.tex:206 | `[[CPU MEDIA]] / [[CPU P95]] / [[CPU MÁX]]` | 0,09 / 0,14 / 0,16 |
| pruebas.tex:208 | `[[RSS MEDIA]] / [[RSS P95]] / [[RSS MÁX]]` | 33,02 / 33,24 / 33,25 |
| pruebas.tex:212 | `[[INTERPRETACIÓN DE RNF-02 SEGÚN EL RESULTADO]]` | texto (b) del prompt |
| pruebas.tex:588 (10.10) | — | ítem: RNF-02 medido con uso normal, sin ráfaga de eventos de archivo |
| pruebas.tex:601 (síntesis) | latencia cumple RNF-01 | latencia y consumo cumplen RNF-01 y RNF-02 |
| requerimientos.tex:224 | `[[ESTADO SEGÚN RNF-02]]` | Implementado: CPU media 0,09 % y memoria residente de 33 MB |
| producto.tex:136 | 8 implementados … RNF-02 `[[ESTADO SEGÚN RNF-02]]` | 9 implementados, 5 parciales, 1 no implementado (9 + 5 + 1 = 15, coincide con la tabla de RNF) |
| conclusiones.tex:20 | consumo `[[CODIGO: RNF-02]]` | consumo medio de 0,09 % de CPU y 33 MB de memoria residente (RNF-02) |
| conclusiones.tex:47 | `[[CODIGO: actualizar conteo con RNF-02, RNF-03 y RNF-13]]` | 9 implementados, 5 parciales y 1 no implementado `[[CODIGO: actualizar conteo con RNF-03 y RNF-13]]` |
| pruebas.tex:126 (10.2.4) | RNF-02 en "Verificación manual o medición" | sin cambio (ya estaba) |

## T4. Gate y despliegue

| Archivo:línea | Antes | Después |
|---|---|---|
| producto.tex:97 (9.2.4) | — | gate implementado y demostrado con su script; no ejecutado desde el planificador; planificador desactivado en la nube y versión instalada anterior al gate |
| producto.tex:122 | RF-02 (sin TLS) | RF-02 (TLS sin verificar) |
| producto.tex:138 | "el canal entre el agente y la API no está cifrado" | sin cifrado verificado de extremo a extremo: HTTP en el despliegue local; en la nube, con TLS en la instancia, todavía no se verificó con un agente |
| producto.tex:142 (9.4) | red de distribución no creada; "no está operativo para usuarios finales" | Terraform aplicado; Caddy con ACME publica el panel y `/api`; API solo en la interfaz local; SSM sin SSH; red de distribución no utilizada; evidencia del 06/10; sin evidencia de agente ni de inicio de sesión `[[CODIGO: resultado del Prompt C]]`; instancia apagada fuera de las pruebas |
| producto.tex:225 (9.6) | Previsto mediante la red de distribución con TLS | TLS terminado por el proxy en la instancia; falta la verificación de extremo a extremo con un agente y la autenticación mutua |
| requerimientos.tex:63 (RF-02) | Parcial: canal sin TLS (ver RNF-13) | igual + `[[CODIGO: resultado del Prompt C]]` |
| requerimientos.tex:246 (RNF-13) | No implementado | igual + `[[CODIGO: resultado del Prompt C]]` |
| arquitectura.tex:177 (tab. servicios) | red de distribución para HTTPS | administración remota sin SSH; HTTPS mediante el proxy inverso (Caddy) en la instancia |
| arquitectura.tex:193 | nube "diseñada y aplicada en forma parcial" | "aplicada pero sin verificación de extremo a extremo con un agente" |
| arquitectura.tex:207-214 (7.5.2) | red de distribución con HTTPS; instancia solo acepta tráfico de la red de distribución; publicación sin SSH | Caddy + ACME + `/api`; API solo en la interfaz local; administración y publicación por SSM, sin SSH |
| arquitectura.tex:237-251 (tab. 7.VII) | red de distribución "No creada" | instancia: vuelve sola tras detener y arrancar; fila nueva "Proxy inverso con TLS (Caddy)", verificado el 06/10; red de distribución "No utilizada: reemplazada por el proxy en la instancia"; reentrenamiento: versión anterior al gate; fila nueva "Envío de eventos desde un agente: sin evidencia" `[[CODIGO: resultado del Prompt C]]` |
| arquitectura.tex:255 | "no tiene acceso operativo para usuarios finales ni cifrado TLS en ningún tramo" | TLS entre el cliente y la instancia; falta la verificación de extremo a extremo con un agente; RF-02 y RNF-13 sin cambio `[[CODIGO: resultado del Prompt C]]` |
| arquitectura.tex:298 (HTTPS) | la red de distribución terminaría TLS | el proxy de la instancia termina TLS; canal del agente sin verificación de extremo a extremo `[[CODIGO: resultado del Prompt C]]` |
| arquitectura.tex:304 (HTTP sin TLS) | "En el entorno verificado, el canal no está cifrado…" | HTTP en el despliegue local; HTTPS en el diseño de la nube sin verificación con un agente; sin autenticación mutua `[[CODIGO: resultado del Prompt C]]` |
| arquitectura.tex:310 (síntesis) | "sin la capa que provee el cifrado" | "con TLS terminado en la propia instancia, pero sin verificación de extremo a extremo con un agente" |

chapter01.tex:53, el marcador del despliegue queda.

**Figuras desactualizadas (no editadas; se rehacen en L3)**
- Figura 7.2 (`despliegue_aws`):
  - caja "CloudFront distribution – [no creado] (pendiente habilitación cuenta)";
  - flechas "/ origin" y "/api origin";
  - caja "S3 frontend + OAC + CF Functions – [desplegado] en state";
  - instancia "EC2 … [a verificar] state running; estado_producto dice apagada/t3.micro";
  - faltan el proxy Caddy con TLS/ACME, la API en la interfaz local y la redirección HTTP→HTTPS.

  "deploy via SSM Run Command" sigue siendo válida.
- Figura 7.1 (`despliegue_local`): sin etiquetas afectadas.

## T5. Marcadores cerrados
- conclusiones.tex:23: `[[CODIGO: actualizar si se reentrena]]` (borrado; la frase usa "1 de las 5 metas", correcto).
- conclusiones.tex:72: `[[CODIGO: actualizar si el reentrenamiento cambia los resultados.]]` (borrado; el párrafo usa 13,3 % y 15,4 %).

## Cifras viejas sin reemplazo (no se cambiaron)
- pruebas.tex:333: subas de la mediana del puntaje de 3,9 a 5,6; máximo mediano de 63,7 a 65,8; explicaciones solo de variables de Isolation Forest; "en 7 de los 60 casos" ninguna variable superó el umbral de explicación.
- pruebas.tex:346: "el 93,3 % de los usuarios parte por encima" en el umbral 40.
- Figura `curva_umbral` (10.6.3): generada con el modelo anterior (incluye la tasa de alertas a 70 del 16,8 %).
- pruebas.tex:331: "ninguno en crítico" en los días sin inyección (el prompt no lo confirma con el juego vigente).
- datos.tex:59 frente a datos.tex:82: 61.283 pares usuario-día ≠ 49.048 + 12.236 = 61.284. Es una inconsistencia que apareció al unificar 12.236.
- datos.tex:82-86: 111.742 y 20.741 secuencias, detención en la época 22, pérdida de validación 0,0805 y 67.375 parámetros. Pueden provenir del candidato del 23/08; no hay dato vigente.
- datos.tex (8.1 y 8.3): el entrenamiento se describe solo con CLUE-LDS; la aclaración de 10.5 menciona 92 eventos reales del agente.
- arquitectura.tex:243, fila "Buckets de almacenamiento" (Dashboard estático): no se sabe si el bucket del panel sigue en uso con Caddy.
- pruebas.tex:144 y 542: la corrida del planificador de agosto (0,1155 → 0,1175) no corresponde al juego vigente; sin cambio.

## Marcadores [[...]] que quedan
- chapter01.tex:53: confirmar estado del despliegue.
- chapter04.tex:437-438: canal y fechas de la encuesta.
- requerimientos.tex:63 y 246: resultado del Prompt C (RF-02, RNF-13).
- arquitectura.tex:249, 255, 298 y 304: resultado del Prompt C.
- producto.tex:142: resultado del Prompt C.
- producto.tex:165: seguridad (art. 9).
- pruebas.tex:283: Pearson con el modelo vigente.
- pruebas.tex:333: usuarios y cobertura de las detecciones.
- pruebas.tex:346: curva completa con el modelo vigente.
- conclusiones.tex:20: TLS y autenticación mutua, y estado del objetivo 1.
- conclusiones.tex:36: resultado de seguridad y estado.
- conclusiones.tex:40-41: cantidad de pruebas y cobertura, y estado.
- conclusiones.tex:47: actualizar conteo con RNF-03 y RNF-13.
- conclusiones.tex:122: ajustar según la cobertura.
- conclusiones.tex:126: limitaciones de seguridad e IAM real.
