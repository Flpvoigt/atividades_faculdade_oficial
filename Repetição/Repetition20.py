capital = float(input('Digite o capital inicial (valor investido): R$ '))
taxa_percentual = float(input('Digite a taxa de juros mensal em % (ex: 12 para 12%): '))
periodo = int(input('Digite o período do investimento (em meses): '))

taxa_juros = taxa_percentual / 100
montante = capital

print(f'\n--- Simulação de Juros Compostos ---')
print(f'Capital inicial: R$ {capital:.2f}')
print(f'Taxa de juros mensal: {taxa_percentual}%')
print(f'Período: {periodo} meses\n')

for mes in range(1, periodo + 1):
    juros = montante * taxa_juros
    montante += juros
    print(f'Mês {mes}: Juros = R$ {juros:.2f} | Montante = R$ {montante:.2f}')

print(f'\nMontante final após {periodo} meses: R$ {montante:.2f}')
print(f'Total de juros ganhos: R$ {montante - capital:.2f}')