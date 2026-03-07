'''def linha():
    print('-' * 30)
    
linha()
print('Oi' .center(30, " "))
linha()'''

'''def linha(msg):
    print('-' * 30)
    print(msg .center(30, " "))
    print('-' * 30)


linha('Batman')'''


'''def soma(n1, n2):
    s = n1 + n2
    print(f'A soma é {s}')

soma(int(input('Digite o n1:')), int(input('Digite o n2:')))'''

def contador(*n):
    s = 0
    for c in lista:
        s += int(c)
    print(f'A soma é {s}')

lista = list()

while True:
    m = input('Digite um número ou digite S para sair: ')
    if m == 'S':
        break
    else:
        lista.append(m)

contador(lista)

