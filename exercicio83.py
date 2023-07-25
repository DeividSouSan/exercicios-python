"""
Crie um programa que o usuário digite uma expressão qualquer que use parenteses. Seu programa deverá análisar se a expessão passada está com os parênteses abertos e fechados na ordem correta.
"""

#'(a + b * (c + (z - y)))'
#'(a + (c + (z - y) + w)))'
#'((a + b) * c)(x + y(3 + 2 / 3) * z)'
#'((((a + b) * c) + 2) / 4))'
#'a + b ) * c ('
# str(input("Digite uma expressão: "))
brackets = list()
expr = '((a + b) * c)(x + y(3 + 2 / 3) * z)'

for char in expr:
    if char in '()':
        brackets.append(char)

openBrackets = brackets[:len(brackets) // 2]
closedBrackets = brackets[len(brackets) // 2:]

if len(openBrackets) == len(closedBrackets):
    if ')' in openBrackets or '(' in closedBrackets:
        print("A expressão não é válida")
    else:
        print("A expressão é válida.")
else:
    print("A expressãon não é válida.")

print(brackets)
print(openBrackets)
print(closedBrackets)


