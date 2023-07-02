"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
import datetime

ano = int(input('Digite o ano [0 - Ano Atual]: '))
if ano == 0:
    ano = datetime.date.today().year

ehBissexto = ((ano % 100 != 0) and (ano % 4 == 0)) or (ano % 400 == 0)

print(f"O ano de {ano} é BISSEXTO.") if ehBissexto else print(f"O ano de {ano} NÃO é BISSEXTO.")