numeros = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso')
    else:
        print('Impossível adicionar valor duplicado')
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'N':
        break
print('=-' * 20)
numeros.sort()
print(f'Você digitou os valores {numeros}')

