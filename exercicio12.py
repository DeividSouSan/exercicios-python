"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""

precoProduto = float(input("Qual é o preço do produto? R$ "))

novoPreco = precoProduto * 0.95
print(f"Preço Anterior: R$ {precoProduto} | Com desconto de 5%: R$ {novoPreco:.2f}.")