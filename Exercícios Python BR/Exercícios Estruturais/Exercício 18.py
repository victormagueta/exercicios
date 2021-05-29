'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input('Qual o tamanho em MB do arquivo a ser baixado? '))
velocidade = float(input('Qual a velocidade em Mbps da sua internet? '))

tempo = round(tamanho / (velocidade / 8)) / 60

print(f'Para baixar um arquivo de {tamanho} MB com uma internet de {velocidade} Mbps, o download demorará aproximatamente {tempo:.1f} minutos para concluir.')
