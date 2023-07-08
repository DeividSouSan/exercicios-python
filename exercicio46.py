"""
Faça um programa que mostre na tela uma contafem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
from cprint import *

for i in range(10, 0, -1):
    print(i, end=" ", flush=True)
    sleep(1)

cprint("BOOM", C_RED)
sleep(1)