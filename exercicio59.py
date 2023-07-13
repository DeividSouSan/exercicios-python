"""
Crie um programa que leia dois valores e mostre o menu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
from lin import *
from cprint import *

values = []
operations = ['Somar', 'Multiplicar', 'Maior', 'Novos Números', 'Sair do Programa']

title("MENU", "≃=", 25)
sleep(0.5)
for i in range(0, 2):
    value = int(input(f"Insira o {len(values) + 1}º valor: "))
    values.append(value)


while True:
    sleep(0.5)
    lin('--', 25)
    print("Operações: ")
    for index, op in enumerate(operations):
        sleep(0.2)
        print(f"[{index + 1}] - {op.capitalize()}")
    lin('--', 25)

    op = int(input('Qual opção?\n>> '))

    match op:
        case 1:
            # Somar
            soma = values[0] + values[1]
            cprint(f"!A soma de {values[0]} com {values[1]} é {soma}.!", BOLD, C_WHITE)
        case 2:
            # Multiplicar
            multiplicacao = values[0] * values[1]
            cprint(f"!A multiplicacao de {values[0]} por {values[1]} é {multiplicacao}.!", BOLD, C_WHITE)   
        case 3:
            # Maior
            maior = max(values)
            cprint(f"!O maior valor entre {values[0]} e {values[1]} é {maior}.!", BOLD, C_WHITE)
        case 4:
            # Novos Números
            soma = values[0] + values[1]
            for i in range(0, 2):
                value = int(input(f"Insira o {i + 1}º valor: "))
                values[i] = value
        case 5:
            # Sair do Programa
            print("Saindo...")
            sleep(1)
            break
        case __:
            cprint("!Opção inválida. Tente de novo.!", C_RED)
    sleep(1)

print("Programa Finalizado.")