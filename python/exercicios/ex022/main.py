nome = str(input('Digite seu nome completo: '))
nome.strip()

semespaco = len(nome)-nome.count(' ')
divnome = nome.split()
primeironome = divnome[0]


print(nome.upper())
print(nome.lower())
print(semespaco)
print(len(primeironome))
