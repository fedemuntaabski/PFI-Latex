# Correcciones E75 — informe v9, parte 1

Rama: `correcciones-e75-revision`. Sin push.

## 1.1 Redacción de las figuras 6.1 y 6.2
`chapters/e50_uml.tex`, líneas 12 y 24 (solo esas): la frase final pasó a «La versión completa, con el detalle técnico de cada paso y conexión, se presenta en el Anexo~H.» Los párrafos de 6.3 a 6.9 (clases) no se tocaron. Finales de línea CRLF intactos (`git diff`: 2 líneas). Commit `98d7708`.

## 1.2 Detalles gráficos de las vistas de diseño
Fuentes en `images/diagramas/Cargar/*.tex`, PDF recompilado y copiado a `images/diagramas/uml/`. Commit `660436a`.
- **6.1** (`01v_flujo_informacion_diseno.tex`): el título del carril «Reentrenamiento offline (proceso aparte)» se movió de la esquina superior izquierda a la derecha (`anchor=north east`, `off.north east`); la línea punteada que baja desde PostgreSQL ya no lo cruza.
- **6.2** (`02v_componentes_protocolos_diseno.tex`): los cinco servicios gestionados se desplazaron de x=17,0 a x=18,6 cm, lo que ensancha el tramo de los ramales. «PostgreSQL/TLS» y «SMTP STARTTLS» quedan dentro del tramo, sin tocar el borde del recuadro. El título «Servicios de AWS de apoyo» pasó debajo de su recuadro porque las líneas punteadas HTTPS lo cruzaban.
- **6.3 a 6.9**: sin cambios. Las etiquetas «usa» y «crea» van sobre sus líneas, que es la convención UML y viene de `estilos_uml.tex` (no modificable). No hay etiquetas sobre cajas.
- **Pendiente menor (no corregido):** en 6.1 las tres etiquetas «HTTPS» entre carriles (Envía el evento → Valida el esquema; Inicia sesión → Atiende las lecturas; Confirma la acción → Registra la confirmación) rozan el borde de las cajas porque el hueco entre carriles es de unos 1,3 cm. Arreglarlo exige reordenar los carriles; el autor decide.
- PNG en `revision_diagramas/`: `antes-096…104.png` (las 9 páginas) y `despues-096.png`, `despues-097.png` (6.1 y 6.2). Sin commitear.

## Compilación desde cero
`latexmk -C`, `git checkout main.dvi`, `latexmk -pdf main.tex`: terminó sin errores. Los «Rerun» del registro son de pasadas intermedias; el `main.log` final no tiene referencias ni citas indefinidas. 283 páginas en el PDF, con el pie «Página X de 281» en las 281 numeradas. La búsqueda de `??`, `efsec`, `ref{` y `TODO` dio 0 en el texto. Las 12 coincidencias de `[[` son `Callable[[…]]` de los diagramas de clases (falsos positivos). No hay un script de verificación en el repo; usé `pdftotext` y `grep` sobre el PDF.

## 1.3 Revisión de coherencia (solo reporte, sin cambios)
**Sección 9.3** dice que las correcciones están implementadas y probadas en el código pero no forman parte de la release desplegada (`b499fa3`).

**a) «publicado», «desplegado», «en la instancia»**. Ninguno contradice 9.3. Quedan consistentes:
- 9.3 y la sección 10.4.3 (10.4.x, «En la instancia corre la release b499fa3», «el código desplegado pasa su propia suite»): describen el estado verificado de `b499fa3`.
- Introducción (líneas «API central desplegada en la nube», «componentes desplegados en forma independiente») y sección de herramientas («las versiones publicadas», «se publican con HTTPS»): descripciones generales, no afirman que las correcciones estén publicadas.
- «Algoritmos propietarios no publicados» y «herramienta publicada por los autores del conjunto de datos»: otro sentido.

**b) Números viejos**. Sin ocurrencias de 623, 446, 94,7, 89,3, 90,2, 93,2, 87,03 y 87,10. Las demás son falsos positivos:
- 659: «1 659» en una tabla de tamaños de muestra.
- 476: «421.476» (VAN del escenario optimista).
- 177: «Página 177» y la entrada de la BCG en el índice.
- 183: «Página 183» y «−183.466» (VAN pesimista).
- 93,5: columna del agente o de la API (no el total) en la tabla de cobertura de la sección 10; el total es 92,8.

**c) «Defectos menores del agente», «Correcciones del planificador», «pipeline en curso», «mapeo de respaldo»**. Sin ocurrencias en el PDF.

**d) Figuras de la sección 6 sin mención por número**. Ninguna: las 10 figuras tienen al menos un `\ref` en `chapters/e50_uml.tex`. La 6.4 (`fig:diagrama-clases-api`) se cita 2 veces.
