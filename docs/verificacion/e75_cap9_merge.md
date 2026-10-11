# e75 — comillas, merge y push

Commit: `61550cd docs: unifica comillas en «pipeline en curso»` (sin trailers). Las 3 «…» pasaron a ``\emph{pipeline} en curso'' (como ``Que hacer ahora:''); CRLF intacto.

## Verificación (pdftotext, 261 páginas físicas)
- «: 0, »: 0
- "pipeline en curso": 3 (cap. 4, 9 y 13), con comillas “ ”
- "??": 0
- Páginas con texto bajo "Página N de M": ninguna
- Total: "de 259" (sin cambios)

## Merge y push
`git merge --ff-only e75/cap9-producto` sobre e75/cierre: fast-forward OK.

```
To https://github.com/fedemuntaabski/PFI-Latex
   36d0380..61550cd  e75/cierre -> e75/cierre
```

Hash final: 61550cd3b9faf6e0a43f85fdeecab841267e43d5

```
61550cd docs: unifica comillas en «pipeline en curso»
1d1e1d6 cap13: protege RF-21 de cortes de línea en la Tabla 13.I y actualiza la corrección del reentrenamiento fallido
73da1ee cap7: corrige la cantidad de endpoints en la Tabla 7.II
c26e572 cap9: alinea producto con el código (loopback, clave de administración, endpoints, corridas del planificador, nuevas limitaciones)
aa1ac6c cap4: CU-03 3a con el comportamiento real del reentrenamiento fallido y nota de RF-02 en loopback
36d0380 indice: corrige el número de página de Bibliografía
c2cd490 cap13: aclara que las corridas reales las rechazó la regla anterior
```
