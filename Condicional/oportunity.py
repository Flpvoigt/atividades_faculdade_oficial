x = float(input("Entre com o primeiro projeto: "))
y = float(input("Entre com o segundo projeto: "))

if x > y:
    z = x - y 
    print(f"Custo de oportunidade entre os projetos é {z}")

elif y > x:
    z = y - x 
    print(f"Custo de oportunidade entre os projetos é {z}")
    
else:
    print("Ambos possuem o mesmo valor")