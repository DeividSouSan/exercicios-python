"""
Crie uma tupla totalmente preenchida com uma contagem por extenso de zero até vinto. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numberInWords = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte")

while True:
    num = int(input("Insira um número entre 0 e 20: "))
    
    if 0 <= num <= 20:
        print("Digite um número entre 0 e 20.")
        break

for number, inWords in enumerate(numberInWords):
    if num == int(number):
        print("Você digitou o número", inWords)
