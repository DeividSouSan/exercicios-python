"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão na ordem de colocação. Depois mostre:
- Os 5 primeiros
- Os últimos 4 colocados
- Times em ordem alfabética
- Em que posição está o time da Chapecoense
"""

clubRankings = (
    "Botafogo",
    "Flamengo",
    "Grêmio",
    "São Paulo",
    "Fluminense",
    "Palmeiras",
    "Bragantino",
    "Athletico-PR",
    "Fortaleza",
    "Cruzeiro",
    "Internacional",
    "Atlético-MG",
    "Cuiabá",
    "Santos",
    "Corinthians",
    "Bahia",
    "Goiás",
    "Coritiba",
    "Vasco da Gama",
    "América-MG"
)

print("Lista de times:", clubRankings)
print("Os últimos 4 colocados: ", clubRankings[len(clubRankings) - 4:])
print("Times em ordem alfabética: ", sorted(clubRankings))

try:
    print("Em que posição está o time da chapecoense:", clubRankings.index("Chapecoense") + 1)
except ValueError:
    print("O time da Chapecoense não está entre os 20 primeiro colocados.")
