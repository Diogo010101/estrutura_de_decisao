#11 Reajuste de salário

salario = float(input("Digite o salário: "))
if salario >= 0.0 and salario <= 280.00:
    reajuste = salario * 20 / 100
    novoSalario = salario + reajuste
    print ("Salario anterior R$ {:.2f}".format(salario))
    print("O percentual de aumento foi de 20%")
    print("O valor de reajuste é R$ {:.2f}".format(reajuste))
    print("Salario atualizado R$ {:.2f}".format(novoSalario))
elif salario > 280.00 and salario <=700.00:
    reajuste = salario * 15 / 100
    novoSalario = salario + reajuste
    print("Salario anterior R$ {:.2f}".format(salario))
    print("O percentual de aumento foi de 15%")
    print("O valor de reajuste é R$ {:.2f}".format(reajuste))
    print("Salario atualizado R$ {:.2f}".format(novoSalario))
elif salario >700.00 and salario <= 1500.00:
    reajuste = salario * 10 / 100
    novoSalario = salario + reajuste
    print("Salario anterior R$ {:.2f}".format(salario))
    print("O percentual de aumento foi de 10%")
    print("O valor de reajuste é R$ {:.2f}".format(reajuste))
    print("Salario atualizado R$ {:.2f}".format(novoSalario))
elif salario >1500.00:
    reajuste = salario * 5 / 100
    novoSalario = salario + reajuste
    print("Salario anterior R$ {:.2f}".format(salario))
    print("O percentual de aumento foi de 5%")
    print("O valor de reajuste é R$ {:.2f}".format(reajuste))
    print("Salario atualizado R$ {:.2f}".format(novoSalario))
else:
    print("Verifique os valores digitados")


    