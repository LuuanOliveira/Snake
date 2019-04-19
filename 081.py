numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break
print(f'Você digitou {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os números em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não foi encontrado ')