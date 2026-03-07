n1 = float(input('Digite o 1 valor: '))
n2 = float(input('Digite o 2 valor: '))

e = int(input('Escolha uma opção:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\nR: '))

while e != 5:
    if e == 1:
        print('\n' * 10)
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é {s}')
    elif e == 2:
        print('\n' * 10)
        m = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {m} !')
    elif e == 3:
        print('\n' * 10)
        if n1 > n2:
            print(f'O {n1} é maior que {n2}')
        else:
            print(f'O {n2} é maior que o {n1} !')
    elif e == 4:
        print('\n' * 15)
        n1 = float(input('Digite o 1 valor: '))
        n2 = float(input('Digite o 2 valor: '))
    else:
        print('\n' * 10)
        print('Erro ! O valor não foi reconhecido ou está errado !')
    e = int(input('Escolha uma opção:\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\nR: '))

print('Fim')