# E75 / 18: sesión en vivo (D7)

Rama `e75/entrega`, commit desplegado `e1e7450`. Fecha: 2026-10-10. Host: `https://3-147-149-208.sslip.io`. Sin secretos en este informe: de las keys solo figuran hashes.

## 1. Resultado por paso

| Paso | Resultado | Evidencia |
|---|---|---|
| 0. Precondiciones y SSM | OK | Rama y merges correctos, nada en el 8001. `ADMIN_PASSWORD` y `OPERADOR_PASSWORD` generadas (20 caracteres, distintas) y cargadas en SSM como SecureString (versión 3 las dos) y en `api/.env` (ignorado por git). `SMTP_PASSWORD` de SSM coincide con la de `api/.env` (16 caracteres): **no se rotó** (decisión del autor). |
| 1. Ensayo local | OK | `ensayo_demo_pep.py` rc=0, primer `critico` en el evento #44 (90,03). `test_e2e_pdp_pep.py`: 2 passed. Con el `.venv` (el Python global falla: TensorFlow con NumPy 2, `np.complex_`). |
| 2. Revert de ACL | OK en consola elevada / FAIL sin elevar | Ver §2. |
| 3. Keys de agente | OK | Altas con `--uid demo-pfi`: `FEDE-PC-FEDE` (hash `f46317cf…`, se revocó 1 key previa `9342f579…`) `LAPTOP-7E9NKCHE-feder` (hash `d57ab4eb…`, sin keys previas) y `Santi-PC-User` (PC del compañero, hash `fd4f7da5…`, sin keys previas; alta posterior al cierre, con la instancia apagada). La key de cada equipo se mostró una sola vez. |
| 4. Prender | OK | running, SSM Online, `/api/health/ready` 200 por HTTPS. |
| 5. Desplegar | OK | API release `20261010-115202-e1e7450` (reinicia `scoring-api` y toma las passwords nuevas). Caddy 2.11.7 con el Caddyfile nuevo, API solo en `127.0.0.1:8001`. Frontend `20261010-115453`; `dist/` sin la key de `frontend/.env`, sin passwords ni keys de agente, sin rutas de disco. |
| 6. TLS | OK | Ver §3. |
| 7. Login por curl | OK | Ver §4. El login en navegador queda a cargo del autor. |
| 8. Agente real | OK | Ver §5. |
| 9. Rechazos | OK | `uid` ajeno 403; `agent_id` ajeno 403; confirmación de `uid` ajeno 403; agente con `http://` fuera de loopback aborta con rc=1 (`fuera de loopback ... solo se acepta https://`). |
| 10. Cierre | OK | Agente detenido, `--revert` rc=0 desde `acl_backup.txt`, `icacls` sin `DENY`, overrides de país e `isLocalIP` limpiados. Reset de `demo-pfi` (200, luego 404 "sin eventos"). Instancia **stopped** (`estado.ps1`). `revisar_gastos.ps1`: gasto del mes USD 1,80 de 20, `[VERDE]`. |

## 2. Prueba manual de reversión de ACL

- **Consola sin privilegios: FAIL.** `icacls /restore` terminó con error 1300 (privilegios no asignados), `revert()` cayó al respaldo `/remove:d` y se perdió la denegación previa del usuario.
- **Consola elevada: `RESULTADO: PASS (5 chequeos)`.** Log `ACL restaurada desde acl_backup.txt`, sin `respaldo /remove:d`. La denegación previa `(DENY)(W)` sigue en `previo.txt`, el acceso se restauró y `acl_backup.txt` se descartó.
- **Código revisado** (`agent/enforcement.py:213-263`): coincide con el diseño documentado. El 1300 es del entorno, no de la lógica: `icacls /restore` necesita `SeRestorePrivilege`, que solo tiene un proceso elevado. `/deny` y `/save` funcionan sin elevar.
- En la sesión en vivo el `--revert` corrió elevado y usó `/restore` (rc=0).

## 3. TLS de punta a punta

| Chequeo | Resultado |
|---|---|
| Certificado | Sin errores de validación, emisor Let's Encrypt (`CN=YE2`), sujeto `3-147-149-208.sslip.io`, vence 01/04/2027, TLS 1.2 |
| `curl` sin `-k` | HTTP 200, `ssl_verify=0` |
| `http` → `https` | 308 con `Location: https://3-147-149-208.sslip.io/` |
| Puerto 8001 desde afuera | cerrado |
| `/api/docs` | 404 |
| HSTS | `Strict-Transport-Security: max-age=31536000` (sin `includeSubDomains` ni `preload`) |

## 4. Login en la nube (curl)

- Admin: token de 43 caracteres, distinto de `SCORING_ADMIN_KEY`.
- Operador: token de 43 caracteres; `PUT /config/umbrales` con ese token → **403**; `GET /usuarios` → 200 antes del logout y **401** después.
- Los logins usaron las passwords nuevas de SSM.

## 5. Agente real contra la EC2

- Agente elevado, `agent_id=FEDE-PC-FEDE`, `dry_run=False`, con `SCORING_AGENT_KEY` y sin `SCORING_ADMIN_KEY`. Sin `Circuit breaker ABIERTO`.
- Secuencia de niveles: `medio` (68,9) → `medio` → `bajo` (35,9) → `medio` → con el país simulado RU y `isLocalIP=False`: `file_created` → **`critico` 97,06, `terminar_y_denegar`**. No se observó el nivel `alto`: el score pasó de 52 a 97 en un solo evento.
- El agente terminó `python.exe` (el `demo_exfil`, `rc=15`) y denegó `C:\PFI_DEMO\confidencial`: `icacls` mostró `FEDE-PC\FEDE:(OI)(CI)(N)`. Después, `--revert` lo levantó.
- `demo_exfil.py` corrió con el token de sesión del admin como `SCORING_ADMIN_KEY` (ver riesgo 2).

## 6. Cambios para la tesis

1. **Estado del despliegue:** API, Caddy y frontend desplegados en la EC2 desde el commit `e1e7450`, probados el 2026-10-10 y la instancia apagada al cierre (stopped, gasto del mes USD 1,80 de 20).
2. **TLS verificado de punta a punta:** certificado de Let's Encrypt válido para `sslip.io`, redirección 308, 8001 cerrado, `/api/docs` 404.
3. **Login en la nube:** token opaco de 43 caracteres distinto de las claves fijas, rol operador con 403 en endpoints de administración, token invalidado en el logout (401).
4. **HSTS:** presente con `max-age=31536000`. El texto no debe prometer `includeSubDomains` ni `preload`.
5. **Reversión de ACL (RNF-06, objetivo 4):** verificada con `icacls /restore` conservando las denegaciones previas, **con la condición de correr el agente y `--revert` elevados**. Sin elevación degrada a `/remove:d` y pierde las denegaciones previas. Hay que decirlo en la tesis.
6. **Ciclo PDP→PEP en vivo:** llegó a `critico` con `terminar_y_denegar`, terminó el proceso y denegó la carpeta (97,06 en la nube; en el ensayo local, 90,03). Corregir si algún texto dice que el margen es de centésimas.
7. **Rechazos de RF-02:** 403 por `uid`, `agent_id` y confirmación ajenos, y el agente aborta con `http://`.
8. **Higiene abierta:** la App Password de Gmail sigue viva y en la historia pública del repo (`c3e0534`, `02_seguridad.md:221`); no se rotó. No afirmar en la tesis que esa higiene está cerrada.

## 7. Riesgos para la demo del 20/10

1. **Consola de administrador obligatoria** para el agente y para `--revert`.
2. **Emails reales posibles.** `demo_exfil.py --no-notify` falló: el reset del uid invalida las sesiones, así que el `GET/PUT /config/notificaciones` con el token de sesión dio 401 y las notificaciones no se desactivaron. La configuración actual notifica en `medio`, con un destinatario (`s***@gmail.com`). El agente generó muchos eventos `medio`, así que pudieron salir emails reales (revisar esa bandeja). Para la demo, desactivar `notif_niveles` desde el dashboard antes de empezar, o usar la admin key fija en la consola de `demo_exfil`.
3. **`SCORING_ADMIN_KEY` de `api/.env` no sirve en la nube:** el reset dio 403 (causa probable: difiere de la de SSM, no se verificó). `demo_exfil.py` necesita la admin key real de SSM; hay que copiarla a esa consola.
4. **Margen de `critico`:** en la nube el salto fue limpio (97,06), pero el ensayo local sigue dando 90,03 contra 90. No contar con que `alto` aparezca antes de `critico`.
5. **Python global roto** (TensorFlow con NumPy 2): usar siempre el `.venv`.
6. **La PC del compañero (`Santi-PC-User`) tiene key pero no se probó con el agente real.** Hay que ensayarla antes de la demo: consola de administrador, `.venv` propio y la key entregada por un canal privado.
7. **Red de la facultad:** solo deja pasar el 443; la demo va por `https://…sslip.io`, no por otros puertos.
8. **Costo:** la instancia apagada sigue cobrando EIP + EBS (~USD 6/mes). Prender solo para la demo y apagar al terminar.
9. **Login en navegador no probado en esta sesión** (admin con `PUT` 200, operador en solo lectura, `sessionStorage` con el token de 43 caracteres): lo hace el autor.
10. **`python-dotenv` avisa de líneas que no puede parsear** en `.env` (ruido inocuo en consola).
