#🚀 Desafio Módulo 1: Simulador de Orçamento de Pintura
#Imagine que você foi contratado para criar um programa que ajude uma empresa de reforma. O programa deve calcular quanto material será necessário e o custo total para pintar uma parede.

from math import ceil

largura = float(input('Digite a largura em m: '))
altura = float(input('Digite a altura em m: '))
area = largura*altura
preco = float(input('Qual o preço da lata de tinta?: R$'))

tinta = ceil(area/2)

custo = tinta*preco

print(f'O valor necessário para pintar {area:.2f}m, usando {tinta}l de tinta é de R${custo:.2f}')