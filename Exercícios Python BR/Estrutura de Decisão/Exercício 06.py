'''
Faça um Programa que leia três números e mostre o maior deles.
'''

numero_um = float(input('Digite um número: '))
numero_dois = float(input('Digite um outro número: '))
numero_tres = float(input('Digite mais um número: '))

if numero_um > numero_dois and numero_um > numero_tres:
    print(f'O número {numero_um} é o maior entre {numero_dois} e {numero_tres}')
elif numero_dois > numero_um and numero_dois > numero_tres:
    print(f'O número {numero_dois} é o maior entre {numero_um} e {numero_tres}')
elif numero_tres > numero_um and numero_tres > numero_dois:
    print(f'O número {numero_tres} é o maior entre {numero_dois} e {numero_um}')
else:
    print('Todos os números são iguais.')
