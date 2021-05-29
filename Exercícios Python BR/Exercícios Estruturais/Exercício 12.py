'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.
Use a seguinte fórmula: (72.7*altura) - 58
'''

altura = float(input('Qual a sua atual altura? Por favor, digite em metros. '))

peso_ideal = (72.7 * altura) - 58

print(f'De acordo com a sua altura de {altura} m, o seu peso ideal é {peso_ideal:.1f} kg.')