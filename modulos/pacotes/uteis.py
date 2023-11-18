def soma(a = 0, b = 0, c = 0):
    r = a + b + c
    return r

def mult(a, b, c = 0):
    r = a * b * c
    return r

num = int(input('Insira um número: '))
numo = int(input('Insira outro número: '))
numt = int(input('Insira outro número: '))
print(f'a soma desses números valem: {soma(num, numo, numt)}')
print(f'a multiplicação desses números valem: {mult(num, numo, numt)}')

