# Diagramas v75 — renders Mermaid

Fuente: `modelo_datos_pfi75.md` (en la raíz del repo, no en `documentacion/`). Rama `feature/diagramas-v75`. Los renders ya existían en `images/diagramas/v75/` y están commiteados en `27e8167`; en esta pasada solo se verificaron (sin re-renderizar, sin nuevos commits, sin tocar `.tex`).

Origen: 9 bloques `mermaid` (1 erDiagram, 7 classDiagram, 1 flowchart) → 14 diagramas, cada uno en PDF + PNG (3136 px de ancho = escala 4, ≈300 dpi a ~26 cm). Cuatro bloques se partieron para legibilidad: ER en 2, §4.3 (schemas) en 3, §4.5 (scoring) en 2 y despliegue en 2 (aws / local).

## Archivos y dimensiones
Factor = 13,5 cm / ancho PDF (21,2 cm); el texto base ronda 12 pt en el PDF.

| Archivo (.pdf / .png) | PDF (pt) | PNG (px) | Tamaño a 13,5 cm de ancho |
|---|---|---|---|
| er_postgres_config_modelos | 600 × 403 | 3136 × 2084 | 13,5 × 9,1 cm |
| er_postgres_scoring_eventos | 600 × 696 | 3136 × 3644 | 13,5 × 15,7 cm |
| clases_agente_collectors | 600 × 220 | 3136 × 1108 | 13,5 × 5,0 cm |
| clases_agente_enforcement | 600 × 354 | 3136 × 1824 | 13,5 × 8,0 cm |
| clases_api_schemas_eventos | 600 × 258 | 3136 × 1308 | 13,5 × 5,8 cm |
| clases_api_schemas_config | 564 × 207 | 2944 × 1040 | 13,5 × 5,0 cm (ancho natural 19,9 cm) |
| clases_api_schemas_accion_health | 427 × 101 | 2212 × 472 | 13,5 × 3,2 cm (ancho natural 15,1 cm) |
| clases_api_redis | 600 × 386 | 3136 × 1992 | 13,5 × 8,7 cm |
| clases_api_scoring_orquestacion | 515 × 323 | 2680 × 1656 | 13,5 × 8,5 cm (ancho natural 18,2 cm) |
| clases_api_scoring_modelos | 600 × 231 | 3136 × 1168 | 13,5 × 5,2 cm |
| clases_api_iam_auth_config | 600 × 296 | 3136 × 1512 | 13,5 × 6,7 cm |
| clases_api_persistencia | 600 × 438 | 3136 × 2268 | 13,5 × 9,9 cm |
| despliegue_aws | 600 × 559 | 3136 × 2916 | 13,5 × 12,6 cm |
| despliegue_local | 600 × 463 | 3136 × 2404 | 13,5 × 10,4 cm |

## Verificación de legibilidad (12–15 cm)
- A 13,5 cm el texto base queda en ≈7,7 pt; a 12 cm ≈6,8 pt; a 15 cm ≈8,5 pt. Legible, pero justo en el extremo de 12 cm.
- Revisados visualmente (rasterizados): `er_postgres_scoring_eventos` (el más alto) y `despliegue_aws` (el más denso): se leen todos los nodos, columnas y etiquetas de aristas. Los demás son menos densos y de ancho igual o menor.
- Ninguno quedó ilegible, así que no hizo falta partir más.

## Despliegue sin emojis
Los PDF de `despliegue_aws` y `despliegue_local` no tienen emojis (`pdftotext` sin glifos pictográficos). Se usan `[desplegado]`, `[no creado]`, `[a verificar]` y `solo local`. Contenido de nodos y aristas conservado.

## Problemas / observaciones
1. `modelo_datos_pfi75.md` está en la raíz, no en `documentacion/` como indicaba el pedido.
2. En `modelo_datos_pfi75.md` §5 la leyenda en prosa (línea ~334) todavía usa emojis (✅ ❌ ⚠️ 🖥️ 🧪) y el bloque mermaid fuente también: el reemplazo por texto está solo en los renders. Si se vuelve a renderizar desde el `.md`, reaparecerían.
3. `[desplegado]` reemplaza ✅ también en nodos que dicen "probado/verificado desde local" (Upstash, Supabase, Gemini): el matiz queda en el texto del nodo. 🧪 (SMTP) quedó como `[solo tests]`.
4. Los nombres difieren del esquema del pedido (`er_postgres.pdf`, `despliegue.pdf` únicos) porque ER y despliegue se partieron en dos cada uno.
5. Tres PDF (`clases_api_schemas_config`, `clases_api_schemas_accion_health`, `clases_api_scoring_orquestacion`) son más angostos que 21,2 cm (15–20 cm); a ancho 13,5 cm en LaTeX el texto queda algo más grande que en el resto. Sin problema.
