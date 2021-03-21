# Escreva um código que o usuário forneça o cateto oposto e o adjacente, e ele mostre o tamanho da hipotenusa #

from math import hypot
co = float(input('Qual o comprimento do Cateto OPOSTO? '))
ca = float(input('Qual o comprimento do Cateto ADJACENTE? '))

print(f'O tamanho da Hipotenusa é {(ca**2 + co**2) ** (1/2):.2f}.')
print(f'o tamanho da Hipotenusa é {hypot(co,ca):.2f}.')