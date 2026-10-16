# Diagramas E75 en Mermaid

Rama `docs/diagramas-e75` (desde `e75/cierre`). Sin commit ni push. Preámbulo, numeración y tamaños sin cambios: solo contenido de `chapters/e50_uml.tex`, `arquitectura.tex` y `datos.tex`.

## Fuentes
- Repo de código `G:\pfi\Agente-Aut-...`: `modelo_datos_pfi75.md` (copia de trabajo del 2026-10-16, sin commitear) y `docs/infra/arquitectura_aws.md` (sin trackear). `documentacion/insumos/arquitectura_aws_actual.md` no existe; `docs/arquitectura_aws_actual.md` vive solo en `chore/revision-scripts-infra`.
- Código leído de solo lectura para flujo, componentes y objetos: `routes.py`, `schemas.py` (validación de esquema), `auth.py` (key por agente, `autorizar_agente`), `hybrid_service.py` (`en_aprendizaje`, regla de piso), `iam_service.py`, `metricas_service.py` (gate), `reentrenamiento_scheduler.py`, `agent/api_client.py` (circuit breaker 401/403).
- No hay correcciones del profesor sobre diagramas (confirmado por el autor).

## Inventario y veredicto
| Fig. | Antes (E50, PNG sin fuente) | Veredicto | Ahora |
|---|---|---|---|
| 6.1 flujo | diagrama-flujo.png 8192×5996 | Desactualizado y mal compuesto | `flujo_informacion.mmd` |
| 6.2 componentes | diagrama-componentes.png 1235×940 | Desactualizado (IAM, scheduler/gate, hash chain, validación) | `componentes.mmd` |
| 6.3, 6.4 clases agente | diagrama-clases-agente.png 2505×735 | Ilegible, sin buffer ni breaker | `clases_agente_1/2.mmd` |
| 6.5 a 6.11 clases API | diagrama-clases-api.png 16941×3844 | Ilegible y desactualizado | 7 diagramas por tema (esquemas eventos, esquemas config, Redis, scoring, IAM, auth, persistencia) |
| 6.12 objetos | diagrama-objetos.png | Instancia real vigente | `objetos.mmd` (sin `hybrid_anchor`, que era null) |
| 7.1 despliegue local | TikZ | Vigente | `despliegue_local.mmd` (pedido: todo a Mermaid) |
| 7.2 AWS | TikZ, t3.small, sin EIP/SG/IAM/Session Manager | Desactualizado | `aws_despliegue.mmd` + nueva fig. 7.3 `aws_apoyo.mmd` |
| 8.1, 8.2 ER | TikZ | Vigente | `er_scoring_eventos.mmd`, `er_config_modelos.mmd` |
| Redis (nuevo) | no existía | | `redis_claves.mmd`, **no insertado** (queda de apoyo) |

## Qué se regeneró
Fuente en `images/diagramas/mermaid/*.mmd`, salida en `images/diagramas/mermaid/pdf/*.pdf` (vectorial, texto real). `render.ps1` o `render.sh` reproducen todo: `mmdc` genera SVG a tamaño natural y `svg2pdf.js` lo imprime a PDF con Chromium de puppeteer (el PDF directo de `mmdc` comprime todo a 800 px). Requiere `npm i @mermaid-js/mermaid-cli` fuera del repo.
Los `.tex` TikZ y los PNG viejos quedan sin referenciar, sin borrar.
Tamaño de texto a ancho de página (cuerpo 12 pt): 6,9 pt (componentes, clases del agente 1) a 10,5 pt; el resto, 7 a 9 pt. El flujo se compactó de 5,7 a 7,5 pt.

## Diagrama AWS
- Capítulo 7, sección «Despliegue en la nube», figura 7.2 (`fig:despliegue-aws`) y figura 7.3 (`fig:despliegue-aws-apoyo`, nueva, con su párrafo introductorio).
- Se partió en dos porque en una sola el texto bajaba de 5,5 pt: **decisión a validar**. 7.2: navegador y agente, HTTPS 443, Elastic IP, Security Group (80/443, sin SSH), EC2 t3.medium apagada por defecto con Caddy, API, Keycloak (punteado, opcional) y dashboard, Upstash, Supabase, Gemini y SMTP (punteados), GitHub Actions solo CI, región us-east-2. 7.3: rol IAM, SSM Parameter Store (11), Session Manager y Run Command, S3 deploy, y CloudFront y S3 frontend en gris punteado (definidos, no desplegados).
- Sin recursos fuera de `arquitectura_aws.md`. «Agente PEP en el endpoint» va como cliente externo.

## Compilación
`latexmk -pdf main.tex`: 0 errores (`^!`), 0 referencias o citas indefinidas, 0 «??» en el texto. Overfull `\hbox`: 4, igual que antes (los `\vbox` de 36,9 pt son del encabezado y crecen con las páginas). Páginas: 267 antes, 278 ahora (+11 por las figuras nuevas y partidas).

## Cierre de las preguntas
- 7.2 y 7.3 quedan como dos figuras; notas de los ER aceptadas; `revocacion` y Keycloak punteado aceptados.
- `redis_claves.mmd` no se inserta: la tabla `tab:claves-redis` del cap. 8 ya dice lo mismo y con la vigencia. Queda de apoyo.
- `datos.tex`: "quince" pasa a "dieciséis" tipos de clave; "Ninguna utiliza la expiración nativa" pasa a "Casi ninguna", con la deduplicación como excepción (`dedup_service.py:54`, `ex=`); la fila Configuración suma los proveedores de identidad (`config:iam`).
- `informes_e75/auditoria_mockups.md` aparece sin trackear: no es de esta sesión.

## Datos confirmados por el autor
- **Tipo de instancia: `t3.medium`** (confirmado). Está en las figuras 7.2 y 7.3 y ahora también en el texto de `arquitectura.tex` (párrafo de «Despliegue en la nube» y fila «Instancia de cómputo de la API» de `tab:diseno-vs-despliegue`).
- **Keycloak en la EC2.** `arquitectura_aws.md` lo ubica en la misma instancia (`/auth/*` a 127.0.0.1:8080), pero no está en el tfstate (se instala por SSM). Va punteado y rotulado «opcional».

## Inconsistencias de CloudFront (reportadas, sin corregir)
Ninguna menciona CloudFront como parte del sistema desplegado:
- `chapters/arquitectura.tex:256` (tabla `tab:diseno-vs-despliegue`) y `chapters/producto.tex:142`: dicen que la red de distribución de contenidos no se utiliza. Consistente.
- `chapters/arquitectura.tex:233` (párrafo de la fig. 7.3) y la fig. 7.3: CloudFront y el bucket del dashboard figuran como definidos en Terraform y no desplegados. Si se prefiere cero CloudFront en las figuras, se quita el nodo `CF` de `aws_apoyo.mmd`.
- **Buckets (resuelto).** Con Caddy, `desplegar_frontend.ps1` sube `dist/` al bucket de deploy y por SSM lo baja a `/srv/pfi-frontend`; el bucket del dashboard quedó sin uso. Se reescribió la fila «Buckets de almacenamiento» de `tab:diseno-vs-despliegue`, el párrafo de la fig. 7.3 y el nodo S3 deploy de la figura («releases de la API y del dashboard»).
- **Tipo de instancia en el texto (resuelto).** Antes solo figuraba en el TikZ viejo; ahora el texto dice `t3.medium`.
