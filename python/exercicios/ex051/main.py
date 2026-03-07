a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = a1 + (10-1)*r
for n in range(a1, d+r , r):
    print(n)