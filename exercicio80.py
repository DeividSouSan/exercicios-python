"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar sort()). No final, mostre a lista ordenada na tela.
"""

numbers = list()

for i in range(10):
    currentNum = int(input('Digite um número: '))

    if len(numbers) == 0:
        numbers.append(currentNum)

    elif len(numbers) >= 1:
        for index, element in enumerate(numbers):
            if currentNum < element:
                print(f"{currentNum} é menor que {element}")
                numbers.insert(index, currentNum);
                break
            else:
                print(f"{currentNum} é maior que {element}")

            if index + 1 == len(numbers):
                numbers.append(currentNum)
                break

print(numbers)