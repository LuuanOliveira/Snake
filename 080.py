lista = []
for contador in range(0, 5):
    numero = int(input('Digite um valor: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-=' * 20)
print(f'Os valores digitado em ordem foram {lista}')
