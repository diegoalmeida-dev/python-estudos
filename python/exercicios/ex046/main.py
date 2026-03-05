import time

t = 10

for c in range(1, 11):
    print(f'Faltam {t} segundos...\n')
    t -= 1
    time.sleep(1)
print('Os fogos estouraram !')