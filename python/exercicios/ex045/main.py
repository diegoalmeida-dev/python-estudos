import random

escolhas = ['pedra', 'papel', 'tesoura']

npc = random.choice(escolhas)
player = str(input('Vamos jogar Jokenpô !\nDigite uma das opções abaixo:\nPedra\nPapel\nTesoura\nR: '))
player.lower

if player == npc:
    print(f'Empate ! Eu escolhi {npc} e você escolheu {player}')
elif player == 'pedra' and npc == 'tesoura':
    print('Perdi ! Pedra mata tesoura !')
elif player == 'tesoura' and npc == 'pedra':
    print('Venci ! Pedra mata tesoura !')
elif player == 'tesoura' and npc == 'papel':
    print('Perdi ! Tesoura mata papel !')
elif player == 'papel' and npc == 'tesoura':
    print('Venci ! Tesoura mata papel !')
elif player == 'papel' and npc == 'pedra':
    print('Perdi ! Papel mata pedra !')
elif player == 'pedra' and npc == 'papel':
    print('Venci ! Papel mata pedra !')
else:
    print(f'Algo deu errado, você escolheu {player} e eu {npc}')