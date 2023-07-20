"""
Crie um programa que simule o funcoinamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
"""

availableNotes= [50, 10, 1]

print("=~" * 25)
print("BEM VINDO AO BANCO CeV")
print("=~" * 25)

withdrawMoney = int(input("Valor a ser sacado: R$"))

for note in availableNotes:
    print(f"Total de {withdrawMoney // note} notas de R$ {note}")

    withdrawMoney %= note

print("Muito obrigado pela preferência, volte sempre.")