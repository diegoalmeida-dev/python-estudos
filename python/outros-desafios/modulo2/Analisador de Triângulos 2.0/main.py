#Este é um clássico que confunde muita gente, mas você vai tirar de letra. O programa deve ler o comprimento de três retas e dizer ao usuário

lado1 = float(input('Digite o valor do lado 1: '))
lado2 = float(input('Digite o valor do lado 2: '))
lado3 = float(input('Digite o valor do lado 3: '))

if lado1 > lado2 + lado3 or lado2 > lado3 + lado1 or lado3 > lado1 + lado2:
    print('Não pode ser um triângulo !')
else:
    if lado1 == lado2 == lado3:
        print('Equilátero !')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isóceles !')
    else:
        print('Escaleno !')