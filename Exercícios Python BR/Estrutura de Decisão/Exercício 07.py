'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numero_um = float(input('Digite um número qualquer: '))
numero_dois = float(input('Digite um outro número qualquer: '))
numero_tres = float(input('Digite um mais número qualquer: '))

lst = []
lst.extend(numero_tres, numero_um, numero_dois)
lst.sort()
print(lst)
