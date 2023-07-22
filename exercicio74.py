"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
"""
from random import randint

randomNumbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(randomNumbers)
print("Menor valor da tupla: ", min(randomNumbers))
print("Maior valor da tupla: ", max(randomNumbers))
