nome1 = input("Digite o nome do primeiro país: ")
ouro1 = int(input("Quantidade de medalhas de ouro: "))
prata1 = int(input("Quantidade de medalhas de prata: "))
bronze1 = int(input("Quantidade de medalhas de bronze: "))
pontos1 = ouro1 * 3 + prata1 * 2 + bronze1

nome2 = input("\nDigite o nome do segundo país: ")
ouro2 = int(input("Quantidade de medalhas de ouro: "))
prata2 = int(input("Quantidade de medalhas de prata: "))
bronze2 = int(input("Quantidade de medalhas de bronze: "))
pontos2 = ouro2 * 3 + prata2 * 2 + bronze2

nome3 = input("\nDigite o nome do terceiro país: ")
ouro3 = int(input("Quantidade de medalhas de ouro: "))
prata3 = int(input("Quantidade de medalhas de prata: "))
bronze3 = int(input("Quantidade de medalhas de bronze: "))
pontos3 = ouro3 * 3 + prata3 * 2 + bronze3

# Coloca os países em ordem decrescente de pontos
if pontos1 < pontos2:
    pontos1, pontos2 = pontos2, pontos1
    nome1, nome2 = nome2, nome1

if pontos1 < pontos3:
    pontos1, pontos3 = pontos3, pontos1
    nome1, nome3 = nome3, nome1

if pontos2 < pontos3:
    pontos2, pontos3 = pontos3, pontos2
    nome2, nome3 = nome3, nome2

print("\nClassificação:")
print("1º lugar:", nome1, "-", pontos1, "pontos")
print("2º lugar:", nome2, "-", pontos2, "pontos")
print("3º lugar:", nome3, "-", pontos3, "pontos")