# Caballo de Troya · skill de Claude Code

«Le vendo sistemas de captación con IA a clínicas dentales, pero cuando les mando la oferta no me contesta nadie.»

Le explicas tu caso a Claude y esta skill te dice:

1. **Por qué no te compran**: lee tu caso y tu oferta (o el PDF que mandas).
2. **En qué estás fallando**: sin rodeos, con la prueba sacada de tu propia propuesta.
3. **Tu caballo de Troya**: el MVP con el que entras al cliente, con el diagnóstico, los números en euros y el mensaje
   para pedir la llamada en vez de mandar otro PDF.

Hecha por [Denis Corral · Sell Your AI](https://sellyourai.io).

## Qué necesitas

- [Claude Code](https://claude.com/claude-code)
- Python 3 (solo librería estándar, para la calculadora del caso de negocio)

## Instalación

```bash
git clone https://github.com/deniscorral3am/caballo-de-troya-skill.git ~/.claude/skills/caballo-de-troya
```

## Uso

En Claude Code escribe `/caballo-de-troya` (o «no me contesta nadie cuando mando la oferta») y cuéntale:
a quién vendes, qué ofreces, cómo lo vendes hoy (pásale tu PDF o tu mensaje) y qué te responden.
El informe se guarda en `~/Desktop/Caballo de Troya/<caso>/informe.md`.

Calculadora sola, sin Claude:

```bash
python3 ~/.claude/skills/caballo-de-troya/motor/numeros.py --leads 120 --conv 15 --conv-objetivo 22 --ticket 900 --mvp 490 --sistema 1500
```

## La guía

[`GUIA.md`](GUIA.md): el método explicado para aplicarlo tú, con o sin Claude.

## Estructura

- `SKILL.md`: instrucciones de la skill
- `GUIA.md`: la guía para aplicarlo
- `motor/numeros.py`: caso de negocio en euros (cuánto pierde, cuánto recuperas, cuántas veces se paga)
- `ref/fallos.md`: los 13 fallos por los que no te contestan
- `ref/caballo.md`: cómo diseñar el MVP de entrada
- `ref/diagnostico.md`: preguntas y números del diagnóstico
- `ref/plantilla.md`: el informe que te entrega
