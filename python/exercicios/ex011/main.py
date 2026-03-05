largura = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))

a = largura*h
qt = (a//2) + 1

print(f'A área a ser pintada é {a:.2f} e você vai precisar de {qt} latas de tinta ! (1 a mais para garantia dos pedaços pequenos)')