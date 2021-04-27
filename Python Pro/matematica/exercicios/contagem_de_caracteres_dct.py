def contar_caracteres(s):
    """Funcão que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('victor')
    {'c': 1, 'i': 1, 'o': 1, 'r': 1, 't': 1, 'v': 1}
    >>> contar_caracteres('magueta')
    {'a': 2, 'e': 1, 'g': 1, 'm': 1, 't': 1, 'u': 1}

    :param s: string a ser contada
    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('victor'))
    print()
    print(contar_caracteres('magueta'))
