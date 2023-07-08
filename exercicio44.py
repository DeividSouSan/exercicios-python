"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros
"""
from time import sleep
from lin import *
from cprint import *

title("GERENCIADOR DE PAGAMENTOS", "=~", 25)

lin("=", 50)
precoTotal = float(input("Preço Total das Compras: R$"))

lin("-", 50)
opcoesPagamento = int(input("Qual opção de pagamento?\n\
- À vista dinheiro/cheque (10% de desconto) [1]\n\
- À vista no cartão (5% de desconto) [2]\n\
- Em até 2x no cartão (sem desconto) [3]\n\
- 3x ou mais no cartão (20% de juros) [4]\n\
Opção escolhida: "))
lin("=", 50)

sleep(1)

match opcoesPagamento:
    case 1:
        DESCONTO = precoTotal * 0.90 # 10% de desconto
        cprint(f"Sua compra de R${precoTotal:.2f} vai custar R$:!{DESCONTO:.2f}!.[à vista no dinheiro]", BOLD,C_GREEN)
    case 2:
        DESCONTO = precoTotal * 0.95 # 5% de desconto
        cprint(f"Sua compra de R${precoTotal:.2f} vai custar R$:!{DESCONTO:.2f}!.[à vista no cartão]", BOLD,C_GREEN)
    case 3:
        PARCELA = precoTotal / 2 
        cprint(f"Sua compra de R${precoTotal:.2f} será parcelada em 2x de R$!{PARCELA:.2f}!.[2x cartão s/ juros]", BOLD,C_GREEN)
    case 4:
        while True:
            numeroParcelas = int(input("Quantas parcelas? [0, 1, 2 são inválidos] > "))
            NUM_PARCELAS_VALIDO = False if numeroParcelas in [0, 1, 2] else True
            if NUM_PARCELAS_VALIDO:
                break

        PRECO_FINAL = precoTotal * 1.20
        PARCELA = (PRECO_FINAL) / numeroParcelas # 20% de juros

        cprint(f"Sua compra de R${precoTotal:.2f} será parcelada em {numeroParcelas}x de R$!{PARCELA:.2f}! e vai custar R${PRECO_FINAL:.2f} no final.", BOLD,C_GREEN)
    case __:
        print("Opção escolhida inválida.")