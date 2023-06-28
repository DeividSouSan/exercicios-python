"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""

num = float(input("Digite um número: "))

parteDecimal = num % 1

print(f"O número digitado foi {num}. Sua parte inteira é {num - parteDecimal}.")
