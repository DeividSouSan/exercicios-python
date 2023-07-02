
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

valores = ["Primeiro", "Segundo", "Terceiro"]

for i in range(0, 3):
    num = int(input(f"{valores[i]} valor:"))
    valores[i] = num

print(f"O menor valor digitado foi {min(valores)} e o maior valor digitado foi {max(valores)}.")