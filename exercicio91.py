"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guade esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep 

players = {
            'player1': None,
            'player2': None,
            'player3': None,
            'player4': None
        }

players['player1'] = randint(1, 6)
players['player2'] = randint(1, 6)
players['player3'] = randint(1, 6)
players['player4'] = randint(1, 6)

playersRanking = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))

print(playersRanking)
