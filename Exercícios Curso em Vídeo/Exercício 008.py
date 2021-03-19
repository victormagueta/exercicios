# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros #

dist = float(input('Digite uma distância em metros: '))

print(f'''A medida de {dist}m corresponde a:
{dist / 1000}km
{dist / 100}hm
{dist / 10}dam
{dist * 10}dm
{dist * 100}cm
{dist * 1000}mm''')
