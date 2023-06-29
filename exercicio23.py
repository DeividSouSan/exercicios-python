num = int(input("Digite um número: "))

unidade = num % 10
dezena = int(((num % 100) - unidade) / 10)
centena = int(((num % 1000) - dezena - unidade) / 100)
milhar = int(((num % 10000) - centena - dezena - unidade) / 1000)

print(f"Unidade: {unidade}.\n\
Dezena: {dezena}.\n\
Centena: {centena}.\n\
Milhar: {milhar}.")