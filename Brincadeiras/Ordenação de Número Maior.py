# Faça um programa que o usuário forneca 3 números aleatórios e receba eles ordenados decrescentemente #

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite um último número: '))


if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print (a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)