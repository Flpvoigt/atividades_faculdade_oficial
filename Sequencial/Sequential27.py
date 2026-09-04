consumo_watts = float(input("Digite o consumo de watts por hora: "))
tempo_hh = float(input("Digite a quantidade de horas diárias: "))
consumo_dd = float(input("Digite a quantidade dias: "))

consumo_mm = consumo_watts * tempo_hh * consumo_dd

print(f"seu consumo mensal sera de {consumo_mm}")