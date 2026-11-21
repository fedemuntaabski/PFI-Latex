# Cifras sin re-medir con el camino por defecto del 16/11 (pedido al repo de código)

Origen: actualización de la memoria LaTeX con `docs/devolucion_90/devolucion_latex.md` (rama `revision-caps7a13`).
El camino por defecto cambió el 16/11: IF sin país + regla de ubicación + novedad informativa. Las cifras de abajo siguen en el `.tex` con la configuración anterior, rotuladas como "configuración anterior" o "Sin medir". Si se miden, se reemplazan.

Reglas de siempre: no usar HOLDOUT (ya se usó una vez con el default final); el criterio se escribe antes de medir; nada con datos sintéticos o inyectados; SHA-256 de los artefactos de producción antes y después.

## Prioridad alta (aparecen en tablas del cap. 11)

| # | Cifra | Valor en el `.tex` hoy | Dónde | Cómo medir (sugerido) |
|---|---|---|---|---|
| 1 | Días con algún evento ≥ alto / días que cierran en alto, 51 usuarios DEV | 2,66 % / 1,29 % (config. anterior); "Sin medir" para el vigente | `tab:metas-modelo`, `tab:efecto-default` | La misma simulación evento a evento que dio 2,66/1,29 (y antes 14,04/4,95), con el default vigente |
| 2 | FPR ≥ alto en los primeros 3 días del usuario (arranque en frío, 130 usuarios) | 11,43 % (config. anterior); "Sin medir" para el vigente | `tab:efecto-default`, `tab:limitaciones-producto` (fila "Arranque en frío") | Mismo script que dio 11,43 % |
| 3 | Tasa de anomalías del IF en prueba (12.236 usuario-días) | 0,81 % (99), rotulada "modelo con la variable de país" | `tab:metricas-modelo`, `tab:metas-modelo` (meta 1–3 %) | `decision_function < 0` del `isolation_forest.joblib` vigente sobre el test de Fase 4 |
| 4 | FPR ≥ alto del IF sin calibrar como único detector, DEV | 15,17 %, rotulada "modelo con la variable de país" | `tab:metricas-modelo` | Mismo cálculo con el IF sin país |

## Prioridad media (rendimiento y despliegue)

| # | Cifra | Estado | Dónde |
|---|---|---|---|
| 5 | Latencia local: máximo y rendimiento secuencial (eventos/s) de la medición del 16/11 | Se quitaron de `tab:rnf01` porque solo había media, p50, p95 y p99 | `tab:rnf01`. Puede estar en `scripts/evidencia/bench_rnf01_resultado_iso_20261116.json` |
| 6 | Valores aislados más altos y repeticiones con otras semillas (antes 18,2–56,9 ms; p95 13,26 y 13,33) | Rotulados "medición del 15/11, configuración anterior" | `pruebas.tex`, párrafo después de `tab:rnf01` |
| 7 | Ensayo de la cadena de decisión (`demo_exfil`): evento en que llega a alto y a crítico, acción confirmada | Rotulado "configuración anterior; con la versión vigente no se repitió" | `sec:pruebas-e2e` |
| 8 | Agente real contra la EC2 con la release `20261116-103416-4e85d1d`: tiempo a crítico, acción y reversión | Rotulado "versión anterior" (crítico a ~36 s; 3 demos 33,8–40,3 s) | `sec:verificacion-despliegue`. Antes, `demo/reset_toma.ps1` (Lucía quedó en crítico). Apagar la EC2 al terminar |
| 9 | Suite ejecutada en la instancia con la release nueva | Rotulado "versión anterior" (496 aprobadas, 4 omitidas, 7 con error; 91,38 % / 89,63 %) | `sec:verificacion-despliegue` |
| 10 | Rearranque de la instancia: tiempo hasta listo | Rotulado "versión anterior" (41 s) | `sec:verificacion-despliegue` |

## Prioridad baja (confirmaciones)

| # | Cifra | Estado | Dónde |
|---|---|---|---|
| 11 | Cobertura combinada (líneas + ramas) del total API + agente | "--" en `tab:cobertura-codigo` (solo están las de cada componente: 94,10 % y 92,32 %) | `tab:cobertura-codigo` |
| 12 | Cobertura de la copia limpia en la configuración de CI (515 aprobadas, 33 omitidas) | Se cita la del 14/11 (87,60 % líneas / 85,73 % combinada) | `sec:integracion-continua` |
| 13 | Cantidad de pruebas que fijan explícitamente el camino de la v1 | El texto dice 18; puede haber cambiado con las 9 de la API nuevas | `pruebas.tex`, inventario |
| 14 | ¿Las pruebas de vitest cubren `LearningProgressBadge` (RF-26)? | El texto dice que RF-26 se verifica a mano | `pruebas.tex`, cobertura de requerimientos |
| 15 | Etiquetar con el protocolo de `docs/etiquetado/` las 8 alertas nuevas del IF sin país (sin tocar las etiquetas congeladas) | Sin etiquetar; por eso se cita 14/162 = 8,6 % y no 14/111 | `sec:etiquetado-provisional` |

## No medir (declarado como limitación o trabajo futuro)

- HOLDOUT con la regla de ubicación enmendada: no se repite. La corrida única queda declarada.
- Tasa de disparos de la regla de ubicación ante viajes o VPN corporativa: no hay datos del dominio.
- Recall: sin ataques etiquetados del dominio.

## Formato de devolución

Una tabla por número (#), con el valor, la fecha, el commit y el script/archivo de salida, igual que en `devolucion_latex.md`.
