"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule mostre o comprimento da hipotenusa.
"""
from math import sqrt
catOposto = float(input("Cateto Oposto: "))
catAdjacente = float(input("Cateto Adjacente: "))

hipotenusa = sqrt(catOposto**2 + catAdjacente**2)

print(f"Hipotenusa: {hipotenusa}.")