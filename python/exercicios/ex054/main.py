import datetime

ano_atual = int(datetime.datetime.now().strftime('%Y'))

menores = 0
maiores = 0

for c in range(1, 8):
    a = int(input(f'Digite o ano de nascimento da {c} pessoa: '))
    c =  ano_atual - a
    if c < 21:
        print('Menor de idade')
        menores += 1
    else:
        print('Maior de idade')
        maiores += 1

print(f'{menores} pessoas ainda são menores de idade e {maiores} já atingiram a maioridade')


