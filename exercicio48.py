"""
Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
from cprint import *

somaValores = 0
qntdNumeros = 0


for i in range(1, 501):
    if (i % 2 == 1) and (i % 3 == 0):
        qntdNumeros += 1
        somaValores += i

cprint(f"A soma dos {qntdNumeros} solicitados é !{somaValores}!.", C_BLUE)