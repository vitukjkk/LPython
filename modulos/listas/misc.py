num = [1, 5, 7, 8]
print(num)
num[2] = 1
print(num)
num.append(12) # ADICIONA UM VALOR
print(num)
num.sort() # ORGANIZA
print(num)
num.sort(reverse = True) # ORGANIZA AO INVERSO
print(num)
num.insert(2, 0) # INSERE O SEGUNDO VALOR NA POSIÇÃO QUE FOI INDEXADA
print(num)
num.pop() # REMOVE O ULTIMO ELEMENTO num.pop(2) | ELIMINA O SEGUNDO ELEMENTO INDEXADO
print(num)
if 1 in num: num.remove(1)
else: print('nao achei o numero 4!')