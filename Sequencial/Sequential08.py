variavel_a = input("Digite o valor de A: ")
variavel_b = input("Digite o valor de B: ")

auxiliar = variavel_a
variavel_a = variavel_b
variavel_b = auxiliar

print("Novo valor de A:", variavel_a)
print("Novo valor de B:", variavel_b)