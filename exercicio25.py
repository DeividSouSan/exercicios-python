"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
"""

nome = str(input("Qual seu nome completo: "))

print(f"Seu nome tem 'Silva'? {'silva' in nome.strip().lower() } ")
