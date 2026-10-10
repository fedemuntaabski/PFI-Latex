# Plan: llevar a la tesis los resultados del repo de código (E75)

## Reglas
- Rama `e75/textos-codigo` desde la rama de trabajo vigente del LaTeX (la que tiene mergeado `correcciones-e75-latex`). Commits en español SIN atribución a Claude/Claude Code. Antes de pushear: `git log <base>..HEAD --format=%B | grep -ci claude` = 0. Push al terminar. Nunca --force.
- Fuente de verdad: los informes del repo de código en `G:\pfi\Agente-Aut-nomo-de-Vigilancia-Conductual-y-Mitigaci-n-de-Riesgo-de-Identidad\informes_codigo_e75/` (02, 04, 05, 11, 12, 13, 14, 15 y 16). **Usá las cifras del informe 16 §2** donde difieran del 15. El repo de código solo se LEE.
- No inventes cifras ni estados: cada texto nuevo sale de un informe. Si algo no está, dejalo como marcador.
- Redacción impersonal, en presente, español académico, con el estilo del resto del documento y sin rutas de archivo del repo de código en el cuerpo (en las tablas de evidencia sí se pueden nombrar los tests). Citas con `\parencite`.
- Los resultados que dependen de la sesión en vivo con la EC2 (TLS de punta a punta con un agente real, login en la nube, estado del despliegue, HSTS) se dejan como marcadores `[[EN_VIVO: …]]`. Todos los `[[CODIGO…]]` actuales se reemplazan por texto o pasan a `[[EN_VIVO…]]`.
- NO toques el texto del gate de promoción de RF-21 (CU-03, épica 3, §9.2.4, §10.9): depende de otro merge.
- Compilá con latexmk después de cada capítulo.

## Cambios

### 1. Objetivos (cap. 1) y su cumplimiento (tabla 13.I)
Reformulá los objetivos específicos con los textos de `05_objetivos.md` §1 y de los informes:
- 1: texto del 05, ajustado a lo implementado en el 11 (TLS, credencial individual ligada a su identidad, sin respaldo en la admin key).
- 2: texto del 05.
- 3: el actual, más la aclaración del 05 ("medida en el servidor de la API, sin incluir el envío de notificaciones").
- 4: el del 13 §7.
- 6: el del 05.
- 7: el del 11 §6.
- 8: el del 05.
- 9: se mantiene el 85 %, aclarando que se mide sobre líneas en la API y en el agente (15 §6).

Después, completá la tabla 13.I con el estado y la evidencia de cada objetivo, coherentes con los textos nuevos:
- 4 y 9: Cumplido;
- 1 y 7: Cumplido, con la parte de verificación en la nube como `[[EN_VIVO]]`;
- 2: Parcial, con las cifras del 04;
- 6: según el gate (dejá un marcador `[[GATE]]`).
Revisá también el texto de 13.1 y 13.2 para que no contradiga la tabla.

### 2. Requerimientos (cap. 4)
- RF-02: texto del 11 §6. La parte de verificación con un agente real contra la nube va como `[[EN_VIVO]]`.
- RF-31: texto del 12 §4.
- RNF-03: texto del 11 §6, sin decir que la CSP "se agrega en el proxy": no se implementa y va como limitación.
- RNF-06: texto del 13 §7. La oración de la verificación manual queda condicionada (`[[EN_VIVO: prueba manual de revert]]`).
- RNF-13: "Implementado en el despliegue (TLS con certificado público, redirección a HTTPS, API solo en loopback detrás del proxy); el agente rechaza URLs http fuera de loopback", más `[[EN_VIVO]]` para la verificación de punta a punta.
- Recontá los estados de RF y RNF a partir de las tablas y actualizá TODOS los conteos del documento: cap. 4, tabla 9.II, 9.7, 13.1 y el marcador de conteo de 13.1.
- Buscá en TODO el documento y alineá con el token de sesión del 11: "clave de administrador", "sessionStorage", "control de la interfaz", "X-API-Key", "credenciales fijas". Incluye CU-02 flujo alternativo 3a, HU-14 y la tabla de protocolos.

### 3. Producto (cap. 9)
- 9.2: control de acceso (token de sesión, roles, keys de agente con `--uid`) según el 11.
- Tabla 9.III (Ley 25.326): el marcador del art. 9 se reemplaza con los controles del 11 (TLS, credencial individual ligada, token con vencimiento y logout, secretos en SSM); la verificación en la nube va como `[[EN_VIVO]]`. La fila de Gemini, con el texto del 12 §5.
- Tabla 9.IV de limitaciones:
  - "Canal sin cifrar entre agente y API": actualizar (el agente exige https; falta la verificación de punta a punta → `[[EN_VIVO]]`);
  - "Clave de agente no ligada a su identificador": **resuelta** (11);
  - "Autenticación permisiva sin claves configuradas": actualizar (sin respaldo en la admin key; modo estricto en la nube);
  - "Reversión de permisos amplia": **resuelta** (13 §7);
  - "Prompt injection": texto del 12 §5;
  - agregar "Sin autenticación mutua por certificado (mTLS)", con el diseño del 02 §5 como trabajo futuro;
  - agregar "Sin política de seguridad de contenido (CSP) en el dashboard".
  Si una limitación queda resuelta, sacala de la tabla o marcala como resuelta según el criterio del resto del capítulo, y mencionala en 10.9.
- 9.6.2: reemplazo completo con el texto del 12 §5.
- Si 9.6 queda con un solo hijo después de los cambios, corregilo (sin hijo único).

### 4. Pruebas (cap. 10)
- 10.1 (tabla de técnicas): sumar la prueba E2E automatizada PDP→PEP y la medición de cobertura (coverage.py).
- 10.2:
  - inventario y resultados con las cifras del 16 §2 (335 API, 177 agente, 512 en total);
  - sacar "No se mide la cobertura de código…";
  - nueva subsección de cobertura con el texto y la tabla del 15 §6 (cifras del 16 §2: 91,6 % y 89,3 %);
  - CI con el job `agent-windows` y el umbral del job `api`.
- 10.2.4 (evidencia por requerimiento): RF-18, RF-19, RF-22 y RF-31 pasan a "Prueba automatizada"; RF-26 a prueba parcial; RNF-13 deja de ser "No implementado".
- 10.3: agregar la prueba E2E con el texto del 14 §9.
- 10.5: corregir "CLUE-LDS más 92 eventos reales del agente" con el texto del 04 §5 aviso 1, y el marcador de Pearson con el del 04 §2 (−0,22, 234 usuarios, p < 0,001, más la nota opcional de los 15 usuarios).
- 10.6:
  - el marcador de las 3 detecciones, con el texto del 04 §3;
  - el de la curva, con el texto del 04 §4;
  - reemplazar la figura `images/pruebas/curva_umbral.pdf` por `<RUTA_REPO_CODIGO>/informes_codigo_e75/modelo/curva_umbral_completa.pdf` y ajustar el epígrafe;
  - aclarar que 14,3 % / 21,6 % son por nivel ≥ alto, incluida la regla de piso (04 §5 aviso 3).
- 10.9 (decisiones): sumar filas por la seguridad B, la reversión precisa, los controles de Gemini y la cobertura, con el resultado que motivó cada una.
- 10.10 (limitaciones): la regresión sigue con 6 discrepancias (14 §5; el valor esperado de big-maroon cambió); sacar la limitación de cobertura no medida; mantener la del frontend sin tests, como declaración.

### 5. Conclusiones (cap. 13)
- 13.4 trabajo futuro:
  - sacar los ítems resueltos (reversión acotada; pruebas "agregar pruebas a los requerimientos sin prueba");
  - actualizar el ítem de pruebas (tests del frontend, `metricas_service`, latencia con Redis real);
  - el ítem de seguridad: mTLS con el diseño del 02 §5, CSP e IdP real.
- Reemplazá los marcadores de 13.4 según corresponda.

### 6. Bibliografía
- `Rose2020` y `Hu2014`: pasar de `@Article` con journal "NIST" a `@TechReport` (institution con llaves dobles, number SP 800-207 / SP 800-162), como `NIST2023_800207A`.

## Cierre
Informe `informes_e75/20_textos_codigo.md`:
- cambios por capítulo (archivo y línea, antes → después en lo sustancial);
- conteos RF/RNF antes → después;
- lista de marcadores que quedan (`[[EN_VIVO…]]` y `[[GATE]]`), con su ubicación y qué dato falta;
- resultado de la compilación.