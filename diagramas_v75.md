# Diagramas v75 (Mermaid -> PDF/PNG)

Fuente: `modelo_datos_pfi75.md` del repo PFI (no está en este repo; leído desde `G:\pfi\Agente-Aut-...\`, sin modificar). Render: `npx @mermaid-js/mermaid-cli` (sin dependencias nuevas), PDF vectorial + PNG (escala 4, >= 530 dpi a 15 cm de ancho). Salida: `images/diagramas/v75/`. No se tocó ningún `.tex`; no hay commit.

## Archivos (14 PDF + 14 PNG)

Original 9 diagramas -> 14 archivos, porque 4 se partieron (ver abajo).

| Archivo (.pdf/.png) | Ancho natural x alto (px CSS) | PNG (px) | Fuente a 15 cm | Fuente a 12 cm |
|---|---|---|---|---|
| `clases_agente_collectors` | 1133 x 400 | 3136 x 1108 | 6.0 pt | 4.8 pt |
| `clases_agente_enforcement` | 1011 x 588 | 3136 x 1824 | 6.7 pt | 5.4 pt |
| `clases_api_iam_auth_config` | 1218 x 586 | 3136 x 1512 | 5.6 pt | 4.5 pt |
| `clases_api_persistencia` | 828 x 598 | 3136 x 2268 | 8.2 pt | 6.6 pt |
| `clases_api_redis` | 1066 x 676 | 3136 x 1992 | 6.4 pt | 5.1 pt |
| `clases_api_schemas_accion_health` | 552 x 118 | 2212 x 472 | 12.3 pt | 9.9 pt |
| `clases_api_schemas_config` | 735 x 260 | 2944 x 1040 | 9.3 pt | 7.4 pt |
| `clases_api_schemas_eventos` | 815 x 339 | 3136 x 1308 | 8.3 pt | 6.7 pt |
| `clases_api_scoring_modelos` | 1169 x 434 | 3136 x 1168 | 5.8 pt | 4.7 pt |
| `clases_api_scoring_orquestacion` | 670 x 414 | 2680 x 1656 | 10.2 pt | 8.1 pt |
| `despliegue_aws` | 968 x 900 | 3136 x 2916 | 7.0 pt | 5.6 pt |
| `despliegue_local` | 968 x 742 | 3136 x 2404 | 7.0 pt | 5.6 pt |
| `er_postgres_config_modelos` | 1047 x 694 | 3136 x 2084 | 6.5 pt | 5.2 pt |
| `er_postgres_scoring_eventos` | 820 x 952 | 3136 x 3644 | 8.3 pt | 6.6 pt |

"Fuente a 15/12 cm" = tamaño efectivo del texto base de Mermaid (16 px) al insertar el PDF con ese ancho. Criterio usado: >= ~6 pt a 15 cm.

## Cambios de contenido

- **Despliegue**: emojis reemplazados por texto entre corchetes: ✅ `[desplegado]`, ❌ `[no creado]`, ⚠️ `[a verificar]`, 🖥️ `[solo local]`, 🧪 `[solo tests]`. Se quitaron palabras que quedaban duplicadas ("no creada", "tests,"), nada más. La leyenda con emojis (L334 del .md) está fuera del bloque Mermaid y no se renderiza.
- `clases_api_iam_auth_config`: **el diagrama original no compila** en Mermaid (`Parse error ... Expecting 'NEWLINE', 'EOF', got 'LABEL'`) por la etiqueta `agent_key:{hash}`. Para renderizar se cambió a `agent_key (hash)` y `config:*` a `config (prefijo)`. El `.md` fuente sigue con el error.

## Diagramas partidos (no se leían a 12–15 cm: 3,2–4,2 pt)

| Original | Partes | Criterio |
|---|---|---|
| `er_postgres` (3,9 pt) | `er_postgres_scoring_eventos` (historial_scores, eventos_crudos, drift_alerts) · `er_postgres_config_modelos` (politicas, reentrenamientos, metricas_modelo, agent_keys) | Cada parte conserva sus relaciones |
| `clases_api_schemas` (3,2 pt) | `_eventos` · `_config` · `_accion_health` | Clases sueltas en una sola fila ancha |
| `clases_api_scoring` (4,2 pt) | `_orquestacion` · `_modelos` | `hybrid_service` aparece en ambas para conservar sus relaciones |
| `despliegue` (4,0 pt) | `despliegue_local` · `despliegue_aws` | Los servicios externos se repiten en cada parte; ambos con layout `TB` y `%%{init}%%` de espaciado (no cambia contenido) |

Los PDF/PNG de los originales sin partir se eliminaron para que no se use por error una versión ilegible.

## Problemas pendientes

- Por debajo de 6 pt a 15 cm: `clases_api_iam_auth_config` (5,6), `clases_api_scoring_modelos` (5,8). A 12 cm, bajo 5 pt: `clases_agente_collectors` (4,8), `clases_api_iam_auth_config` (4,5), `clases_api_scoring_modelos` (4,7). Se recomienda insertarlos a 15 cm; si deben ir más chicos, partirlos.
- `hybrid_service` se dibuja con `<> process_event`: en el `.md` está escrito `{ <<module>> process_event }` en una línea y Mermaid pierde el estereotipo. Es de la fuente, no del render.
- Los PNG y PDF salen con el ancho ya escalado por Mermaid (800 px fijo); el tamaño real de texto depende del ancho natural de la tabla.
- Verificación visual hecha sobre `er_postgres` (previo al split), `clases_api_scoring` (previo), `despliegue_aws`, `despliegue_local` y `clases_api_scoring_modelos`; el resto se juzgó por la métrica de fuente, no a ojo.
