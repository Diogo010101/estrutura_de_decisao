# 03 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Digite 'F' para Feminino ou 'M' para Masculino ")
if sexo.upper() == "F":
    print("O sexo escolhido foi \"Feminino\" ")
elif sexo.upper() == "M":
    print("O sexo escolhido foi \"Mesculino\" ")
else:
    print("Opção inválida")