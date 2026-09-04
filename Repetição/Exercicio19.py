valor_imovel = float(input('Digite o valor do imóvel: R$ '))
num_parcelas = int(input('Digite o número de parcelas: '))
taxa_juros_percentual = float(input('Digite a taxa de juros mensal em % (ex: 3 para 3%): '))
taxa_juros = taxa_juros_percentual / 100

amortizacao = valor_imovel / num_parcelas
saldo_devedor = valor_imovel

print('\n--- Simulação SAC ---')
print(f'Valor do imóvel: R$ {valor_imovel:.2f}')
print(f'Número de parcelas: {num_parcelas}')
print(f'Taxa de juros mensal: {taxa_juros * 100}%')
print(f'Amortização (fixa): R$ {amortizacao:.2f}\n')

for parcela in range(1, num_parcelas + 1):
    juros = saldo_devedor * taxa_juros
    prestacao = amortizacao + juros
    saldo_devedor -= amortizacao

    print(f'Parcela {parcela}: Prestação = R$ {prestacao:.2f} | Juros = R$ {juros:.2f} | Amortização = R$ {amortizacao:.2f} | Saldo devedor = R$ {saldo_devedor:.2f}')