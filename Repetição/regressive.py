minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = minutos * 60 + segundos

while total_segundos >= 0:
    minutos_atuais = total_segundos // 60
    segundos_atuais = total_segundos % 60

    print(f"{minutos_atuais:02d}:{segundos_atuais:02d}")

    total_segundos = total_segundos - 1