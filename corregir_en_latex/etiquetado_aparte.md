# Etiquetado de triage de CLUE DEV (punto aparte, pendiente de decidir)

> Sección autocontenida, para sumar a la memoria solo si se decide enviarla. Encajaría como **10.8 Etiquetado de triage**, antes de la evaluación de usabilidad (que pasaría a 10.9). Las cifras son **provisionales**: falta la confirmación de un analista.
>
> **Antes de incluirla hay que decidir cómo se declara quién hizo las etiquetas.** El texto de abajo dice "un etiquetador único". Si las etiquetas no las puso una persona del equipo, la memoria debería decirlo explícitamente en 10.8.1 y en las limitaciones (10.8.4): un evaluador lo va a preguntar.

---

## 10.8 Etiquetado de triage

Como CLUE-LDS no incluye ataques etiquetados, se construyó un etiquetado de triage sobre días reales de la partición DEV. La pregunta de cada etiqueta no es si hubo un ataque, algo que el conjunto de datos no permite confirmar, sino si un analista de un centro de operaciones de seguridad abriría el caso para revisarlo.

### 10.8.1 Método

Se seleccionaron 403 usuario-días de DEV posteriores al corte temporal: las 163 alertas del camino por defecto y 240 días sin alerta, muestreados con pesos para poder estimar la proporción sobre el total de días sin alerta. Cada caso se presentó como una ficha con los eventos del día, la línea base del usuario, sus desvíos y los días vecinos, con el usuario enmascarado y sin mostrar el puntaje, el nivel ni el detector que alertó.

El protocolo se fijó por escrito antes de ver ningún caso. Define tres veredictos (merece revisión, no merece revisión y no se puede saber), nueve categorías de señal con criterios cuantitativos (descarga masiva, borrado masivo, compartición externa, operaciones de administración, fallos de inicio de sesión, horario atípico, recursos nuevos, volumen atípico y automatización), una severidad de 0 a 3 y una confianza de 1 a 3. Para limitar la circularidad con el modelo, el protocolo exige decidir primero por lo que el modelo no observa (tipo de operación, amplitud de las rutas, ritmo y secuencia) y solo después por el volumen y el horario. Las etiquetas se congelaron antes de cruzarlas con las alertas.

### 10.8.2 Resultados

TABLA 10.XI: Resultado provisional del etiquetado de triage sobre DEV

| Medida | Resultado |
|---|---|
| Alertas que merecían revisión | 14 de 162 (8,6 %; IC 95 % de 3,9 % a 15,0 %, bootstrap por usuario) |
| Alertas con origen en Isolation Forest que merecían revisión | 13,5 % |
| Alertas originadas solo por la novedad de recurso que merecían revisión | 0 de 58 |
| Días sin alerta que merecían revisión | 3 de 240 (1,05 % ponderado; IC 95 % de 0 % a 3,8 %) |
| Consistencia del etiquetador (40 casos reetiquetados sin ver la primera etiqueta) | Veredicto: 40 de 40; categoría: kappa de 0,91 |

Fuente: elaboración propia.

### 10.8.3 Lectura

Nueve de cada diez alertas del camino por defecto corresponden, para un revisor, a actividad rutinaria. Ninguna de las 58 alertas originadas solo por la detección de novedad resultó revisable: en su mayoría se trata de archivos sueltos o carpetas que el propio usuario crea en su espacio de trabajo. Los días sin alerta que merecían revisión existen, pero con tres casos no es posible afirmar su cantidad. Estos resultados no constituyen una medida de detección ni de precisión frente a ataques, sino de la utilidad de las alertas para el triage. No se modificó ningún modelo ni umbral a partir de ellos.

### 10.8.4 Limitaciones

- **Etiquetador único y sin confirmación.** Todas las etiquetas son provisionales hasta que un analista revise la planilla. El analista verá la etiqueta antes de decidir, lo que introduce un sesgo de anclaje hacia confirmarla.
- **Consistencia propia, no acuerdo entre revisores.** El kappa de 0,91 mide la consistencia del mismo etiquetador; la muestra de reetiquetado contiene un solo caso positivo.
- **Circularidad parcial.** El volumen, el horario y los recursos nuevos son también variables del modelo; el orden de decisión del protocolo la reduce, pero no la elimina.
- **Sin verdad de fondo.** Los datos están seudonimizados y no incluyen el contenido de los archivos ni la confirmación del titular de la cuenta.
- **Día cerrado y dominio de nube.** El etiquetado no cubre la oscilación dentro del día y no se transfiere al dominio del agente.

### Pendiente para cerrar

1. Que un analista complete la planilla (`docs/etiquetado/planilla_analista.csv`) y recalcular el cruce con `scripts/etiquetado/cruzar.py`.
2. Si se confirma que ninguna alerta de solo novedad es revisable, decidir si la novedad debe seguir elevando el nivel o pasar a ser solo informativa.
3. Medir el acuerdo con un segundo revisor ciego.
