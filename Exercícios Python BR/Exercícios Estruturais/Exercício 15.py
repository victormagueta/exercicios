'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valor = float(input('Qual o valor você ganha por hora trabalhada? '))
horas = float(input('Quantas horas você trabalho neste mês? '))

salário_bruto = valor * horas
inss = salário_bruto * (8/100)
ir = salário_bruto * (11/100)
sindicato = salário_bruto * (5/100)
salário_liquido = salário_bruto - inss - ir - sindicato

print(f'''Você trabalho {horas} horas neste mês, o valor da hora é de R$ {valor:.2f}.
Seu salário bruto foi de {salário_bruto:.2f}. 
- O desconto do IR de 11% foi de R$ {ir:.2f}
- O desconto do INSS de 8% foi de R$ {inss:.2f}
- O desconto do Sindicato de 5% foi de R$ {sindicato:.2f}

Sendo assim, seu salário líquido este mês é de R$ {salário_liquido:.2f}
''')
