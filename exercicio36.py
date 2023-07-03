"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from math import ceil
valorCasa = int(input("Qual o valor da casa? R$ "))
salarioComprador = float(input("Qual o salário do comprador? R$ "))
qntdAnos = int(input("Quantos anos para quitar? "))

prestacao = valorCasa / (qntdAnos * 12)

prestacaoMaximoPermitido = (0.3 * salarioComprador)
qntdAnosMinima = ceil(valorCasa / (prestacaoMaximoPermitido * 12))

emprestimoPermitido = False if prestacao >= prestacaoMaximoPermitido  else True

if emprestimoPermitido:
    print(f"Empréstimo Permitido. A prestação mensal é R$ {prestacao:.2f}. O valor máximo da prestação permitido para o seu salário é de R$ {prestacaoMaximoPermitido}")
else:
    print(f"Empréstimo Negado. Prestação (R$ {prestacao:.2f}) é 30% ou mais do salário do comprador (R$ {salarioComprador:.2f}).\n\
O valor máximo da prestação permitido é de R$ {prestacaoMaximoPermitido}, para atingir esse valor parcele em, no mínimo, {qntdAnosMinima} anos.")