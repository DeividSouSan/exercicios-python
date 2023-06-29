"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
"""

num = int(input("Digite um número: "))

digitos = {"unidade": 0, "dezena": 0, "centena": 0, "milhar": 0}

for casa in digitos:
    digitos[casa] = num % 10

    num //= 10

print(f"Unidade: {digitos['unidade']}.\n\
Dezena: {digitos['dezena']}.\n\
Centena: {digitos['centena']}.\n\
Milhar: {digitos['milhar']}.")