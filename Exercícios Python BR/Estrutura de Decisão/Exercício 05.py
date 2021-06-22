'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

primeira_nota = float(input('Digite sua primeira nota do ano: '))
segunda_nota = float(input('Digite sua segunda nota do ano: '))

media = (primeira_nota + segunda_nota) / 2

if media >= 7 and media < 10:
    print(f'Parabéns! A sua nota final foi {media}. Você foi APROVADO!')
elif media < 7:
    print(f'A sua nota final foi {media}. Você foi REPROVADO! Estude mais!')
elif media == 10:
    print(f'A sua nota final foi {media}. Você foi APROVADO COM DISTINÇÃO!')
