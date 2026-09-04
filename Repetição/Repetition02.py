total = 0
x = int(input("Digite um número inteiro de 1 a 10: "))

if 1 <= x <= 10:
    total = 1

    for numero in range(1, x + 1):
        total = total * numero

    print(f"{x}! = {total}")
else:
    print("Número inválido")
