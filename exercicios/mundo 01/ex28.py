from random import randint
from time import sleep

print('=-=' * 20)
print('Vou pensar em um número de 0-5, tente advinhar qual é!')
print('=-=' * 20)

num = int(input('Insira o número: '))
ns = randint(0, 5)
print('PROCESSANDO...')
sleep(3)

if ns == num:
    print('Parabéns!! Você acertou.\n\
    Você me venceu dessa vez...')
else: 
    print(f'Você errou!! Tente novamente :)\n\
O número que pensei foi: {ns}')