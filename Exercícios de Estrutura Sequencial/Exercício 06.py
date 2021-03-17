# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. #

import math
r = int(input('Informe o raio do círculo para ser calculado a área: '))

area = r * math.pi

print(f'A área do círculo informado é de {area:.2f}.')
