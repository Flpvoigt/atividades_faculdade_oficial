produtos = []
a = float(input("Digite o preço do produto 1: "))
b = float(input("Digite o preço do produto 2: "))
c = float(input("Digite o preço do produto 3: "))
d = float(input("Digite o preço do produto 4: "))
e = float(input("Digite o preço do produto 5: "))
f = float(input("Digite o preço do produto 6: "))
g = float(input("Digite o preço do produto 7: "))
h = float(input("Digite o preço do produto 8: "))

produtos.append(a)
produtos.append(b)
produtos.append(c)
produtos.append(d)
produtos.append(e)
produtos.append(f)
produtos.append(g)
produtos.append(h)

total = 0

for produto in produtos:
    total = total + produto

print(total)