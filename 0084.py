pessoas = [] #Principal 
dados = [] #Temporaria
maispesado = menospesado = 0
while True:
    dados.append(str(input('Nome: '))) #Posição 0
    dados.append(float(input('Peso: '))) #Posição 1
    if len(pessoas) == 0:
        maispesado = menospesado = dados[1]
    else:
        if dados[1] > maispesado:
            maispesado = dados[1]
        if dados[1] < menospesado:
            menospesado = dados[1]
    print('-' * 10)
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break   
print(f'Você cadastrou {len(pessoas)} Pessoas')
print(f'O maior peso foi {maispesado}KG ', end='')
for pessoa in pessoas:
    if pessoa[1] == maispesado:
        print(f'[{pessoa[0]}]')
print()
print(f'O menor peso foi {menospesado}KG ', end='')
for pessoa in pessoas:
    if pessoa[1] == menospesado:
        print(f'[{pessoa[0]}]')
print()
