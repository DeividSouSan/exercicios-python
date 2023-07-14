"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
from cprint import *
from lin import title

title("10 Primeiros Termos de uma P.A", "=~", 25)

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

posicaoTermoFinal = 10
posicaoUltimoTermoMostrado = 0

while True:
    for i in range(posicaoUltimoTermoMostrado, posicaoTermoFinal):
        print(f"{primeiroTermo + (razao * i)} ->", end=" ")

    print('PAUSA')

    numProximosTermos = int(input("Quantas termos a mais? "))

    if numProximosTermos <= 0:
        break
    else:
        posicaoUltimoTermoMostrado = posicaoTermoFinal
        posicaoTermoFinal = posicaoUltimoTermoMostrado + numProximosTermos
    
print("FIM")