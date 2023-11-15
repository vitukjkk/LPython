pessoas = list()

n = int(input('insira o número de pessoas a cadastrar: '))
for c in range (0, n):
    name = input('Insira o nome da pessoa: ')
    idade = int(input('Insira a idade dessa pessoa: '))
    print(f'Pessoa cadastrada: {name}, {idade} anos')
print(f'Número de pessoas cadastradas: {c}')