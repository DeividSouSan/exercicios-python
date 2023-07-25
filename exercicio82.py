"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

numbersList = list()

while True:

    num = int(input("Digite um número: "))

    numbersList.append(num)

    keepRunning = str(input("Quer continuar? [S/N] "))
    if keepRunning.lower() == 'n':
        break


evenList = [num for num in numbersList if num % 2 == 0]
oddList = [num for num in numbersList if num % 2 != 0]

print("Lista de números: ", numbersList)
print("Lista de números pares: ", evenList)
print("Lista de números ímpares: ", oddList)
