"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa deverá ser interrompido quando o número solicitado for negativo.
"""

while True:
    value = input("Digite um número [SAIR para sair]: ")

    if (value.lower() == "sair") or (value.isalpha() == True) or (int(value) < 0):
        print("Programa Finalizado.")
        break
    elif value.find(".") != -1:
        print("Digite um númeor INTEIRO.")
        continue

    print(f"Tabuada do {value}: ")
    for i in range(1, 11):
        print(f"{value} x {i:2} = {int(value) * i}")

    