km = int(input('Quantos km tem a viagem?: '))

if km <= 200:
    v = km*0.5
    print(f'O valor da passagem é R${v:2f}')
else:
    v = km*0.45
    print(f'O valor da passagem é R${v:.2f}')