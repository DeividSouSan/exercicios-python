"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

segUm = float(input("Primeiro segmento: "))
segDois = float(input("Segundo segmento: "))
segTres = float(input("Terceito segmento: "))

if segUm < (segDois + segTres) and segDois < (segUm + segTres) and segTres < (segUm + segDois):
    print("Os segumentos acima PODEM FORMAR um triângulo.")
else:
    print("Os segumentos acima NÃO PODEM FORMAR um triângulo.")