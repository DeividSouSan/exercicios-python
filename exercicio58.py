"""
Melhore o jgo do desafio 28 onde o computador vai escolher um número entre 1 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from lin import *
from cprint import *
from random import randint
from time import sleep

title("JOGO DA ADIVINHAÇÃO", "≃", 25)
sleep(1)
print("Vou escolher um número entre 1 e 10 e você vai tentar adivinhar qual é.")

while True:
    confirmacaoPalavras = ['sim', 's', 'vamos', 'ok', 'pode ser', 'tudo bem', 'bora']
    negacaoPalavras = ['não', 'n', 'sair', 'não quero', 'hoje não']

    sleep(1)

    try:
        comecarJogo = str(input("Vamos jogar? [S/N]\n>> "))

        if comecarJogo.lower() in confirmacaoPalavras:
            break
        elif comecarJogo.lower() in negacaoPalavras:
            print("Encerrando programa...")
            quit()
        else:
            raise Exception("Digite 'sim' ou 'não'.")
    except Exception as err:
        print(err)

sleep(1)

numeroAleatorio = randint(1, 10)
print("Pensei em um número entre 1 e 10. Qual é o seu palpite?")

numeroTentativas = 0

while True:
    numeroTentativas += 1

    while True:
        try:
            tentativa = int(input(C_RED + ">> " + END_C))

            if tentativa < 1 or tentativa > 10:
                raise Exception("Insira um número dentro do intervalo de 1 à 10.")
            else:
                break
            
        except ValueError:
            print("Insira um númeor inteiro entre 0 e 10.")

        except Exception as err:
            print(err)

    if tentativa == numeroAleatorio:
        break
    elif tentativa < numeroAleatorio:
        cprint("O número que eu pensei é !maior!. Tente de novo.", C_GREEN)
    else:
        cprint("O número que eu pensei é !menor!. Tente de novo.", C_RED)

print(f"Parabéns. Você acertou o número!\nForam {C_YELLOW} {numeroTentativas} {END_C} tentativas.")