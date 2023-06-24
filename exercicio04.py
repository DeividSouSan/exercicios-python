"""
Faça um programa que leia algo pelo teclado e mostre na tella o seu tipo primitivo e todas as informações possíveis sobre ela.
"""

#Lendo o valor
info = input("Insira algo: ")

# Escrevento na tela cada método
print(f"O tipo primitivo desse valor é {type(info)}.\
    Só tem espaços? {info.isspace()} \
    É um número? {info.isnumeric()}\
    É alfabético? {info.isalpha()}\
    É alfanumérico? {info.isalnum()}\
    Está em maiúsculas? {info.isupper()}\
    Está em minúsculas? {info.islower()}\
    Está capitalizada? {info.istitle()}")