# Ajuste de citas (rama e75/cap7-8-11-12)

Commit: biblio: número de artículo de Landauer, título de Aliyu y URL de Osterwalder. Sin push.

## 1) Landauer2023Survey
`eid = {100470}` → `pages = {100470}`. En el PDF: «Vol. 12, pág. 100470. Disponible en: DOI: 10.1016/j.mlwa.2023.100470».

## 2) Aliyu2024
Confirmado en el PDF de jatit.org (21 páginas):
- Título (portada, en mayúsculas): DYNAMIC ACCESS CONTROL AT THE NETWORK EDGE USING AN ADAPTIVE RISK-BASED ACCESS CONTROL SYSTEM (ad-RACs). El PDF lo imprime todo en mayúsculas, así que en la entrada quedó en mayúscula inicial por palabra y «ad-RACs» tal cual: «Dynamic Access Control at the Network Edge Using an Adaptive Risk-Based Access Control System (ad-RACs)». Es la decisión editorial a confirmar.
- Autores: Muhammad Bello Aliyu, Muhammad Garba, Danlami Gabi, Hassan U. Suru, Musa S. Argungu (ya cargados antes).
- J. Theor. Appl. Inf. Technol., 15 feb. 2024, Vol. 102, n.º 3. Páginas 980–1000 (numeración impresa 980 a 1000). Se agregó `pages = {980--1000}`.
- El título anterior de la entrada («An Adaptive Risk-Based Access Control System for Dynamic Authorization Using Machine Learning at the Edge») no figuraba en el PDF.

Oraciones del documento que citan Aliyu2024 (sin modificar):
1. `chapters/chapter02.tex:217`: «El control de acceso adaptativo basado en riesgo (RAdAC) se ha consolidado como una de las principales líneas de investigación para abordar los desafíos de seguridad en entornos dinámicos. Dentro de este enfoque, destaca el desarrollo de *ad-RACs* (*Adaptive Risk-Based Access Control System*), un sistema diseñado para gestionar autorizaciones de acceso en tiempo real mediante la evaluación continua del riesgo asociado a cada solicitud \parencite{Aliyu2024}. A diferencia de los mecanismos tradicionales, que suelen basarse en verificaciones realizadas únicamente durante la autenticación inicial, esta propuesta considera el contexto de cada interacción antes de tomar una decisión de acceso.»
2. `chapters/chapter04.tex:141`: celda de tabla «Fuente académica | \textcite{Aliyu2024}».
3. `chapters/chapter04.tex:238`: celda de tabla «Fuente académica | \textcite{Aliyu2024} (ad-RACs)».
Para el autor: el resumen del PDF describe ad-RACs como un sistema en el borde de red que estima riesgo con CatBoost a partir de cuatro entradas (contexto del usuario, sensibilidad del recurso, severidad de la acción e historial de riesgo), con política Chinese wall y actualización del historial. «Evaluación continua del riesgo de cada solicitud» y «considera el contexto de cada interacción» son consistentes con eso; «en tiempo real» no aparece en el resumen (revisar si se quiere sostener).

## 3) Osterwalder2010
- (a) `https://www.wiley.com/en-us/Business+Model+Generation-p-9780470876411`: 200, sin redirección; abre la página del libro (Osterwalder y Pigneur, ISBN 978-0-470-87641-1). **Queda esta.**
- (b) `https://www.wiley.com/en-us/9780470876411`: 404 (descartada).
- (c) `https://www.strategyzer.com/library/business-model-generation`: 200 (no usada).
ISBN y urldate (2026-10-11) conservados.

## 4) Verificación (pdflatex, biber, pdflatex, pdflatex)
- Landauer 2023: aparece «pág. 100470» y el DOI. 
- Título de Aliyu: 1 aparición (bibliografía).
- URL de Osterwalder: sin «%3A» ni «%2C» (0 en todo el documento).
- «??»: 0. Ninguna página con texto debajo de «Página N de M». Total «de 263».
