print('Escolha a base do número que deseja converter:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Digite a opção: '))

if opcao == 1:
    numero = input('Digite o número binário: ')
    base = 2
elif opcao == 2:
    numero = input('Digite o número octal: ')
    base = 8
elif opcao == 3:
    numero = input('Digite o número hexadecimal: ')
    base = 16
else:
    print('Opção inválida!')
    base = 0

if base != 0:
    numero = numero.upper()
    decimal = 0
    tamanho = len(numero)

    for i in range(tamanho):
        digito = numero[i]

        if digito.isdigit():
            valor_digito = int(digito)
        else:
            valor_digito = ord(digito) - ord('A') + 10

        posicao = tamanho - 1 - i
        decimal += valor_digito * (base ** posicao)

    print(f'{numero} na base {base} equivale a {decimal} em decimal')