valor_real = float(input("Digite seu valor em real: "))

dolar = valor_real * 5.15
euro = valor_real * 6.01
libra = valor_real * 7.01

print(f"O valor de {valor_real} convertido para moedas estrangeiras fica: \ndolar: {dolar:.2f} \neuro: {euro:.2f} \nlibra: {libra:.2f}")