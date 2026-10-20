"""Modelo económico-financiero del PFI (E75).

Genera las tablas del capítulo de negocio: clientes activos (12.IV), flujos netos (12.V),
indicadores (12.VI), sensibilidad a la tasa (12.VII), a la nube (12.VIII) y al costo de
adquisición y abandono (12.IX), y el punto de equilibrio por año.
    python modelo_financiero.py            -> resumen en consola
    python modelo_financiero.py --latex    -> tablas LaTeX (pegar en el capítulo de negocio)
Todos los supuestos están en SUPUESTOS. Moneda: USD constantes, flujos anuales, sin valor residual.
"""
import math
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
    "costo_nube_por_endpoint": 0.10,    # USD por endpoint/mes (almacenamiento de eventos más margen por lo no medido)
    "comision_pagos": 0.03,             # procesador de pagos, sobre ingresos
    "ingresos_brutos": 0.03,            # supuesto conservador, sobre ingresos
    "ventas_por_canal": 0.50,           # proporción de clientes que llegan por MSSP/integradores
    "comision_canal": 0.20,             # comisión del MSSP sobre lo que vende
    # Costos fijos mensuales por año: equipo, y contador + mesa de ayuda + certificado (tabla 12.II)
    "fijo_mensual_por_anio": [3500, 6000, 9000, 11000, 12000],
    "soporte_mensual_por_anio": [125, 167, 167, 167, 167],   # año 1 sin certificado (ya está en la inversión)
    # Infraestructura de nube escalonada según los equipos monitoreados (tabla 12.II)
    "infra_base": 179,                  # hasta 1.500 equipos
    "infra_mas_1500": 45,               # PostgreSQL medio
    "infra_por_3000": 73,               # otro par de instancias por cada 3.000 sobre los primeros 3.000
    "infra_por_5000": 20,               # otro Redis por cada 5.000 sobre los primeros 5.000
    "infra_mas_6000": 100,              # PostgreSQL grande
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


def margen_contribucion_cliente(nube=None):
    nube = S["costo_nube_por_endpoint"] if nube is None else nube
    pct = S["comision_pagos"] + S["ingresos_brutos"] + S["ventas_por_canal"] * S["comision_canal"]
    return ARPU_CLIENTE * (1 - pct) - nube * S["endpoints_por_cliente"]


def infraestructura(equipos):
    """Gasto mensual de nube según los equipos monitoreados (tabla 12.II)."""
    g = S["infra_base"]
    if equipos > 1500:
        g += S["infra_mas_1500"]
    if equipos > 3000:
        g += math.ceil((equipos - 3000) / 3000) * S["infra_por_3000"]
    if equipos > 5000:
        g += math.ceil((equipos - 5000) / 5000) * S["infra_por_5000"]
    if equipos > 6000:
        g += S["infra_mas_6000"]
    return g


def costo_fijo_mensual(anio, clientes):
    """Equipo + contador y soporte + infraestructura escalonada (anio desde 0)."""
    return (S["fijo_mensual_por_anio"][anio] + S["soporte_mensual_por_anio"][anio]
            + infraestructura(clientes * S["endpoints_por_cliente"]))


def punto_equilibrio(anio, clientes, nube=None):
    return math.ceil(costo_fijo_mensual(anio, clientes) / margen_contribucion_cliente(nube))


def simular(esc, nube=None, cac=None, churn=None):
    nube = S["costo_nube_por_endpoint"] if nube is None else nube
    cac = esc["cac"] if cac is None else cac
    churn = esc["churn_mensual"] if churn is None else churn
    cac_unit = cac
    clientes, filas = 0.0, []
    for a in range(S["horizonte_anios"]):
        ing = var = fijo = cac = 0.0
        altas = 0.0
        for _ in range(12):
            n = esc["altas_mensuales"][a]
            altas += n
            clientes = clientes * (1 - churn) + n
            rev = clientes * ARPU_CLIENTE
            ing += rev
            var += (clientes * S["endpoints_por_cliente"] * nube
                    + rev * (S["comision_pagos"] + S["ingresos_brutos"])
                    + rev * S["ventas_por_canal"] * S["comision_canal"])
            fijo += costo_fijo_mensual(a, clientes)
            cac += n * cac_unit
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
    base = simular(S["escenarios"]["Base"])
    for a, f in enumerate(base):
        cf = costo_fijo_mensual(a, f["clientes"])
        print(f"  Año {a + 1}: costo fijo mensual {fmt(cf)}, equilibrio {punto_equilibrio(a, f['clientes'])} clientes")
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
    print("\\hline\n\\end{tabular}\n")
    print("% --- Sensibilidad del VAN a la nube por equipo (USD 0,10 / 0,30 / 0,60), por escenario ---")
    k = S["tasa_descuento"]
    base = S["escenarios"]["Base"]
    for n in res:
        print(f"{n} & " + " & ".join(
            fmt(van([f['flujo'] for f in simular(S['escenarios'][n], nube=v)], k)) for v in (0.10, 0.30, 0.60)) + " \\\\")
    print("% --- Escenario base: VAN según costo de adquisición (1.000 / 1.500 / 2.500) y abandono (1,5 / 2 / 3 %) ---")
    print("VAN & " + " & ".join(
        fmt(van([f['flujo'] for f in simular(base, cac=v)], k)) for v in (1000, 1500, 2500)) + " \\\\")
    print("VAN & " + " & ".join(
        fmt(van([f['flujo'] for f in simular(base, churn=v)], k)) for v in (0.015, 0.02, 0.03)) + " \\\\")
    print("% --- Punto de equilibrio (escenario base): año, costo fijo mensual, equilibrio ---")
    for a, f in enumerate(simular(base)):
        print(f"{a + 1} & {fmt(costo_fijo_mensual(a, f['clientes']))} & {punto_equilibrio(a, f['clientes'])} \\\\")


if __name__ == "__main__":
    latex() if "--latex" in sys.argv else consola()
