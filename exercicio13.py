"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""

salarioAnterior = float(input("Qual o salário do funcionário: R$ "))

novoSalario = salarioAnterior * 1.15

print(f"Salário Anterior: R$ {salarioAnterior} | Salário Pós-aumento: R$ {novoSalario:.2f}.")