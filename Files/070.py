total = totmil = menor = contador = 0
barato = ''
while True: 
    produto = str(input('Produto: '))
    preco = float(input('Preço R$: '))
    contador += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    #else:
        #if preco < menor:
            #menor = preco
            #barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos que custaram mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')