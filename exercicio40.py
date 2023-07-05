"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 7.0: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
from cprint import *

primeiraNota = float(input("Primeira Nota: "))
segundaNota = float(input("Segunda Nota: "))

media = (primeiraNota + segundaNota) / 2

APROVADO = media >= 7.0
RECUPERACAO = 5.0 <= media < 7.0
REPROVADO = media < 5.0

if APROVADO:
    cprint(f"Média: {media:.1f} -> !APROVADO!!", BOLD, C_GREEN)
elif RECUPERACAO:
    cprint(f"Média: {media:.1f} -> !RECUPERAÇÃO!!", BOLD, C_YELLOW)
elif REPROVADO:
    cprint(f"Média: {media:.1f} -> !REPROVADO!!", BOLD, C_RED)

