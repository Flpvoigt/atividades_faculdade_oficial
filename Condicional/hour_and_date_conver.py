data_hora = input("Digite a data e hora (dd/mm/aa hh:mm): ")

dia = data_hora[0:2]
mes = int(data_hora[3:5])
ano = data_hora[6:8]
hora = data_hora[9:11]
minuto = data_hora[12:14]

match mes:
    case 1:
        mes_extenso = "janeiro"
    case 2:
        mes_extenso = "fevereiro"
    case 3:
        mes_extenso = "março"
    case 4:
        mes_extenso = "abril"
    case 5:
        mes_extenso = "maio"
    case 6:
        mes_extenso = "junho"
    case 7:
        mes_extenso = "julho"
    case 8:
        mes_extenso = "agosto"
    case 9:
        mes_extenso = "setembro"
    case 10:
        mes_extenso = "outubro"
    case 11:
        mes_extenso = "novembro"
    case 12:
        mes_extenso = "dezembro"
    case _:
        mes_extenso = "mês inválido"

print(f"{dia} de {mes_extenso} de 20{ano}, às {hora} horas e {minuto} minutos.")