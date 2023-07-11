

somaIdades = 0
mediaIdade = 0
homemMaisVelho = {'nome': '', 'idade': 0}
mulheresMenosDeVinte = 0

for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nomePessoa = str(input("Nome: "))
    idadePessoa = int(input("Idade: "))
    sexoPessoa = str(input("Sexo [M/F]: "))

    somaIdades += idadePessoa

    if  sexoPessoa.lower() == 'm' and idadePessoa > homemMaisVelho['idade']:
        homemMaisVelho = {'nome': nomePessoa, 'idade': idadePessoa}
    
    if sexoPessoa.lower() == 'f' and idadePessoa < 20:
        mulheresMenosDeVinte += 1

mediaIdade = somaIdades / 4

print(f"\nA média de idade do grupo é de {mediaIdade} anos.\nO homem mais velho tem {homemMaisVelho['idade']} anos e se chama {homemMaisVelho['nome']}.\nAo todo são {mulheresMenosDeVinte} mulheres com menos de 20 anos.")
