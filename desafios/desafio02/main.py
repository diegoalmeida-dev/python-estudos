dia = input('Em qual dia você nasceu?: ')
mes = input('De qual mês? (nome extenso): ')
ano = input('De qual ano?: ')

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if int(dia) > 31:
    print('Em que planeta você vive que o mês tem mais que 31 dias?')
elif mes not in meses:
    print(f'Em que planeta você vive que tem um mês chamado {mes}?')
else:
    print(f'Você nasceu no dia {dia} de {mes} de {ano}, correto?')

