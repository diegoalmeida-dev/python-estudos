pi = float(input('Qual o preço do produto?: '))
fp = int(input('Qual a forma de pagamento?:\n1: À vista dinheiro/cheque (10% de desconto)\n2: À vista cartão (5% de desconto)\n3: Até 2x no cartão\n4: 3x ou mais no cartão (20% de juros)\nR: '))

if fp == 1:
    d = 10/100*pi
    v = pi-d
    print(f'Sua compra deu o valor de R${v}')
elif fp == 2:
    d = 5/100*pi
    v = pi-d
    print(f'Sua compra deu o valor de R${v}')
elif fp == 3:
    print(f'Sua compra deu o valor de R${pi}')
elif fp == 4:
    j = 20/100*pi
    v = pi+j
    print(f'Sua compra deu o valor de R${v}')
else:
    print('Algo deu errado !')