"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
A - Quantos números foram digitados
B - A lista de valores, ordenada de forma decrescente
C - Se o valor 5 foi digitado e está ou não na lista
"""

numbersList = list()

while True:

    num = int(input("Digite um número: "))

    numbersList.append(num)

    keepRunning = str(input("Quer continuar? [S/N] "))
    if keepRunning.lower() == 'n':
        break


listLength = len(numbersList)
sortedList = sorted(numbersList, reverse=True)
containNumberFive = 'está' if 5 in numbersList else 'não está'

print(f"\nNúmeros digitados: {listLength}\nLista de valores: {sortedList}\nO número 5 (cinco) {containNumberFive} na lista.")