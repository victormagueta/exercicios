# Crie um algoritmo que leia a temperatura em Graus Celsius e converta para Fahrenheit ou Kelvin #

temp = float(input('Digite a temperatura em Graus Celsius: '))
conv = input('Você quer converter para Fahrenheit ou Kelvin? F ou K ').upper()

if conv == 'F':
    fah = 9 * temp / 5 + 32
    print(f'A temperatura {temp:.1f} Celsius convertida para Fahrenheit é igual a {fah:.2f}F.')
elif conv == 'K':
    kel = temp + 273.15
    print(f'A temperatura {temp:.1f} Celsius convertida para Kelvin é igual a {kel:.2f}K.')
else:
    print(f'Você digitou uma entrada inválida. Tente novamente!')
