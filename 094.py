pessoas = [] #Lista
pessoa = {} #Dicionário
soma = media = 0 #Variaveis simples começando em 0
while True: #Loop infinito - enquanto for verdade, faça:
    pessoa.clear() #Limpando o dict
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #Tudo maiusculo pegando a primeira posição
        if pessoa['Sexo'] in 'MF':
            break
        print('ERROR: digite M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade'] #soma recebe soma mais a idade da pessoa, a cada iteração
    pessoas.append(pessoa.copy()) #Fazendo um copia do dict para a lista
    while True:
        resposta = str(input('Quer continuar cadastrando? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: responda apenas S ou N')
    if resposta == 'N':
        break
print('=' * 45)
print(f'    -> Total de pessoas cadastradas: {len(pessoas)}') #len é o tamanho da lista pessoas
media = soma / len(pessoas)
print(f'    -> Média de idade das pessoas cadastradas: {media:5.2f} anos')
print('=> As mulheres cadastradas foram ', end='')
for people in pessoas:
    if people['Sexo'] == 'F':
        print(f'    -> {people["Nome"]}, ', end='')
print()
print('=> Pessoas acima da média de idade do grupo: ')
for people in pessoas:
    if people['Idade'] >= media:
        print('    ')
        for chave, valor in people.items():
            print(f'{chave} = {valor}; ', end='')
        print()