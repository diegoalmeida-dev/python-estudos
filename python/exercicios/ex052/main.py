n = int(input('Digite um número: '))
d = 0

for c in range(1, n+1):
    v = n%c
    if v == 0:
        print(f'{c} divide')
        d += 1
    else:
        print(f'{c} não divide')

if d > 2:
    print('Não primo')
else:
    print('Primo')
