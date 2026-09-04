x = int(input('Digite um número: '))

print(f'\nTabuada de {x}:')
for i in range(1, 11):
    resultado = x * i
    print(f'{x} x {i} = {resultado}')