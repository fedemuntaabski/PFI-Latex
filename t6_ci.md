# T6. Diagnóstico del CI con `startup_failure` (2026-11-16)

## Pruebas hechas

| Prueba | Resultado |
|---|---|
| Workflow mínimo `hello.yml` (un solo `echo`, sin actions ni `uses:`), rama `diag/ci-hello`, sin `ci.yml` (commit `5411111`, corrida 43868561491) | `startup_failure`, `path: BuildFailed` y 0 jobs |
| Última corrida de `ci.yml` en `entrega/limpieza` (43795155605) | `startup_failure`, `path: BuildFailed` |
| `workflow_dispatch` del 15/11 (43706419315) | `queued` durante más de 24 h, sin jobs creados |
| `GET actions/permissions` | `enabled: true`, `allowed_actions: all`, `sha_pinning_required: false` |
| `GET actions/permissions/workflow` | `default_workflow_permissions: read` |
| Plan de la cuenta | `free`, repo privado y del usuario (sin organización, así que no aplica ninguna política de org) |
| Uso de Actions (API de facturación nueva) | oct: 1117 min de Linux y 242 de Windows (≈1601 de 2000 con el multiplicador x2); nov: 4 y 1; monto neto US$ 0 |
| Otros repos de la cuenta con Actions | solo `Quest` (última corrida el 11/05, `failure` común, no `startup_failure`) |

## Conclusión

El fallo **no está en `ci.yml`**: un workflow sin ninguna action falla igual, antes de crear un job. Tampoco vienen de ahí las actions pinneadas, las políticas (no hay organización y está `allowed_actions: all`) ni la cuota de minutos (noviembre casi no tiene consumo). La causa está del lado de la cuenta o del repo en GitHub, con lo que la consulta abierta con soporte es el camino.

## Reintento autorizado (16/11, 11:11 ART)

Con autorización del autor, por la API se deshabilitó y se volvió a habilitar Actions en el repo (`PUT actions/permissions`: `enabled=false` y después `enabled=true`, `allowed_actions=all`). Después se disparó una corrida nueva de `hello.yml` con un commit vacío (`acee9b3`, corrida 43883082662).

Resultado: **otra vez `startup_failure`**, con 0 jobs y un check suite de `github-actions` sin check runs ni mensaje. La corrida anterior no se puede re-ejecutar (403, "This workflow run cannot be retried").

Conclusión: se agotó lo que se puede hacer desde el repo. Queda la consulta de soporte de GitHub.

## Pendiente del autor

1. Sumar esta evidencia a la consulta de soporte: el número de corrida 43868561491 con `hello.yml` y `path: BuildFailed`.
2. ~~Deshabilitar y rehabilitar Actions~~: hecho el 16/11 por la API, sin efecto (ver arriba).
3. Revisar Settings → Billing → Budgets and alerts (un presupuesto de US$ 0 que corte el producto Actions) y el método de pago. La API devolvió 404 para los presupuestos.
4. Cuando vuelva a correr: borrar la rama `diag/ci-hello` (`git push origin --delete diag/ci-hello`).

Mientras tanto, la memoria no puede decir "CI en verde". Lo verificable es la suite en local con la misma configuración que el CI (ver T7).
