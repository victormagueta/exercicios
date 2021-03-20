# Faça um algoritmo que leia o preço de um produto qualquer e mostre o seu novo preço, com o desconto aplicado #

price = float(input('Quanto custa o produto? '))
discount = float(input('Qual será o percentual de desconto aplicado? '))

print(f'''O produto que custava R$ {price:.2f}, com o desconto de {discount} % aplicado, sairá por R$ {price - (price * (discount / 100)):.2f}.''')
