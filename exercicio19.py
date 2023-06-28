"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido.
"""
from math import floor
from random import randint
from time import sleep

def loading(frase, time):
    timeBetween = time / 3

    print(frase, end="", flush=True)
    sleep(timeBetween)
    print(".", end="", flush=True)
    sleep(timeBetween)
    print(".", end="", flush=True)
    sleep(timeBetween)
    print(".", end="", flush=True)

listaAlunos = list()

for i in range(0, 4):
    aluno = str(input("Insira o nome do aluno(a): "))
    listaAlunos.append(aluno)

numAleatorio = floor(randint(0, 3))

loading("Sorteando", 3)
sleep(1)

print(f"\nO aluno(a) sorteado(a) foi {listaAlunos[numAleatorio]}")
