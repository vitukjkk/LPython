# LISTAS SÃO MUTÁVEIS!

lanche = ['pao', 'pizza', 'ovo', 'carne']
print(lanche)
lanche[2] = 'pudim'
print(lanche)

if 'pizza' in lanche:
    lanche.remove('pizza') 
print(lanche)