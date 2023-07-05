"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acoro com a idade:
- MIRIM: até 9 anos;
- INFANTIL: até 14 anos;
- JUNIOR: até 19 anos;
- SÊNIOR: até 25 anos;
- MESTRE: acima de 25 anos;
"""
from cprint import *
from datetime import date

anoNascimento = int(input("Ano de Nascimento: "))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

def classificacaoAtleta(idade):
    MIRIM = idade <= 9
    INFANTIL = 9 < idade <= 14
    JUNIOR = 14 < idade <= 19
    SENIOR = 19 < idade <= 25
    MESTRE = idade > 25

    if MIRIM:
        classificacao = "MIRIM"
    elif INFANTIL:
        classificacao = "INFANTIL"
    elif JUNIOR:
        classificacao = "JUNIOR"
    elif SENIOR:
        classificacao = "SENIÔR"
    elif MESTRE:
        classificacao = "MESTRE"

    return classificacao
    
cprint(f"O atleta tem {idade} anos.\nClassificação: !{classificacaoAtleta(idade)}!.", ITALIC, C_BLUE)