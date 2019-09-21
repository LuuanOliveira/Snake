time = []
dados = {}
partidas = []

while True:
    dados.clear()
    dados['Nome'] = str(input('Jogador: '))
    total = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    partidas.clear()
    for contador in range(0, total):
        partidas.append(int(input(f'    Quantos gols na {contador+1}º partida: ')))
    dados['Gols'] = partidas[:] #Chave gols recebe uma cópia da lista de partidas
    dados['Total'] = sum(partidas) #Chave total recebe a soma do que está em partidas
    time.append(dados.copy())
    while True:
        print('¨' * 35)
        resposta = str(input('Adicionar outro jogador? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('[ERROR]: Resposta Inválida')
    if resposta == 'N':
        break

#--Cabeçalho--
print('-' * 40)
print('', end='')
for elemento in dados.keys():
    print(f'{elemento:<15}', end='')
print()
# --          --

print('-' * 40)
for chave, valor in enumerate(time):
    print(f'{chave:3>} ', end='') #:4> Centralizar a direita com 4 casas
    for dado in valor.values():
        print(f'{str(dado):<15}', end='') #:<15 Centralizar a esquerda com 15 casas
    print()
print('-' * 40)

while True:
    busca = int(input('Dados do jogador: (999 Parar) '))
    if busca == 999:
        break
    if busca >= len(time): #Se a busca for maior que o tamanho do time
        print(f'[ERRO]: Jogador {busca} não existe')
    else:
        print(f'APROVEITAMENTO DO JOGADOR - {time[busca]["Nome"]}: ')
        for indice, gols in enumerate(time[busca]['Gols']):
            print(f'    -> {indice+1}° jogo fez {gols} Gols')
    print('-' * 40)