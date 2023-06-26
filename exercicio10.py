"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostr quantos dólares ela pode comprar.
"""

dinheiroReal = float(input("Quanto dinherio você tem na carteira: "))

cotacaoDolar = 4.77

print(f"Com esse dinheiro você pode comprar: {round((dinheiroReal/cotacaoDolar), 2)}$")