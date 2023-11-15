pessoas = {'Nome':'vitor', 'Idade':'19', 'Sexo':'M'}
print(pessoas.keys())   # MOSTRA AS CHAVES
print(pessoas.items())  # MOSTRA TUDO
print(pessoas.values()) # MOSTRA OS VALORES

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('fim')