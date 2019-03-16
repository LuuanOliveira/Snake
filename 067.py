while True:
    numero = int(input('Tabuada = '))
    if numero < 0:
        break
    print('-' * 30)
    for contador in range (1, 11):
        print(f'{numero} x {contador} = {numero*contador}')
    print('-' * 30)
print('Programa Encerrado ...')