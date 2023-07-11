"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

anoAtual = date.today().year

numeroMaiorIdade = 0
numeroMenorIdade = 0

for i in range(1, 8):
    anoNascimento = int(input("Digite o ano de nascimento da pessoa: "))
    idadePessoa = anoAtual - anoNascimento


    if idadePessoa >= 18:
        numeroMaiorIdade += 1
    else:
        numeroMenorIdade += 1

print(f"Antigiram maioridade: {numeroMaiorIdade}.\nAinda não atingiram: {numeroMenorIdade}.")

