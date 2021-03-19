# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. #

c = float(input('Informe a temperatura em Celsius para conversão: '))

f = c * (9/5) + 32

print(f'A temperatura de {c:.1f} C equivale a {f:.1f} F.')