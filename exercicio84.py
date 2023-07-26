"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- Uma lista com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves
"""

registeredPeople = [['Deivid', 56.5], ['Ana', 50.5], ['Alice', 39.6], ['Davi', 90.9], ['Claudio', 90.9]]

""" while True:
    currentPersonName = str(input('Nome: '))
    currentPersonWeight = float(input('Peso: '))

    registeredPeople.append([currentPersonName, currentPersonWeight])

    keepRunning = str(input('Quer continuar? [S/N] '))
    if keepRunning.lower() == 'n':
        break
 """

higherWeight = 0
listaMaiorPeso = []

# Verifica qual o maior peso
for personData in registeredPeople:
    if personData[1] > higherWeight:
        higherWeight = personData[1]

# Verifica quais pessoas tem o maior peso
for personData in registeredPeople:
    if personData[1] == higherWeight:
        listaMaiorPeso.append(personData[0])

lightestWeight = 0
listaMenorPeso = []

for id, personData in enumerate(registeredPeople):
    if id == 0:
        lightestWeight = personData[1]
    elif personData[1] < lightestWeight:
        lightestWeight = personData[1]

# Verifica quais pessoas tem o maior peso
for personData in registeredPeople:
    if personData[1] == lightestWeight:
        listaMenorPeso.append(personData[0])

print(f"Pessoas Registradas: {len(registeredPeople)}")
print(f"O maior peso foi {higherWeight} de {listaMaiorPeso}")
print(f"O menor peso foi {lightestWeight} de {listaMenorPeso}")
