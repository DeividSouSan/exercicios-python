"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = str(input("Digite seu nome completo: "))

nome = nome.split()

print(f"Seu primeiro nome é {nome[0]}.\nSeu último nome é {nome[-1]}.")