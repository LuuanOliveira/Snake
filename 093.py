dados = {}
partidas = []
dados['Nome'] = str(input('Jogador: '))
total = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for contador in range(0, total):
    partidas.append(int(input(f'    Quantos gols na {contador+1}º partida: ')))
dados['Gols'] = partidas[:] #Chave gols recebe uma cópia da lista de partidas
dados['Total'] = sum(partidas) #Chave total recebe a soma do que está em partidas
print('==' * 15)
print(dados)
print('==' * 15)
for chave, valor in dados.items():
    print(f'O campo {chave} tem o valor {valor}')
print('==' * 15)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas')
for indice, valor in enumerate(dados["Gols"]):
    print(f'    -> Na partida {indice+1}, fez {valor} Gols')
print(f'Totalizando {dados["Total"]} Gols')