s = float(input('Digite seu salário: '))

if s > 1250.0:
    ns = s+(10/100*s)
    print(f'Seu novo salário é {ns}')
else:
    ns = s+(15/100*s)
    print(f'Seu novo salário é {ns}')