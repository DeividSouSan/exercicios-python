"""
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada de cada um e que permita que o usuário possa ver as notas de cada aluno individualmente.
"""

from lin import *

studentGrades = []

print('=-' * 25)
print(f'{"MÉDIAS": ^50}')
print('=-' * 25)

while True:
    currentStudent = []

    currentStudent.append(str(input("Nome: "))) 
    currentStudent.append(float(input('Nota 1: ')))
    currentStudent.append(float(input('Nota 2: ')))

    studentGrades.append(currentStudent)

    keepRunning = str(input('Continuar? [S/N] '))
    if keepRunning.lower() == 'n':
        break

print(f'{"Nº":<3} | {"Nome":<10} | {"Nota":>10}')
print('--' * 25)

for id, student in enumerate(studentGrades):
    print(f'{id:<3} | {student[0]:<10} | {(student[1] + student[2]) / 2:>10}')

print('--' * 25)

while True:
    try:
        studentID = int(input("Mostrar notas de qual aluno? [-1 interrompe] "))

        if studentID == -1:
            break
        elif studentID < 0:
            raise ValueError
        elif not (0 <= studentID < len(studentGrades)):
            raise IndexError

        print(f"{studentGrades[studentID][0]} - Nota 1: {studentGrades[studentID][1]} | Nota 2: {studentGrades[studentID][2]}")

    except ValueError:
        print("> Digite um número inteiro positivo.")
        continue
    except IndexError:
        print("> Digite um ID que conste na lista.")
        continue
