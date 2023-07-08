"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
from cprint import *
from lin import title

title("10 Primeiros Termos de uma P.A", "=~", 25)

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for i in range(0, 10):
    print(f"{primeiroTermo + (razao * i)} ->", end=" ")

print("Fim.")