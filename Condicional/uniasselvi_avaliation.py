nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 <= nota2 and nota1 <= nota3:
    maior1 = nota2
    maior2 = nota3
elif nota2 <= nota1 and nota2 <= nota3:
    maior1 = nota1
    maior2 = nota3
else:
    maior1 = nota1
    maior2 = nota2

media = (maior1 + maior2) / 2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")