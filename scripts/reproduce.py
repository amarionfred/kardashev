import math

SIGMA = 5.670374419e-8

def show(label, value):
    print(f'{label}: {value}')

print('== Feed ratio (mass of feed per kg of product) ==')
for grade_ppb, recovery in [(10, 1.0), (10, 0.5), (5, 0.5), (10, 0.3)]:
    feed = 1 / (grade_ppb * 1e-9 * recovery)
    show(f'feed for 1 kg He-3 @ {grade_ppb} ppb, {int(recovery*100)}% recovery', f'{feed:,.0f} kg = {feed/1000:,.0f} t')

print()
print('== Heat per gram of product ==')
for grade_ppb, recovery in [(10, 0.5), (10, 0.3), (5, 0.5)]:
    feed_kg = 1e-3 / (grade_ppb * 1e-9 * recovery)
    for mj in (0.5, 0.7):
        q_gj = feed_kg * mj / 1000
        show(f'{grade_ppb} ppb {int(recovery*100)}% @ {mj} MJ/kg', f'{q_gj:,.0f} GJ/g = {q_gj/3.6:,.0f} MWh/g')

print()
print('== Recuperation, 85% (Mark-III claimed) ==')
for gj in (100, 140, 165, 235, 200, 280):
    show(f'{gj} GJ gross', f'net {gj*0.15:,.1f} GJ = {gj*0.15/3.6:,.1f} MWh')

print()
print('== Night storage, 1.4 MW over 14.75 days ==')
t_s = 14.75 * 86400
E_mwh = 1.4e6 * t_s / 3.6e9
show('energy', f'{E_mwh:,.0f} MWh')
show('battery mass @ 250 Wh/kg', f'{E_mwh*1000/0.25:,.0f} kg = {E_mwh*1000/0.25/1000:,.1f} t')

print()
print('== Radiator at 300 K ==')
flux = SIGMA * 300**4
show('blackbody W/m2', f'{flux:,.0f}')
show('two-sided eps 0.9 W/m2', f'{flux*0.9*2:,.0f}')
show('1 MW needs m2', f'{1e6/(flux*0.9*2):,.0f}')

print()
print('== Break-even product per tonne of hardware ==')
for launch in (1_000_000, 500_000, 100_000):
    product_per_tonne = launch / 20_000_000 * 1000
    show(f'launch ${launch:,}/kg', f'{product_per_tonne:,.0f} kg per tonne')

print()
print('== Aluminium vs helium-3 ==')
he3_per_tonne_value = 5e-6 * 20_000_000
al_per_tonne_value = 50 * 3.97
show('He-3 value per tonne of feed @ 5 mg/t, $20M/kg', f'${he3_per_tonne_value:,.2f}')
show('Al value per tonne of feed (50 kg, $3.97/kg)', f'${al_per_tonne_value:,.2f}')
show('revenue per kg of product: He-3 vs Al', f'${20_000_000:,.0f} vs ${3.97} = {20_000_000/3.97:,.0f}x')

print()
print('== Primary energy vs Sagan Type I ==')
W = 620e18 / 31557600
K = (math.log10(W) - 6) / 10
show('human primary energy (W)', f'{W:.2e}')
show("Sagan's K", f'{K:.2f}')
show('power multiplier to Type I (1e16 W)', f'{1e16/W:,.0f}x')

print()
print('== Lunation ==')
show('day (s)', f'{29.53059*86400:,.0f}')
show('night (s)', f'{29.53059*86400/2:,.0f}')
