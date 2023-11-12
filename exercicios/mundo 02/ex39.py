idade = int(input('Insira sua idade: '))

if idade < 18:
    print('Voce ainda precisa se alistar!')
    print('Faltam {} ano(s) para voce se alistar!'.format(18 - idade))
elif idade > 18:
    print('Voce ja se alistou há {} ano(s)!'.format(idade - 18))
    print('Parabéns!')
else:
    print('Voce tem 18 anos, esta na hora de se alistar!')