"""
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
from cprint import *
from lin import title

title("10 Primeiros Termos de uma P.A", "=~", 25)

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

i = 0
while i < 10:
    print(f"{primeiroTermo + (razao * i)} ->", end=" ")
    i += 1

print("PAUSA")