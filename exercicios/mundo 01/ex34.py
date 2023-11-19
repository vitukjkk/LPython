sal = float(input('Insira seu salário (R$): '))

if sal > 1250:
    # 10 %
    sal = sal + (sal * 10 / 100)
else:
    # 15 %
    sal  = sal + (sal * 15 / 100)
print('O seu novo salário é: {:.2f}'.format(sal))