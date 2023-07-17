"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma dentre eles (desconsiderando a condição de parada).
"""

values = []
while True:
    value = str(input("Digite um número INTEIRO [FIM para parar]: "))

    if value.lower() == "fim":
        break
    elif (value.lower().isalpha() == True) or (value.find('.') != -1):
        print("Digite um número INTEIRO ou 'FIM'. Números de ponto flutuante não são válidos.")
        continue

    values.append(int(value))

print(f"O número de valores digitados foi {len(values)} e a soma entre eles é {sum(values)}.")
