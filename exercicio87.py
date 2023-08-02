"""
Aprimore o desafio anterior, mostrando no final:
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha
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

# Somando os Valores Pares
evenSum = 0
for row in matrix:
    for element in row:
        if element % 2 == 0:
            evenSum += element

thirdColumnSum = matrix[0][2] + matrix[1][2] + matrix[2][2]

highestValueSecondRow = max(matrix[1])

print("A soma de todos os valores pares digitados é: ", evenSum)
print("A soma dos valores da terceira coluna é: ", thirdColumnSum)
print("O maior valor da segunda linha é: ", highestValueSecondRow)


