'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

genero = input('Qual seu gênero? M - Masculino ou F - Feminino? ').upper()

if genero == 'F':
    print('Ok, seu gênero é feminino.')
elif genero == 'M':
    print('Certo, seu gênero é Masculino.')
else:
    print('Gênero inválido, tente novamente.')
