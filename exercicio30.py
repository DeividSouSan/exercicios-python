"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
"""

num = int(input("Digite um número: "))

ehPar = num % 2 == 0

if ehPar:
    print('O número digitado é PAR!')
else:
    print('O número digitado é ÍMPAR')