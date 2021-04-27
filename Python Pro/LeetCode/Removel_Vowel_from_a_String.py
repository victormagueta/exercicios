palavra = 'Piauiense'
vogal = 'iauiee'
"""Código para retirar as vogais de uma palavra:

Ex. 
Palavra = Piauiense
Resultado = Pns
"""

for letra in vogal:
    palavra = palavra.replace(letra, '')

print(palavra)
