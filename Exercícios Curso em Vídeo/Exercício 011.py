# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta #
# Para pintá-la, considere que cada litro de tinta pinta uma área de 2m2 #

larg = float(input('Qual a Largura da Parede? '))
alt = float(input('Qual a Altura da Parede? '))

area = larg * alt
tinta = area / 2

print(f'''A sua parede tem {larg:.2f}m x {alt:.2f}m, sua área é de {area:.2f}m2
Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.''')
