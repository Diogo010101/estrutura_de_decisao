# 02 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("Digite um número qualquer: "))
if valor >=0:
    print("O número {:.2f} é positivo".format(valor))
else:
    print("O valor {:.2f} é negativo".format(valor))

    