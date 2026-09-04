soma = 0
maior_salario = 0
menor_salario = 0

for funcionario in range(1, 11):
    salario = float(input(f'Digite o salário do funcionário {funcionario}: '))

    soma += salario

    if funcionario == 1:
        maior_salario = salario
        menor_salario = salario
    else:
        if salario > maior_salario:
            maior_salario = salario
        if salario < menor_salario:
            menor_salario = salario

media = soma / 10

print('\n--- Resultado Final ---')
print(f'Maior salário: R$ {maior_salario:.2f}')
print(f'Menor salário: R$ {menor_salario:.2f}')
print(f'Média salarial: R$ {media:.2f}')
print(f'Total dos salários: R$ {soma:.2f}')