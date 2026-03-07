'''n = input('Digite seu nome: ')
i = input('Digite sua idade: ')
s = input('Digite seu sexo: ')
t = input('Qual o seu trabalho?: ')

dados = {
    'nome': n,
    'idade': i,
    'sexo': s
}

dados['trabalho'] = t

for k, v in dados.items():
    print(f'{k}: {v}')'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('UF: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())
    
for c in brasil:
    print(c)