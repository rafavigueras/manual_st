"""Cifras del capitulo 31 (Parte V): Polonia como cambio de perimetro real entre 2025 y 2027.

Datos: Santander en el EBA 2025, todas las carteras (investigacion/datos-publicos.md y su
validacion). El bloque "Polonia" de la ficha agrupa toda la exposicion a contrapartes polacas
del grupo, no solo la de Santander Bank Polska, asi que es una aproximacion de lo que sale.
"""
grupo = {"exp": 1_384_138, "prov0": 21_893, "adv": 65_983, "base": 46_875}
polonia = {"exp": 52_704, "prov0": 1_215, "adv": 3_018, "base": 2_113}


def tasas(d):
    return (d["adv"] - d["prov0"]) / d["exp"], (d["base"] - d["prov0"]) / d["exp"]


ga, gb = tasas(grupo)
pa, pb = tasas(polonia)
sin = {k: grupo[k] - polonia[k] for k in grupo}
sa, sb = tasas(sin)
print(f"Grupo 2025:        exposicion {grupo['exp']:,}; adverso {ga:.2%}; base {gb:.2%}")
print(f"Bloque Polonia:    exposicion {polonia['exp']:,} ({polonia['exp'] / grupo['exp']:.1%} del grupo); "
      f"adverso {pa:.2%}; aumento de provisiones {polonia['adv'] - polonia['prov0']:,} M EUR")
print(f"Grupo sin Polonia: exposicion {sin['exp']:,}; adverso {sa:.2%}; base {sb:.2%}")
print(f"Efecto en la tasa del grupo: {(sa - ga) * 1e4:+.1f} pb de exposicion; en importe: "
      f"{-(polonia['adv'] - polonia['prov0']):,} M EUR de perdidas adversas menos")
rwa_grupo = 627_012
print(f"Perdidas de Polonia despues de impuestos sobre los RWA del grupo: "
      f"{(polonia['adv'] - polonia['prov0']) * 0.7 / rwa_grupo * 1e4:.0f} pb (antes de contar su margen y sus RWA)")
