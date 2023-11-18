def contador(i, f, p):
    """
    i = inicio da contagem
    f = fim da contagem
    p = passo da contagem
    """
    while i <= f:
        i += p
        print(i)
    else: print('fim do programa!')

contador(1, 10, 2)