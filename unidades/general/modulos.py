# import biblioteca
# from biblioteca import pacote

import math

num = float(input("insira um número: "))
raiz = math.sqrt(num)
print("o resultado é: {}".format(math.floor(raiz)))
print("a aproximação positiva do número é: {}".format(math.ceil(num)))
print("a aproximação negativa do número é: {}".format(math.floor(num)))

import random
print("um número aleatório: {}".format(random.randint(1, 100)))