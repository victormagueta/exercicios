# Estou pensando em um número de 1 a 10. Em qual número estou pensando? #


from random import randint

num = int(input('Digite o número que estou pensando: '))

lista = list(range(1, 11))
pens = lista.shuffle(lista)
print(lista)
