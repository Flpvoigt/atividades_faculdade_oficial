a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Potenciação:", a ** b)

if b != 0:
    print("Divisão:", a / b)
    print("Parte inteira:", a // b)
    print("Resto:", a % b)
    print("Raiz:", a ** (1 / b))
else:
    print("Não é possível dividir ou calcular raiz usando zero.")