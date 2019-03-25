tot18 = toth = totm20 = 0
while True:
    print('-' *20)
    print('CADASTRO DE PESSOAS')
    print('-' *20)

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1 
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} Homens Cadastrados')
print(f'Ao todo foram {totm20 } Mulheres com menos de 20 anos')