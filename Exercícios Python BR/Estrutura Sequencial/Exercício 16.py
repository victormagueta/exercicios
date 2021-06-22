'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area = float(input('Qual o tamanho da área a ser pintada? '))

litros_de_tinta = round(area / 18)

preco = litros_de_tinta * 80

print(f'Para pintar a área de {area:.1f} m, você precisará de {litros_de_tinta} galão(ões) de tinta. Isso custará R$ {preco:.2f}')
