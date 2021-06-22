'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

numero_1 = float(input('Digite um número qualquer: '))
numero_2 = float(input('Digite um outro número qualquer: '))

if numero_1 > numero_2:
    print(f'O número {numero_1} é o maior entre os dois digitados')
elif numero_2 > numero_1:
    print(f'O número {numero_2} é o maior entre os dois digitados')
else:
    print('Os dois números são iguais')
