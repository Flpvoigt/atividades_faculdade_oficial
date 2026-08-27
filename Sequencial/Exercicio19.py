montante = float(input("Digite o montante: "))
taxa = float(input("Digite a taxa de rendimento (%): "))

rendimento = montante * taxa / 100
montante_final = montante + rendimento

print("Rendimento:", rendimento)
print("Montante final:", montante_final)