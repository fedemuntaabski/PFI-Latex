# L4a – seguridad

Rama: e75/correcciones-e50-v2. Compilación: sin errores, sin "??", sin referencias indefinidas.

| # | Archivo | Ubicación | Cambio |
|---|---|---|---|
| 1 | chapters/requerimientos.tex | RNF-04, celda Estado | "Implementado" → "Implementado (ver nota c)" |
| 2 | chapters/requerimientos.tex | Notas, tras nota b | Nota c agregada (mapeo de respaldo; \ref a 9.6.1, `sec:sintesis-limitaciones`) |
| 3 | chapters/producto.tex | 9.6.1, fila "El agente conserva un mapeo propio…" | Sin cambio: ya dice que con la API actual no se ejecuta; consistente con nota c |
| 4 | chapters/producto.tex | 9.6.1, fila mTLS | Título "…(mTLS) ni firma de las respuestas"; Impacto y Tratamiento ampliados con los textos pedidos |
| 5 | chapters/arquitectura.tex | 7.6, párrafo previo a la tabla 7.VIII | Oración sobre respuestas sin firma y TLS (no entra en una celda); \ref a 9.6.1 |
| 6 | chapters/conclusiones.tex | 13.4, ítem Seguridad | "autenticación mutua por certificado y la firma de las respuestas del PDP" |
| 7 | chapters/pruebas.tex | 10.5.1, tras "…esas etiquetas." | Oración sobre modelos no supervisados, sin sobremuestreo ni balanceo |

## Hallazgos
- "imbalanced": solo en chapters/archivo/obsoleto_e50.tex:135 (archivo no incluido por main.tex). Ninguna tabla de tecnologías vigente lo menciona; sin cambio.
- Referencia: la tabla de limitaciones está en 9.6.1 (`sec:sintesis-limitaciones`); `sec:limitaciones-producto` es 9.6, por eso se usó la primera.
- Tabla de limitaciones: la fila mTLS arranca en la página 150 del PDF y la tabla continúa en la 151 (corte normal de longtable entre filas/página); no se ve desborde.
- Overfull \vbox del log: ya existían antes de L4a.
