x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
soma = 0

for i in range(1, y + 1):
    novo_valor = soma + x
    print(f'{soma} + {x} = {novo_valor}')
    soma = novo_valor

print(f'\nA soma de {x} repetido {y} vezes é: {soma}')