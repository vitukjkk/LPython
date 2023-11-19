casa = float(input('Insira o valor da casa: '))
sal = float(input('Insira o valor do seu salário: '))
ano = int(input('Insira em quantos anos você deseja pagar: '))

preço = casa / (ano * 12)
pres = sal * 30 / 100

if preço >= pres: 
    print(f'Para financiar essa casa em {ano} ano(s), o valor da prestação seria: R${preço} por mês.\n\
Empréstimo NEGADO!')
else: print('Empréstimo CONCEDIDO!')