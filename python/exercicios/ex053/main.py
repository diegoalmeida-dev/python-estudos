f = input('Digite uma frase:').strip().upper()

p = f.split()
tj = ''.join(p)
i = ''

for le in range(len(tj) - 1, -1, -1):
    i += tj[le]

if i == tj:
    print('Palindromo')
else:
    print('Não é')