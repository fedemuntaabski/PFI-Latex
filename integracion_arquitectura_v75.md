# Integración capítulo Arquitectura v75

Rama: `feature/cap-arquitectura-v75` (desde `feature/cap-datos-v75`). Sin push.

## Cambios
- `main.tex:265`: `\input{chapters/arquitectura} % provisorio: reordenar luego`, inmediatamente antes de `chapters/datos`.
- `chapters/arquitectura.tex`: sin modificar. Preámbulo sin tocar.

## Verificaciones previas
- `images/diagramas/v75/despliegue_local.pdf`: existe.
- `images/diagramas/v75/despliegue_aws.pdf`: existe.
- Clave bib `Rose2020`: existe (`biblio.bib:67`).

## Compilación (latexmk, tras borrar auxiliares ignorados)
- Errores: 0.
- `\ref`/`\cite` sin resolver: 0.
- Páginas: 228. Capítulo 10 "Arquitectura y tecnologías": págs. 100–110.
- Profundidad del índice: `tocdepth=3` (chapter, section, subsection, subsubsection presentes en `main.toc`); `secnumdepth=3`.
- Overfull `\hbox` en `arquitectura.tex`: 0 (el tramo de log 5100–5211 no contiene ninguno). Los 6 Overfull `\hbox` del documento caen en `chapter03.tex` (E50): 14.97pt, 0.60pt, 18.48pt, 14.97pt, 1.07pt, 7.32pt.
- Overfull `\vbox` (36.86pt, "output is active"): muchos, en zona previa a arquitectura (E50), no atribuibles a `arquitectura.tex`.
- Marcadores `[[...]]` (preexistentes, ninguno en arquitectura.tex):
  - `chapters/producto.tex:127`
  - `chapters/pruebas.tex:200`, `:202`, `:206`
  - `chapters/requerimientos.tex:220`

### Advertencia (no es ref sin resolver)
Labels duplicados entre capítulo nuevo y E50:
- `tab:lenguajes`: `arquitectura.tex:26` y `chapter03.tex:480`
- `tab:protocolos`: `arquitectura.tex:260` y `chapter03.tex:652`

Se resuelve solo al eliminar el capítulo "Tecnologías" de E50 (ver abajo). Hasta entonces `\ref` a esos labels apunta a una de las dos definiciones (la última).

## Obsoleto / duplicado en E50 (SOLO LECTURA, nada borrado)

Todo en `chapters/chapter03.tex`.

| Rango | Título | Notas |
|---|---|---|
| 466–674 | Capítulo "Tecnologías" completo (`\clearpage` en 466; `\label{sec:tecnologias}` en 468) | Cap. 7 en el PDF, págs. 80–91 |
| 467–474 | Intro del capítulo + monorepo con 5 subsistemas | |
| 475–502 | Sección "Lenguajes de programación" | `tab:lenguajes` en 480 |
| 503–605 | Sección "Frameworks y librerías" | API 506, Agente 538, Frontend 556, Pipeline offline 586 |
| 606–646 | Sección "Arquitectura de red" | Topología general 608 (incluye topología Docker Compose), Justificación de cada decisión de red 638 |
| 647–674 | Sección "Protocolos de comunicación" | `tab:protocolos` en 652 |
| 695–703 | Sección "Diagrama de Arquitectura" + figura `fig:diagrama-arquitectura` (`images/diagramas/diagramaarquitectura.png`) | Dentro del capítulo "Modelo de Datos" (676–703); queda reemplazada por `despliegue_local.pdf` / `despliegue_aws.pdf` |

Equivalencias en `arquitectura.tex`: Lenguajes (20), Frameworks (47), Servicios e infraestructura (156), Arquitectura de despliegue (187), Protocolos (256).

Referencias a revisar al borrar: `sec:tecnologias` (solo definido, 468) y `fig:diagrama-arquitectura` (solo definido, 701); no hay `\ref` a ellos en ningún `.tex`. Los labels duplicados `tab:lenguajes` y `tab:protocolos` desaparecen al borrar.

Posible solape (a confirmar al reordenar, no incluido en lo obligatorio): "Diagrama de flujo de información" (316–325) y "Diagrama de componentes" (327–336) del capítulo "Diagramas UML"; capítulo "Modelo de Datos" 676–693 (redis.png, supabase.png) frente a `datos.tex`.
