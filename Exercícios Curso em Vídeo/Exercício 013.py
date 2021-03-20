# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com a porcentagem de aumento apresentada #

slr = float(input('Qual o valor do seu salário? R$ '))
rjst = float(input('Qual será o percentual a ser reajustado? '))

srjst = slr + (slr * (rjst / 100))

print(f'''O seu salário de R$ {slr:.2f}, aplicado o reajuste de {rjst:.1f}%, irá para R$ {srjst:.2f}.''')
