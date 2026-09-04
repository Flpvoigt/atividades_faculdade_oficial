total1 = 0
total2 = 0
total3 = 0
total_nulo = 0 

while True:
    print("1 - Leo Stronda, 2 - Davy Jones, 3 - The Rock ")
    candidatos = input("Digite apenas o número: ").upper()

    match candidatos:
        case "1":
            total1 = total1 + 1

        case "2":
            total2 = total2 + 1

        case "3":
            total3 = total3 + 1

        case _ :
            total_nulo = total_nulo + 1

    if total1 > total2 and total1 > total3:
        print()
        print(f"{total1} - voto registrado para Leo Stronda")

    elif total2 > total1 and total2 > total3:
        print()
        print(f"{total2} - voto registrado para Davy Jones")
    elif total3 > total1 and total3 > total2:
        print()
        print(f"{total3} - voto registrado para The Rock")

    else:
        print(f"{total_nulo} - Votos nulos")
    
    if input("Deseja votar novamente (s/n): ") != "n".lower():
            if total1 > total2 and total1 > total3:
                print(f"Leo Stronda venceu com: {total1} votos")
        
            elif total2 > total1 and total2 > total3:
                print(f"Davy Jones venceu com:{total2} votos")
            elif total3 > total1 and total3 > total2:
                print(f"The Rock venceu com: {total3} votos")

            else:
                print(f"A maioria dos votos foram nulo: {total_nulo} votos nulos")
            break
    

