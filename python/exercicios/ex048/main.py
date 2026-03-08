s = 0
cont = 0
for c in range(1,501):
    if c%2 != 0:
        if c%3 == 0:
         print(c)
         s += c
         cont += 1
print(f'O resultado é {s} com {cont} números')