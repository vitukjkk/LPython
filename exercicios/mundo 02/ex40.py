n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1 + n2) / 2

if media < 6: print('Você está REPROVADO!')
elif media == 6: print('Você está de RECUPERAÇÃO!')
else: print('Você foi APROVADO!')
print(f'Sua média foi: {media}')