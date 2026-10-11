# E75 — Ajustes del capítulo 13, índice, y merge y push de `e75/cierre`

Los commits no llevan trailers Co-Authored-By ni "Generated with" (se verificó con `git log`: 0 coincidencias).

## 1. Estado (solo lectura, antes de los cambios)

| Control | Resultado |
|---|---|
| `e75/cap13-conclusiones` → ca9f27e | ✓ |
| `e75/cierre` (1a226ce) es ancestro de ca9f27e | ✓ |
| `e75/objetivos-especificos` (8378807) es ancestro de ca9f27e | ✓ |
| 641a3c8 es ancestro de ca9f27e | ✓ — **discrepancia**: la rama `e75/cap4-requerimientos` apunta a **957784d** ("docs: informes de verificación de objetivos específicos y capítulo 4"), un commit hijo de 641a3c8. 957784d también es ancestro de ca9f27e |
| `e75/cap10-pruebas` (90ad393) es ancestro de ca9f27e | ✓ |
| Fast-forward de `e75/cierre` a ca9f27e | posible ✓ |
| `git status` | **discrepancia**: había un solo archivo sin seguimiento, `docs/verificacion/e75_cap13_latex.md`, el informe anterior que se dejó fuera del commit a propósito |

El autor aprobó continuar con las dos discrepancias.

`git remote -v`:
```
origin	https://github.com/fedemuntaabski/PFI-Latex (fetch)
origin	https://github.com/fedemuntaabski/PFI-Latex (push)
```
`origin/e75/cierre` existía en 1a226ce, igual que la rama local.

## 2. Ajustes (rama `e75/cap13-ajustes`, creada desde ca9f27e)

| Punto | Archivo | Antes | Después | Commit | OK |
|---|---|---|---|---|---|
| a | chapters/conclusiones.tex:42-43 (Tabla 13.I, objetivo 6) | "produjeron modelos candidatos / que no superaron al vigente y no se promovieron" (cortado en dos líneas, 1 coincidencia) | "produjeron modelos candidatos / que la regla de promoción anterior rechazó, por lo que no se promovieron" | c2cd490 "cap13: aclara que las corridas reales las rechazó la regla anterior" | ✓ |
| b | main.tex:287-288 | `\addcontentsline{toc}{chapter}{Bibliograf\'{\i}a}` + `\printbibliography{}` | `\printbibliography[heading=bibintoc]` (el documento usa biblatex) | 36d0380 "indice: corrige el número de página de Bibliografía" | ✓ |

Causa del punto b: la entrada del índice se agregaba antes de `\printbibliography`, que abre página nueva, así que quedaba registrada con la última página de las conclusiones (186). Con `heading=bibintoc`, biblatex escribe la entrada dentro del encabezado del capítulo. Se respetó el final de línea CRLF en los dos archivos.

### Compilación y verificación

Cadena: `pdflatex` → `biber` → `pdflatex` → `pdflatex`. biber terminó sin ERROR ni WARN, y `main.log` no tiene referencias indefinidas ni avisos de recompilación. El PDF tiene 260 páginas físicas.

| Verificación (pdftotext) | Resultado |
|---|---|
| El índice dice "Bibliografía 187" (`main.toc`: `{187}{chapter*.1}`) | ✓ |
| La página "Página 187 de 258" tiene el título "Bibliografía" | ✓ |
| Total del pie: todas las páginas dicen "de 258" | ✓ |
| Frase nueva "que la regla de promoción anterior rechazó, por lo que no se promovieron" | 1 ✓ |
| Frase vieja "no superaron al vigente" | 0 ✓ |
| "??" en todo el PDF | 0 ✓ |
| Páginas con texto debajo de "Página N de M" | 0 ✓ (las páginas 1 y 2 son carátulas y no tienen pie) |

## 3. Merge y push

- `git checkout e75/cierre && git merge --ff-only e75/cap13-ajustes`: fast-forward de 1a226ce a 36d0380.
- `git push -u origin e75/cierre`: `1a226ce..36d0380  e75/cierre -> e75/cierre`, y la rama sigue a `origin/e75/cierre`. Sin force push y sin publicar las ramas intermedias.
- Hash final de `e75/cierre`: **36d03801c62cb945be8869ee29c75bb49af1cbc3**

`git log --oneline -8`:
```
36d0380 indice: corrige el número de página de Bibliografía
c2cd490 cap13: aclara que las corridas reales las rechazó la regla anterior
ca9f27e docs: conclusiones con métricas y trabajo futuro actualizado
90ad393 latex cap 10
dfa99d6 docs: corrige capítulo 10 y Tabla 13.I contra los resultados vigentes
957784d docs: informes de verificación de objetivos específicos y capítulo 4
641a3c8 docs: corrige capítulo 4 y Tabla 13.I contra el código
8378807 docs: alinea objetivos específicos 1, 3, 4 y 6 con el código
```

## Entregables

- `main.pdf`, compilado desde 36d0380, en la raíz del repo (`G:\Latex\PFI-Latex\main.pdf`; está en .gitignore).
- Este informe, sin seguimiento en git.
