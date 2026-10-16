# Auditoría de mockups y capturas del dashboard

Solo lectura. No se modificó ninguna imagen ni `.tex`.

## 1. Alcance

- Único capítulo con pantallas en el documento: `chapters/e50_diseno_ux.tex` (incluido en `main.tex:276`, cap. "Justificación de diseño y mockups", `chap:diseno`).
- `chapters/archivo/obsoleto_e50.tex` repite las mismas imágenes pero **no está en `main.tex`**: se excluye.
- Logo: `images/logo_umbral.png`, usado solo en `chapters/negocio.tex:308` (`fig:logo`).
- Todas las imágenes de `images/mockups/` vienen del commit `39903e0` (2026-08-14). Ninguna se recapturó desde entonces. El logo es del commit `e7211f3` (2026-10-07), posterior a todas las capturas.

## 2. Cómo presenta el texto cada imagen

El capítulo (líneas 7-9) declara que los **wireframes** son una *reconstrucción estructural* hecha a partir de pantallas ya construidas, no bocetos previos. Cada pantalla trae un par:

| Tipo | Caption | Fuente declarada | Presentada como |
|---|---|---|---|
| `*-wireframe.png` | "Wireframe de baja fidelidad: …" | elaboración propia | **MOCKUP/wireframe** (diseño, puede diferir del sistema) |
| `*-real*.png` | "Pantalla real: `/ruta`" | "elaboración propia, captura del sistema" | **CAPTURA del sistema real** (debe coincidir) |

Conclusión de política: los wireframes pueden diferir; las 9 imágenes `-real` **deben** coincidir con el sistema actual.

## 3. Inventario

| Pantalla | Ruta | Imagen | `e50_diseno_ux.tex` | Caption | Presentada como | Última modif. |
|---|---|---|---|---|---|---|
| Login | `/login` | `mockups/mockup-login-wireframe.png` | 31 | Wireframe de baja fidelidad: Acceso (Login) | Wireframe | 2026-08-14 |
| Login | `/login` | `mockups/mockup-login-real.png` | 36 | Pantalla real: `/login` | Captura | 2026-08-14 |
| Usuarios (vista general) | `/` | `mockups/mockup-usuarios-wireframe.png` | 68 | Wireframe …: Usuarios (listado) | Wireframe | 2026-08-14 |
| Usuarios | `/` | `mockups/mockup-usuarios-real.png` | 73 | Pantalla real: `/` (listado de usuarios) | Captura | 2026-08-14 |
| Detalle de usuario | `/usuarios/:uid` | `mockups/mockup-detalle-wireframe.png` | 111 | Wireframe …: Detalle de usuario | Wireframe | 2026-08-14 |
| Detalle de usuario | `/usuarios/:uid` | `mockups/mockup-detalle-real.png` | 116 | Pantalla real: `/usuarios/:uid` (detalle) | Captura | 2026-08-14 |
| Alertas | `/alertas` | `mockups/mockup-alertas-wireframe.png` | 150 | Wireframe …: Alertas | Wireframe | 2026-08-14 |
| Alertas | `/alertas` | `mockups/mockup-alertas-real.png` | 155 | Pantalla real: `/alertas` (estado vacío) | Captura | 2026-08-14 |
| Umbrales | `/umbrales` | `mockups/mockup-umbrales-wireframe.png` | 187 | Wireframe …: Configuración de umbrales | Wireframe | 2026-08-14 |
| Umbrales (arriba) | `/umbrales` | `mockups/mockup-umbrales-real-1.png` | 192 | Pantalla real: `/umbrales` (parte superior: rangos por nivel) | Captura | 2026-08-14 |
| Umbrales (scroll) | `/umbrales` | `mockups/mockup-umbrales-real-2.png` | 197 | Pantalla real: `/umbrales` (scroll: acciones, periodicidad y notificaciones) | Captura | 2026-08-14 |
| Auditoría | `/auditoria` | `mockups/mockup-auditoria-wireframe.png` | 231 | Wireframe …: Auditoría | Wireframe | 2026-08-14 |
| Auditoría | `/auditoria` | `mockups/mockup-auditoria-real.png` | 236 | Pantalla real: `/auditoria` | Captura | 2026-08-14 |
| Estado del sistema | `/salud` | `mockups/mockup-estado-wireframe.png` | 266 | Wireframe …: Estado del sistema | Wireframe | 2026-08-14 |
| Estado del sistema | `/salud` | `mockups/mockup-estado-real.png` | 271 | Pantalla real: `/salud` | Captura | 2026-08-14 |
| Con historial | `/historial` | `mockups/mockup-historial-wireframe.png` | 299 | Wireframe …: Con historial | Wireframe | 2026-08-14 |
| Con historial | `/historial` | `mockups/mockup-historial-real.png` | 304 | Pantalla real: `/historial` | Captura | 2026-08-14 |
| Logo (no es pantalla) | — | `logo_umbral.png` | `negocio.tex:308` | Logotipo del producto. | Identidad de marca | 2026-10-07 |

Faltan en el documento: no hay captura de Detalle ni de Alertas con un usuario en nivel alto/crítico, ni de Usuarios con niveles distintos de "Medio".

## 4. Hallazgos ya visibles en las capturas (sin abrir el dashboard)

1. **Marca desactualizada (todas las capturas con barra superior)**: la barra dice **"UEBA Dashboard"** con un ícono de escudo genérico. El producto ahora es **UMBRAL** (logo con escudo azul oscuro + línea/punto ámbar, `logo_umbral.png`). El texto del capítulo habla de "el nombre del sistema" sin nombrarlo, así que no hay contradicción textual, pero la captura no muestra la marca del documento. Afecta: usuarios, detalle, alertas, umbrales (x2), auditoría, estado, historial. Login no muestra marca.
2. **Datos personales reales visibles**: `mockup-umbrales-real-2.png` muestra emails reales en "Emails admin" (`fedemunta@gmail.com`, `ssantiagomociulsky@gmail.com`). Conviene reemplazarlos por datos de ejemplo en la recaptura.
3. **Ruido de captura**: `mockup-alertas-real.png` (`localhost:5173/alertas`) y `mockup-estado-real.png` (`localhost:5173/historial`) muestran la barra de estado del navegador abajo a la izquierda; en estado la URL ni siquiera corresponde a la pantalla. `mockup-detalle-real.png` está cortada (solo 5 filas de eventos); `mockup-umbrales-real-1.png` muestra "100.0(" truncado en el campo Crítico.
4. **Datos de prueba visibles**: UIDs `demo-pfi`, `smoketest-redisreal-1786456432`; fechas de agosto 2026. Aceptable, pero el "smoketest" se nota.
5. **Estados poco ilustrativos**: todos los usuarios están en nivel **Medio**; Alertas vacío; Detalle con un solo punto en el gráfico ("Actual"). No se ven los colores verde/naranja/rojo/rosa/violeta que el capítulo (línea 15) describe en prosa.
6. El capítulo menciona en la barra "indicador de alertas activas y selector de tema"; en la captura aparecen dos botones de ícono (campana verde, sol) y un **"Salir"** que el texto no menciona.

## 5. Checklist por pantalla

Formato: `[ ]` para tildar contra el sistema real. Lo marcado **(texto)** es afirmado por el capítulo; el resto es lo que se ve en la captura actual.

### Elementos comunes (barra superior; todas menos Login)
- [ ] Logo/nombre: captura = ícono escudo + "UEBA Dashboard". ¿Ahora dice UMBRAL / usa `logo_umbral`?
- [ ] 6 accesos en orden: Usuarios, Con historial, Alertas, Umbrales, Auditoría, Estado del sistema **(texto)**
- [ ] Ítem activo resaltado en azul
- [ ] Botón campana (verde) = indicador de alertas activas **(texto)**; ¿muestra contador cuando hay alertas?
- [ ] Botón sol/luna = tema claro/oscuro **(texto)**
- [ ] Botón "Salir"
- [ ] Tema oscuro por defecto **(texto)**; fondo azul-negro

### Login (`/login`)
- [ ] Una sola tarjeta centrada sobre fondo oscuro **(texto)**
- [ ] Ícono llave + título "Acceso a configuración"
- [ ] Texto de ayuda: "Ingresá tu usuario y contraseña del dashboard. La sesión se guarda solo para esta pestaña…"
- [ ] Campo usuario (prellenado "admin"), campo contraseña, botón "Entrar" (azul)
- [ ] Sin logo ni barra superior (¿ahora hay logo UMBRAL?)

### Usuarios (`/`)
- [ ] Ícono + título "Usuarios (N)" + subtítulo "Usuarios monitoreados con nivel de riesgo sugerido, acción y cobertura de score."
- [ ] Contador "N DE N USUARIOS"
- [ ] Filtro desplegable "Todos los niveles" **(texto: filtro por nivel)**
- [ ] Columnas: UID, NIVEL, ACCIÓN, COBERTURA, ÚLTIMA ACTIVIDAD
- [ ] Badge de nivel con ícono (captura: solo "Medio" ámbar); verificar bajo/alto/crítico y colores verde/ámbar/naranja/rojo **(texto)**
- [ ] Badge cobertura: "Completa" (azul) / "Parcial" (gris)
- [ ] Filas clicables hacia el detalle **(texto)**
- [ ] Timestamps en formato ISO crudo (`2026-08-11T14:31:48+00:00`); ¿sigue así?

### Detalle de usuario (`/usuarios/:uid`)
- [ ] Título "Detalle de usuario"
- [ ] Tarjeta superior: UID monoespaciado + par de badges (nivel, cobertura) **(texto)**
- [ ] "RISK SCORE" en tipografía grande con color de acento **(texto)**; captura 49.58 ámbar
- [ ] Acción sugerida en texto completo bajo el score **(texto)**
- [ ] "Histórico de score": ícono, nota "El punto de hoy es provisional (día aún no cerrado); el histórico incluye solo días ya cerrados." **(texto)**
- [ ] Gráfico eje 0-100 (25/50/75/100), punto "Actual" provisional
- [ ] "Eventos recientes": nota "Últimos hasta 20 eventos… (RF-09)… no reemplaza a ninguno de los dos." **(texto)**
- [ ] Columnas: Timestamp, Tipo, Score, Nivel, Acción, Detalle
- [ ] Timestamps en formato `8/11/2026, 11:31:48 AM` (distinto del listado)
- [ ] Máx. 20 filas, más reciente primero **(texto)**
- [ ] ¿Falta botón "volver"/breadcrumb? (no aparece en la captura)

### Alertas (`/alertas`)
- [ ] Título "Alertas (N)"
- [ ] Texto: "…usuarios en nivel alto o critico… No hay historial persistente ni notificaciones push: 'reconocer' solo oculta el resaltado de 'nueva' en esta pestaña…" **(texto)**
- [ ] Columnas: UID, Nivel, Acción, Última actividad, Estado
- [ ] Estado vacío: ícono escudo + "Sin alertas activas." **(texto)**
- [ ] Estado con alertas: badge nivel alto/crítico, resaltado "nueva", botón "reconocer"; **no capturado**
- [ ] Sin ícono junto al título (a diferencia de Usuarios)

### Umbrales (`/umbrales`)
- [ ] Título "Configuración de umbrales" + subtítulo "…del sistema UEBA." (¿sigue "UEBA"?)
- [ ] "Umbrales por nivel": 4 filas con borde de color (verde, ámbar, naranja, rojo), pares desde/hasta contiguos **(texto)**
- [ ] Valores: Bajo 0-40, Medio 40-70, Alto 70-90, Crítico 90-100.0(truncado)
- [ ] "Desde" de Bajo deshabilitado (0)
- [ ] Botón "Guardar umbrales" propio **(texto)**
- [ ] "Acción por nivel": 4 selects (Bajo/Medio/Alto: Alertar; Crítico: Terminar y denegar) + "Guardar acciones" **(texto)**
- [ ] "Periodicidad de reentrenamiento": "PERIODICIDAD ACTUAL 27 días", campo "Nuevo valor (días)", "Guardar periodicidad", nota "Preferencia de periodicidad. El reentrenamiento es manual…"
- [ ] Disposición: umbrales arriba; acción y periodicidad en dos columnas; notificaciones al final **(texto)**
- [ ] "Notificaciones": chips toggle por nivel (Bajo, Medio, Alto, Crítico; captura: Medio y Alto activos) **(texto)**
- [ ] Lista "Emails admin" con "Quitar", campo "nuevo@email.com" + "Agregar", "Guardar notificaciones"
- [ ] Niveles adicionales rosa/violeta (RF-13) **(texto)**; no capturado
- [ ] Emails reales visibles → reemplazar

### Auditoría (`/auditoria`)
- [ ] Título "Auditoría de configuración" + subtítulo "…persistido en Postgres via POST /config/auditoria."
- [ ] Tarjetas cronológicas descendentes **(texto)**
- [ ] Cada tarjeta: tipo (Acción por nivel / Periodicidad de reentrenamiento / Notificaciones), fecha/hora y "actor a7acfd3a" **(texto: actor)**
- [ ] Diff monoespaciado `valor_viejo → valor_nuevo` **(texto)**
- [ ] Entradas "Sin cambios detectables entre valores."
- [ ] ¿Aparecen cambios de umbrales por nivel? (la captura no muestra ninguno)
- [ ] ¿Actor sigue siendo hash en lugar de nombre?

### Estado del sistema (`/salud`)
- [ ] Título "Estado del sistema" + badge "healthy" **(texto: estado agregado)**
- [ ] 3 tarjetas: "Artefactos cargados: Sí", "Redis: OK", "Postgres: OK" **(texto)**
- [ ] Lista de 8 artefactos con badge OK: isolation_forest, scaler_isoforest, lstm_autoencoder, scaler_lstm, type_encoding, lstm_threshold, config_score_hibrido, train_references **(texto)**
- [ ] ¿Cambió la lista de artefactos o aparece alguno nuevo?
- [ ] Pie de captura con URL equivocada (`/historial`) → recapturar limpio

### Con historial (`/historial`)
- [ ] Título "Usuarios con historial (N)"
- [ ] Nota "uids con historial diario cerrado en Postgres. Puede diferir del listado operacional (Redis): un uid reseteado conserva su historial acá." **(texto)**
- [ ] Una sola columna UID **(texto)**
- [ ] Filas clicables o no (no se ve)

### Logo (`images/logo_umbral.png`, `negocio.tex:308`)
- [ ] Escudo azul oscuro con línea de actividad blanca, línea ámbar de umbral y punto ámbar
- [ ] "UMBRAL" en mayúsculas sans-serif de peso alto + eslogan "confianza continua, después del login"
- [ ] Verificar que sea el mismo que el dashboard; ¿el favicon/barra superior ya lo usa?

## 6. Veredicto preliminar (solo por capturas vs texto del cap.)

| Pantalla | Veredicto preliminar | Motivo |
|---|---|---|
| Login | Probablemente vigente | Sin marca; verificar si sumó logo |
| Usuarios | Desactualizada leve | Marca "UEBA Dashboard"; un solo nivel visible |
| Detalle | Desactualizada leve/fuerte (según la rama de detalle + logo) | Marca; nivel único; gráfico de un punto; cortada |
| Alertas | Desactualizada leve | Marca; ruido de captura; sin alertas reales |
| Umbrales | Desactualizada leve | Marca; emails reales; truncado en Crítico |
| Auditoría | Desactualizada leve | Marca |
| Estado | Desactualizada leve | Marca; URL equivocada en pie |
| Historial | Desactualizada leve | Marca |

Confirmar contra el sistema real con Claude in Chrome (ver prompt abajo).

## 7. Recomendación

- Esperar el merge de la vista de detalle y del logo antes de recapturar, así se captura una sola vez.
- Las 9 `-real` están presentadas como captura: si el dashboard cambió, hay que recapturarlas. Los wireframes no necesitan reemplazo.
- Estados a capturar: Usuarios con niveles mezclados (bajo/medio/alto/crítico + uno parcial); Alertas con al menos una alerta alto/crítico y otra vacía; Detalle de un usuario en nivel alto con histórico de varios días y 20 eventos; Umbrales con emails de ejemplo; navegador sin barra de estado.

## 8. Prompt para Claude in Chrome

Pegar junto con la sección 5 (checklist):

> Tengo el dashboard de UMBRAL abierto en esta pestaña (localhost), ya logueado. Te paso un checklist por pantalla de cómo se ven las capturas del documento. Recorré cada pantalla del dashboard SIN cambiar ninguna configuración (no guardes formularios, no toques umbrales, acciones ni notificaciones, no borres usuarios) y para cada una decime:
> - qué coincide con el checklist,
> - qué difiere (elementos que faltan, sobran o cambiaron: logo, columnas, niveles, colores, textos),
> - veredicto: actualizada / desactualizada leve / desactualizada fuerte.
> Al final, dame la lista de pantallas que tengo que recapturar y en qué estado conviene capturarlas (por ejemplo, con un usuario en nivel alto visible).
