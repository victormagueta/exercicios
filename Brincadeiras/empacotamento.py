def somar(*args):
    soma = 0
    for i in range(len(args)):
        soma += args[i]
    return soma

print(somar(1))