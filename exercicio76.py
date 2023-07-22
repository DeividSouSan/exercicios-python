

print("-"*50)
print(f"{'LISTAGEM DE PREÇOS':^50}")
print("-"*50)

shopItems = (
    f"{'Lápis':.<35} {'R$'} {'1.75':>10}",
    f"{'Borracha':.<35} {'R$'} {'2.00':>10}",
    f"{'Caderno':.<35} {'R$'} {'15.90':>10}",
    f"{'Estojo':.<35} {'R$'} {'25.00':>10}",
    f"{'Transferidor':.<35} {'R$'} {'4.20':>10}",
    f"{'Compasso':.<35} {'R$'} {'9.99':>10}",
    f"{'Mochila':.<35} {'R$'} {'120.32':>10}",
    f"{'Canetas':.<35} {'R$'} {'22.30':>10}",
    f"{'Livro':.<35} {'R$'} {'34.90':>10}",
)

for item in shopItems:
    print(item)