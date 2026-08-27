valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite um outro número: "))
valor3 = float(input("Digite um outro número: "))

resultado = (valor1 + valor2 + valor3) / 3
ponderada = (valor1 * 1 + valor2 * 2 + valor3 * 3) / 6

print(f"sua média ponderada é: {ponderada:.2F}") # esse :.2f serve para formatar os valore e deixar apenas duas casas decimasi depois da virgula Ex: 2.80
print(f"sua média aritmética é: {resultado:.2F}")