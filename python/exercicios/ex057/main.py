s = str(input('Digite o seu sexo [M/F]: '))

sexos = ['M', 'F', 'f', 'm']

while s not in sexos:
    print('Erro')
    s = str(input('Digite o seu sexo [M/F]: '))

if s == 'M':
    print('Seja bem vindo !')
else:
    print('Seja bem vinda !')