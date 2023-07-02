"""
Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80 Km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada Km/h acima do limite.
"""

velocidadeCarro = int(input("Qual é a velocidade atual do carro? "))

velocidadeMaxPermitida = 80

acimaVelociade = velocidadeCarro > 80

if acimaVelociade:
    precoMulta = (velocidadeCarro - velocidadeMaxPermitida) * 7.0

    print(f"Multado. Você ultrapassou o limite de velocidade permitido que é de 80 Km/h. Você deve pagar uma multa de R$ {precoMulta:.2f}!")

print("Tenha um bom dia. Dirija com segurança.")