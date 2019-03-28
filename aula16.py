print('== TUPLAS ==')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#Tuplas são Imutáveis
#lanche[1] = 'Refrigerante' Error

#print(lanche)
#print(lanche[0]) Fatiando á Tupla
#print(lanche[-1])
#print(lanche[-3])
#print(lanche[2:])
#print(lanche[:3])

#for comida in lanche:
    #print(f'Eu vou comer {comida}')

#for contador in range(0, len(lanche)):
    #print(contador)

#for contador in range(0, len(lanche)):
    #print(lanche[contador])

#for contador in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[contador]}')

#for contador in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[contador]} na posição {contador}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')