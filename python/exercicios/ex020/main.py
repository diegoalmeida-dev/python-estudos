import random

a1 = str(input('Digite o 1 nome: '))
a2 = str(input('Digite o 2 nome: '))
a3 = str(input('Digite o 3 nome: '))
a4 = str(input('Digite o 4 nome: '))

nomes = [a1, a2, a3, a4]
random.shuffle(nomes)

print(nomes)