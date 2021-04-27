def contar_caracteres(s):
    """Funcão que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('victor')
    c: 1
    i: 1
    o: 1
    r: 1
    t: 1
    v: 1
    >>> contar_caracteres('magueta')
    a: 2
    e: 1
    g: 1
    m: 1
    t: 1
    u: 1

    :param s: string a ser contada
    """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('victor')
    print()
    contar_caracteres('magueta')
