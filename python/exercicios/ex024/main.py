c = input('Digite o nome da sua cidade: ')

d = c.split()
v = str(d[0])

if v.capitalize() == 'Santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')