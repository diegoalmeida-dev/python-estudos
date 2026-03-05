'''import time

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numeros:
    if n > 5:
        print(n, ' Oi')
        time.sleep(0.5)
    else:
        print(n)
        time.sleep(0.5)'''

'''n = int(input('Digite um número:'))

for c in range(0, n+1, 2):
    print(c)'''


s = 0
for c in range(1, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma total foi {s}')