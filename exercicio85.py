"""
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares em ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

numbers = [[],[]]
for i in range(7):
    num = int(input(f'Digite o {i+1}º número: '))

    ehPar = num % 2 == 0
    if ehPar:
        numbers[0].append(num)
    elif not ehPar:
        numbers[1].append(num)

numbers[0].sort()
numbers[1].sort()
print('Os valores pares digitados foram: ', numbers[0])
print('Os valores ímpares digitados foram: ', numbers[1])


