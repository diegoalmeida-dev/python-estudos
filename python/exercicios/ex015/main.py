d = int(input('Quantos dias alugados?: '))
kmr = float(input('Quantos km rodados? '))

pkm = kmr*0.15
pd = d*60

t = pkm+pd

print(f'O custo do aluguel foi {t:.2f}')