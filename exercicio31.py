"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.
"""

dist = float(input("Insira a distância da viagem: "))

precoPromocional = dist >= 200
precoKm = 0.45 if precoPromocional else 0.50

print(f"Sua viagem é de {dist:.2f} Km, portânto sua passagem irá custar R$ {(dist * precoKm):.2f}.")