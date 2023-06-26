"""
Faça um programa que leia um número inteiro e escreva na tela a sua tabuada.
"""
num = int(input("Digite um número para ver sua tabuada: "))

print(15*"-")

for i in range(1, 11):
    print(f"{num} x {i:2} = {num*i}")

print(15*"-")

