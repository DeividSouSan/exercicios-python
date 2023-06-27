"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 R$ por dia e 0.15 R$ por Km rodado.
"""

qntdKm = float(input("Quantos Km foram percorridos? Km "))
qntdDias = int(input("Quantos dias o ficou alugado? "))

totalPagar = (qntdDias * 60) + (qntdKm * 0.15)

print(f"O total a pagar por {qntdDias} dia(s) alugado(s) e {qntdKm} km percorridos é {totalPagar:.2f} R$.")