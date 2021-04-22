numeros = []
pares = []
impares = []
while True: 
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break
for indice, valor in enumerate(numeros):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-=' * 20)
print(f'Lista completa: {numeros}')
print(f'Números pares digitados: {pares}')
print(f'Números ímpares digitados: {impares}')