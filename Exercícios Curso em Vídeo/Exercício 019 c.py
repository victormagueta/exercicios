# Escreva um código que você forneca o numero de participantes e seus nomes, e o computador sorteie uma pessoa #

from random import choice
from time import sleep

sorteio = []
nome = input('Qual o nome da pessoa que vai participar do sorteio? ')
resp = input('Outra pessoa irá participar do sorteio? Sim ou não? ').lower()
sorteio.append(nome)

if resp == 'sim':
    while resp == 'sim':
        nome = input('Qual o nome da pessoa que vai participar do sorteio? ')
        sorteio.append(nome)
        resp = input('Outra pessoa irá participar do sorteio? Sim ou não? ').lower()

    sorteado = choice(sorteio)

    print(f'Os participantes do sorteio foram {sorteio}')
    sleep(0.2)
    print('O vencedor do sorteio foi...')
    sleep(0.5)
    print('.' * 3)
    sleep(0.5)
    print('.' * 3)
    sleep(0.5)
    print(f'{sorteado.capitalize()}! Parabéns!')

elif resp == 'não' or resp == 'nao':
    print(f'Sorteio com um único participante!? Tente novamente... ')
else:
    print('O que você fez? KKKK Tenta novamente ai, vai!')
