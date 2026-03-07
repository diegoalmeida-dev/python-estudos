# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint
from time import sleep

npc = randint(0, 5)
player = int(input('Adivinhe um número de 0 a 5: '))
print('Analisando...')
sleep(2)
if npc == player:
    print('\033[32mParabéns !\033[m')
else:
    print(f'\033[31mPerdeu ! Eu escolhi {npc}\033[m')