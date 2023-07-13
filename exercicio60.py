

from time import sleep
numero = int(input("Digite um número: "))

print(f"O fatorial de {numero} é:", end=" ")

# Formata no terminal o processo do fatorial
for i in range(numero, 0, -1):
    sleep(0.5)
    print(f"{i}", end=" ", flush=True)

    if (i == 1):
        sleep(1)
        print("=", end=" ", flush=True)
    else: 
        print("*", end=" ", flush=True)

# Cálcula o fatorial
for i in range((numero - 1), 0, -1):
    numero *= i

sleep(0.5)
print(numero)