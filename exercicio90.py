"""
Faça um programa  que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

studentInfo = {
    'nome': '',
    'media': 0,
    'situacao': ''
}

studentInfo['nome'] = str(input('Nome: '))

# VERFIFICANDO SE O NÚMERO É VÁLIDO
while True:
    studentInfo['media'] = float(input('Média: '))
    if 0 <= studentInfo['media'] <= 10:
        break
    else:
        print("Digite um número real entre 0 e 10!")

# VERIFICANDO O STATUS DO ESTUDANTE
if studentInfo['media'] <= 5:
    studentInfo['situacao'] = 'REPROVADO'
elif studentInfo['media'] < 7:
    studentInfo['situacao'] = 'RECUPERAÇÃO'
else: 
    studentInfo['situacao'] = 'APROVADO'

# MOSTRANDO AS INFORMAÇÕES DO DICIONÁRIO
print('=~'*25)
print(f"O Nome do Aluno é {studentInfo['nome']}")
print(f"A Média é {studentInfo['media']}")
print(f"A Situação é {studentInfo['situacao']}")
print('=~'*25)
