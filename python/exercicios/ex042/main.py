r1 = float(input('Digite o valor da 1 reta: '))
r2 = float(input('Digite o valor da 2 reta: '))
r3 = float(input('Digite o valor da 3 reta: '))

if r1+r2 < r3 or r2+r3 < r1 or r3+r1 < r2:
    print('Não pode ser um triângulo !')
else:
    print('Pode ser um triângulo !')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isóceles')
    else:
        print('Escaleno')