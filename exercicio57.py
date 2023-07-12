"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
while True:
    try:
        sexoPessoa = str(input("Insira o seu sexo, para masculino M e feminino F: "))
        if sexoPessoa.lower() == 'm' or sexoPessoa.lower() == 'f':
            break
        else:
            raise Exception('Caractere de sexo inválido!')
    except Exception as err:
        print(err)

print("Obrigado! Essa informação será útil.")
