"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.
"""

wordsTuple = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

def quaisVogais(word: str):
    vogais = []
    for letter in word:
        if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
            vogais.append(letter)

    yield vogais


for index, vogais in enumerate(map(quaisVogais, wordsTuple)):
    print(f"A palavra {wordsTuple[index]} tem", *vogais)
