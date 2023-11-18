try:
    a = int(input('Insira um número: '))
    b = int(input('Insira outro número: '))
    c = a / b
except (ValueError, TypeError): print('Voce deve digitar um número!')
except ZeroDivisionError: print('Voce nao pode dividir por 0!')
else:
    print(f'O resultado é {c}')
finally: print('volte sempre!')