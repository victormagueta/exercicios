# Faça um programa que o usuário digite o valor a ser sacado e o programa distribua a quais notas serão entregues #
# As notas disponiveis são 100, 50, 20, 10, 5 e 1. #
# O valor mínimo para saque varia de 10 reais até 1000 reais #

saqueinit = (int(input('Digite o valor a ser sacado: ')))
saque = saqueinit

if 10 <= saque <= 1000:
    notas_cem = saque  // 100
    saque = saque % 100

    notas_cinquenta = saque // 50
    saque = saque % 50

    notas_vinte = saque // 20
    saque = saque % 20

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_um = saque // 1
    saque = saque % 1

    print(f'''Para sacar R$ {saqueinit:.2f} você vai sacar:
{notas_cem} notas de R$ 100,00;
{notas_cinquenta} notas de R$ 50,00;
{notas_vinte} notas de R$ 20,00;
{notas_dez} notas de R$ 10,00
{notas_cinco} notas de R$ 5,00;
{notas_um} notas de R$ 1,00''')
else:
    print(f'O valor de R$ {saque:.2f} não pode ser sacado, apenas valores entre R$ 10,00 e R$ 1.000,00')