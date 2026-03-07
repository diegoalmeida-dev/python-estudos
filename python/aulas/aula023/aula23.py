try:
    n = int(input('Número: '))
except Exception as e:
    print(f'Isso não é um número ! {e}')
else:
    print(f'Você digitou {n}')
finally:
    print('Volte sempre')