soma = 0
homem_velho = 0
mulheres_novas = 0
for c in range(1, 5):
    #nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ')
    soma += idade
    if sexo == 'M':
        if idade > homem_velho:
            homem_velho = idade
    else:
        if idade < 20:
            mulheres_novas += 1
print(soma)
media = soma/c

print(f'A média de idade é {media}\nO homem mais velho tem {homem_velho} anos e {mulheres_novas} mulher tem menos que 20 anos')