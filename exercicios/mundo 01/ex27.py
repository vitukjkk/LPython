nome = str(input('Insira seu nome: ')).strip()

n = nome.split()
print(f'Analisando...\n\
Prazer em te conhecer {nome}!\n\
Seu primeiro nome é: {n[0]}\n\
Seu último nome é: {n[-1]}\
')
