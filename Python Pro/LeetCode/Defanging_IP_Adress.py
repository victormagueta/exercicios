""" Defanging um Endereço de IP é trocar todo . por [.]

Ex.

Adress = '1.1.1.1'
Output = '1[.]1[.]1[.]1[.]
"""

IP = input('Digite um número de IP: ')

for ponto in IP:
    IP_Defanging = IP.replace('.', '[.]')

print(f'O IP {IP} adulterao ficou {IP_Defanging}')
