"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from lin import *
from cprint import *
from time import sleep
from random import randint

def quemVenceu(jogadaUsuario, jogadaComputador):

    COMPUTADOR_VENCE = (jogadaUsuario == 0 and jogadaComputador == 1) or (jogadaUsuario == 2 and jogadaComputador == 0) or (jogadaUsuario == 1 and jogadaComputador == 2)
    EMPATE = jogadaUsuario == jogadaComputador

    if EMPATE:
        venceu = "EMPATE"
    elif COMPUTADOR_VENCE:
        venceu = "COMPUTADOR VENCE."
    elif not COMPUTADOR_VENCE:
        venceu = "JOGADOR VENCE"

    return venceu

title("JOKENPO!", "=~", 25)

sleep(0.5)

JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']

lin('-', 50)
jogadaUsuario = int(input("Suas opções:\n\
[0] PEDRA\n\
[1] PAPEL\n\
[2] TESOURA\n\
Qual sua jogada? "))
lin('-', 50)

jogadaComputador = randint(0, 2)

sleep(1)

lin('=', 50)
print(f"COMPUTADOR: {JOGADAS[jogadaComputador]}\n\
JOGADOR: {JOGADAS[jogadaUsuario]}")
lin('=', 50)

print(quemVenceu(jogadaUsuario, jogadaComputador))

"""
PEDRA X PEDRA = PEDRA = EMPATE
0 X 0

PEDRA X PAPEL = PAPEL = COMP VENCE
0 X 1
PAPEL X PEDRA = JOG = VENCE
1 X 0

PEDRA X TESOURA = PEDRA = JOG VENCE
0 X 2
TESOURA X PEDRA = PEDRA = COMP VENCE
2 X 0

PAPEL X PAPEL = PAPEL= EMPATE
1 X 1

PAPEL X TESOURA = TESOURA = COMP VENCE
1 X 2
TESOURA X PAPEL = TESOURA = JOG VENCE
2 X 1

TESOURA X TESOURA = TESOURA = EMPATE
2 X 2
"""