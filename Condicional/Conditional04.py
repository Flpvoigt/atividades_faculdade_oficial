primeira_nota = float(input("Entre com a primeira nota: "))
segunda_nota = float(input("Entre com a segunda nota: "))

media = (primeira_nota * 4 + segunda_nota * 6) / 10

if media >= 7:
    print("Aprovado")

else:
    print("Reprovado")