# Faça um programa que leia algo na tela e mostre o seu tipo primitivo e todas as informações possíveis sobre ele #
x = input('Digite algo: ')


print(f'O tipo primitivo desse objeto é {type(x)}')

print(f"Só tem espaço? {x.isspace()}")

print(f'É número? {x.isnumeric()}')

print(f'É Alfabético? {x.isalpha()}')

print(f'É Alfanumérico? {x.isalnum()}')

print(f'Está em maiúsculas? {x.isupper()}')

print(f'Está em minúsculas? {x.islower()}')

print(f'Está capitalizada? {x.istitle()}')