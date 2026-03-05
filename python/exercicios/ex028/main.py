import random
import time

r = int(input('Adivinhe o número de 1 a 5: '))
n = random.randint(1, 5)

print('Pocessando...')
time.sleep(2)

if r == n:
    print('Acertou !')
else:
    print(f'Errou ! Eu pensei no número {n}')