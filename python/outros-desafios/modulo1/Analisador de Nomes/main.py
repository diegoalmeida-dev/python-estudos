#🔠 Desafio Módulo 1: Analisador de Nomes (Strings)
#Para fechar o Módulo 1 com chave de ouro, vamos praticar a Manipulação de Textos. Essa é uma das partes mais importantes, pois quase todo programa lida com nomes, e-mails ou endereços.

nome = input('Digite seu nome: ').strip()
divisao = nome.split()
print(f'{nome.upper()}\n{nome.lower()}\n{len(nome)-nome.count(' ')}\n{len(divisao[0])}')