x = int(input('Digite a base: '))
y = int(input('Digite o expoente: '))
resultado = 1

for i in range(1, y + 1):
    novo_valor = resultado * x
    print(f'{resultado} x {x} = {novo_valor}')
    resultado = novo_valor

print(f'\n{x} elevado a {y} é: {resultado}')