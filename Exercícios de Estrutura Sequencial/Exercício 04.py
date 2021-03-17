# Faça um Programa que peça as 4 notas bimestrais e mostre a média. #

p1 = float(input('Digite a nota da sua primeira prova: '))
p2 = float(input('Digite a nota da sua segunda prova: '))
p3 = float(input('Digite a nota da sua terceira prova: '))
p4 = float(input('Digite a nota da sua quarta prova: '))

media = (p1 + p2 + p3 + p4) / 4

print(f'A média das suas 04 provas trimestrais foi {media}')
