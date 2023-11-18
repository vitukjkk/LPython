name = str(input('Insira seu nome: ')).strip()

print(f'Seu nome em maiúsculas é: {name.upper()}')
print(f'Seu nome em minúsculas é: {name.lower()}')
print(f'O tamanho do seu nome é: {name.__len__() - name.count(" ")}')
