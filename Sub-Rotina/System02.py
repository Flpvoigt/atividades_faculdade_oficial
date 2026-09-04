
cpf = input("Digite os 11 números do CPF: ")

quantidade = 0

for numero in cpf:
    quantidade += 1

if quantidade != 11:
    print("CPF inválido.")

else:
    iguais = True

    for i in range(1, 11):
        if cpf[i] != cpf[0]:
            iguais = False

    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if iguais:
        print("CPF inválido.")
    elif digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        print("CPF válido.")
    else:
        print("CPF inválido.")
