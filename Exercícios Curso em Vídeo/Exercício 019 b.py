# Escreva um código que você forneca o numero de participantes e seus nomes, e o computador sorteie uma pessoa #

from random import choice
part = int(input('Quantas pessoas vão participar do sorteio? '))
sorteio = []

for i in range (part):
    nome = input('Qual o nome da pessoa a ser incluída? ')
    sorteio.append(nome)
print(sorteio)
sorteado = choice(sorteio)
print(sorteado)

