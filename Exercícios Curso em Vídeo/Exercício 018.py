# Faça um programa que leia um ângulo qualquer e mostre seu seno, cosseno e tangente #

import math
angulo = float(input('Digite o ângulo que você deseja: '))

sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print(f'''O seno do ângulo de {angulo} graus é de {sin:.2f}
O cosseno do ângulo de {angulo} graus é de {cos:.2f}
A tangente do ângulo de {angulo} graus é de {tg:.2f}''')
