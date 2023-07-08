"""

"""
from cprint import *
num = int(input("Digite um número: "))


divisoes = 0

for i in range(num, 0, -1):
    if num % i == 0:
        cprint(f"!{i}!", C_WHITE, BG_GREEN, end=" ")
        divisoes += 1;
    else:
        cprint(f"!{i}!", C_RED, end=" ")

    EH_PRIMO = True if divisoes == 2 else False

print(f"\nO número {num} é primo") if EH_PRIMO == True else print(f"\nO número {num} não é primo.")
# NÃO TERMINADO