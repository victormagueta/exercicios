# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar e quantos euros#
# Considere o dólar do dia#

mny = float(input('Quanto dinheiro você tem na carteira? R$ '))
dol = 5.48
euro = 0.84

print(f'''Com R$ {mny:.2f} você consegue comprar U$ {mny / dol:.2f} 
E com U$ {mny / dol:.2f} você consegue comprar € {(mny / dol) * euro:.2f}''')