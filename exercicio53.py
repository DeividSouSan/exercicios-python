"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços e símbolos especiais.

Exemplos de palíndromos:
A sacada da casa
Apos a sopa
A torre da derrota
O lobo ama o bolo
Anotaram da data da maratona
Socorram-me subi no onibus em marrocos
"""
frase = str(input("Digite uma frase: "))

# Modificando a frase para ela ficar sem caracteres especiais e em minúsculo
frase_limpa = frase.lower()
frase_limpa = "".join(filter(str.isalnum, frase_limpa))

# Invertendo a frase
frase_inversa = ""

for i in reversed(frase_limpa):
    frase_inversa += i

EH_PALINDROMO = True if frase_limpa == frase_inversa else False

if EH_PALINDROMO:
    print(f"A frase {frase} é um palíndromo.\nFrase: {frase_limpa}\nFrase Invertida: {frase_inversa} ")
else:
    print(f"A frase {frase} não é um palíndromo.\nFrase: {frase_limpa}\nFrase Invertida: {frase_inversa} ")
