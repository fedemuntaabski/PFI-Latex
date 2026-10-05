# Integración producto v75

Rama `feature/cap-producto-v75` (desde `feature/cap-pruebas-v75`). Sin push, sin trailers, preámbulo y `chapters/producto.tex` sin modificar.

## main.tex
Línea 265 nueva: `\input{chapters/producto} % provisorio: reordenar luego`, inmediatamente antes de `\input{chapters/pruebas}` (ahora línea 266).

## Referencias de producto.tex
- `chap:requerimientos` -> chapters/requerimientos.tex:2 OK
- `chap:pruebas` -> chapters/pruebas.tex:2 OK
- `sec:validacion-escenarios` -> chapters/pruebas.tex:240 OK

## Compilación (aux borrados con `git clean -fdX`, latexmk)
- Errores: 0
- \ref/\cite sin resolver: 0
- Overfull \hbox en producto.tex: 0
- Páginas: 205 (antes 196)
- Índice: tocdepth=3 (14 chapter, 62 section, 94 subsection, 38 subsubsection)

## Marcadores `[[...]]` en el documento (6 líneas, 10 marcadores)
| Archivo:línea | Marcador |
|---|---|
| chapters/producto.tex:127 | [[ESTADO SEGÚN RNF-02]] |
| chapters/pruebas.tex:200 | [[CPU MEDIA]] [[CPU P95]] [[CPU MÁX]] |
| chapters/pruebas.tex:202 | [[RSS MEDIA]] [[RSS P95]] [[RSS MÁX]] |
| chapters/pruebas.tex:206 | [[INTERPRETACIÓN DE RNF-02 SEGÚN EL RESULTADO]] |
| chapters/pruebas.tex:309 | [[RESULTADOS DE LA EVALUACIÓN HEURÍSTICA: ...]] |
| chapters/requerimientos.tex:220 | [[ESTADO SEGÚN RNF-02]] |

