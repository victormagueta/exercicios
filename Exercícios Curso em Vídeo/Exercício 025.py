"""Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
"""

nome = input('Qual o seu nome completo? ').title()
print(nome.__contains__('Silva'))

"""Outra solução é:"""

print('Silva' in nome)