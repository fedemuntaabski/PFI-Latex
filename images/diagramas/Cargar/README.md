# Diagramas de arquitectura (TikZ)

Cada diagrama es un `.tex` `standalone` que se compila solo y genera su `.pdf`. Todos cargan los estilos de `estilos_uml.tex`, que tiene que estar en la misma carpeta. Usan solo TikZ y librerías estándar, sin `tikz-uml`.

| Archivo | Contenido |
|---|---|
| `01_flujo_informacion` | Flujo de un evento: agente → API → Redis/Postgres → IAM/correo → respuesta → enforcement → confirmación. Incluye contingencia (buffer + circuit breaker), lectura del dashboard y reentrenamiento offline |
| `02_componentes_protocolos` | Componentes y despliegue (host Windows, EC2 con Caddy/API/Keycloak, SaaS, estación local) con el protocolo de cada conexión |
| `03_clases_agente_pep` | Clases y módulos de `agent/` (exhaustivo) |
| `04_clases_api_paquetes` | Vista de paquetes de `api/app/scoring/` e índice de las láminas 04a–04e |
| `04a_clases_api_estado` | Estado en Redis: `UserScoringState` y sus partes, `redis_state`, claves Redis |
| `04b_clases_api_scoring` | Pipeline de scoring: `hybrid_service`, IsoForest, LSTM, features, baseline personal, drift, XAI, artefactos |
| `04c_clases_api_iam_auth` | `IAMProvider` y sus implementaciones, `iam_service`, `auth`, `dedup_service`, `notifications` |
| `04d_clases_api_persistencia_config` | `routes` (endpoints y nivel de auth), `main`, `config_store`, `history_store`, reentrenamiento y gate, tablas Postgres |
| `04e_clases_api_schemas` | Contratos HTTP (`schemas.py`, pydantic) |
| `05_objetos_evento` | Diagrama de objetos: instantánea de un `POST /eventos` (valores ilustrativos) |

## Uso en el documento

PDF ya compilado (es la opción más simple):

```latex
\usepackage{graphicx}
\includegraphics[width=\linewidth]{diagramas/01_flujo_informacion.pdf}
```

Los diagramas de clases son grandes (son exhaustivos). Conviene ponerlos en una página apaisada (`pdflscape`) o a página completa con `width=\linewidth, height=\textheight, keepaspectratio`.

Desde el fuente, para que el texto use la tipografía del documento:

```latex
\usepackage{standalone}  % en el preámbulo, junto con tikz y las librerías de estilos_uml.tex
\includestandalone[width=\linewidth]{diagramas/01_flujo_informacion}
```

## Recompilar

```
pdflatex 01_flujo_informacion.tex
```

Hace falta `pdflatex` (MiKTeX o TeX Live) con los paquetes `tikz`, `standalone`, `underscore` y `lmodern`.
