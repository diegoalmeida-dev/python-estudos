# Aula 06

n = input('Digite algo: ')

if n.isnumeric():
    print(f'{n} é um número !')
elif n.isalpha():
    print(f'{n} é um texto !')
elif n.isalnum():
    print(f'{n} contém texto e número !')
else:
    print(f'A classe de {n} é', type(n))