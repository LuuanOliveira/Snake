#numeros = [1, 2, 3, 4]
#numeros[2] = 6 Posição 2 recebe 6
#numeros.append(7) Adiciona ao final da lista
#numeros.sort(reverse=True) Organiza a lista decrescente
#numeros.insert(2, 2) #Insere o valor 2 na posição 2 
#numeros.pop(2) #Remove na posição 2
#numeros.remove(2) #Remove a primeira ocorrência do número 2
#if 5 in numeros: #Se existir 5 em números REMOVA
#    numeros.remove(5)
#else: #Se não, PRINT
   # print('Esse valor não existe no contexto atual')
#print(numeros)
#print(f'Essa lista tem {len(numeros)} elementos')
#-------------------------------------------------------#

#valores = [] #list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for valor in valores: Para cada valor em valores: faça
   # print(f'{valor}...')

#for contador in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))

#for posicao, valor in enumerate(valores): #enumerate traz a posição do elemento na lista
#    print(f'Na posição {posicao} encontrei o valor {valor}')
#-------------------------------------------------------#

a = [2, 3, 4, 7]
#b = a Cria uma ligação entre as listas
b = a[:] #Cria uma cópia sem ligações entre as duas listas 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')