'''def contador(i, f, p):
    """
    -> Faz um contador
    :param i: início da contagem
    :param f: final da contagem
    :param p: quanto pular
    """
    c = i
    while c <= f:
        print(f'{c}')
        c += p
    print('Fim')

contador(1, 50, 3)

help(contador)'''

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(4, 5)