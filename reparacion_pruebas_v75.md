# Reparación cap. pruebas v75

Rama: `feature/cap-pruebas-v75`. Sin push. Sin trailers. main.tex y preámbulo sin tocar. Stash intacto.

## 1. Estado previo
Working tree: `M chapters/requerimientos.tex`, `M images/pruebas/curva_umbral.pdf`.

| Rama | git log --oneline -5 |
|---|---|
| feature/cap-requerimientos-v75 | 4a054dc integracion requerimientos / 17725cd detalles / c240892 commit / cf2b2d1 redaccion 75 / 58bb408 parte de demo y pantallas |
| feature/diagramas-v75 | f942985 cambios / 27e8167 commit / 4a054dc integracion requerimientos / 17725cd detalles / c240892 commit |
| feature/cap-pruebas-v75 (previo) | 1d65ba1 cambios bibliografia / 4a054dc / 17725cd / c240892 / cf2b2d1 |

Stash: `stash@{0}: On feature/diagramas-v75: wip-pruebas-diagramas-v75`
Archivos (`--name-status`): `M chapters/pruebas.tex`, `D images/curva_umbral.png`.

## 2-4. Verificaciones
- `curva_umbral.pdf`: vectorial (`pdfimages -list` sin imágenes), página 453.5 x 255.1 pt = 16 x 9 cm, sin metadato Title, sin título dentro del gráfico, leyenda "E1: exfiltración  E2: fuera de horario  E3: cambio de país  E4: combinado". OK.
- `requerimientos.tex`: tabla RNF categoría `p{2.9cm}` (línea 207); matriz de trazabilidad primera columna `p{3.2cm}` (línea 511). OK.

## 5-6. Compilación (latexmk, auxiliares borrados con `git clean -fdX`)
- Errores: 0
- Referencias/citas sin resolver: 0
- Páginas: 196
- Profundidad del índice: `tocdepth=3` (main.toc: 13 chapter, 56 section, 88 subsection, 38 subsubsection)
- Overfull \hbox: 6 en total, todos en `requerimientos.tex`; 0 en `pruebas.tex`. **Objetivo NO cumplido** (6 > 5; 3 > 8 pt).

| Línea(s) | Exceso | Contexto |
|---|---|---|
| 160--160 | 14.97 pt | longtable de 4 columnas; celda de cabecera "Transparencia" en columna 1.9 cm |
| 166--167 | 0.60 pt | idem (encabezado repetido) |
| 273--274 | 18.48 pt | entorno itemize |
| 300--300 | 14.97 pt | item "La API persiste la nueva política…" |
| 634--634 | 1.07 pt | |
| 667--667 | 7.32 pt | |

Mayores a 8 pt: 160, 273, 300. No corregí nada (contenido de requerimientos.tex congelado por indicación).

Nota extra: el log tiene 194 `Overfull \vbox (36.86pt too high) has occurred while \output is active` (≈70 dentro de requerimientos.tex; el resto en capítulos posteriores). No pedidos; probable longtable/flotante. No investigado.

## 7. Commit
`baeb122` en `feature/cap-pruebas-v75`: `chapters/requerimientos.tex` + `images/pruebas/curva_umbral.pdf`. main.tex, chapters/pruebas.tex y biblio.bib no tenían cambios. Sin trailers.

## 8. Comparación con el stash
- `chapters/pruebas.tex`: **idéntico** al de HEAD (`git diff stash@{0} HEAD -- chapters/pruebas.tex` vacío).
- `images/curva_umbral.png`: el stash lo **borra**. En HEAD ya no existe en esa ruta; el movimiento a `images/pruebas/curva_umbral.png` ya está en 1d65ba1 con el mismo blob (95afe9b). Contenido del stash ya contenido en HEAD.

Conclusión: el stash no aporta nada que falte en `feature/cap-pruebas-v75`. Decisión de drop: tuya.
