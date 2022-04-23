# 06 Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n3 < n1:
    print(f"O maior número foi {n1}")
elif n2 > n1 and n3 < n2:
    print(f"O maior número foi {n2}")
elif n3 > n1 and n2 < n3:
    print(f"O maior número foi {n3}")
else:
    print("Nenhum dos três número foi o maior")