---
name: caballo-de-troya
description: Te dice por qué tus prospectos no te contestan ni te compran, en qué estás fallando sin rodeos, y diseña tu caballo de Troya (el MVP con el que entras al cliente) a partir de un diagnóstico con números. Úsala cuando digan /caballo-de-troya, «comenta CLAUDE», «mando la oferta y no me contesta nadie», «no me compran», «revisa mi oferta», «cómo entro a este cliente» o pasen una propuesta/PDF que no funciona.
---

# /caballo-de-troya: por qué no te compran y con qué entrar

La mayoría de gente que vende servicios (IA, automatizaciones, webs, marketing) a negocios hace lo mismo: detecta un
problema que **cree** que tiene el cliente, monta un PDF con la solución y el precio y lo manda. Nadie contesta. No es la
oferta: es que no hubo diagnóstico, nadie puso los números encima de la mesa y le estás pidiendo que compre un sistema
entero a un desconocido. El caballo de Troya es lo contrario: **un MVP pequeño, rápido y medible**, nacido de un
diagnóstico hecho **con** el cliente, que demuestra el resultado y abre la puerta al sistema completo.

Referencias: `ref/fallos.md` (los fallos y cómo detectarlos) · `ref/caballo.md` (cómo diseñar el caballo) ·
`ref/diagnostico.md` (preguntas y números del diagnóstico) · `ref/plantilla.md` (el informe que se entrega).
Motor: `motor/numeros.py` (caso de negocio en euros). Informes: `~/Desktop/Caballo de Troya/<caso>/`.

## 01 · Leer el caso
Pedir, si no lo ha dado ya (lo que haya, no hace falta todo):
- **Sector y cliente al que vende** (p. ej. clínicas dentales) y **qué le ofrece** (p. ej. sistema de captación con IA).
- **Cómo lo vende hoy**: el mensaje, el PDF o la propuesta que manda (leerlo entero si lo pasa), el precio y el canal.
- **Qué pasa**: no contestan, contestan «es caro», «no lo entiendo», «ahora no», se enfrían tras la llamada…
- **Números que tenga** del cliente o del sector (leads al mes, conversión, ticket). Si no los tiene, eso ya es un fallo.
Si falta algo clave, hacer como mucho 4 preguntas con AskUserQuestion (opciones sacadas de lo que ya dijo).

## 02 · En qué estás fallando (sin rodeos)
Recorrer `ref/fallos.md` contra su caso y quedarse con los **3–5 fallos que de verdad tiene**, ordenados por lo que más
le cuesta. Cada uno: el fallo en una frase, la **prueba** sacada de su caso (cita literal de su PDF o de lo que contó) y
qué cambia. Directo, como lo diría un mentor que quiere que venda: «El problema no es X, es Y». Nada de relleno,
nada de «en general está bien». Si la propuesta tiene cosas buenas, una línea al final.

## 03 · Tu caballo de Troya
1. **Diagnóstico**: con `ref/diagnostico.md`, escribir las preguntas que tiene que hacerle al cliente (adaptadas a su
   sector) y el guion corto para pedir esa llamada en vez de mandar el PDF.
2. **Números**: estimar el caso de negocio con `python3 motor/numeros.py …` usando sus datos o rangos del sector
   **marcados como supuestos** (nunca presentarlos como datos reales). Si el caso sale débil, decirlo: es la razón de que
   no compren.
3. **El MVP**: diseñarlo con `ref/caballo.md` (un problema, un resultado medible, 7–30 días, precio que no hace dudar,
   y el puente al sistema completo). Proponer 2 opciones y recomendar una con el porqué.
4. **Mensaje de entrada** para su canal (DM, email, WhatsApp, puerta fría): corto, en euros, sin PDF, pidiendo la llamada
   de diagnóstico.

## 04 · Entregar
Escribir el informe en `~/Desktop/Caballo de Troya/<caso>/informe.md` siguiendo `ref/plantilla.md`. En la respuesta,
corto: los 3 fallos principales, el caballo recomendado con su precio y la ruta del informe. Ofrecer el siguiente paso
(simular la llamada de diagnóstico haciendo tú de cliente, o reescribir su propuesta).

## Reglas
- **Nunca inventar** cifras del cliente, casos ni testimonios. Lo estimado va como supuesto y con rango.
- Hablar en **euros y en el idioma del dueño del negocio**, no en el del técnico (nada de «automatización de flujos»,
  «ROI a validar», «hipótesis»).
- El caballo de Troya **no es lo más barato que tengas**: es lo más pequeño que demuestra el resultado que vendes. Un
  caballo que te ancla en otro servicio (p. ej. webs de 500 € cuando vendes captación) te posiciona mal.
- Primero firma, luego construye: no se monta nada gratis «para que lo vean».
