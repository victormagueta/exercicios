# Faça um programa que calcule o valor a ser pago pelo aluguel de um carro #
# o valor do carro custa R$ 60,00 por dia e R$ 0,15 o km rodado #

dias = int(input('Por quantos dias o carro foi alugado? '))
odometro = float(input('Quantos quilometros foram rodados? '))

valor = (dias * 60) + (odometro * 0.15)

print(f'''O carro foi alugado por {dias} dias;
Você rodou {odometro} km com o carro;
Dessa forma, o valor total a pagar é de R$ {valor:.2f}''')
