"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
"""

nomeCidade = str(input("Em que cidade você nasceu: "))

if nomeCidade.strip().split(" ")[0].lower() == "santo":
    print("Você nasceu em uma cidade que começa com 'Santo'.")
else:
    print("Você não nasceu em uma cidade que começa com 'Santo'.")
