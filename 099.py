from time import sleep
def linha():
    print('-' * 20)

def maior(* numero):
    contador = maior = 0
    linha()
    print('Analisando...')
    for valor in numero:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Total de {contador} valores')
    print(f'O maior valor foi {maior}')


#Programa Principal
maior(1, 2, 3, 4, 5, 6)
maior(1, 2, 3,)
maior(0, 7, 9)
maior(10)
maior()
