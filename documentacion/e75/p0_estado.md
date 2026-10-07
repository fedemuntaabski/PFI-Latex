# P0 — Estado previo al paquete E75

Fecha: 07/10/2026. Entrega E75: 20/10/2026. Este informe no modifica contenido del documento.

## 1. Estado de ramas

- Rama al iniciar: `e75/correcciones-forma` (L1, tip `854eee0`).
- `main` (= `origin/main`) está en `8ec7d82 primer commit`: es un stub, no contiene el documento.
- L1 **no está mergeada** en `main` ni en ninguna otra rama. Desciende linealmente de
  `refactor/estructura-v75` (`87af6b0`), que es la última versión integrada del documento
  (v75), y le suma las cuatro tandas de forma más el registro (`5157d99`..`854eee0`).
- `e75/contenido-nuevo` (L2) **no existe** (ni local ni en `origin`). No hay secciones que
  comparar con T2, T3, T4, T6, T7, T9, T11, T12 y T19: todos esos bloques se aplican desde cero.

## 2. Rama creada

- `e75/paquete` creada desde el tip de L1 (`854eee0`), por decisión explícita: `main` no se toca.
- Los insumos estaban en `documentacion/` y no en `documentacion/e75/`; se movieron a
  `documentacion/e75/` (`textos_e75.md`, `modelo_financiero.py`, `logo_umbral.svg`,
  `logo_umbral.png`).
- `README.md` tiene una modificación previa sin commitear (`c` → `pdflatex main`); queda fuera
  de este commit.

## 3. Detección

### 3.1 Línea "Fuente"

No existe un comando `\fuente`. El documento usa, dentro del float y después de
`\caption`/`\label`:

```latex
{\small Fuente: elaboración propia.\par}
```

48 apariciones (21 "elaboración propia.", 18 "elaboración propia a partir de los resultados…",
9 "elaboración propia, captura del sistema."). Al aplicar los bloques:
`\fuente{Elaboración propia.}` → `{\small Fuente: elaboración propia.\par}` (minúscula después de
"Fuente:", como en el resto del documento). En `longtable` va inmediatamente después de
`\end{longtable}`, como ya indican los bloques.

### 3.2 Niveles y numeración

- Clase `book`; primer nivel `\chapter`, luego `\section`/`\subsection`/`\subsubsection`
  (`secnumdepth` = 3). Coincide con lo que suponen los bloques.
- Capítulos numerados en arábigo: 1 Introducción, 2 Antecedentes, 3 Análisis comparativo del
  estado del arte, 4 Requerimientos, casos de uso e historias de usuario, 5 Justificación de
  diseño y mockups, 6 Diagramas UML, 7 Arquitectura y tecnologías, 8 Datos, 9 Producto
  implementado, 10 Pruebas y resultados, 11 Análisis de mercado y competitividad.
- Bibliografía sin número (`\addcontentsline`); anexos tras `\appendix`.
- Tablas: `\thechapter.\Roman{table}` (p. ej. 3.VII).
- Con T16 como capítulo nuevo tras Mercado, sería el 12; T19 (Conclusiones) el 13, antes de la
  bibliografía. El orden se fija en `main.tex` con `\input` (no es preámbulo).

### 3.3 Bibliografía

- Archivo: `biblio.bib` (biblatex + biber, estilo `iso-authoryear`).
- Rose 2020 (NIST SP 800-207) → **`Rose2020`**.
- Landauer 2022b (CLUE-LDS, Zenodo, doi 10.5281/zenodo.7119953) → **`Landauer2022Dataset`**.
  (`Landauer2022` es el artículo de IEEE BigData.)
- T22 trae `henderson1970`, que ya existe como **`Henderson1970`**: no agregar la entrada; si se
  cita, usar la clave existente. Las demás claves de T22 (`osterwalder2010`, `larman2003`,
  `ley25326`, `ley20744`, `ley27483`, `aaip2018`, `dnpdp2016`) no existen y no chocan.

### 3.4 Floats y tablas largas

- `longtable`: **disponible** (`\usepackage{array,longtable}`).
- `float` (`[H]`): **no cargado**. El documento usa `[h]` + `\FloatBarrier` (paquete
  `placeins`). Como no se toca el preámbulo: en T9 (tabla) y T18 (figura) reemplazar `[H]` por
  `[h]` y agregar `\FloatBarrier` después del entorno.

### 3.5 Carpeta de figuras

No hay `\graphicspath`; las figuras se referencian como `images/...` (subcarpetas `diagramas`,
`mockups`, `pruebas`). T18 usa `figuras/logo_umbral.png` → usar `images/logo_umbral.png`.

### 3.6 Etiquetas

Las etiquetas de capítulo existentes usan el prefijo `chap:`, no `cap:`. Capítulos 1, 2, 3, 5 y
6 no tienen etiqueta. De las secciones pedidas, seis no tienen etiqueta (ver mapa, sección 6).

## 4. Logo

`documentacion/e75/logo_umbral.png` copiado a `images/logo_umbral.png`.

## 5. Modelo financiero

`python -I documentacion/e75/modelo_financiero.py`:

```
Inversión inicial: USD 23.000
Ingreso mensual por cliente: USD 390  (USD 5.20 por endpoint)
Margen de contribución mensual por cliente: USD 283
  Punto de equilibrio año 1: 13.3 clientes activos
  Punto de equilibrio año 2: 22.1 clientes activos
  Punto de equilibrio año 3: 32.7 clientes activos
  Punto de equilibrio año 4: 39.8 clientes activos
  Punto de equilibrio año 5: 43.3 clientes activos

Pesimista: VAN=-202.527 TIR=no existe payback=no recupera descontado=no recupera necesidad máx. de fondos=360.837
  año 1: clientes 5 ingresos 13.656 flujo -50.105
  año 2: clientes 14 ingresos 47.011 flujo -70.935
  año 3: clientes 30 ingresos 107.691 flujo -92.966
  año 4: clientes 41 ingresos 170.242 flujo -71.640
  año 5: clientes 49 ingresos 213.642 flujo -52.192
  sensibilidad VAN: {'20%': '-223.337', '30%': '-184.970', '35%': '-170.030'}

Base: VAN=35.084 TIR=38,8 % payback=3,8 años descontado=4,5 años necesidad máx. de fondos=100.894
  año 1: clientes 11 ingresos 28.297 flujo -42.496
  año 2: clientes 41 ingresos 129.175 flujo -35.398
  año 3: clientes 86 ingresos 309.088 flujo 17.228
  año 4: clientes 132 ingresos 522.725 flujo 101.831
  año 5: clientes 168 ingresos 712.449 flujo 195.938
  sensibilidad VAN: {'20%': '54.826', '30%': '19.633', '35%': '7.456'}

Optimista: VAN=336.532 TIR=131,8 % payback=2,2 años descontado=2,4 años necesidad máx. de fondos=50.251
  año 1: clientes 22 ingresos 57.616 flujo -27.251
  año 2: clientes 74 ingresos 237.985 flujo 28.086
  año 3: clientes 150 ingresos 543.689 flujo 140.224
  año 4: clientes 236 ingresos 925.131 flujo 311.523
  año 5: clientes 307 ingresos 1.289.189 flujo 500.375
  sensibilidad VAN: {'20%': '406.266', '30%': '280.320', '35%': '234.598'}
```

(La consola de Windows muestra mal las tildes; la salida se transcribe con la codificación
corregida, sin cambiar ningún número.)

Cotejo con T16/T17: **coincide**.

| Dato en el texto | Texto | Script |
|---|---|---|
| Inversión inicial | USD 23.000 | 23.000 |
| Ingreso por cliente / margen | USD 390 / USD 283 | 390 / 283 |
| Punto de equilibrio | 13 → 43 clientes | 13,3 → 43,3 |
| Base: VAN, TIR | USD 35.084; 38,8 % | 35.084; 38,8 % |
| Base: payback simple / descontado | 3,8 / 4,5 años | 3,8 / 4,5 |
| Base: VAN al 35 % | USD 7.456 | 7.456 |
| Base: necesidad de fondos | USD 100.894 | 100.894 |
| Optimista: VAN, payback | USD 336.532; 2,2 años | 336.532; 2,2 |
| Pesimista: necesidad de fondos | USD 360.837 | 360.837 |
| LTV (T16) | 283 / 0,02 = 14.150 | margen 283, churn base 2 % |

Las tablas de T17 marcadas `[TABLA: ...]` se generan con `--latex` al aplicar el bloque.

## 6. Mapa de etiquetas: `textos_e75.md` → documento

"CREAR" = no existe; agregar `\label` en la línea indicada al aplicar el paquete.

| Etiqueta en textos_e75.md | Etiqueta real | Ubicación |
|---|---|---|
| `cap:antecedentes` | CREAR (`chap:antecedentes`) | `chapters/chapter02.tex:1` |
| `cap:comparativo` | CREAR (`chap:comparativo`) | `chapters/chapter04.tex:1` |
| `cap:requerimientos` | `chap:requerimientos` | `chapters/requerimientos.tex` |
| `cap:diseno` | CREAR (`chap:diseno`) | `chapters/e50_diseno_ux.tex:1` |
| `cap:uml` | CREAR (`chap:uml`) | `chapters/e50_uml.tex:1` |
| `cap:arquitectura` | `chap:arquitectura` | `chapters/arquitectura.tex` |
| `cap:datos` | `chap:datos` | `chapters/datos.tex` |
| `cap:producto` | `chap:producto` | `chapters/producto.tex` |
| `cap:pruebas` | `chap:pruebas` | `chapters/pruebas.tex` |
| `cap:mercado` | `chap:mercado` | `chapters/e50_mercado.tex` |
| `cap:negocio` | nuevo → `chap:negocio` | T16 |
| `cap:conclusiones` | nuevo → `chap:conclusiones` | T19 |
| (cap. 1, sin uso en textos) | sin etiqueta | `chapters/chapter01.tex:1` |
| `sec:punto-ciego` (2.1.1) | CREAR | `chapters/chapter02.tex:9` |
| `sec:sintesis-diferenciadores` (3.4) | CREAR | `chapters/chapter04.tex:382` |
| `sec:validacion-diseno` (3.5.2) | CREAR | `chapters/chapter04.tex:401` |
| `sec:encuesta` (3.6) | `sec:encuesta-usuarios` | `chapters/chapter04.tex:416` |
| `sec:conjunto-datos` (8.1) | `sec:dataset` | `chapters/datos.tex:7` |
| `sec:modelo-relacional` (8.5.1) | CREAR | `chapters/datos.tex:145` |
| `sec:cumplimiento-requerimientos` (9.3) | `sec:cumplimiento` | `chapters/producto.tex:101` |
| `sec:integracion-continua` (10.2.3) | CREAR | `chapters/pruebas.tex:100` |
| `sec:escenarios` (10.6) | `sec:validacion-escenarios` | `chapters/pruebas.tex` |
| `sec:interpretacion` (10.6.4) | CREAR | `chapters/pruebas.tex:300` |
| `sec:marco-legal`, `sec:metas-modelo`, `sec:tratamiento-datos` | nuevas | T11, T9, T12 |
| `tab:canvas`, `tab:cumplimiento-objetivos`, `tab:metas-modelo`, `tab:supuestos-fin`, `tab:tratamiento-datos`, `fig:logo` | nuevas, sin conflicto | T16, T19, T9, T17, T12, T18 |

Claves de cita a ajustar al aplicar:

| En textos_e75.md | Clave real |
|---|---|
| `rose2020` | `Rose2020` |
| `landauer2022b` | `Landauer2022Dataset` |
| `henderson1970` (T22) | `Henderson1970` (ya existe) |

## 7. Otros avisos

- `[H]` no compila sin `float`: usar `[h]` + `\FloatBarrier` (3.4).
- `\fuente{...}` no existe: usar la forma de 3.1.
- El bloque T9 tiene `[[VERIFICAR]]` sobre el comando de fuente: queda resuelto por 3.1.
- `README.md` modificado fuera de este paquete; no se commitea.
