'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
VOGAIS = ['a','e', 'i', 'o', 'u']
CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']

letra = input('Digite uma letra qualquer: ').lower()

if letra in VOGAIS:
    print(f'A letra "{letra}" é uma vogal!')
elif letra in CONSOANTES:
    print(f'A letra "{letra}" é uma consoante.')
else:
    print(f'"{letra}" isto não é uma letra. Tente novamente!')