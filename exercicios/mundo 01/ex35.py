print('=-=' * 20)
print('Analisador de Triângulos')
print('=-=' * 20)

a = float(input('Insira o primeiro segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))

if a < b + c and b < c + a and c < a + b: print('Eles podem formar um Triângulo!')
else: print('Não podem formar um Triângulo!')