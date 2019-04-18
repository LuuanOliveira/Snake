lista = []
maior = menor = 0
for posicao in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {posicao}: ')))
    if posicao == 0:
        maior = menor = lista[posicao]
    else:
        if lista[posicao] > maior:
            maior = lista[posicao]
        if lista[posicao] < menor:
            menor = lista[posicao]
print('=' * 35)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}..', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}..', end='')
print()