n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

if not n1.isnumeric():
    print(f'{n1} não é um número !')
elif not n2.isnumeric():
    print(f'{n2} não é um número !')
else:
    s = int(n1) + int(n2)
    print(f'A soma entre {n1} e {n2} é {s}')
