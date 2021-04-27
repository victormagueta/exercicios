"""Faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados

Ex.
>>> Digite um número: 1834
unidade: 4 dezena: 3 centena: 8 milhar: 1
"""

num = int(input('Digite um número inteiro: '))

#Cálculo do Milhar
mil = num // 1000 % 10
#Cálculo da Centena
cen = (num % 1000) // 100 % 10
#Cálculo da Dezena
dez = num // 10 % 10
#Cálculo da Unidade
unid = num // 1 % 10

#Resposta Final
print(f'''Analisando o número {num}:
Milhar: {mil}
Centena: {cen}
Dezena: {dez} 
Unidade: {unid}
''')