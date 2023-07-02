"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para salários infeiores ou iguais, o aumento é de 15%.
"""

salarioAtual = float(input("Qual é o salário do fucnionário? R$ "))

salarioAlto = salarioAtual > 1250

porcetagemAumento = 0.10 if salarioAlto else 0.15

salarioNovo = salarioAtual + (salarioAtual * porcetagemAumento)

print(f"Quem ganhava R$ {salarioAtual:.2f} passa a ganhar R$ {salarioNovo:.2f} agora.")