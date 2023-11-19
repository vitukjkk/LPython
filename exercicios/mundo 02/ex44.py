print('=-=' * 20)
print('STORE - HARMONIA PLACE')
print('=-=' * 20)

valor = float(input('Insira o valor do produto: R$'))

print('FORMAS DE PAGAMENTO\n\
[1] Dinheiro (10% desconto)\n\
[2] À vista no cartão (5% desconto)\n\
[3] 2x no cartão\n\
[4] 3x no cartão (20% juros)')

pgt = int(input('Insira a forma de pagamento: '))

match pgt:
    case 1: print(f'Preço do produto: {valor}\nVocê pagará: R${valor - (valor * 10 / 100)}')
    case 2: print(f'Preço do produto: {valor}\nVocê pagará: R${valor - (valor * 5 / 100)}')
    case 3: print(f'Preço do produto: {valor}\nVocê pagará: R${valor}')
    case 4: print(f'Preço do produto: {valor}\nVocê pagará: R${valor + (valor * 20 / 100)}')