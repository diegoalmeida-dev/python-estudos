import random

npc = random.randint(1, 10)
p = int(input('Digite um número: '))
tt = 0

while p != npc:
    print('Errou ! Tente novamente !')
    p = int(input('Digite um número:'))
    tt += 1

print(f'Parabéns !, Você acertou em {tt} tentativas !')


