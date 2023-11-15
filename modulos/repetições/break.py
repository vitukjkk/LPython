n = s = 1
while n != 999:
    n = int(input('Digite um número: '))
    s += 1
    if n == 999:
        break
print(f'fim do programa! Números digitados: {s}')