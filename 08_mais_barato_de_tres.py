# Esse programa solicita o preço de três produtos e escolhe o mais barato para comprar

nome01 = input("Digite o nome do produto: ")
produto01 = float(input("Digite  o preço do produto: "))

nome02 = input("Digite o nome do segundo produto: ")
produto02 = float(input("Digite  o preço do segundo produto: "))

nome03 = input("Digite o nome do terceiro produto: ")
produto03 = float(input("Digite  o preço  terceiro produto: "))


if produto01 > produto02 and produto02 > produto03:
    print("Você deve comprar \"{}\" esse é o produto mais barato, custando R$ {:.2f}".format(nome03, produto03))
elif produto01 > produto03 and produto03 > produto02:
    print("Você deve comprar \"{}\" esse é o produto mais barato, custando R$ {:.2f}".format(
        nome02, produto02))
elif produto03 > produto01 and produto02 > produto01:
    print("Você deve comprar \"{}\" esse é o produto mais barato, custando R$ {:.2f}".format(
        nome01, produto01))
else:
    print("Escolha o que você mais gosta")
    print("{} R$ {:.2f}}".format(nome01, produto01))
    print("{} R$ {:.2f}}".format(nome02, produto02))
    print("{} R$ {:.2f}}".format(nome03, produto03))
