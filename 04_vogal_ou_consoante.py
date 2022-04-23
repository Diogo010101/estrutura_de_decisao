# 04 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogal = "a" and "e" and "i" and "o" and "u"
letra = input("Digite uma letra: ")
if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U":
    print(f"A letra {letra} é uma vogal")
elif letra.upper() == "B" or letra.upper() == "C" or letra.upper() == "D" or letra.upper() == "F" or letra.upper() == "G" or letra.upper() == "H" or letra.upper() == "J" or letra.upper() == "K" or letra.upper() == "L" or letra.upper() == "M" or letra.upper() == "N" or letra.upper() == "P" or letra.upper() == "Q" or letra.upper() == "R" or letra.upper() == "S" or letra.upper() == "T" or letra.upper() == "V" or letra.upper() == "W" or letra.upper() == "X" or letra.upper() == "Y" or letra.upper() == "Z":
        print(f"A letra {letra} é uma Consoante")
else:
    print("Opção inválida")
