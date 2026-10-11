# Ajuste de figuras 7.2, 8.1 y 8.2

## Cambios
- 8.1 y 8.2: barras con `\textbar{}` y espacios ("iso | lstm", etc.); letra `\footnotesize` (10 pt en clase 12 pt), sin escala (ancho 11,3 cm < textwidth); tipo de dato en negro; `DEFAULT now()` quitado de created_at y nota unica en cada figura antes de "Fuente"; `UNIQUE(uid, fecha)` solo en la fila fecha; tablas apiladas en una columna (8.1 en pag. 117, 8.2 en pag. 118 impresas); relaciones punteadas mantenidas.
- 7.2: flecha de "Almacen de parametros" llega a la API (se intercambiaron par y S3 de lugar); GitHub Actions a 1 cm de AWS; caption "Arquitectura de despliegue en la nube".
- Texto del capitulo: "estado de cada recurso" aparecia solo en el caption; no hubo otro ajuste.

## Verificacion
- "??": 0. Total "de 262". Ninguna pagina con texto bajo "Pagina N de M".
- "estado de cada recurso": 0 (texto e indice de figuras).
- pdftotext en pags. PDF 119 y 120: "iso | lstm", "umbrales | acciones | reentrenamiento", "iso | lstm | benchmark_dev", "candidato | vigente", "alta | revocacion". Sin "isollstm".
- PNG (110 dpi) en docs/verificacion/figuras_tikz/v2/.
- Observacion: el rotulo "uid (logica)" de la 8.1 queda pegado a la esquina de la linea.
