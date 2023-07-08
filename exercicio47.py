"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

from time import sleep
for i in range(1, 51):
    print(i if i % 2 == 0 else "", end=" ", flush=True)
    sleep(1)