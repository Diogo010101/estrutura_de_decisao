# 07 Esse Programa lê três números e mostra o maior e o menor deles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num3 < num2:
    maior = num1
    menor = num3
    print("Maior {} Menor {}".format(maior, menor))
elif num3 > num1 and num2 < num1:
    maior = num3
    menor = num2
    print("Maior {} Menor {}".format(maior, menor))
elif num2 > num1 and num3 < num1:
    maior = num2
    menor = num3
    print("Maior {} Menor {}".format(maior, menor))
elif num3 > num2 and num1 < num2:
    maior = num3
    menor = num1
    print("Maior {} Menor {}".format(maior, menor))
elif num2 > num3 and num1 < num3:
    maior = num2
    menor = num1
    print("Maior {} Menor {}".format(maior, menor))
else:
    print("Digite número diferentes")