from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for contador in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)