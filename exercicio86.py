"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matrix =  [[], [], []]

for i in range(3):
    for j in range(3):
        num = int(input(f'Linha: {i} | Coluna: {j} : '))
        matrix[i].append(num)

for row in matrix:
    for element in row:
        print(f'[{element:^5}]', end=' ')
    print()