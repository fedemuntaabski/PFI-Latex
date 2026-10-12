# Citas, riesgo país, FODA y BCG (rama e75/cap7-8-11-12)

Commits: `e8cb780` biblio: verificación contra Crossref, enlaces y fuente del riesgo país; `2fae93a` cap11: FODA y BCG en TikZ. Sin push.
Nota: al empezar, HEAD estaba en `e75/cierre`; se hizo checkout de `e75/cap7-8-11-12` (cierre no se tocó).

## A) Inventario
**A1.** `biblatex[backend=biber, style=iso-authoryear, language=spanish, uniquelist=false, maxcitenames=2, mincitenames=1]` (main.tex:17). No hay `maxbibnames` (valor por defecto del estilo); no hay otras opciones.
**A2.** Claves citadas sin entrada en biblio.bib: ninguna. Entradas sin citar (no salen en la bibliografía): Elbasheer2025, Fahrmann2022, Hamarsheh2025, Hanif2024, Hassan2025, JNSM2025, Mangla2025, Mohammed2023, Parimalla2025, SAJS2025, Verizon2025. Advertencias de biber: ninguna.
**A3.** Clave `Ansari2025`, única cita: `chapters/chapter01.tex:72`: «Este problema es cada vez más relevante, ya que las soluciones tradicionales han demostrado quedarse limitadas frente a amenazas más sofisticadas \parencite{Ansari2025}.» (no modificada).

## B) Verificación contra Crossref
| Entrada | Dato | Antes → después | Fuente |
|---|---|---|---|
| Hariri2019 | año (vol. 33, n.º 4) | 2019 → 2021 | Crossref (published-print) |
| VillarrealVasquez2021 | año (vol. 20, n.º 1); nota | 2021 → 2023; se quitó «Publicado en vol. 20, n.º 1, 2023» | Crossref |
| Glockler2023 | año (vol. 66, n.º 4) | 2023 → 2024 (clave sin cambio) | Crossref (published-print) |
| Landauer2023Survey | n.º de artículo | `number=100470` → `eid=100470` | Crossref |
| JNSM2025 | año (vol. 34, n.º 1) | 2025 → 2026; + urldate | Crossref (journal-issue) |
| Ansari2025 | autor 2; número | «Syed, Sharik Ali» → «Ali, Syed Sharik»; + n.º 12 | Crossref |
| Mohammed2023 | autor 1; tipo | «Mohammed, Mahmood» → «Almansoori, Mahmood»; Miklós con tilde; @Article/WINS → @InProceedings (actas del 1st Workshop on Intelligent Infocommunication Networks, Systems and Services) | Crossref |
| Hamarsheh2025 | autores; páginas | «Hamarsheh, Iyad S.» → «Iseed, Sara and Hamarsheh, Mohammad M. N.»; + págs. 1–6 | Crossref |
| Stylios2023 | autores | Skalkos/Karyda → Chatzis, Sotirios/Thanou, Olga | Crossref |
| Hu2014 | autores | 10 autores → los 7 de Crossref (sin Friedman, Lang, Cogdell); nombres completos | Crossref |
| Parimalla2025 | tipo; autor | @Article/IntechOpen → @InCollection (libro «Mastering Intrusion Detection for Cybersecurity»); «Sowmya, Ch.» → «Likhitha Sowmya, Ch.» | Crossref |
| Hassan2025 | n.º de artículo | + eid 35871 | Crossref |
| Weihrich1982 | DOI | + 10.1016/0024-6301(82)90120-0 (confirmado: Long Range Planning 15(2):54–66, 1982) | Crossref |
| Porter1979 | url, urldate | + https://hbr.org/1979/03/how-competitive-forces-shape-strategy, 2026-10-11 (200) | URL |
| Henderson1970 | url, urldate | + https://www.bcg.com/publications/1970/strategy-the-product-portfolio, 2026-10-11 (página «The Product Portfolio», Bruce Henderson; con curl devuelve 403 por bloqueo de bots, abre con WebFetch) | URL |
| Osterwalder2010 | url, urldate | + página del libro en Wiley (200), 2026-10-11; ISBN conservado | URL |
| Aliyu2024 | autores; urldate | «Aliyu, M. B. and others» → Aliyu, Muhammad Bello; Garba, Muhammad; Gabi, Danlami; Suru, Hassan U.; Argungu, Musa S. (portada del PDF de jatit.org); + urldate. Sale «Disponible en» | PDF jatit.org |
| Elbasheer2025 | url, urldate | + https://arxiv.org/abs/2506.23446 (200) | URL |
| SAJS2025, Verizon2025 | urldate | + 2026-10-11 | URL (200) |
| MENDEZ2026RiesgoPais | entrada nueva | @online, MDZ Online, 2026-10-02, urldate 2026-10-11 (200) | URL |

**No cambiados, para revisar a mano:**
- **Hanif2024** (10.3390/electronics13010175): el DOI corresponde a otro artículo («Explainability and Evaluation of Vision Transformers…», Stassin et al.). Título y autores de la entrada no coinciden. Entrada sin citar.
- **Mangla2025** (10.56127/ijst.v4i1): es un DOI de número (journal-issue) sin título ni autores en Crossref.
- **NIST_AI100_2_2025**: Crossref solo lista a Vassilev y título truncado; la entrada conserva los 6 autores. DOI resuelve (200).
- **Aliyu2024**: el título del PDF es «Dynamic Access Control at the Network Edge Using an Adaptive Risk-based Access Control System (ad-RACs)» y difiere del de la entrada; no se cambió.
- **Hariri2019**: Crossref escribe «Kind, Matias Carrasco»; se mantiene «Carrasco Kind» (forma correcta).
- DOI sin registro en Crossref (DataCite): Landauer2022Dataset (Zenodo; curl 403 por bots) y Kent2015 (resuelve a csr.lanl.gov, 200).
- Títulos con diferencias de mayúsculas respecto de Crossref (Larman2003, Kuppa2022): sin cambios.
- Enlaces comprobados (200): FRED, OWASP, jatit, SAJS, Verizon, Springer, las 6 normas de infoleg, hbr.org, arxiv, wiley, MDZ, DOIs NIST/LANL.
- Ninguna entrada de biblio.bib queda sin DOI ni URL.

## C) Riesgo país (negocio.tex, 12.4.1)
Texto anterior: «…que en la misma semana osciló entre 573 y 650 puntos básicos según el índice EMBI de J.\,P.~Morgan. El resultado, entre el 11 % y el 12 %,…».
Texto nuevo: «…que el 2 de octubre de 2026 llegó a 650 puntos básicos, su máximo del año, según el índice de J.\,P.~Morgan \parencite{MENDEZ2026RiesgoPais}. El resultado, cercano al 12 %,…». No se tocaron el 25 % ni la prima. Observación: el título de la nota dice «más alto en once meses» y la URL «más alto de 2026»; el texto usa «máximo del año» como se pidió.

## D) Figuras
`images/diagramas/tikz/foda.tex` (11.1) y `bcg.tex` (11.2), incluidas con `\input` en `chapters/e50_mercado.tex`; caption, label y «Fuente» intactos. FODA: 2×2, ítems 5/5/3/4 en el orden de las subsecciones, ≤10 palabras, `\footnotesize`, ancho de texto, altura ≤0,6; debilidad 3 «Capacidad de detección todavía limitada.» BCG: ejes y cuadrantes pedidos, círculo UMBRAL en Interrogante, sin marca de agua.

## E) Verificación (pdflatex, biber, pdflatex, pdflatex)
- «??»: 0. Ninguna página con texto debajo de «Página N de M». Total: «de 263».
- Bibliografía: las 40 entradas del .bbl tienen DOI o URL (0 sin ellos).
- «[s.f.]»: 0. «et al.» en la bibliografía: 0 (sí aparece en el texto). «Disponible también desde»: 0. «573» en el cap. 12: 0 (única coincidencia en el documento: id=375738 de una URL).
- PNG (110 dpi) en `docs/verificacion/figuras_tikz/v3/`: figuras 11.1 y 11.2 y págs. 193–197 del PDF (bibliografía).
