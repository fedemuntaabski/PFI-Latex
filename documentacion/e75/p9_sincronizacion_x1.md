# P9 E75 — Sincronización con el diagnóstico X1

Rama `e75/paquete`. Cinco tandas, un commit por tanda, sin push. Compilación tras cada
tanda (pdflatex, biber, pdflatex ×2): 0 errores, 0 referencias o citas indefinidas, sin `??`,
0 advertencias de biber, overfull hbox iguales a la línea base (4). Los overfull vbox
(`\output is active`) vienen del encabezado con el logo UADE, uno por página. Ya existían
(230 en la línea base) y suben a 231 porque el documento gana una página (233 en total).
No son nuevos de contenido y el preámbulo no se toca.

| Tanda | Commit |
|---|---|
| T1 Marcadores X1 | `526b2b0` |
| T2 Tratamiento de datos | `e38b84d` |
| T3 Reentrenamiento | `4159f98` |
| T4 Cap. 11 y lienzo | `2ddd648` |
| T5 Paleta, logo y detalles | `caa4c25` |

## Verificaciones externas

### Disposición DNPDP 60-E/2016, art. 3 (InfoLEG)
- URL: https://www.argentina.gob.ar/normativa/nacional/267922/texto
- Lista de países con legislación adecuada: Estados miembros de la UE y del EEE, Suiza,
  Guernsey, Jersey, Isla de Man, Islas Feroe, Canadá (solo sector privado), Andorra,
  Nueva Zelanda, Uruguay e Israel (solo datos con tratamiento automatizado).
- La Resolución AAIP 34/2019 modifica el art. 3 para incluir al Reino Unido
  (https://www.boletinoficial.gob.ar/detalleAviso/primera/202373/20190226).
- **Ni Estados Unidos ni Brasil figuran** → se agregó la oración de cláusulas contractuales tipo.

### Kent2015
- DOI 10.17021/1179829 → OSTI 1179829 (https://www.osti.gov/biblio/1179829). Coincide.
- Título registrado en OSTI: *Comprehensive, Multi-Source Cyber-Security Events Data Set*
  (agrega "Data Set" al título indicado); autor Kent, Alexander D.; LANL; 21/05/2015.
  En el .bib se usa el título de OSTI.

## T1 — Marcadores que se resuelven con X1
- **a.** RF-04 (`requerimientos.tex`): marcador → "La vida media es fija: se define en la
  configuración del modelo al entrenarlo y no se modifica en tiempo de ejecución." Ningún otro
  lugar dice que sea configurable (8.3 y 9.2.2 solo dan 3 días).
- **b.** 1.4 Metodología (`chapter01.tex`): marcador → texto de las seis fases y las dos
  auditorías. Consistente con la tabla de herramientas del pipeline (cap. 7: "seis fases…
  hasta el puntaje híbrido"), con 8.2 (clasificación de usuarios por volumen) y con 9.2.4.
- **c.** "ml_core": 0 apariciones en los .tex. Sin cambios. La sección 7.1 enumera
  "pipeline de entrenamiento" y "scripts" como subsistemas lógicos, sin afirmar una ubicación
  física; no se tocó.
- **d.** 10.5.1 (`pruebas.tex`): marcador → párrafo sobre LANL con `\parencite{Kent2015}`.
  Único agregado: `\emph{pipeline}`, por estilo del documento. Entrada `@online{Kent2015}` en
  `biblio.bib`.
- **e.** Búsqueda en todos los .tex:
  - LANL, 253, imbalanced, SMOTE: 0 casos previos (las únicas apariciones son las del párrafo nuevo).
  - "balanceo": solo en el marcador reemplazado.
  - "desbalance": cap. 2, estado del arte, como limitación general de los sistemas UEBA en la
    literatura. No presenta el balanceo como parte del pipeline → sin cambios.
  - La tabla de herramientas del pipeline (cap. 7) y el cap. 8 no lo mencionan.

## T2 — Tratamiento de datos (9.5)
- **a.** Fila "Transferencia internacional": regiones según X1 (AWS us-east-2; Supabase en
  São Paulo; Upstash con `[[VERIFICAR: región de Upstash]]`). Columna de la organización:
  "Ni Estados Unidos ni Brasil figuran… requiere las cláusulas contractuales tipo." y
  "cláusulas contractuales modelo" → "esas cláusulas".
- **b.** Fila "Acceso, rectificación y supresión": texto de X1 (la API borra el estado y el
  historial de puntajes; conserva los eventos crudos y las alertas de corrimiento). Pendientes:
  plazo de conservación y procedimiento de supresión que alcance a los eventos crudos, en
  tensión con la cadena de hashes (remite a 9.5.1; se agregó `\label{sec:conservacion-datos}`).
- **c.** 9.5.1: oración nueva sobre el alcance real del borrado (herramienta de limpieza, no
  supresión completa). 9.6, fila renombrada "Sin plazo de conservación ni supresión completa de
  datos", con impacto y tratamiento alineados con b. Coherencia adicional: cap. 13, objetivo 8
  → "quedan pendientes el plazo de conservación y la supresión completa de los datos de un usuario".

## T3 — Reentrenamiento
- **a.** "única corrida":
  - 9.3: dice "la única corrida real del planificador", que es correcto. Se deja y se agrega
    "las dos corridas manuales tampoco produjeron un modelo mejor".
  - Cap. 13, objetivo 6: decía "la única corrida real del reentrenamiento", sin acotar al
    planificador → se corrige en b.
- **b.** Cap. 13, objetivo 6: evidencia con las tres corridas reales (una automática y dos
  manuales) sin promoción; estado → "Parcial" (coincide con RF-21 en cap. 4 y 9.3).
- **c.** 9.2.4: marcador `[[CODIGO: regla de promoción vigente tras el cierre de los modelos]]`.
- **Aviso:** 9.2.4 y RF-21 dicen que el candidato se promueve si "iguala o mejora" las
  métricas. X1 informa un empate que no se promovió. La contradicción queda a cargo del
  marcador nuevo.

## T4 — Capítulo 11 y lienzo
- **a.** 11.1.3 Modalidad de despliegue: diseñado para la nube, con servicios gestionados;
  despliegue verificado del prototipo local con almacenamiento en la nube
  (`\ref{sec:despliegue}`). Sin "100 %" ni "cloud-native".
- **b.** 11.1.1: "bloquear el acceso, aislar el proceso" → "suspender o terminar procesos,
  denegar el acceso a carpetas"; "(restricción de permisos, aislamiento del proceso)" →
  "(suspensión o terminación de procesos, denegación del acceso a carpetas)".
  Se conservó "exigir una verificación adicional": describe lo que los competidores dejan al
  analista, no una acción del producto.
- **c.** 11.1.1 (Sentinel), 11.2.1 y lienzo (Propuesta de valor): explicación por variables,
  redactada en forma opcional por un modelo de lenguaje.
- **d.** 11.2.1: "Arquitectura basada en la separación entre punto de decisión y punto de
  aplicación de NIST SP 800-207".
- **e.** 11.2.3: agregado "mediante el adaptador de identidad, hoy validado con un proveedor simulado".
- **f.** 11.1.3 Canales: "Se prevé una distribución digital directa con alta autogestionada…".
  Coherencia adicional en el lienzo (Canales): "Venta directa, con alta autogestionada prevista, y reventa…".
- **g.** Lienzo, Segmentos: se quitó "en la encuesta," → "el 47 % de la base efectiva de la encuesta (112 participantes…)".

## T5 — Paleta, logo y detalles
- **a.** 5.4: oración con la paleta semafórica del panel (verde, ámbar, naranja, rojo;
  rosa y violeta para niveles adicionales de RF-13).
- **b.** 12.5: "amarillo… niveles de riesgo intermedios" → "un ámbar de acento… coincide con
  el tono que el panel usa para el nivel de riesgo medio". Se borró el `[[VERIFICAR]]`.
- **c.** 12.4: "cercano al 5,35 %" → "cercano al 5,3 %".
- **d.** tab:metas-modelo: `\end{tabular}\par`.
- **e.** Cap. 13, trabajo futuro: el ítem de capacidad de detección agrega "y revisar el
  componente personal en usuarios con historial escaso". Ítems nuevos: Reversión acotada,
  Correcciones del agente y Pruebas (este último con
  `[[CODIGO: ajustar según el resultado de la cobertura]]`).

## Avisos
- Las "253 sesiones anómalas" de LANL vienen del trabajo preliminar del equipo y no se
  verificaron. El archivo de red team del conjunto de Kent contiene alrededor de 749 eventos
  de compromiso. Si 253 es una derivación propia (por ejemplo, sesiones únicas), conviene
  decirlo o revisarlo.
- Regla de promoción "iguala o mejora" frente al empate no promovido (ver T3).

## Marcadores `[[...]]` que quedan

| Archivo | Línea | Texto |
|---|---|---|
| chapters/chapter01.tex | 53 | `[[CODIGO: confirmar estado del despliegue]]` |
| chapters/chapter01.tex | 53 | `[[CODIGO: confirmar según el resultado del Prompt C]]` |
| chapters/chapter04.tex | 437–438 | `[[COMPLETAR: canal, por ejemplo redes sociales y contactos personales y laborales del equipo]]` |
| chapters/chapter04.tex | 438 | `[[COMPLETAR: fechas]]` |
| chapters/requerimientos.tex | 224 | `[[ESTADO SEGÚN RNF-02]]` |
| chapters/producto.tex | 92 | `[[CODIGO: regla de promoción vigente tras el cierre de los modelos]]` |
| chapters/producto.tex | 129 | `[[ESTADO SEGÚN RNF-02]]` |
| chapters/producto.tex | 158 | `[[CODIGO: cifrado TLS entre agente, panel y API; autenticación mutua entre agente y API; credenciales del panel fuera del navegador; claves de agente ligadas a su identificador]]` |
| chapters/producto.tex | 162 | `[[VERIFICAR: región de Upstash]]` |
| chapters/pruebas.tex | 204 | `[[CPU MEDIA]]`, `[[CPU P95]]`, `[[CPU MÁX]]` |
| chapters/pruebas.tex | 206 | `[[RSS MEDIA]]`, `[[RSS P95]]`, `[[RSS MÁX]]` |
| chapters/pruebas.tex | 210 | `[[INTERPRETACIÓN DE RNF-02 SEGÚN EL RESULTADO]]` |
| chapters/conclusiones.tex | 20 | `[[CODIGO: TLS y autenticación mutua]]`, `[[CODIGO: RNF-02]]`, `[[CODIGO]]` |
| chapters/conclusiones.tex | 22 | `[[CODIGO: actualizar si se reentrena]]` |
| chapters/conclusiones.tex | 34 | `[[CODIGO: resultado de seguridad]]`, `[[CODIGO]]` |
| chapters/conclusiones.tex | 38–39 | `[[CODIGO: cantidad de pruebas y cobertura]]`, `[[CODIGO]]` |
| chapters/conclusiones.tex | 45 | `[[CODIGO: actualizar conteo con RNF-02, RNF-03 y RNF-13]]` |
| chapters/conclusiones.tex | 64 | `[[CODIGO: actualizar si el reentrenamiento cambia los resultados.]]` |
| chapters/conclusiones.tex | 106–107 | `[[CODIGO: ajustar según el resultado de la cobertura]]` |
| chapters/conclusiones.tex | 110–111 | `[[CODIGO: limitaciones de seguridad que queden abiertas después del trabajo del repo de código; integración con un proveedor de identidad real.]]` |
