import datetime

ano = int(datetime.date.today().strftime('%Y'))
anonasc = int(input('Digite o seu ano de nascimento: '))

v = ano - anonasc

if v < 9:
    print('Mirim')
elif 10 < v < 14:
    print('Infantil')
elif 15 < v < 19:
    print('Junior')
elif v == 20:
    print('Sênior')
else:
    print('Master')