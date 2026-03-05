n = int(input('Escolha um número (inteiro) para converter: '))
e = int(input("""Escolha uma opção:
          
1: binário:
2: octal:
3: hexadecimal
          
Escolha: """))

if e == 1:
    print(bin(n))
elif e == 2:
    print(oct(n))
else:
    print(hex(n))