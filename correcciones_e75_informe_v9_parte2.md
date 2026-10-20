# Correcciones E75 — informe v9, parte 2

Rama `correcciones-e75-revision`. Sin push. Fuente: `informe_fixes_e75_ronda3.md` y `capturas_e75/`.

## 2.1 Integración continua (10.2.3)
La corrida 39476821123 sobre `605cca3` aprobó los cuatro trabajos. La oración de `chapters/pruebas.tex` pasó a «Sobre la versión que incluye las correcciones descritas en la sección~\ref{sec:estado-despliegue}, el pipeline finaliza con los cuatro trabajos aprobados.» El informe de código no dice expresamente que la rama `fix/e75-limitaciones-menores` contenga todas las correcciones de 9.3: confirmalo.

## 2.2 Capturas
| Figura | Archivo reemplazado | Captura nueva |
|---|---|---|
| 5.2 | mockup-login-real.png | 01_login.png |
| 5.4 | mockup-usuarios-real.png | 02_usuarios.png |
| 5.6 | mockup-detalle-real.png | 03_detalle.png |
| 5.8 | mockup-porque-real-1.png | 04_explicacion_arriba.png |
| 5.9 | mockup-porque-real-2.png | 05_explicacion_senales.png |
| 5.11 | mockup-alertas-real.png | 06_alertas.png |
| 5.13 | mockup-umbrales-real-1.png | 07_umbrales_arriba.png |
| 5.14 | mockup-umbrales-real-2.png | 08_umbrales_abajo.png |
| 5.16 | mockup-auditoria-real.png | 09_auditoria.png |
| 5.18 | mockup-estado-real.png | 10_salud.png |
| 5.20 | mockup-historial-real.png | 11_historial.png |
Las figuras 5.2 a 5.20 se verificaron contra `main.lof` y los captions. Mismos nombres y ancho; los `\includegraphics` no cambiaron. El documento sigue con 283 páginas.

### Ajustes de texto (`chapters/e50_diseno_ux.tex`)
1. Detalle de usuario: se agregó «En la captura, el usuario es nuevo y todavía no tiene días cerrados, por lo que en lugar del gráfico se muestra ese aviso.», porque la captura 03 no muestra el gráfico del histórico.
2. Auditoría: el tipo de cambio pasó a «por ejemplo, Acción por nivel, Periodicidad, Notificaciones, Proveedores de identidad o Umbral de aprendizaje», que es lo que muestra 09.
3. Sin cambios, y siguen siendo ciertas: «La captura muestra usuarios en niveles alto y crítico» (06 muestra 1 Crítico y 4 Alto); «Por qué pasó esto» (3 señales, aprendizaje 17/21, acción «alertar»); Estado del sistema (8 artefactos); Con historial. No hay cantidades de usuarios ni de entradas de auditoría en el texto.

### Riesgos que quedan en las capturas (decidido por el autor: usar las 11 tal cual)
- 08: dos correos reales de administradores y entradas de prueba del log («test-rev75 no usar», «x»).
- 11: uids de prueba (`big-maroon-lynx-radiocontroller`, `digital-harlequin-possum-procuratorfiscal`, `structural-teal-starfish-homeeconomist`, `test-hu15-explicacion-uid`, `test-hybrid-backdated-uid`).
- 09: `[object Object]` en entradas de IAM (defecto de visualización).
- 02 y 06: `FEDE-PC-FEDE` (host real) y `demo-pfi`; 02 con «Sin reportar hace N min».
- El usuario crítico está en aprendizaje (la acción mostrada es «alertar»).

### Wireframes
Los 11 `mockup-*-wireframe.png` dicen «UEBA Dashboard» en la barra. Son PNG sin fuente editable en el repo (no hay TikZ, SVG ni HTML): no se tocaron. Hay que regenerarlos por fuera del repo para cambiarlos a «UMBRAL».

## 2.3 Consentimiento
Confirmado por el autor en este chat. Al final de 3.5.1 (Perfil de los especialistas consultados) se agregó «Los cinco profesionales autorizaron la publicación de su nombre y de sus respuestas.»

## Compilación desde cero
Sin errores, sin referencias indefinidas ni `??`. 283 páginas, «Página X de 281» en las 281 numeradas.
