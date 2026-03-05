ano = int(input('Digite o ano: '))

d = ano%4

if d == 0:
    print('Ano bissexto !')
else:
    print('Não é bissexto !')