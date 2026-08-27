a = float(input("Digite o valor da compra: "))

if a > 30 and a <= 100:
    x = (a / 100) * 5 
    y = a - x
    print(f"seu desconto foi de {x}, ficando com o valor da compra em {y}")

elif a > 100 and a <= 250:
     x = (a / 100) * 10 
     y = a - x
     print(f"seu desconto foi de {x}, ficando com o valor da compra em {y}")

else:
     x = (a / 100) * 15 
     y = a - x
     print(f"seu desconto foi de {x}, ficando com o valor da compra em {y}")