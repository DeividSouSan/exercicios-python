"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
listaAlunos = []

for i in range(1, 5):
    aluno = str(input(f"{i}º aluno(a): "))
    listaAlunos.append(aluno)

shuffle(listaAlunos)

print("A ordem da apresentação será:")
for i in range(0, len(listaAlunos)):
    print(f"{i+1}º {listaAlunos[i]}")