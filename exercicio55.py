"""
Faça um programa que leia o peso de cincos pessoas. No final, mostre qual foi o maior peso e o menor peso lidos.
"""

for ordemPessoa in range(1, 6):
    pesoPessoa = float(input(f"Peso da pessoa {ordemPessoa}: "))

    if ordemPessoa == 1:
        maiorPeso = pesoPessoa
        menorPeso = pesoPessoa
    else:
        if pesoPessoa > maiorPeso:
            maiorPeso = pesoPessoa
        
        if pesoPessoa < menorPeso:
            menorPeso = pesoPessoa

print(f"\nO menor peso foi: {menorPeso}.\nO maior peso foi: {maiorPeso}.")