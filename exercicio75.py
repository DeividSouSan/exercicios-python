"""
Desenvolva um programa que leia quatro valores pelo teclado e os guarde em uma tupla. No final, moste:
- Quantas vezes apareceu o valor 9
- Em que posição foi digitado o primeiro valor 3
- Quais foram os números pares
"""
numbers = tuple()

for i in range(4):
    num = int(input("Digite um número: "))
    numbers += num, 

# Verificando quantas vezes o 9 apareceu
print("Número de vezes que o 9 aparece:", numbers.count(9))

# Posição od primeiro valor 3
try:
    print("Posição do primeiro valor três: ", numbers.index(3) + 2)
except ValueError:
    print("Não existe valor 3 na tupla.")

print("Números pares: ", end="")
# Quais foram os número pares
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")