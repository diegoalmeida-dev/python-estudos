mp = 0
mnp = 0

for c in range(1, 6):
    p = int(input('Digite seu peso: '))
    if c == 1:
        mp = p
        mnp = p
    else:
        if p > mp:
            mp = p
        elif p < mnp:
            mnp = p

print(f'O menor peso é {mnp}kg e o maior peso é {mp}kg')