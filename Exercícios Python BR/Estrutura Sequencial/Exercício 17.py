'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
from math import ceil

M2_POR_LITRO= 6
PRECO_LATA = 80
LITROS_LATA = 18
PRECO_GALAO = 25
LITROS_GALAO = 3.6
MARGEM = 1.1

area = float(input('Qual a área a ser pintada? '))
area_com_margem = area * MARGEM

#Apenas Latas de 18 Litros
quantidade_latas = ceil(area_com_margem / LITROS_LATA)
preco_latas = quantidade_latas * PRECO_LATA

#Apenas Galões de 3.6 litros
quantidade_galao = ceil(area_com_margem / LITROS_GALAO)
preco_galoes = quantidade_galao * PRECO_GALAO

#Misto entre Galões e Latas
quantidade_latas_misto = round(area_com_margem / LITROS_LATA)
preco_latas_misto = (quantidade_latas_misto * PRECO_LATA)
quantidade_galoes_misto = (area_com_margem % LITROS_LATA) // LITROS_GALAO
preco_galoes_misto = quantidade_galoes_misto * PRECO_GALAO
preco_total = preco_latas_misto + preco_galoes_misto

print(f'Para pintar a área de {area} m, você precisará de {quantidade_latas} latas de 18 Litros, considerando uma margem de 10%. Isso custará R$ {preco_latas:.2f}.')
print('ou então,')
print(f'Para pintar a área de {area} m, você precisará de {quantidade_galao} galões de 3.6 Litros, considerando uma margem de 10%. Isso custará R$ {preco_galoes:.2f}.')
print('se não, para minimizar a sobra de tinta,')
print(f'Para pintar a área de {area} m, você precisará de {quantidade_latas_misto} latas de 18 Litros e {quantidade_galoes_misto:.0f} galões de 3.6 Litros, considerando uma margem de 10%. Isso custará R$ {preco_total:.2f}.')
