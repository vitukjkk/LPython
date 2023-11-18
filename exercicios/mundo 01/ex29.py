vel = float(input('Insira a velocidade do veiculo: '))

if vel > 80:
    print(f'Você foi multado!\n\
    Valor da multa: ${(vel-80)*7}')


else: print('Tudo certo, boa viagem!')