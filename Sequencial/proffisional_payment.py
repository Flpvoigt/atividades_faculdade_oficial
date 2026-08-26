x = float(input("quantidade de horas: "))
y = float(input("quantidade de extras: "))
z = float(input("valor da hora: "))
a = float(input("total de discontos: "))


a1 = ((x * z) + (y * z * 1.5)) * (1 - a / 100)
print(a1)