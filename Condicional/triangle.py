a = float(input("Digite o valor1 : "))
b = float(input("Digite o valor2: "))
c = float(input("Digite o valor3: "))


if a + b > c and a + c > b and b + c > a:
    if a == b and b == c and c == a :
        print("Equilátero")

    elif a == b or a == c or b == c:
        print("Isóceles")

    else:
        print("Escaleno")

else:
    print("error")



