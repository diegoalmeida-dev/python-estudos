from math import ceil, sqrt

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

s = ceil((n1+n2)/2)
r = ceil(sqrt(n1+n2))

print(f'A média é {s} e a raiz da soma é {r}')