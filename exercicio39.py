"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
from cprint import *

anoNascimento = int(input("Ano de Nascimento: "))

anoAlistamento = anoNascimento + 18
anoAtual = date.today().year
idade = anoAtual - anoNascimento

cprint(f"Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}.")

if anoAlistamento > anoAtual:
    tempoAteAlistamento = anoAlistamento - anoAtual
    cprint("Ainda faltaM !2 ano(s)! para o alistamento.", BOLD, C_BLUE)
    cprint(f"Seu alistamento será em !{anoAlistamento}!.", BOLD, C_RED)
elif anoAlistamento < anoAtual:
    tempoAteAlistamento = anoAtual - anoAlistamento
    cprint(f"Você já deveria ter se alistado há !{tempoAteAlistamento} ano(s)!", BOLD, C_YELLOW)
    cprint(f"Seu alistamento foi em !{anoAlistamento}!.", BOLD, C_RED)
else:
    cprint("Você tem que se alistar !IMEDIATAMENTE!.", BOLD, C_RED)