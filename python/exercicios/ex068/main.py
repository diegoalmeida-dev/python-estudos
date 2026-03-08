import random
import time

i = input('Vamos jogar par ou ímpar? [S/N]: ')

pnpc = 0
pp = 0


while i == 'S':
    npc = random.randint(0, 5)
    player = int(input('Vamos jogar par ou ímpar ! Digite um número de 1 a 5: '))
    escolha = input('\nAgora escolha entre par ou ímpar usando "P" ou "I": ')

    calculo = (npc+player)%2

    print('Calculando...')
    time.sleep(1)

    if calculo == 0 and escolha == 'P':
        print(f'\nDeu par ! Você venceu !: minha escolha: {npc}, sua escolha: {player}')
        pp += 1
    elif calculo == 0 and escolha == 'I':
        print(f'\nDeu par ! Você perdeu !: minha escolha: {npc}, sua escolha: {player}')
        pnpc += 1
    elif calculo != 0 and escolha == 'P':
        print(f'\nDeu ímpar ! Você perdeu !: minha escolha: {npc}, sua escolha: {player}')
        pnpc += 1
    else:
        print(f'\nDeu ímpar ! Você venceu !: minha escolha: {npc}, sua escolha: {player}')
        pp += 1
    i = input(f'\nDeseja continuar? [S/N]\nPlacar:\nEu: {pnpc}\nVocê: {pp}\nR: ')




