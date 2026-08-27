saldo = float(input("Entre com o saldo: "))
credito = float(input("Entre com o valor de crédito: "))
retirada = float(input("Entre com o valor de retirada: "))

a1 = saldo + credito

if retirada <= a1:
    af = a1 - retirada
    print(f"valor atual disponivel: {af}")

else:
    print("saldo indisponivel")
