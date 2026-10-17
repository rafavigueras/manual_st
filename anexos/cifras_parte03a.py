"""Cifras de los ejemplos NUMEROS y PALANCA de los capitulos 14 a 21 (Parte III, bloque A).

Las del hilo conductor salen de los anexos S0, S1 (segunda parte), S2 y S5; las de bancos
reales, de las notas validadas de investigacion/. Si cambia una cifra aqui, cambia en el texto.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import s0_juguete as s0  # noqa: E402
import s2_migracion as s2  # noqa: E402

print("== Cap. 15: la regla del 10 % de la clase pivote ==")
expo = 1_000.0
pd_mod, pd_bm = 0.1333, 0.1895     # PD adversa del ano 3: satelite y benchmark ilustrativo (anexo S1b)
for cubierto in (0.08, 0.40):
    if cubierto < 0.10:
        pd_final = pd_bm
        txt = "benchmark para toda la clase"
    else:
        pd_final = cubierto * pd_mod + (1 - cubierto) * pd_bm
        txt = "media ponderada justificada"
    print(f"  Modelo cubre {cubierto:.0%} de {expo:,.0f} M EUR -> {txt}: PD {pd_final:.2%}")

print("\n== Cap. 16: concentracion del deterioro en el primer ano (EBA 2025, adverso) ==")
for banco, anos in (("Santander", (21_120, 10_342, 13_390)), ("BBVA", (14_481, 11_154, 9_959))):
    tot = sum(anos)
    print(f"  {banco}: {' / '.join(f'{x:,}' for x in anos)} = {tot:,} M EUR; primer ano {anos[0] / tot:.1%}")

print("\n== Cap. 17: los nuevos S3 del primer ano con la formula del recuadro 8 (S2, adverso) ==")
pd, lg = s2.sendas("adverso")
p1, p2 = pd[1], min(0.6, s2.M2 * pd[1])
e1, e2 = s2.STOCK0["S1"], s2.STOCK0["S2"]
print(f"  S1: {e1:.0f} x {p1:.2%} x {lg[1]:.1%} = {e1 * p1 * lg[1]:.1f}")
print(f"  S2: {e2:.0f} x {p2:.2%} x {lg[1]:.1%} = {e2 * p2 * lg[1]:.1f}")
print(f"  Total provision de nuevos S3 del ano 1: {e1 * p1 * lg[1] + e2 * p2 * lg[1]:.1f}; "
      f"exposicion que entra en S3: {e1 * p1 + e2 * p2:.1f}")

print("\n== Cap. 18: el QA de 2025 en el banco de referencia ==")
rwa = 35_000
pb = 88
neto = pb / 1e4 * rwa
print(f"  {pb} pb sobre {rwa:,} M EUR de RWA = {neto:,.0f} M EUR de CET1 = {neto / 0.7:,.0f} M EUR antes de impuestos")

print("\n== Cap. 19: REA de un S3 IRB con LGD propia (recuadro 10) ==")
stock = 100.0
for lgd_reg, elbe in ((0.45, 0.38), (0.45, 0.42), (0.50, 0.42)):
    rea = max(0.0, (lgd_reg - elbe) * 12.5 * stock)
    print(f"  LGD reg {lgd_reg:.0%}, ELBE {elbe:.0%}: REA = ({lgd_reg:.2f} - {elbe:.2f}) x 12,5 x {stock:.0f} = {rea:.1f}")

print("\n-- Exceso y deficit (simplificado, antes de impuestos) --")
el_reg0, prov0 = 1_000.0, 900.0
dprov, del_reg = 300.0, 150.0
el_reg1, prov1 = el_reg0 + del_reg, prov0 + dprov
deduc0, deduc1 = max(0.0, el_reg0 - prov0), max(0.0, el_reg1 - prov1)
print(f"  Partida: EL reg {el_reg0:,.0f}, provisiones {prov0:,.0f} -> deficit deducido {deduc0:,.0f}")
print(f"  Estres: EL reg {el_reg1:,.0f}, provisiones {prov1:,.0f} -> deficit {deduc1:,.0f}, "
      f"exceso {max(0.0, prov1 - el_reg1):,.0f} (a nivel 2, con limite)")
print(f"  Efecto en CET1: -{dprov:,.0f} de provisiones + {deduc0 - deduc1:,.0f} de deficit que desaparece "
      f"= {-dprov + deduc0 - deduc1:,.0f}")

print("\n-- Descomposicion de la caida de CET1 de la filial (anexo S0, adverso, con margen) --")
tot = None
for nombre in s0.CARTERAS:
    df, _ = s0.proyectar(nombre, "adverso")
    cols = df[["deterioro", "rwa", "margen"]]
    tot = cols if tot is None else tot + cols
rwa0 = tot.rwa.iloc[0]
cet10 = s0.CET1_INICIAL_SOBRE_RWA * rwa0
det = tot.deterioro.iloc[1:].sum()
mar = tot.margen.iloc[1:].sum()
cet13 = cet10 + (-det + mar) * (1 - s0.TIPO_FISCAL)
rwa3 = max(tot.rwa.iloc[3], rwa0)
r0, r3 = cet10 / rwa0, cet13 / rwa3
c_det = -det * (1 - s0.TIPO_FISCAL) / rwa0
c_mar = mar * (1 - s0.TIPO_FISCAL) / rwa0
c_rwa = r3 - cet13 / rwa0
print(f"  RWA de partida {rwa0:,.1f}; final sin suelo {tot.rwa.iloc[3]:,.1f}; con suelo {rwa3:,.1f}")
print(f"  CET1 {r0:.2%} -> {r3:.2%} ({(r3 - r0) * 1e4:+.0f} pb en el ano 3)")
print(f"    deterioro de credito, neto de impuestos: {c_det * 1e4:+.0f} pb ({det:,.1f} M EUR antes de impuestos)")
print(f"    margen dado, neto de impuestos:           {c_mar * 1e4:+.0f} pb ({mar:,.1f} M EUR)")
print(f"    denominador (RWA):                        {c_rwa * 1e4:+.0f} pb")
print(f"    suma: {(c_det + c_mar + c_rwa) * 1e4:+.0f} pb")
sin_suelo = cet13 / tot.rwa.iloc[3]
print(f"  Sin el suelo del REA de partida: CET1 final {sin_suelo:.2%} ({(sin_suelo - r0) * 1e4:+.0f} pb); "
      f"el suelo cuesta {(sin_suelo - r3) * 1e4:.0f} pb")
