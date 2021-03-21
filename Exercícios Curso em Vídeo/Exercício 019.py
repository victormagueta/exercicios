# Faça um programa que sorteie um entre quatro alunos, o programa deve ler o nome dos alunos e escolher um #

from random import choice
from time import sleep

aluno_1 = input('Qual o nome do aluno? ')
aluno_2 = input('Qual o nome do aluno? ')
aluno_3 = input('Qual o nome do aluno? ')
aluno_4 = input('Qual o nome do aluno? ')

sorteio = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(sorteio)

print(f'Os alunos que estão participando do sorteio são {sorteio}')
sleep(0.5)
print('O aluno escolhido foi...')
sleep(0.5)
print('.' * 3)
sleep(0.5)
print('.' * 3)
sleep(0.5)
print('.' * 3)
sleep(0.5)
print(f'{escolhido.capitalize()}!')

