
''' Faça um programa que peça 2 números inteiros e um real. Calcule e mostre:
a) o produto do dobro do primeiro com a metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

numero_um = int(input('Digite um número inteiro: '))
numero_dois = int(input('Digite um outro número inteiro: '))
numero_tres = float(input('Digite um número real: '))

a = (2 * numero_um) * (numero_dois / 2)
b = (3 * numero_um) + numero_tres
c = numero_tres ** 2

print(f'''O produto entre o dobro de {numero_um} e a metade de {numero_dois} é {a};
O triplo de {numero_um} somado com {numero_tres} é {b};
O {numero_tres} elevado ao cubo é {c};
''')