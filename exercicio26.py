"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a aletra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.
"""
frase = str(input("Digite uma frase: "))
frase = frase.strip().lower().replace(" ", "")

print(f"A letra A aparece {frase.count('a')} vezes.\nA primeira letra A é o {frase.find('a') + 1} caractere.\nA última letra A é o {frase.rfind('a') + 1} caractere.");
