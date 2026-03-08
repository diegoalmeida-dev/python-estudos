c = input('Seja bem vindo(a) ! Digite "C" para continuar e "S" para sair: ')

valor = 0

while c == 'C':
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: '))
    valor += preco
    c = input('Há mais algum produto a ser adicionado? Se sim continue [C/S]: ')

print(f'O valor total é {valor}')