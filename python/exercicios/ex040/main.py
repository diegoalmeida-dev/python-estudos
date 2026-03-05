n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

m = (n1+n2)/2

if m < 5.0:
    print('Reprovado !')
elif 5.0 < m < 6.9:
    print('Recuperação !')
else:
    print('Aprovado !')

print(f'Média: {m}')