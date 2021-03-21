# Crie um programa que leia o nome completo de uma pessoa e mostre: #
# O nome completo em letras maiúsculas, minúsculas, a quantidade de letras, qual seu primeiro nome e quantas letras tem #

from time import sleep

nome = input('Digite o seu nome completo: ').strip()
pnome = nome.split(' ')

print('Analisando seu nome...')
sleep(2)
print(f'O seu nome em letra maiúscula é {nome.upper()}.')
print(f'O seu nome em letras minúsculas é {nome.lower()}.')
print(f'O seu nome completo possui {len(nome)} letras.')
print(f'O seu primeiro nome é "{pnome[0].capitalize()}" e ele possui {len(pnome[0])} letras.')
