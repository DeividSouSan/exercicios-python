
from lin import *
from cprint import *
from time import sleep
from random import randint

def quemVenceu(jogadaUsuario, jogadaComputador):

    COMPUTADOR_VENCE = (jogadaUsuario == 1 and jogadaComputador == 2) or (jogadaUsuario == 3 and jogadaComputador == 1) or (jogadaUsuario == 2 and jogadaComputador == 3)
    EMPATE = jogadaUsuario == jogadaComputador

    if COMPUTADOR_VENCE:
        venceu = "COMPUTADOR VENCE."
    elif not COMPUTADOR_VENCE:
        venceu = "JOGADOR VENCE"
    elif EMPATE:
        venceu = "EMPATE"

    return venceu

title("JOKENPO!", "=~", 25)

sleep(0.5)

JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']

lin('-', 50)
jogadaUsuario = int(input("Suas opções:\n\
[1] PEDRA\n\
[2] PAPEL\n\
[3] TESOURA\n\
Qual sua jogada? "))
lin('-', 50)

jogadaComputador = randint(1, 3) + 1

sleep(1)

lin('=', 50)
print(f"COMPUTADOR: {JOGADAS[jogadaComputador - 1]}\n\
JOGADOR: {JOGADAS[jogadaUsuario]}")
lin('=', 50)

print(quemVenceu(jogadaUsuario, jogadaComputador))

"""
PEDRA X PEDRA = PEDRA = EMPATE
1 X 1

PEDRA X PAPEL = PAPEL = COMP VENCE
1 X 2
PAPEL X PEDRA = JOG = VENCE
2 X 1

PEDRA X TESOURA = PEDRA = JOG VENCE
1 X 3
TESOURA X PEDRA = PEDRA = COMP VENCE
3 X 1

PAPEL X PAPEL = PAPEL= EMPATE
2 X 2

PAPEL X TESOURA = TESOURA = COMP VENCE
2 X 3
TESOURA X PAPEL = TESOURA = JOG VENCE
3 X 2

TESOURA X TESOURA = TESOURA = EMPATE
3 X 3
"""