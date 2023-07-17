"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""


relevantValues = {"lowestValue": 0, "highestValue": 0}
counter = 0
valuesSum = 0
while True:
    num = int(input("Digite um número: "))
    counter += 1

    if counter == 1: # Primeira repetição então guarda os primeiros valores
        relevantValues["lowestValue"] = num
        relevantValues["highestValue"] = num

    else: # Próximas repetições comparamos os primeiros valores com o segundo e atribuimos novos valores se as condições forem satisfeitas
        if relevantValues['highestValue'] < num:
            relevantValues["highestValue"] = num

        if relevantValues["lowestValue"] > num:
            relevantValues["lowestValue"] = num

    valuesSum += num

    repeat = str(input("Continuar [s/n]: "))

    if repeat == 's':
        continue

    elif repeat == 'n':
        break

average = valuesSum / counter

print(f"Foram digitados {counter} números. A média entre eles é {average:.2f}.")