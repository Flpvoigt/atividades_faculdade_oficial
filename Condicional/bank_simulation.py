x = float(input("Entre com o saldo: "))
y = float(input("Entre com o valor de crédito: "))
z = float(input("Entre com o valor de retirada: "))

a1 = x + y

if z <= a1:
    af = a1 - z
    print(f"valor atual disponivel: {af}")

else:
    print("saldo indisponivel")
