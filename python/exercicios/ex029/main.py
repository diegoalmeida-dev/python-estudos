v = int(input('Qual a velocidade do carro em km/h (apenas números)?: '))
limite = 80

if v > limite:
    m = (v-limite)*7
    print(f'Você recebeu R${m} de multa !')
else:
    print('Tudo certo !')