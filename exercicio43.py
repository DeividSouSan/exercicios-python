"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule se IMC e mostre seus status, de acordo com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso;
- Entre 18.5 e 25: peso ideal;
- 25 até 30: sobrepeso;
- 30 até 40: obesidade;
- Acima de 40: obesidade mórbida.
"""
from cprint import *

pesoPessoa = float(input("Qual é o seu peso? [kg]: "))
alturaPessoa = float(input("Qual sua altura? [m]: "))

IMC = pesoPessoa / (alturaPessoa ** 2)

ABAIXO = IMC <= 18.5
IDEAL = 18.5 < IMC <= 25
SOBREPESO = 25 < IMC <= 30
OBESIDADE = 30 < IMC <= 40
OBESIDADE_MORBIDA = IMC > 40

if ABAIXO: imc_status = 'abaixo'
elif IDEAL: imc_status = 'ideal'
elif SOBREPESO: imc_status = 'sobrepeso'
elif OBESIDADE: imc_status = '!obesidade!'
elif OBESIDADE_MORBIDA: imc_status = 'obesidade mórbida'

cprint(f"IMC: {IMC:.2f}. Classificação: !{imc_status}!", BG_YELLOW)