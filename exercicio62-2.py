"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. [Utilizando yield]
"""
from lin import title

title("10 Primeiros Termos de uma P.A", "=~", 25)

primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

posicaoTermoFinal = 10
posicaoUltimoTermoMostrado = 0
listaTermos = []
def mostraTermos(inicio, fim):
    for posicao in range(inicio, fim):
        yield primeiroTermo + (razao * posicao)

while True:
    for posicao, termo in enumerate(mostraTermos(posicaoUltimoTermoMostrado, posicaoTermoFinal)):
        print(termo, end=' -> ')
        listaTermos.append(termo)

    if posicao == (posicaoTermoFinal - 1) - posicaoUltimoTermoMostrado:
        print("PAUSE", end='\n')
        numProximosTermos = int(input("Quantas termos a mais? "))

        if numProximosTermos <= 0:
            break
        else:
            posicaoUltimoTermoMostrado = posicaoTermoFinal
            posicaoTermoFinal = posicaoUltimoTermoMostrado + numProximosTermos

print("Fim.")
print(f"Número de termos mostrados: {len(listaTermos)}.")