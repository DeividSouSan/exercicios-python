"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor numero digitado e as suas respectivas posições na lista.
"""

numbersList = list()

for i in range(5):
    num = int(input(f"Digite um valor para a Posição {i}: "))
    numbersList.append(num)

print("Você digitou os valores: ", *numbersList)

maiorValor = max(numbersList)
menorValor = min(numbersList)

posMaiorValor = list()
posMenorValor = list()

for index, num in enumerate(numbersList):
    if num == maiorValor:
        posMaiorValor.append(index)
    
    if num == menorValor:
        posMenorValor.append(index)

print(f"O menor valor é {menorValor} em", *posMenorValor)
print(f"O maior valor é {maiorValor} em", *posMaiorValor)