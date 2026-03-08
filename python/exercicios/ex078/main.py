lista = list()

m = 0

for c in range(1, 6):
    n = int(input('Digite um número: '))
    lista.append(n)
    if n > m:
        m == n
    

print(lista)
print(f'O maior é {m}')
