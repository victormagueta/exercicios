# Estou pensando em um número de 1 a 5. Em qual número estou pensando? #
import random

print('Estou pensando em um número de 1 a 5. Consegue adivinhar qual é? ')
num = int(input('Digite o número que estou pensando: '))

lista = list(range(1, 5))
random.shuffle(lista)
n = lista.pop()

if 1 <= num <= 5:
    if n == num:
        print(f'Parabéns, você acertou! Você disse {num} e eu pensei no número {n}.')
    elif n != num:
        print(f'Que pena, você errou! Você disse {num} e eu pensei no número {n}.')
    else:
        print('Comando Inválido')
else:
    print(f'O número {num} que você digitou não está entre os números 1 e 5. Tente novamente!')
