vc = float(input('Qual o valor da casa?: '))
s = float(input('Qual o seu salário?: '))
t = float(input('Em quantos anos pretende pagar?'))

p = vc/(t * 12)
limite = 30/100*s

if p > limite:
    print('Empréstimo negado ! Você não tem saldo suficiente !')
else:
    print('Empréstimo liberado !')