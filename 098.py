from time import sleep

def linha():
    print('-' * 20)

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.0)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez')
ini = int(input('Início: '))
fin = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fin, pas)