# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês. #

v = float(input('Qual o valor que você recebe por hora trabahada? '))
h = float(input('Quantas horas você trabalhou este mês? '))

salario = v * h

print(f'O total do seu salário este mês é de R$ {salario:.2f}.')
