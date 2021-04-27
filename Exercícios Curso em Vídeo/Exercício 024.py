"""Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome "Santo"
"""

cidade = input('Em que cidade você nasceu? ').lower()

if cidade.startswith('santo'):
    print('Sua cidade começa com o nome Santo.')
else:
    print('Sua cidade não começa com o nome Santo.')

"""Outra solucão é através de lista
conforme abaixo"""

print(cidade[:5] == 'santo')