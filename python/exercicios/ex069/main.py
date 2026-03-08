c = input('Seja bem vindo(a) ! Para inciciar o programa digite "C", para sair digite "S": ')

ci = 0
h = 0
mi = 0
while c == 'C':
    i = int(input('Digite sua idade: '))
    if i > 18:
        ci += 1
    s = input('Digite seu sexo [M/F]: ')
    if s == 'M':
        h += 1
    elif s == 'F' and i < 20:
        mi += 1
    c = input('Deseja continuar? [C/S]')

print(f'Resultados:\n{ci} pessoas tem mais de 18 anos\n{h} foram cadastrados\n{mi} mulheres tem menos de 20 anos')