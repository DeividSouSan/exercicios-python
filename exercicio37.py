"""
Escreva um programa que leia um número inteiro qualquer e preça para usuário escolher qual será a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

try: 
    decimalNum = int(input("Digite um número inteiro: "))

    op = int(input("Escolha uma base para a conversão:\n\
               [1] Binário\n\
               [2] Ocatal\n\
               [3] Hexadecimal\n\
               >>"))
except:
    decimalNum = 0
    op = -1

resultado = ""
base = ""
match op:
    case 1:
        base = ["0b", "binária"]
        resultado = bin(decimalNum).replace(base[0], "")
    case 2:
        base = ["0o", "octal"]
        resultado = oct(decimalNum).replace(base[0], "")
    case 3: 
        base = ["0x", "hexadecimal"]
        resultado = hex(decimalNum).replace(base[0], "").upper()
    case _:
        base = ["", ""]
        resultado = -1

if resultado != -1:
    print(f"A conversão da base decimal {decimalNum} para a base {base[1]} é {resultado}.")
else:
    print("A conversão deu errado.")
