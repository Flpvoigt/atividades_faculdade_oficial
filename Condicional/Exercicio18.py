salario_minimo = float(input("Digite o valor do salário-mínimo: R$ "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
dependentes = int(input("Digite o número de dependentes: "))
horas_extras = float(input("Digite as horas extras trabalhadas: "))

valor_hora = salario_minimo / 5
salario_mes = horas_trabalhadas * valor_hora
valor_dependentes = dependentes * 32
valor_horas_extras = horas_extras * (valor_hora * 1.50)

salario_bruto = salario_mes + valor_dependentes + valor_horas_extras

match salario_bruto:
    case valor if valor < 200:
        percentual_irrf = 0
    case valor if valor <= 500:
        percentual_irrf = 0.10
    case _:
        percentual_irrf = 0.20

irrf = salario_bruto * percentual_irrf
salario_liquido = salario_bruto - irrf

print(f"\nValor da hora: R$ {valor_hora:.2f}")
print(f"Salário do mês: R$ {salario_mes:.2f}")
print(f"Valor dos dependentes: R$ {valor_dependentes:.2f}")
print(f"Valor das horas extras: R$ {valor_horas_extras:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"IRRF: R$ {irrf:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")