"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequẽncia de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

qntdNumeros = int(input("Quantos números quer mostrar: "))
numerosMostrados = 0 
numAtual = 0
numFibonacci = [0, 1]

while numerosMostrados != qntdNumeros - 2:
    numAtual = numFibonacci[numerosMostrados] + numFibonacci[numerosMostrados + 1] 
    
    numFibonacci.append(numAtual)
    numerosMostrados += 1

for num in numFibonacci:
    print(num, end=' -> ')

print("FIM")