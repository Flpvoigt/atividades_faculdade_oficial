vista = 0
prazo_30 = 0
prazo_60 = 0

for cliente in range(1, 11):
    print(f'\nCliente {cliente}')
    print('1 - À vista')
    print('2 - 30 dias')
    print('3 - 60 dias')
    opcao = int(input('Digite a opção de compra: '))

    if opcao == 1:
        vista += 1
    elif opcao == 2:
        prazo_30 += 1
    elif opcao == 3:
        prazo_60 += 1
    else:
        print('Opção inválida!')

print('\n--- Resultado Final ---')
print(f'Clientes que compraram à vista: {vista}')
print(f'Clientes que compraram com 30 dias: {prazo_30}')
print(f'Clientes que compraram com 60 dias: {prazo_60}')
print()