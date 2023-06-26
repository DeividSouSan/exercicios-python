"""
Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.
"""

dist = float(input("Distância em metros: "));

print(f"Equivale a: {dist/1000}km | {dist/100}hm | {dist/10}dam | {dist*10}dm | {dist*100}cm | {dist*1000}mm |")