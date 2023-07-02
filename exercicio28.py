"""
Faça um programa que gere um número aleatório entre 0 e 5 e peça para o usuário digitar um número dentro desse intervalo, se o palpite e o número aleatório forem iguais mostre uma mensagem de 'Parabéns!' para o usuário.
"""
from random import randint

num = randint(0, 5)

palpite = int(input("Em que número pensei? "))

if num == palpite:
    print("Parabéns. Você acertou.")
else:
    print(f"Uma pena. Você errou. Pensei no número {num}.")