x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - potência")
opcao = int(input("Digite a opção: "))

match opcao:
    case 1:
        resultado = x + y
        print(f"{x} + {y} = {resultado}")
    case 2:
        resultado = x - y
        print(f"{x} - {y} = {resultado}")
    case 3:
        multiplicacao = 0

        for i in range(1, y + 1):
            novo_valor = multiplicacao + x
            print(f'{multiplicacao} + {x} = {novo_valor}')
            multiplicacao = novo_valor

        print(f'\nA multiplicação de {x} por {y} é: {multiplicacao}')
    case 4:
        if y == 0:
            print("Não é possível dividir por zero.")
        else:
            resto = x
            divisao = 0
            for i in range(1, (x) + 1):
                if resto < y:
                    break

                novo_valor = resto - y
                print(f"{resto} - {y} = {novo_valor}")

                resto = novo_valor
                divisao += 1

            print(f"Resultado da divisão: {divisao}")
            print(f"Resto da divisão: {resto}")
    case 5:
        potencia = 1

        for i in range(1, y + 1):
            multiplicacao = 0

            print(f"\n{potencia} x {x}:")

            for j in range(1, x + 1):
                novo_valor = multiplicacao + potencia
                print(f"{multiplicacao} + {potencia} = {novo_valor}")
                multiplicacao = novo_valor

            potencia = multiplicacao

        print(f"\n{x} elevado a {y} = {potencia}")