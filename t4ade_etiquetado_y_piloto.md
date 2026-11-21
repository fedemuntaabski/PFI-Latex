# T4a, T4d y T4e: etiquetado, variable de compartición y piloto de host

## T4a. Etiquetado: decisión de citarlo como provisional (16/11)

**Decisión del autor (16/11):** la planilla del analista (`docs/etiquetado/planilla_analista.csv`, paquete en `data/sandbox/20261111/etiquetado/paquete_analista.zip`) no volvió antes de la entrega, así que las cifras del etiquetado se citan como **provisionales**:
- 14 de 162 alertas merecían revisión: 8,6 %, IC 3,9–15,0 %;
- 0 de 58 entre las alertas de solo novedad;
- 1,05 % de los días sin alerta merecían revisión.

No existe `resultado_confirmado.md`. En el LaTeX, §8.5 y §9.1 mantienen la palabra "provisional", con la salvedad de que hubo un solo etiquetador. La consistencia propia fue de 40 de 40 en el veredicto y kappa 0,91 en la categoría. Esa es la consistencia del mismo etiquetador consigo mismo, no un acuerdo entre dos.

Si la planilla vuelve, el procedimiento ya está escrito en `78_plan_confirmacion_etiquetas.md`, que se retiró en la limpieza y se recupera con `git show 60350b5^:docs/revision_modelos_20261028/78_plan_confirmacion_etiquetas.md`:
1. Recalcular `cruce.md` con la etiqueta confirmada.
2. Calcular el kappa contra la etiqueta provisional.
3. Registrar los casos corregidos. Los candidatos marcados de antemano son C282 y C352: el borrado de 13.887 archivos sobre una carpeta que el mismo usuario había subido cuatro días antes.

Las etiquetas congeladas (`228b98c`) no se tocaron en este goal.

## T4d. Variable de compartición externa (trabajo futuro)

**No se hace en esta entrega.**

La hipótesis sale del etiquetado: compartir hacia afuera es el punto flojo, con 2 de 5 casos que merecían revisión sin alerta. Pero se apoya en 5 casos y en etiquetas provisionales, y elegir una variable con esas mismas etiquetas de DEV sería sobreajustar.

Si se hace, el camino ya existe:
- el feature set v2 tiene `n_share_events` (los 8 tipos de `SHARE_TYPES_V2` en `scripts/_score_common.py`);
- se evalúa con el mismo gate (FPR ≥ alto y p90 semanal en DEV, margen 0,01) y con una sola confirmación en HOLDOUT.

## T4e. Piloto de telemetría propia de host (protocolo, no ejecutado)

Es la limitación más grave del sistema. El IsolationForest entrenado con CLUE y aplicado a telemetría de host (LANL 2017) da una FPR ≥ alto de 53,66 %, contra 4,13 % de un IF entrenado en host. Ninguna métrica de CLUE se transfiere al agente sin más. El primer paso es medir en el dominio del agente.

**Objetivo.** Con eventos del propio agente en equipos reales:
- la FPR ≥ alto y la carga de alertas en el dominio del agente;
- con un modelo de host entrenado con esos datos, si las acciones registradas en la bitácora elevan el nivel.

**Diseño.**
1. **Equipos y duración:** al menos 5 equipos Windows de uso laboral real (por ejemplo, una PyME del relevamiento de §5) durante 6 semanas. Las semanas 1 a 4 son línea base y entrenamiento, las 5 y 6 son evaluación. Mínimo para el umbral móvil: 50 usuario-días con recursos, que con 5 equipos se juntan en unas 2 semanas.
2. **Modo de operación:** el agente en `--dry-run` (decide, pero no termina procesos ni deniega carpetas), con `DEMO_ROOT` en una carpeta de trabajo real y la API en la EC2, con una key individual por equipo (`manage_agent_key.py alta --uid`).
3. **Consentimiento y marco legal:** consentimiento informado y por escrito de cada usuario, revocable. Hay que informar:
   - la finalidad;
   - qué se captura: rutas y nombres de archivo de la carpeta vigilada, procesos, destinos de red y horarios;
   - la retención (fin del piloto + 90 días);
   - quién accede: el autor y el director.

   Bajo la Ley 25.326 hace falta el consentimiento libre, expreso e informado (art. 5), con finalidad determinada (art. 4), seguridad (art. 9) y derecho de acceso y supresión (arts. 14 y 16). Bajo la LCT, el control del empleador tiene que ser razonable y conocido por el trabajador (arts. 65, 70 y 71): se acuerda con el empleador y se notifica por escrito. No se capturan contenidos de archivos, teclado ni pantalla.
4. **Seudonimización:** el `uid` se reemplaza por un código por equipo. La tabla de correspondencia queda fuera del repo y fuera de la EC2.
5. **Registro de incidentes confirmados:** una bitácora firmada por el usuario con las acciones "de riesgo" que realmente ejecuta, por ejemplo copiar una carpeta a un USB, usar otra cuenta o compartir hacia afuera. Cada entrada lleva fecha, hora, equipo y acción. Las ejecuta la persona sobre sus propios datos, no se inyectan eventos. Lo que el sistema alerte fuera de la bitácora se revisa con el usuario y se etiqueta con el protocolo de `docs/etiquetado/`.
6. **Métricas, fijadas antes de mirar:**
   - FPR ≥ alto por usuario-día en evaluación;
   - p90 semanal;
   - alertas por usuario y semana;
   - entradas de la bitácora con nivel ≥ alto en el mismo día;
   - comparación entre el IF de CLUE y un IF entrenado con las 4 semanas de base.
7. **Cierre:** borrar los datos crudos a los 90 días y publicar solo agregados.

**Qué no cubre:** ataques de un insider real ni de un adversario que conozca el sistema. Con 5 equipos no hay potencia estadística para el recall: es un piloto de factibilidad y de FPR.
