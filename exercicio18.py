"""
Faça um algoritmo que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, pi, radians

angulo = float(input("Digite o ângulo que você deseja: "))

anguloRad = radians(angulo)

print(f"O ângulo de {angulo}º tem SENO = {sin(anguloRad):.2f} | COSSENO = {cos(anguloRad):.2f} | TANGENTE = {tan(anguloRad):.2f}.")