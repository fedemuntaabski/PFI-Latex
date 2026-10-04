# Integración del capítulo de requerimientos (v75)

Rama: `feature/cap-requerimientos-v75` (desde `fix/bib-detalles-pfi75`). Sin commits. `main.tex` y preámbulo sin cambios.

## 1. Reemplazo del capítulo
- `chapters/chapter03.tex`: líneas 1–392 (desde `\chapter{Requerimientos, Casos de Uso e Historias de Usuario}` hasta la línea previa a `\chapter{Justificación de Diseño y Mockups}`) reemplazadas por `\input{chapters/requerimientos}`.

### Labels del bloque viejo
| Label viejo | Existe en `requerimientos.tex` | `\ref` fuera del bloque viejo |
|---|---|---|
| `tab:actores` | sí (l.16) | no |
| `tab:rf-modulo1`–`6` | sí (l.48–162) | no |
| `tab:rnf` | sí (l.209) | no |
| `sec:casos-de-uso` | sí (l.251) | no |

Los únicos `\ref` a esos labels estaban dentro del bloque viejo (`chapter03.tex:31`) o están en `requerimientos.tex`. No hay referencias huérfanas. Labels nuevos sin equivalente viejo: `chap:requerimientos`, `tab:rf-modulo7`, `sec:cu01`–`04`, `sec:historias-usuario`, `sec:matriz-trazabilidad`, `tab:trazabilidad`, etc.

## 2. Remapeo de IDs (capítulo Justificación de Diseño y Mockups)
Numeración "antes" = `chapter03.tex` original; "después" = archivo actual.

| Antes (línea) | Después (línea) | Cambio |
|---|---|---|
| 399 | 9 | `RF-12 a RF-17, RNF-08, RNF-09` → `RF-12 a RF-17, RNF-07, RNF-15` |
| 435 | 45 | Login: `RNF-09` → `RNF-15` |
| (nueva) | 47 | Login: fila `HU-14 / RNF-03` agregada |
| 443 | 55 | `RF-12` → `RF-16` (texto Usuarios) |
| 468 | 80 | `RF-12` → `RF-16` |
| 470 | 82 | `RNF-09` → `RNF-15` |
| 511 | 123 | `RF-12` → `RF-16` (Detalle) |
| 513 | 125 | `RNF-09` → `RNF-15` |
| 546 | 158 | `RNF-09` → `RNF-15` (Alertas) |
| 554 | 166 | `(RF-13 a RF-17)` → `(RF-12 a RF-15 y RF-17; la periodicidad corresponde a RF-18)` |
| 585 | 197 | `RF-13, RF-14` → `RF-12, RF-14, RF-15, RF-18` |
| 587 | 199 | `RF-15` → `RF-12` (rangos desde/hasta) |
| 589 | 201 | `RNF-08` → `RNF-07` |
| 591 | 203 | `RNF-09 / consistencia` → `RNF-15 / consistencia` |
| 655 | 267 | `RNF-09` → `RNF-15` (Estado del sistema) |
| 686 | 298 | `RF-12 (complementario)` → `RF-16 (complementario)` |

Sin cambio (ID sigue vigente): RF-09 (484→96, 509→121), RF-17 (597→209, 622→234), RNF-11 (515→127, 624→236), CU-01, CU-02.

### Decisiones de criterio (revisar)
- **Pantalla Umbrales (l.197 / 166):** agregué RF-15 (notificaciones por nivel) y RF-18 (periodicidad), que no figuraban en tu tabla de equivalencias, porque los sub-formularios de la pantalla los cubren. RF-13 (cantidad de niveles) no se cita: el requerimiento nuevo dice que se define por API y el dashboard solo edita rangos.
- **Línea 166:** el texto "CU-02 completo" ya no vale con la numeración nueva (periodicidad pasó a CU-03); lo acoté a lo que dice el párrafo.
- **Línea 9:** conservé "RF-12 a RF-17" (módulo 4 completo) sin sumar RF-09/RF-18.

## 3. Referencias pendientes en `requerimientos.tex`
- l.314: `\ref{sec:encuesta}` → `\ref{sec:encuesta-usuarios}` (label ya existente en `chapter04.tex:414`; no se agregó ninguno).
- `[[ESTADO SEGÚN P-C6]]` (RNF-01, RNF-02) y `[[ESTADO SEGÚN P-C10]]` (RNF-09) sin tocar.

## 4. Compilación
Comando: `latexmk -pdf main.tex` en una copia del árbol fuera del repo (sin `.git` ni auxiliares).

> Nota: compilar con `-outdir` fuera del árbol dejó "undefined reference" falsos (`tab:trazabilidad`, `sec:requerimientos-funcionales`): MiKTeX lee el `main.aux` viejo de la raíz del repo. En copia limpia desaparecen. Conviene borrar `main.aux` de la raíz o compilar con `-aux-directory`.

- Errores: **0**.
- Referencias sin resolver (`\ref`/`\cite`): **0**.
- Páginas: **181** (base antes del cambio: 176). Capítulo nuevo: pp. 29–46 (antes 29–41); Mockups ahora arranca en p. 47.
- Índice: máximo nivel = `subsubsection` (12 chapter / 46 section / 78 subsection / 38 subsubsection). Respeta el límite.
- **Overfull `\hbox` en el capítulo nuevo: 46** (base: 0). Todos dentro de `requerimientos.tex`:
  - 24 en las `longtable` de RF/RNF (alignment 7.53 pt, párrafos 3.48 pt): líneas 46–61, 64–85, 88–107, 110–133, 136–157, 160–181, 184–201, 207–248. Causa: las tablas suman 14.6 cm de columnas y exceden el ancho de texto por ~2.6 mm.
  - Párrafos sueltos: 105–106 (25.3 pt), 226, 228–229, 230, 242, 266–267, 515, 519 (de 1.6 a 13.9 pt).
  - Es contenido/anchos del archivo nuevo, que no se modificó; si querés corregirlo, reducir el ancho de la columna "Requerimiento" (~0.3 cm) elimina la mayoría.
