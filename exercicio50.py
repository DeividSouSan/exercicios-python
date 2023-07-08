"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

somaValores = 0

for i in range(1, 7):
    num = int(input(f"Número {i}: "))
    if i % 2 == 0:
        somaValores += num

print("A soma dos valores pares digitado é ", somaValores)
