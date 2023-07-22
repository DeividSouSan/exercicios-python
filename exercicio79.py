"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

uniqueNumbersList = list()

while True:
    value = int(input('Digite um valor: '))

    if value in uniqueNumbersList:
        print("Valor já existe na lista, digite outro.")
        continue
    else:
        uniqueNumbersList.append(value)
        print("Valor adicionado com sucesso!")

    keepRunning = str(input("Quer continuar? [S/N] "))
    if keepRunning.lower() == 'n':
        break

print(f"Valores digitados: {sorted(uniqueNumbersList)}.")
