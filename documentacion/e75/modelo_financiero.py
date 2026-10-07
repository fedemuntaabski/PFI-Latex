"""Modelo económico-financiero del PFI (E75).

Todos los supuestos están en SUPUESTOS. Cambiar un valor y volver a correr:
    python modelo_financiero.py            -> resumen en consola
    python modelo_financiero.py --latex    -> tablas LaTeX (pegar en el capítulo de negocio)

Moneda: USD constantes (sin inflación). Flujos anuales de fondos, sin valor residual.
"""
import sys

SUPUESTOS = {
    "horizonte_anios": 5,
    "tasa_descuento": 0.25,            # costo de oportunidad en USD (ver justificación en el texto)
    "sensibilidad_tasas": [0.20, 0.30, 0.35],
    # Inversión inicial (año 0)
    "inversion_inicial": {
        "Horas del equipo valorizadas (1.000 h x USD 15/h)": 15000,
        "Pasaje de prototipo a producto (instalador, firma de código, hardening)": 6000,
        "Constitución de la sociedad y asesoramiento legal": 1500,
        "Certificado de firma de código para Windows (primer año)": 500,
    },
    # Producto y precio (sección Precio del documento)
    "endpoints_por_cliente": 75,        # PyME de referencia: 50 a 100 equipos
    "precio_business": 4.0,             # USD por endpoint/mes (rango 2 a 5)
    "precio_enterprise": 8.0,           # USD por endpoint/mes (rango 6 a 10)
    "mix_enterprise": 0.30,
    # Costos variables
    "costo_nube_por_endpoint": 0.60,    # USD por endpoint/mes (cómputo, Redis, Postgres, correo)
    "comision_pagos": 0.03,             # procesador de pagos, sobre ingresos
    "ingresos_brutos": 0.03,            # supuesto conservador, sobre ingresos
    "ventas_por_canal": 0.50,           # proporción de clientes que llegan por MSSP/integradores
    "comision_canal": 0.20,             # comisión del MSSP sobre lo que vende
    # Costos fijos mensuales por año (equipo + soporte) e infraestructura base
    "fijo_mensual_por_anio": [3500, 6000, 9000, 11000, 12000],
    "infra_fija_mensual": 250,
    "impuesto_ganancias": 0.25,         # sobre resultado positivo del año (supuesto simplificado)
    "escenarios": {
        "Pesimista": {"altas_mensuales": [0.5, 1, 2, 2, 2], "churn_mensual": 0.030, "cac": 2500},
        "Base":      {"altas_mensuales": [1, 3, 5, 6, 6],   "churn_mensual": 0.020, "cac": 1500},
        "Optimista": {"altas_mensuales": [2, 5, 8, 10, 10], "churn_mensual": 0.015, "cac": 1000},
    },
}

S = SUPUESTOS
INV0 = sum(S["inversion_inicial"].values())
ARPU_ENDP = (1 - S["mix_enterprise"]) * S["precio_business"] + S["mix_enterprise"] * S["precio_enterprise"]
ARPU_CLIENTE = ARPU_ENDP * S["endpoints_por_cliente"]


def margen_contribucion_cliente():
    pct = S["comision_pagos"] + S["ingresos_brutos"] + S["ventas_por_canal"] * S["comision_canal"]
    return ARPU_CLIENTE * (1 - pct) - S["costo_nube_por_endpoint"] * S["endpoints_por_cliente"]


def simular(esc):
    clientes, filas = 0.0, []
    for a in range(S["horizonte_anios"]):
        ing = var = fijo = cac = 0.0
        altas = 0.0
        for _ in range(12):
            n = esc["altas_mensuales"][a]
            altas += n
            clientes = clientes * (1 - esc["churn_mensual"]) + n
            rev = clientes * ARPU_CLIENTE
            ing += rev
            var += (clientes * S["endpoints_por_cliente"] * S["costo_nube_por_endpoint"]
                    + rev * (S["comision_pagos"] + S["ingresos_brutos"])
                    + rev * S["ventas_por_canal"] * S["comision_canal"])
            fijo += S["fijo_mensual_por_anio"][a] + S["infra_fija_mensual"]
            cac += n * esc["cac"]
        res = ing - var - fijo - cac
        imp = max(0.0, res) * S["impuesto_ganancias"]
        filas.append(dict(anio=a + 1, clientes=clientes, altas=altas, ingresos=ing, variables=var,
                          fijos=fijo, cac=cac, impuesto=imp, flujo=res - imp))
    return filas


def van(fl, k):
    return -INV0 + sum(f / (1 + k) ** (i + 1) for i, f in enumerate(fl))


def tir(fl):
    lo, hi = -0.99, 10.0
    if van(fl, lo) * van(fl, hi) > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        if van(fl, lo) * van(fl, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return mid


def payback(fl, k=None):
    acc = -INV0
    for i, f in enumerate(fl):
        f2 = f / (1 + k) ** (i + 1) if k else f
        if acc + f2 >= 0 and f2 > 0:
            return i + (-acc) / f2
        acc += f2
    return None


def necesidad_maxima(fl):
    acc, minimo = -INV0, -INV0
    for f in fl:
        acc += f
        minimo = min(minimo, acc)
    return -minimo


def resultados():
    out = {}
    for nombre, esc in S["escenarios"].items():
        filas = simular(esc)
        fl = [r["flujo"] for r in filas]
        out[nombre] = dict(filas=filas, van=van(fl, S["tasa_descuento"]), tir=tir(fl),
                           payback=payback(fl), payback_desc=payback(fl, S["tasa_descuento"]),
                           necesidad=necesidad_maxima(fl),
                           sens={k: van(fl, k) for k in S["sensibilidad_tasas"]})
    return out


def fmt(x):
    return f"{x:,.0f}".replace(",", ".")


def anios(x):
    return "no recupera" if x is None else f"{x:.1f} años".replace(".", ",")


def pct(x):
    return "no existe" if x is None else f"{x * 100:.1f} %".replace(".", ",")


def consola():
    mc = margen_contribucion_cliente()
    print(f"Inversión inicial: USD {fmt(INV0)}")
    print(f"Ingreso mensual por cliente: USD {fmt(ARPU_CLIENTE)}  (USD {ARPU_ENDP:.2f} por endpoint)")
    print(f"Margen de contribución mensual por cliente: USD {fmt(mc)}")
    for a, f in enumerate(S["fijo_mensual_por_anio"]):
        pe = (f + S["infra_fija_mensual"]) / mc
        print(f"  Punto de equilibrio año {a + 1}: {pe:.1f} clientes activos")
    for n, r in resultados().items():
        print(f"\n{n}: VAN={fmt(r['van'])} TIR={pct(r['tir'])} payback={anios(r['payback'])} "
              f"descontado={anios(r['payback_desc'])} necesidad máx. de fondos={fmt(r['necesidad'])}")
        for f in r["filas"]:
            print(f"  año {f['anio']}: clientes {f['clientes']:.0f} ingresos {fmt(f['ingresos'])} "
                  f"flujo {fmt(f['flujo'])}")
        print("  sensibilidad VAN:", {f"{k:.0%}": fmt(v) for k, v in r["sens"].items()})


def latex():
    res = resultados()
    H = S["horizonte_anios"]
    print("% --- Tabla: flujos netos por escenario (USD) ---")
    print("\\begin{tabular}{l" + "r" * (H + 1) + "}\n\\hline")
    print("Escenario & Año 0 & " + " & ".join(f"Año {i + 1}" for i in range(H)) + " \\\\\n\\hline")
    for n, r in res.items():
        print(f"{n} & {fmt(-INV0)} & " + " & ".join(fmt(f['flujo']) for f in r["filas"]) + " \\\\")
    print("\\hline\n\\end{tabular}\n")
    print("% --- Tabla: clientes activos al cierre de cada año ---")
    print("\\begin{tabular}{l" + "r" * H + "}\n\\hline")
    print("Escenario & " + " & ".join(f"Año {i + 1}" for i in range(H)) + " \\\\\n\\hline")
    for n, r in res.items():
        print(f"{n} & " + " & ".join(f"{f['clientes']:.0f}" for f in r["filas"]) + " \\\\")
    print("\\hline\n\\end{tabular}\n")
    print("% --- Tabla: indicadores ---")
    print("\\begin{tabular}{lrrrrr}\n\\hline")
    print("Escenario & VAN (25\\,\\%) & TIR & Payback simple & Payback descontado & Necesidad máx. de fondos \\\\\n\\hline")
    for n, r in res.items():
        print(f"{n} & {fmt(r['van'])} & {pct(r['tir'])} & {anios(r['payback'])} & "
              f"{anios(r['payback_desc'])} & {fmt(r['necesidad'])} \\\\".replace("%", "\\%"))
    print("\\hline\n\\end{tabular}\n")
    print("% --- Tabla: sensibilidad del VAN a la tasa de descuento ---")
    ks = S["sensibilidad_tasas"]
    print("\\begin{tabular}{l" + "r" * len(ks) + "}\n\\hline")
    print("Escenario & " + " & ".join(f"{int(k * 100)}\\,\\%" for k in ks) + " \\\\\n\\hline")
    for n, r in res.items():
        print(f"{n} & " + " & ".join(fmt(r['sens'][k]) for k in ks) + " \\\\")
    print("\\hline\n\\end{tabular}")


if __name__ == "__main__":
    latex() if "--latex" in sys.argv else consola()
