# P3 — Marco legal y tratamiento de datos (E75)

Rama `e75/paquete`. Fuente: `documentacion/e75/textos_e75.md` (T11, T12, T22). Compila con 0 errores,
0 referencias o citas indefinidas y sin "??" en el PDF (`pdflatex`, `biber`, `pdflatex` ×2; 219 páginas).
Antes de insertar, cada artículo citado en T11 se contrastó con el texto oficial (InfoLEG, consultado el
2026-10-07). Las líneas indicadas corresponden al estado final.

## 1. Verificación de fuentes

URLs base: `L25326` = <https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm>,
`LCT` = <https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm>.

| Norma / artículo | Dice T11 | Dice la fuente | URL | ¿Coincide? |
|---|---|---|---|---|
| Ley 25.326, art. 2 | Dato personal: información referida a "personas **humanas** o de existencia ideal determinadas o determinables" | "Información de cualquier tipo referida a personas **físicas** o de existencia ideal determinadas o determinables" | L25326 | **No** → corregido |
| Ley 25.326, art. 4 | Ciertos, adecuados, pertinentes y no excesivos respecto de la finalidad; no usar para finalidades distintas o incompatibles | Inc. 1: "ciertos, adecuados, pertinentes y no excesivos en relación al ámbito y finalidad…"; inc. 3: "no pueden ser utilizados para finalidades distintas o incompatibles…" | L25326 | Sí |
| Ley 25.326, art. 5 | Consentimiento libre, expreso e informado, salvo excepciones, entre ellas relación contractual necesaria | Inc. 1: "consentimiento libre, expreso e informado"; inc. 2.d: "Deriven de una relación contractual, científica o profesional del titular… y resulten necesarios para su desarrollo o cumplimiento" | L25326 | Sí |
| Ley 25.326, art. 6 | Informar finalidad, destinatarios, existencia del archivo y responsable, derechos de acceso, rectificación y supresión | Incs. a, b y e dicen eso; además c (carácter obligatorio o facultativo de las respuestas) y d (consecuencias de proporcionar los datos); "previamente… en forma expresa y clara" | L25326 | Sí (resumen fiel; omite c y d) |
| Ley 25.326, art. 9 | Medidas técnicas y organizativas para seguridad y confidencialidad | "adoptar las medidas técnicas y organizativas que resulten necesarias para garantizar la seguridad y confidencialidad de los datos personales…" | L25326 | Sí |
| Ley 25.326, art. 10 | Quienes intervienen en el tratamiento están obligados al secreto | "El responsable y las personas que intervengan en cualquier fase del tratamiento… están obligados al secreto profesional" | L25326 | Sí |
| Ley 25.326, art. 12 | Prohibida la transferencia a países u organismos sin protección adecuada, salvo excepciones | "Es prohibida la transferencia… con países u organismos internacionales o supranacionales, que no propocionen niveles de protección adecuados"; inc. 2: excepciones a–e | L25326 | Sí |
| Ley 25.326, arts. 14 a 16 | Acceso, rectificación, actualización y supresión | Art. 14 derecho de acceso; art. 15 contenido de la información; art. 16 "rectificación, actualización o supresión" | L25326 | Sí |
| Ley 25.326, art. 21 | Las bases privadas destinadas a proporcionar informes deben inscribirse en el registro del órgano de control | "Todo archivo… público, y privado destinado a proporcionar informes debe inscribirse en el Registro que al efecto habilite el organismo de control" | L25326 | Sí |
| Decreto 1558/2001 | Reglamenta la Ley 25.326 | "Apruébase la reglamentación de la Ley Nro. 25.326"; dictado 29-nov-2001, BO 03-dic-2001 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=70368> | Sí |
| LCT, art. 70 | Controles personales para proteger los bienes del empleador: dignidad, discreción, medios de selección automática | Igual ("…se harán por medios de selección automática destinados a la totalidad del personal") | LCT | Sí |
| LCT, art. 71 | Los controles deben ser "puestos en conocimiento de la autoridad de aplicación" | "Los controles referidos en el artículo anterior, así como los relativos a la actividad del trabajador, deberán ser **conocidos por éste**" (sustituido por Ley 27.322, BO 15/12/2016) | LCT | **No** → corregido (T11 y T12) |
| LCT, art. 72 | (incluido en "arts. 70 a 72" sin detalle) | "La autoridad de aplicación está facultada para verificar que los sistemas de control… no afecten en forma manifiesta y discriminada la dignidad del trabajador" | LCT | Sí; se explicitó |
| Ley 27.483 | Aprueba el Convenio 108 | Aprueba el Convenio 108 (Estrasburgo, 28/01/1981) **y su Protocolo Adicional** (autoridades de control y flujos transfronterizos). Sanción 06-dic-2018, BO 02-ene-2019, n.º 34.025; entrada en vigor 01/06/2019 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=318245> | Parcial → se agregó el Protocolo adicional |
| Ley 27.699 (Convenio 108+) | `[[VERIFICAR]]` si corresponde citarla | Aprueba el Protocolo modificatorio del Convenio 108 (Estrasburgo, 10/10/2018). Sanción 09-nov-2022, BO 30-nov-2022, n.º 35.058 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=375738> | Existe → se agregó cita y entrada bib |
| Res. AAIP 47/2018 | Medidas de seguridad recomendadas para el tratamiento de datos personales | "Medidas de seguridad recomendadas para el tratamiento y conservación de los datos personales en medios informatizados" (Anexo I) y no informatizados; deroga Disp. DNPDP 11/2006 y 9/2008. Dictada 23-jul-2018, BO 25-jul-2018, n.º 33.918. Sus considerandos citan el Decreto 746/2017, que atribuye a la AAIP la aplicación de la Ley 25.326 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=312662> | Sí |
| Disp. DNPDP 60-E/2016 | Criterios sobre países con protección adecuada y cláusulas contractuales modelo, dictados por la AAIP | Art. 1: cláusulas contractuales tipo de transferencia internacional (cesión y prestación de servicios); art. 3: lista de países con legislación adecuada. Dictada por la **Dirección Nacional de Protección de Datos Personales** (16-nov-2016), BO 18-nov-2016, n.º 33.507 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=267922> | Parcial → se corrigió el organismo emisor |
| Ley 25.326 (ficha) | Año 2000 | Sanción 04-oct-2000, promulgación parcial 30-oct-2000, BO 02-nov-2000, n.º 29.517 | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=64790> | Sí |
| LCT (ficha) | t.o. Decreto 390/1976, año 1976 | Ley 20.744 sancionada 05-sep-1974, BO 27-sep-1974, n.º 23.003; texto ordenado por Decreto 390/1976 (13/5/1976) | <https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=25552> | Sí; el año de la entrada pasa a 1974 (publicación de la ley) |

## 2. Correcciones respecto de T11/T12

**T11, art. 2**
```
- …referida a personas humanas
+ …referida a personas físicas
```

**T11, órgano de control y normas complementarias**
```
- El órgano de control es la Agencia de Acceso a la Información Pública (AAIP), que dicta normas
- complementarias, entre ellas las medidas de seguridad recomendadas para el tratamiento de datos
- personales \parencite{aaip2018} y los criterios sobre países con protección adecuada y cláusulas
- contractuales modelo para la transferencia internacional \parencite{dnpdp2016}. Argentina adhiere
- además al Convenio 108 del Consejo de Europa para la protección de las personas con respecto al
- tratamiento automatizado de datos de carácter personal \parencite{ley27483}.
- [[VERIFICAR: Ley 27.483 … Convenio 108+.]]
+ El órgano de control es la Agencia de Acceso a la Información Pública (AAIP), que asumió las
+ funciones de la entonces Dirección Nacional de Protección de Datos Personales. Entre las normas
+ complementarias dictadas por ambos organismos se encuentran las medidas de seguridad recomendadas
+ para el tratamiento de datos personales \parencite{AAIP2018} y las cláusulas contractuales tipo
+ para la transferencia internacional, junto con la lista de países con legislación adecuada
+ \parencite{DNPDP2016}. Argentina aprobó además el Convenio 108 del Consejo de Europa para la
+ protección de las personas con respecto al tratamiento automatizado de datos de carácter personal y
+ su Protocolo adicional \parencite{Ley27483}, y el Protocolo modificatorio que lo actualiza,
+ conocido como Convenio 108+ \parencite{Ley27699}.
```

**T11, LCT arts. 70 a 72**
```
- …salvaguarden la dignidad del trabajador, se practiquen con discreción y mediante medios de
- selección automática, y sean puestos en conocimiento de la autoridad de aplicación (arts.~70 a 72).
+ …salvaguarden la dignidad del trabajador, se practiquen con discreción y mediante medios de
+ selección automática (art.~70). Esos controles, así como los relativos a la actividad del
+ trabajador, deben ser conocidos por este (art.~71), y la autoridad de aplicación está facultada
+ para verificar que no afecten su dignidad (art.~72).
```

**T12, tabla, fila "Consentimiento e información", columna de la organización**
```
- …(política de uso aceptable o cláusula contractual), y comunicarlo a la autoridad de aplicación
- laboral (LCT, art.~71).
+ …(política de uso aceptable o cláusula contractual); la LCT exige que los controles relativos a la
+ actividad del trabajador sean conocidos por este (art.~71).
```

## 3. Cambios

- **T11** → `chapters/chapter02.tex` l.102–154: nueva subsección **2.1.9** "Marco legal: protección
  de datos personales" (`sec:marco-legal`), inmediatamente después de 2.1.8 "Estándares y marcos
  normativos" y antes de 2.2. El texto es el de T11 con las correcciones de §2.
- **T22** → `biblio.bib` l.374–427: `Ley25326`, `Ley20744`, `Ley27483`, `Ley27699` (nueva),
  `AAIP2018`, `DNPDP2016`. `@misc` con `howpublished` (BO, número y fecha de publicación), `date`,
  `url` (InfoLEG) y `urldate`. Se quitaron las `note` con `[[VERIFICAR]]`. La fecha completa va en
  `howpublished` porque `iso-authoryear` muestra solo el año. Se respetaron los finales de línea CRLF del archivo.
  No se agregaron `osterwalder2010`, `larman2003` ni `henderson1970` de T22 (no forman parte de este paquete;
  `Henderson1970` ya existe).
- **T12** → `chapters/producto.tex` l.137–178: nueva sección **9.5** "Tratamiento de datos personales
  y viabilidad legal" (`sec:tratamiento-datos`), antes de "Limitaciones conocidas", con la tabla
  **9.III** (`tab:tratamiento-datos`) y las subsecciones 9.5.1 Conservación, 9.5.2 Datos de
  entrenamiento y 9.5.3 Descargo de responsabilidad.
- **Fila nueva en limitaciones** → `chapters/producto.tex` l.223, al final de la tabla
  `tab:limitaciones-producto`: "Sin plazo de conservación de datos" / "La supresión de datos de un usuario
  rompe la verificación de la cadena de \emph{hashes}." / "Trabajo futuro: cierre de la cadena por
  período (sección~\ref{sec:tratamiento-datos})."
- **3.6.6** → `chapters/chapter04.tex` l.485: al final se agregó "El tratamiento de los datos personales
  que realiza el sistema y su encuadre en la Ley 25.326 se analizan en la sección~\ref{sec:tratamiento-datos}."
  (se imprime "sección 9.5").

Adaptaciones de forma (como en P2):
- Claves de cita al estilo del `.bib` (CamelCase): `ley25326` → `Ley25326`, `ley20744` → `Ley20744`,
  `ley27483` → `Ley27483`, `aaip2018` → `AAIP2018`, `dnpdp2016` → `DNPDP2016`.
- Tabla de T12 con el formato del capítulo: columnas `>{\raggedright\arraybackslash}p{}` de
  3,0/5,8/5,3 cm, encabezados en negrita, `\hline` entre filas, `\caption` y `\label` separados.
- `\fuente{…}` → `{\small Fuente: elaboración propia a partir de la Ley 25.326 y la Ley de Contrato de Trabajo.\par}`.
- Etiquetas: `sec:modelo-relacional` → `sec:modelo-datos` (datos.tex l.142, "Modelo de datos");
  `sec:conjunto-datos` → `sec:dataset` (datos.tex l.7). No se crearon etiquetas nuevas. Esto resuelve el
  `[[VERIFICAR: etiquetas \ref…]]` de T12, que no se insertó.

Numeración resultante: en el capítulo 9 "Limitaciones conocidas" pasa de 9.5 a **9.6** y "Síntesis" a 9.7;
la tabla de limitaciones pasa de 9.III a **9.IV**. En el capítulo 2, la subsección nueva es 2.1.9 y
el resto no se corre (2.2 sigue igual).

## 4. Pendientes

- `[[CODIGO: cifrado TLS…; autenticación mutua…; credenciales del panel fuera del navegador; claves de
  agente ligadas a su identificador]]` (producto.tex l.158), visible. **Contradicción**: la tabla de
  limitaciones (9.6) dice que el canal agente–API **no** está cifrado, que la clave de agente **no** está
  ligada a su identificador y que la clave de administración se guarda en el navegador; RNF-13 figura como
  no implementado. Hay que resolver el marcador según el estado real del código antes de la entrega.
- `[[VERIFICAR: región de Upstash y de Supabase]]` (producto.tex l.162), visible. No se puede verificar
  desde la documentación; requiere revisar las consolas o la configuración de los servicios.
- Decreto 1558/2001: se nombra sin `\parencite` (como en T11), así que no tiene entrada bib. Se puede
  agregar si se quiere citar (BO 03-dic-2001, n.º 29.787; verNorma id=70368).
- Sugerencia (sin aplicar): el art. 4, inc. 7 de la Ley 25.326 ("Los datos deben ser destruidos cuando
  hayan dejado de ser necesarios o pertinentes a los fines para los cuales hubiesen sido recolectados") y el
  art. 16, inc. 7 (conservación según plazos legales o contractuales) son la base normativa directa de
  9.5.1 Conservación. Citarlos ahí reforzaría la limitación.
- Sugerencia (sin aplicar): el art. 6 también exige informar el carácter obligatorio o facultativo de los
  datos y las consecuencias de proporcionarlos (incs. c y d). El resumen de T11 los omite, aunque no es incorrecto.
