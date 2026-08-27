dividendo = int(input("Digite o primeiro número: "))
divisor = int(input("Digite o segundo número: "))

if dividendo < 0 or divisor <= 0:
    print("Digite um dividendo positivo e um divisor maior que zero.")
else:
    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor
        quociente = quociente + 1

    print("Quociente:", quociente)
    print("Resto:", resto)