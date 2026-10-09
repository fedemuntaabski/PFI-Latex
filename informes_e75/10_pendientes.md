# E75 — Pendientes del día: código y verificaciones abiertas

Rama `correcciones-e75-latex`. Fecha: 2026-10-09.

**Alcance:** solo los 10 commits de hoy, de `a692424` (informe 00) a `6f98061` (informe 09). Las notas previas de `documentacion/e75/` no se tienen en cuenta. Los números de línea son los del estado de `6f98061`.

Cada ítem dice qué hay que verificar, de qué commit o informe viene y qué texto de la tesis hay que actualizar según lo que se encuentre.

---

## 1. Para verificar en el repo de código

### 1.1 Marcadores `[[CODIGO]]` (22 en total)
Se inventariaron hoy (00) y siguen en el PDF (09). Ninguno se tocó.

**A. Prompt C: TLS de extremo a extremo con un agente real y estado del despliegue**
- [ ] `chapters/chapter01.tex:59`: `[[CODIGO: confirmar estado del despliegue]]` y `[[CODIGO: confirmar según el resultado del Prompt C]]`
- [ ] `chapters/requerimientos.tex:63`: RF-02 (canal agente → API), `[[CODIGO: resultado del Prompt C]]`
- [ ] `chapters/requerimientos.tex:248`: RNF-13 (cifrado), `[[CODIGO: resultado del Prompt C]]`
- [ ] `chapters/arquitectura.tex:249`: tabla de despliegue, fila "Envío de eventos desde un agente"
- [ ] `chapters/arquitectura.tex:255`: párrafo sobre TLS y acceso
- [ ] `chapters/arquitectura.tex:298` y `:304`: tabla de protocolos (HTTPS / HTTP sin TLS)
- [ ] `chapters/producto.tex:142`: estado del despliegue (9.4)
- [ ] `chapters/producto.tex:165`: `[[CODIGO: cifrado TLS entre agente, panel y API; autenticación mutua …; credenciales del panel fuera del navegador; claves de agente ligadas a su identificador]]`
- [ ] `chapters/conclusiones.tex:25`: `[[CODIGO: TLS y autenticación mutua]]` y `[[CODIGO]]`
- [ ] `chapters/conclusiones.tex:134`: limitaciones de seguridad abiertas e integración con un IdP real (13.4, último ítem)

> Si cambia el estado de RF-02 o de RNF-13, hay que revisar también los conteos de RF y RNF (13.1, `conclusiones.tex:51-52`) y la tabla 9.II.

**B. Modelo vigente**
- [ ] `chapters/pruebas.tex:284`: `[[CODIGO: Pearson con el modelo vigente]]`
- [ ] `chapters/pruebas.tex:334`: `[[CODIGO: usuarios y cobertura de las detecciones con el modelo vigente]]`
- [ ] `chapters/pruebas.tex:347`: `[[CODIGO: curva completa con el modelo vigente]]` (puede requerir regenerar `images/pruebas/curva_umbral.pdf`)
- [ ] `chapters/conclusiones.tex:130`: `[[CODIGO: ajustar según el resultado de la cobertura]]` (13.4)

**C. Seguridad, pruebas y conteos**
- [ ] `chapters/conclusiones.tex:41`: `[[CODIGO: resultado de seguridad]]` y `[[CODIGO]]`
- [ ] `chapters/conclusiones.tex:45-46`: `[[CODIGO: cantidad de pruebas y cobertura]]` y `[[CODIGO]]` (cantidad de tests y cobertura del repo)
- [ ] `chapters/conclusiones.tex:52`: `[[CODIGO: actualizar conteo con RNF-03 y RNF-13]]`

### 1.2 Gemini / RF-31 (commit `9f1dcf9`, informe 07)
Hoy el documento da por vigentes tres cosas: el servicio es opcional, tiene un texto predefinido de respaldo y el nivel y la acción los decide el motor de *scoring*. El resto figura como "recomendado". Si algún control ya existe en el código, hay que pasarlo a "implementado" en los lugares indicados.

**Lugares de la tesis que dependen de este bloque:**

| Texto | Ubicación |
|---|---|
| 9.6.2 "Inyección de instrucciones en la redacción asistida". Era 9.6.1 hasta `6f98061` | `chapters/producto.tex:253-267` |
| Fila "Prompt injection en la redacción asistida", tabla 9.IV | `chapters/producto.tex:249` |
| Tabla 9.III, transferencia internacional, "Pendiente: …" | `chapters/producto.tex:169` |
| RF-31, requerimiento y estado "Implementado" | `chapters/requerimientos.tex:137` |
| Trazabilidad (matriz y CU-02) | `chapters/requerimientos.tex:320`, `:552` |
| Tabla 9.II, fila CU-02 | `chapters/producto.tex:124` |
| Cobertura de pruebas, "Sin prueba registrada" | `chapters/pruebas.tex:128` |
| "Cinco requerimientos funcionales … no tienen prueba" | `chapters/pruebas.tex:586` |
| 13.4, ítem "Redacción asistida del correo" | `chapters/conclusiones.tex:125-126` |
| Tabla de servicios (Gemini) | `chapters/arquitectura.tex:185` |

**Checklist:**
- [ ] **Afirmación deducida y no verificada:** "la respuesta del modelo no vuelve al agente ni modifica la configuración" (9.6.2, `producto.tex:257`). Confirmar que la salida de Gemini se usa solo como cuerpo del correo. Si no es así, hay que reescribir el párrafo del impacto acotado.
- [ ] **Campos enviados:** listar qué datos entran exactamente al prompt (puntaje, nivel, usuario, procesos, rutas, destinos, contexto IAM). Si van agregados y no crudos, corregir 9.6.2, la tabla 9.III y 13.4.
- [ ] **Separación instrucciones/datos:** ¿se usa `system_instruction` o un rol de sistema, o se concatena todo en un solo string?
- [ ] **Delimitado y escapado** de los campos de telemetría.
- [ ] **Límites** de longitud, de caracteres o de cantidad de eventos.
- [ ] **Validación de la salida** (formato, longitud, URLs) y caída al texto predefinido si falla.
- [ ] **Bloque fijo de datos objetivos** en la plantilla del correo, separado del texto generado.
- [ ] **Timeout y errores:** una falla o una demora de Gemini lleva al texto predefinido sin bloquear la evaluación.
- [ ] **Tests:** si hay un test del respaldo o del cliente de Gemini, pasar RF-31 a "Prueba automatizada" (`pruebas.tex:128`) y cambiar "Cinco" por "Cuatro" (`pruebas.tex:586`).
- [ ] **Desactivación y despliegue:** cómo se apaga (variable de entorno sin clave) y si está activo en la nube.
- [ ] **Estado "Implementado" de RF-31** (`requerimientos.tex:137`): se puso a partir de lo que ya decía el documento. Confirmar en el código. Si cambia, hay que revisar los conteos 31/29/2 en el cap. 4 (síntesis), la tabla 9.II, 9.7 y 13.1 (`conclusiones.tex:51`).

---

## 2. Quedó sin chequear en la tesis (no depende del código)

### Bibliografía
- [ ] **`OWASP2025LLM`** (`biblio.bib:465`, commit `9f1dcf9`): confirmar en el navegador el año (2024) y el título exacto. genai.owasp.org devolvió 403 al pedido automático.
- [ ] **Llaves simples en las entradas NIST** (`Rose2020` l. 68, `Hu2014` l. 78, `NIST2023_800207A` l. 88; detectado en 07): revisar en la lista de referencias si sale "National Institute of Standards y Technology". Si sale así, poner la institución entre llaves dobles.
- [ ] **`Aliyu2024`** (`biblio.bib:252`, informe 03): tiene `and others`. ¿Se completan los autores?

### Transcripciones (commit `53b778b`, informe 04): hace falta el audio
- [ ] Responder las 22 preguntas de "Preguntas para vos" del informe 04: palabras dudosas en C, D, E y F, y decidir si se usan corchetes con la forma correcta en lugar de `[inaudible]`.
- [ ] Anexo E, l. 10: la frase del "18 de agosto" y el "50 % del avance" (mecánica de entregas). ¿Queda, se recorta o se comenta?
- [ ] Anexo D: turnos con hablantes mezclados (l. 10, 12, 30, 34, 38, 62 y 72).
- [ ] Decidir los ítems de "Sin cambios: para que decidas": "logonear", palabras existentes dudosas, "Y." y "Okay", "tiki, tiki".

### Gantt (commit `8328e49`, informe 05)
- [ ] Reexportar el Gantt (PDF vectorial, apaisado, partido por incremento o por fechas) para que se lea impreso. Hoy queda en ~1,9 pt.
- [ ] El Gantt no está organizado por los dos incrementos de la sección 1.4, y el texto del anexo dice que sí.
- [ ] Marcador rojo del día 13/06 en el eje; etiqueta "[HITO] Defensa Final…" cortada en la imagen.
- [ ] "Hitos de entrega" en el texto (`schedule_of_activities.tex:3`) y en el epígrafe (l. 10). Es mecánica de entregas fuera de las transcripciones (09). Se resuelve junto con la reexportación.

### Modelo de negocio (commit `c49f107`, informe 06)
- [ ] ¿Se detallan en la tabla 12.II los costos fijos de los años 2 a 4 (6.000, 9.000 y 11.000)?
- [ ] Necesidad de fondos pesimista: la tabla dice 360.837 y la suma redondeada da 360.838. Es redondeo; decidir si se aclara.

### Encuesta (commit `1a81562`, informe 08)
- [ ] Las fechas de difusión se omitieron. Si aparecen, agregarlas en 3.6 (`chapter04.tex:437`) y en el Anexo B (`surveys.tex:3`).

### Forma y redacción (commit `6f98061`, informe 09)
- [ ] Pretérito con hechos fechados en `producto.tex:97`, `producto.tex:138` y `conclusiones.tex:40`. Se dejó así a propósito; reescribir si se quiere todo en presente.
- [ ] "Figura~\ref" con mayúscula en medio de oración (3.6 y `schedule_of_activities.tex:3`). Viene del informe 02.
- [ ] Overfull del encabezado (uno por página): se corrige con `\headheight`, pero mueve el cuerpo de todas las páginas.

### Carátula (commit `b5b93fb`, informe 01)
- [ ] Si el título cambia, volver a correr `cover/generar_caratula.js` y reemplazar `cover/Caratulafinal.pdf`.

### Revisión visual sin hacer
Los informes 01, 05 y 06 rasterizaron sus páginas; los commits `9f1dcf9`, `1a81562` y `6f98061` no. Hay que mirar en `build/main.pdf`:
- [ ] 9.6, 9.6.1 y 9.6.2 (párrafo nuevo, subsección nueva y lista de controles).
- [ ] Tabla 9.IV con la fila nueva (si corta bien entre páginas en el `longtable`), y tabla 9.III.
- [ ] RF-31 en la tabla del Módulo 4 y en la matriz de trazabilidad.
- [ ] Primer párrafo de 3.6 y del Anexo B.
- [ ] Ítem nuevo de 13.4.

---

## Resumen

| Bloque | Commit | Ítems | Qué texto queda bloqueado |
|---|---|---|---|
| `[[CODIGO]]` Prompt C / TLS / despliegue | `a692424` (inventario) | 10 ubicaciones | Cap. 1, RF-02, RNF-13, 7.x, 9.4, 13.1, 13.4 |
| `[[CODIGO]]` modelo vigente | `a692424` | 4 | 10.x (Pearson, cobertura, curva), 13.4 |
| `[[CODIGO]]` seguridad y conteos | `a692424` | 3 | 13.1 |
| Gemini / RF-31 en el código | `9f1dcf9` | 11 | 9.6.2, 9.III, 9.IV, RF-31, 10.x, 13.4 |
| Bibliografía | `e2cdba5`, `9f1dcf9` | 3 | Lista de referencias |
| Transcripciones (audio) | `53b778b` | 4 | Anexos C a F |
| Gantt | `8328e49` | 4 | Anexo A |
| Negocio | `c49f107` | 2 | 12.II, 12.V |
| Encuesta | `1a81562` | 1 | 3.6, Anexo B |
| Forma | `6f98061` | 3 | 9.x, 13.1, 3.6, Anexo A, encabezado |
| Carátula | `b5b93fb` | 1 | Carátula |
| Revisión visual | `9f1dcf9`, `1a81562`, `6f98061` | 5 | PDF |
