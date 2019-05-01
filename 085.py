lista = [[], []] #Uma lista com duas listas internas
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor) #Adicionando o valor na posição 0 da lista
    else:
        lista[1].append(valor)
print('-' * 20)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares foram {lista[0]}')
print(f'Os valores ímpares foram {lista[1]}')