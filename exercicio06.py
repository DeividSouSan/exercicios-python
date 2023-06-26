"""
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
"""
import math
num = int(input("Digite um número: "))

print(f"O dobro de {num} é {2*num}.\nO triplo de {num} é {3*num}.\nA raiz quadrada de {num} é {round(math.sqrt(num), 2)}.")