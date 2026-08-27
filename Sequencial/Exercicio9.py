preco_de_compra = float(input("Digite o preco de compra: "))
Percentual_de_lucro = float(input("Digite o percentual de lucro: "))

calculo1 = (preco_de_compra / 100) * Percentual_de_lucro
resultado = preco_de_compra + calculo1

print(f"preco venda é igual a: {resultado}")
