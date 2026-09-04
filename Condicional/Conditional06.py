x = float(input("Entre com o valor1: "))
y = float(input("Entre com o valor2: "))
z = input("+, -, *, /, **:  ")

match z:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case "**":
        print(x ** y)    