"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No finalmostre: quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.
"""
from lin import *
# from copy import deepcopy

# CLASSE PESSOAS
class Person:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

    def __repr__(self) -> str:
        return f"Person Age: {self.age} Sex: {self.sex}"

# VARIÁVEIS

qntyOver18 = 0
qntyMens = 0
qntyWomanLower20 = 0
signedPeople = []

# PROGRAMA
title("CADASTRE UMA PESSOA", '=~', 25)

while True:
    age = int(input("Idade: "))
    sex = str(input("Sexo [M/F]: "))

    if age > 18:
        qntyOver18 += 1

    if sex.lower() == 'm':
        qntyMens += 1

    if sex.lower() == 'f' and age < 20:
        qntyWomanLower20 += 1

    signedPeople.append(Person(age, sex))

    keepRunning = str(input("Quer continuar? [S/N]: "))

    if keepRunning == 's':
        continue
    elif keepRunning == 'n':
        break
    else:
        print("Caractere desconhecido. Continuando...")

print("Programa encerrado!")

print(f"Total de pessoas com mais de 18: {qntyOver18}\nAo todo temos {qntyMens} homens cadastrados\nE temos {qntyWomanLower20} mulheres com menos de 20 anos")

