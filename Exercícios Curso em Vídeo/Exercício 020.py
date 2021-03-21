# Faça um programa que sorteie a ordem de apresentação de um trabalho entre quatro alunos #

from random import shuffle
aluno_1 = input('Qual o nome do aluno? ').capitalize()
aluno_2 = input('Qual o nome do aluno? ').capitalize()
aluno_3 = input('Qual o nome do aluno? ').capitalize()
aluno_4 = input('Qual o nome do aluno? ').capitalize()

sorteio = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(sorteio)
#print(f'A ordem de apresentação será {sorted(sorteio)}')
print(f'A ordem de apresentação será {sorteio}')
