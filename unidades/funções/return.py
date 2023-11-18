def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'a soma vale {s}')
    return s

resp = 0
resp += somar(1, 2, 3)
resp += somar(9, 5, 4)
resp += somar(1, 3, 7)
print(resp)