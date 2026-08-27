Primeiro_projeto = float(input("Entre com o primeiro projeto: "))
segundo_projeto = float(input("Entre com o segundo projeto: "))

if Primeiro_projeto > segundo_projeto:
    z = Primeiro_projeto - segundo_projeto 
    print(f"Custo de oportunidade entre os projetos é {z}")

elif segundo_projeto > Primeiro_projeto:
    z = segundo_projeto - Primeiro_projeto 
    print(f"Custo de oportunidade entre os projetos é {z}")
    
else:
    print("Ambos possuem o mesmo valor")