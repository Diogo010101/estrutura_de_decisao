# 05 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
# A mensagem "Reprovado", se a média for menor do que sete
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota_01 = float(input("Digite a nota do primeiro semestre: "))
nota_02 = float(input("Digite a nota do segundo semestre: "))
media = (nota_01 + nota_02) / 2
if media >= 7:
    print("Aprovado(a)")
elif media < 7:
    print("Reprovado(a)")
elif media == 10:
    print("Aprovado(a) com Distinção")
else:
    print("Nota inválida! Verifique os valores digitados.")