a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificar qual é maior
if a > b and a > c: maior = a
if b > a and b > c: maior = b
if c > a and c > b: maior = c

# Verificar qual é menor
if a < b and a < c: menor = a
if b < a and b < c: menor = b
if c < a and c < b: menor = c

print(f'O menor valor digitado foi: {menor}\n\
O maior valor digitado foi: {maior}')