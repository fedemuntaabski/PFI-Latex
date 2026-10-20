# Informe de correcciones E75 — tanda 3

Rama: `correcciones-e75-revision`. Sin push. Solo contenido; sin cambios de preámbulo, estilos, numeración ni paquetes. No se tocaron 1.1.1, 1.2 ni 1.3.

## Cambios aplicados

| ID | Archivo | Estado |
|---|---|---|
| P1-A | chapters/chapter02.tex (2.2.6) y chapters/e50_mercado.tex (11.3, punto 3) | Aplicado: ambas usan `\ref{sec:ea-edr}`. La causa era un carácter de control (retorno de carro) en lugar de `\r` en `\ref`. Verificado: sin bytes de control sueltos en los `.tex`. |
| P1-B | biblio.bib, chapters/negocio.tex (12.3 y fuente de la tabla 12.II) | Aplicado: eliminadas `Upstash2026Pricing` y `Supabase2026Pricing`; agregada la frase "Los precios corresponden a los publicados por los proveedores en octubre de 2026." Sin citas restantes. |
| P1-C | chapters/chapter04.tex (3.6.1) | Aplicado |
| P1-D | chapters/chapter04.tex (título y texto de 3.6.5, 3.6.9) | Aplicado; `\ref{sec:mapeo-agente}` (8.4). |
| P1-E | — | **Pendiente**: sin cambios hasta que el autor confirme el umbral. Diagrama `05_objetos_evento.tex:110` dice 0.0874; tablas 8.II (`datos.tex:112`) y 10.VII (`pruebas.tex:284`) dicen 0,1180. |
| P2-A | biblio.bib (Liu2008, Hochreiter1997, Malhotra2016, Gama2014, Welford1962); chapter02.tex (2.1.5.1, 2.1.5.2, 2.1.7.1, 2.1.7.3); producto.tex (9.2.2) | Aplicado |
| P2-B | biblio.bib (Fielding2000, Rescorla2018, Haber1991); chapter02.tex (nueva 2.1.10, `sec:fundamentos-tecnicos`, e intro de 2.1); chapter01.tex (1.5); arquitectura.tex (inicio de 7.2) | Aplicado |
| P2-C | chapters/chapter04.tex (intro de la sección 3) | Aplicado; `\ref{chap:mercado}`. |
| P2-D | chapters/requerimientos.tex (4.5.3) | Aplicado; la tabla 9.IV conserva la fila "Reentrenamiento fallido registrado como en curso" (`producto.tex:228`). Se mantuvo el `\ref{sec:sintesis-limitaciones}` existente. |
| P2-E | chapters/requerimientos.tex (HU-02, HU-03, HU-14, HU-15) | Aplicado |
| P2-F | chapters/arquitectura.tex (7.2) | Aplicado; el resto de la oración ya estaba en presente. |
| P3-A | chapters/appendix/surveys.tex | Aplicado: `\caption[corto]{...}` en 15 figuras (B.2 a B.17, salvo B.1 y B.6, que ya eran cortas). Sin superposiciones restantes en las listas de figuras y de tablas. |
| P3-B | chapter02.tex (ABAC en 2.1.4.2; título de 2.2.2.2) | Aplicado. No había menciones textuales del título anterior; el label `sec:ea-ueba-dl` no cambia. |

## No aplicado

- **P1-E**: a la espera del valor vigente.
- **P3-C** (figura 6.3): no se modificó. El ancho del diagrama (≈ 1495 pt) lo fijan las coordenadas absolutas de las cinco columnas de clases (hasta x = 40,4 cm), no la cantidad de líneas de atributos; resumir las constantes de `config` y `collectors` solo reduce la altura, y la figura queda limitada por el ancho. No se compiló una versión alternativa; la conclusión surge del análisis de la geometría del `.tex`. Mejorar la escala exigiría reubicar clases, lo que la consigna excluye.
- **Consentimiento de los entrevistados** (final de 3.5.1): no agregado; falta confirmación del autor.

## Verificación

- `latexmk -pdf main.tex` compila sin errores ni referencias o citas indefinidas.
- `pdftotext` sobre el PDF: 0 apariciones de `efsec`, `ref{`, `chap:`, `tab:` y `??`. Las apariciones de `sec:` y `fig:` corresponden a código en los diagramas de clases (claves Redis `scoring:config:...`), no a referencias rotas.
- La sección 2.1.10 aparece en el índice y en el cuerpo.

## Notas

1. Los archivos `.tex` tienen finales de línea CRLF en la copia de trabajo; las ediciones los conservaron.
2. Las `\parencite` nuevas usan claves verificadas en `biblio.bib`.
