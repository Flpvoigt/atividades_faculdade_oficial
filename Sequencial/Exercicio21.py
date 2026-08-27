x = int(input("Digite a quantidade de minutos: "))

hh = x // 60
mm = x % 60

print(f"{hh:02d}:{mm:02d}") #esse 02d é pra deixar padrao do relogio 00:00
