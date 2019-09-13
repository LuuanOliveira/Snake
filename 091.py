from random import randint #Randomizar números inteiros aleatórios
from time import sleep #Esperar
from operator import itemgetter 
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),} #Dict
ranking = [] #Lista
print('== SORTEIO ==')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no Dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#Ordenar neste caso pelo valor, que é a posição 1 do dict | Reverse para mostrar a ordem reversa
print('== COLOCAÇÃO ==')
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º Lugar: {valor[0]} com {valor[1]}')
    sleep(1)