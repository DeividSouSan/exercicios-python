"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais.
"""

from cprint import *

primeiroValor = int(input("Primeiro número: "))
segundoValor = int(input("Segundo número: "))

if primeiroValor > segundoValor:
    cprint("O !primeiro! valor é maior.", BOLD, C_GREEN)
elif segundoValor > primeiroValor:
    cprint("O !segundo! valor é maior.", BOLD, C_GREEN)
else:
    cprint("!Não existe valor maior!, ambos são iguais.", UNDERLINE)