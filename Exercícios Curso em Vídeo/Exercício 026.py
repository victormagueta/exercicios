'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ').lower().strip()

if 'a' in frase:
    print(f' A frase "{frase}" possui {frase.count("a")} letras "a".')
    print(f'A primeira letra "a" da frase "{frase}" está na posição {frase.find("a") + 1}')
    print(f'A última letra "a"da frase "{frase}" está na posição {frase.rfind("a") + 1}')
else:
    print('Sua frase não possui letra "A"')