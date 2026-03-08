n = int(input('Digite um valor para ver sua tabuada ou digite 0 para sair: '))

while n != 0:
    for c in range(1, 11):
        r = c*n
        print(f'{c}x{n} = {r}')
    n = int(input('Digite um valor para ver sua tabuada ou digite "S" para sair: '))

print('Fim')