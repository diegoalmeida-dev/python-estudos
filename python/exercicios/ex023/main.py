n = input('Digite um número: ')


if len(n) == 4:
    unidade = n[-1]
    dezena = n[-2]
    centena = n[-3]
    milhar = n[-4]
    print(f'''Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}''')

elif len(n) == 3:
    unidade = n[-1]
    dezena = n[-2]
    centena = n[-3]
    print(f'''Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: 0''')

elif len(n) == 2:
    unidade = n[-1]
    dezena = n[-2]
    print(f'''Unidade: {unidade}
Dezena: {dezena}
Centena: 0
Milhar: 0''')
    
else:
    unidade = n[-1]
    print(f'''Unidade: {unidade}
Dezena: 0
Centena: 0
Milhar: 0''')