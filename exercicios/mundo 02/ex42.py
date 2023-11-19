print('=-=' * 20)
print('Analisador de Triângulos v2.0')
print('=-=' * 20)

a = float(input('Insira o primeiro segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))

if a < b + c and b < c + a and c < a + b: 
    print('Eles podem formar um Triângulo!')
    if a == b and b == c: print('Este triângulo é EQUILÁTERO!')
    elif a != b and b != c: print('Este triângulo é ESCALENO!')
else: print('Não podem formar um Triângulo!')