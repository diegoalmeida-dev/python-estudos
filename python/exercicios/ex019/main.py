import random

a1 = input('Digite o 1 aluno: ')
a2 = input('Digite o 2 aluno: ')
a3 = input('Digite o 3 aluno: ')
a4 = input('Digite o 4 aluno: ')
alunos = [a1, a2, a3, a4]

aluno = random.choice(alunos)

print(f'O aluno escolhido foi {aluno}')