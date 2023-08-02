"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista completa.
"""

from random import sample

guesses = []

numberOfGames = int(input("Quantos jogos? "))

for i in range(numberOfGames):
    row = []

    row = sample(range(1, 61), 6)

    guesses.append(row)

for guess in guesses:
    print(guess)


"""
row = random.sample(range(1, 61), 6)

Ou  

while len(row) < 6:
        randomNumber = randint(1, 60)

        if randomNumber in row:
            continue

        row.append(randomNumber)
"""