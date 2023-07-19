"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: qual é o total gasto na compra, quantos produtos custam mais de 10000 R$ e qual é o nome do produto mais barato.
"""

from lin import *

def totalBought(prod):
    total = 0
    for product in prod:
        total += product['price']

    return total

def qntyAbove1000(prod):
    totalAbove1000 = 0
    for product in prod:
        if product['price'] > 1000:
            totalAbove1000 += 1

    return totalAbove1000

def cheapestProduct(prod):
    cheapestProd = 0
    cheapestProdId = 0

    for index, product in enumerate(prod):
        if index == 0:
            cheapestProd = product['price']
            cheapestProdId = index
        else:
            if cheapestProd > product['price']:
                cheapestProd = product
                cheapestProdId = index

    return prod[cheapestProdId]

print(25*"=~")
print("Loja Super Baratão")
print(25*"=~")

# Descomente para ter um teste rápido
""" products = [
    {"name": 'Lapiseira', 'price': 6.0},
    {"name": 'Caderno', 'price': 25.0},
    {"name": 'Computador', 'price': 12000.0},
    {"name": 'Impressora', 'price': 750.0},
    {"name": 'Celular', 'price': 1800.0},
    {"name": 'Salgandinho', 'price': 3.0}
] """

# Comente se quiser utilizar o teste rápido
products = []

while True:

    productName = str(input("Nome do Produto: "))
    productPrice = float(input("Preço: R$ "))

    thisProduct= {'name': productName, 'price': productPrice}
    products.append(thisProduct)

    keepRuning = str(input("Quer continuar? [S/N]: "))
    if keepRuning.lower() == 'n':
        print('Finalizando programa...')
        break

print(f"O total da compra foi R$ {totalBought(products):.2f}.\nTemos {qntyAbove1000(products)} produtos custando acima de R$ 1000.00.\nO produto mais barato foi {cheapestProduct(products)['name']} que custa R${cheapestProduct(products)['price']:.2f}")
