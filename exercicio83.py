"""
Crie um programa que o usuário digite uma expressão qualquer que use parenteses. Seu programa deverá análisar se a expessão passada está com os parênteses abertos e fechados na ordem correta.
"""

#'(a + b * (c + (z - y)))'
#'(a + (c + (z - y) + w)))'
#'((a + b) * c)(x + y(3 + 2 / 3) * z)'
#'((((a + b) * c) + 2) / 4))'
#'a + b ) * c ('

bracketStack = list()
expr = str(input("Digite uma expressão: "))

for symbol in expr:
    if symbol == '(':
        bracketStack.append('(')
    elif symbol == ')':
        if len(bracketStack) > 0:
            bracketStack.pop()
        else:
            bracketStack.append(')')

if len(bracketStack) == 0:
    print("A expressão é válida.")
else:
    print("A expressão não é válida devido aos símbolos sem pares: ", bracketStack)
    
"""
Cada caractere da pilha vai ser percorrido, quando o caracterefor ( ele é adicionado na pilha, se o símbolo encontrado for ) ele verifica se tem algo na pilha, se houver então ele remove o último ( adiionado, caso não haja nada significa que aquele ( não tem par.
""" 



