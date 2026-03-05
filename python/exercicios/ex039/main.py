import datetime

i = int(input('Quando você nasceu?: '))
ano = int(datetime.date.today().strftime('%Y'))
v = ano - i

if v == 18:
    print('Vá se alistar !')
elif v < 18:
    print('Ainda vai se alistar !')
else:
    print('Já passou da hora de se alistar')