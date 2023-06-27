"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta um área de 2 metros quadrados.
"""

larguraParede = float(input("Largura: "))
alturaParede = float(input("Altura: "))

area = larguraParede * alturaParede

litrosTinta = area / 2

print(f"Sua parede tem {alturaParede} altura, {larguraParede} de largura e possui uma área de {area}. Serão necessários {litrosTinta:.2f} litros de tinta para pinta-la.")
