#!/usr/bin/env python3
"""Caso de negocio en euros para el caballo de Troya.

Uso:
  python3 numeros.py --leads 120 --conv 0.15 --conv-objetivo 0.22 --ticket 900 [--margen 0.6] \
                     --mvp 490 [--sistema 1500] [--meses 12]

  --leads           leads (o contactos, llamadas…) al mes
  --conv            conversión actual a venta/cita pagada (0.15 = 15 %)
  --conv-objetivo   conversión prudente alcanzable con tu solución
  --perdidos        alternativa a --conv-objetivo: % de leads que hoy se pierden y recuperarías (0.1 = 10 %)
  --ticket          valor medio de una venta (€)
  --margen          margen bruto del cliente sobre el ticket (por defecto 1 = se mide facturación)
  --mvp             precio del MVP (pago único)
  --sistema         precio mensual del sistema completo (opcional)
"""
import argparse


def eur(x):
    return f'{x:,.0f} €'.replace(',', '.')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--leads', type=float, required=True)
    ap.add_argument('--conv', type=float, required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--conv-objetivo', type=float)
    g.add_argument('--perdidos', type=float)
    ap.add_argument('--ticket', type=float, required=True)
    ap.add_argument('--margen', type=float, default=1.0)
    ap.add_argument('--mvp', type=float, required=True)
    ap.add_argument('--sistema', type=float)
    ap.add_argument('--meses', type=int, default=12)
    a = ap.parse_args()
    for name in ('conv', 'conv_objetivo', 'perdidos', 'margen'):
        v = getattr(a, name)
        if v is not None and v > 1:
            setattr(a, name, v / 100)   # admite 15 o 0.15

    ventas_hoy = a.leads * a.conv
    extra = a.leads * (a.conv_objetivo - a.conv) if a.conv_objetivo is not None else a.leads * a.perdidos
    extra_mes = extra * a.ticket * a.margen
    label = 'margen' if a.margen < 1 else 'facturación'

    print(f'\nHoy: {ventas_hoy:.0f} ventas/mes · {eur(ventas_hoy * a.ticket)} de facturación')
    print(f'Recuperable: {extra:.1f} ventas/mes → {eur(extra_mes)} de {label} al mes · {eur(extra_mes * a.meses)} en {a.meses} meses')
    x_mvp = extra_mes / a.mvp if a.mvp else float('inf')
    print(f'MVP de {eur(a.mvp)}: se paga {x_mvp:.1f} veces en el primer mes')
    if a.sistema:
        x_sis = extra_mes / a.sistema
        print(f'Sistema de {eur(a.sistema)}/mes: {x_sis:.1f}× lo que cuesta')
    peor = min(x_mvp, extra_mes / a.sistema if a.sistema else x_mvp)
    if peor >= 3:
        veredicto = 'CASO FUERTE: el número vende solo. Ponlo encima de la mesa.'
    elif peor >= 2:
        veredicto = 'CASO JUSTO: se puede vender, pero con objeción de precio. Baja el alcance o sube el impacto.'
    else:
        veredicto = 'CASO DÉBIL: aquí está el «es caro». Cambia de problema, de cliente o de precio antes de ofrecer.'
    print(veredicto)
    print('\nRecuerda: si algún dato es supuesto, dilo como supuesto y con rango.')


if __name__ == '__main__':
    main()
