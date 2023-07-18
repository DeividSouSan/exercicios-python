
from lin import *
from random  import randint

title("Vamos Jogar Par ou Ímpar: ", "=~", 25)

WIN_STREAK = 0

while True:
    # do {} while () 
    while True:
        lin('~', 50)
        choice = str(input("Par ou Ímpar? [PAR/IMPAR]: "))

        if choice.lower() == 'par' or choice.lower() == 'impar':
            break
        elif choice.isalnum() == True:
            print("Digite PAR ou IMPAR!")
            continue
        
    userValue = int(input("Digite um valor [0 -> 10]: "))

    lin('-', 50)

    computerValue = randint(0, 10)

    VALUES_SUM = userValue + computerValue
    NUMBER_RESULT = "par" if (VALUES_SUM) % 2 == 0 else "impar"

    print(f"Você jogou {userValue} e o computador jogou {computerValue}. A soma é {VALUES_SUM} um número {NUMBER_RESULT}.")

    if choice.lower() == NUMBER_RESULT:
        GAME_RESULT = 'Você VENCEU!'
        WIN_STREAK += 1
        print(f"{GAME_RESULT}")

    else:
        GAME_RESULT = 'Você PERDEU!'
        print(f"{GAME_RESULT}")
        break

lin('~', 50)
print(f"GAME OVER! Você venceu {WIN_STREAK} vezes.")
