"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras tem ao todo (sem contar os espaços);
- Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite seu nome completo: "))

print(f"Seu nome em maiúsculas é {nome.upper()}.\n\
Seu nome em minúsculas {nome.lower()}.\n\
Seu nome tem ao todo {len(nome.replace(' ', ''))} letras.\n\
Seu primeiro nome é {nome.split(' ')[0]} e ele tem {len(nome.split(' ')[0])} letras.")
