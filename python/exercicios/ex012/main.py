#Aula 7

p = float(input('Digite o preço do produto: R$'))

d = p*(5/100)
np = p - d

print(f'O preço R${p} com 5% de desconto é R${np:.2f}')