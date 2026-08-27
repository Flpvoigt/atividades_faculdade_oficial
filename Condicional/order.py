a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b

print("Ordem crescente:", a, b, c)

