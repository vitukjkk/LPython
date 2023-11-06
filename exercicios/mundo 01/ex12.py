desc = float(input("insira o preço em R$:"))
porc = int(input("insira a porcentagem:"))
print("com o desconto de {}%, fica: {}".format(porc, desc * porc / 100))