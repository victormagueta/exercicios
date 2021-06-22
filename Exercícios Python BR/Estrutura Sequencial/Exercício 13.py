'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
genero = input('Para iniciar, preciso saber o seu gênero. Você é Homem ou Mulher? (H, M) ').lower()
h = float(input('Agora, por favor, digite sua altura em metros: '))

if genero == 'h':
    print(f'O seu peso ideal, de acordo com a sua altura {h} e o seu gênero é {72.7 * h - 58:.1f}')
elif genero == 'm':
    print(f'O seu peso ideal, de acordo com a sua altura {h} e o seu gênero é {62.1 * h - 44.7:.1f}')
else:
    print('Você digitou um comando inválido')
