# E75 / 22: cierre de la tesis

Rama `e75/cierre`, desde `e75/textos-codigo`. Fuentes: `documentacion/e75/18_en_vivo.md`, `10b_gate.md`, `21_cifras_finales.md`, `22_ci_fix.md` y `informes_e75/20_textos_codigo.md`.

## 1. Cambios por capítulo

- **Cap. 1** (`chapter01.tex`): los dos marcadores de la descripción de componentes pasan a "desplegada en la nube (verificada el 10 de octubre de 2026)"; se saca el marcador del envío seguro.
- **Cap. 4** (`requerimientos.tex`): RF-02 con la verificación del 10/10 (403 por usuario, agente y confirmación ajenos; el agente aborta con `http://`); RF-21 pasa a Implementado, con 11 pruebas, el script de evaluación y la limitación de la promoción desde el planificador; RNF-06 con la prueba manual en consola elevada y el requisito de `SeRestorePrivilege`; RNF-13 verificado; conteo de la síntesis: 31 RF implementados.
- **Cap. 7** (`arquitectura.tex`): tabla de despliegue, texto de TLS, tabla de seguridad y fila de HTTP sin TLS con la verificación del 10/10 (Let's Encrypt, 308, puerto de la API cerrado, documentación no expuesta, instancia apagada fuera de pruebas y demostraciones).
- **Cap. 9** (`producto.tex`): 9.2.4 con 5,5 a 7,5 minutos según la máquina, 11 pruebas, feature set versionado y equivalencia byte a byte con v1 (replay de 800 eventos); tabla 9.II (CU-03 5 implementados, total 31/31/0); 9.5 con el estado del despliegue y la sesión en vivo (agente real: crítico 97,06 con `terminar_y_denegar`; no se observó `alto`); 9.3 art. 9; tabla 9.IV: HSTS implementado y verificado en "Sin CSP", fila nueva sobre la reversión con privilegios; 9.7 con los conteos.
- **Cap. 10** (`pruebas.tex`): inventario 529 pruebas (352 + 177), 35 y 14 archivos; tabla de resultados (352 con artefactos; 328 + 15 omitidas en la configuración del CI); fecha de ejecución 10/10; CI con los cuatro trabajos (SO, runtime, qué mide, umbral); tabla de cobertura con total combinado 91,1; párrafo del módulo de métricas (98,8 %); equivalencia del feature set en 10.5; síntesis.
- **Cap. 13** (`conclusiones.tex`): tabla 13.I objetivos 1, 4, 6, 7 y 9; conteo de 13.1 (31 RF implementados).

## 2. Conteos finales

| | Valor |
|---|---|
| RF | 31 implementados, 0 parciales |
| RNF | 15: 12 implementados, 3 parciales (RNF-05, RNF-09, RNF-11), 0 no implementados |
| Lugares verificados | cap. 4 (síntesis), tabla 9.II, 9.7 y 13.1: iguales |
| Pruebas | API 352, agente 177, total 529; CI sin artefactos 328 + 15 omitidas |
| Archivos de test | API 35, agente 14 |
| Cobertura de líneas | API 93,9 %, agente 89,3 %, total 92,5 % |
| Cobertura líneas + ramas | API 92,4 %, agente 88,1 %, total 91,1 % (celda "--" completada) |
| Sentencias | 2465 + 1116 = 3581 |

## 3. Diferencias del CI (22 contra la 10.2 anterior)

- Umbral del trabajo `api`: 75 % → 74 % combinado (líneas + ramas).
- Se agregan el informe informativo por líneas (sin umbral) y los cuatro archivos de pruebas del agente independientes del SO, que corren en `api` sin cobertura.
- `agent-windows` (windows-latest, Python 3.11, 85 % de líneas): sin cambio de umbral.
- `frontend` (Node 24) e `infra` (Terraform 1.16.4): se explicitan versiones y que no tienen umbral.
- Se saca "los cuatro trabajos finalizaron correctamente… sin ajustes": el 22 documenta que la corrida #71 de `api` falló por falta de `pyarrow`, corregida; no hay evidencia de una corrida posterior en verde (el 21 no pudo consultar el CI). La tesis cuenta la falla y la corrección.
- Queda explícito que la evidencia del 85 % es la medición local completa, con artefactos, y que el umbral de `api` es una red contra regresiones.

## 4. Otras decisiones

- Higiene: ningún texto afirma haber rotado o limpiado credenciales filtradas del historial (grep sin coincidencias). No se agregó texto sobre el tema.
- Se descartó el recuento de la tabla de resultados "Windows 10 con Python 3.12": el 21 no lo informa para esta ejecución.
- La inserción "el criterio de promoción… la versión instalada en la nube es anterior" de 9.2.4 se mantuvo tal cual: no hay dato nuevo en las fuentes.
- La tabla 13.I deja huecos al final de página por filas largas que no se parten (comportamiento de `longtable` ya existente).

## 5. Verificación

- `latexmk -pdf -outdir=build main.tex`: rc=0, sin errores (`^!` = 0), `undefined` = 0.
- `??` en el PDF: 0. `grep -rn "\[\[" chapters main.tex`: vacío.
- `pdftotext`: sin "EN_VIVO", "GATE", "pasó por alto", 512, 335, 91,6, 90,9 ni 306; "7,5 minutos" solo en el rango nuevo.
- Sin heading seguido de heading ni subsección con hijo único en los capítulos incluidos.
- Revisión visual a 100 ppp: tabla 13.I, tabla 9.IV (fila Sin CSP), tabla de cobertura de 10.2.4 y 9.2.4.
- PDF final: 261 páginas (el pie numera hasta 259).
