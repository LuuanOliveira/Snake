from time import sleep
n1 = int(input('\033[34m1° Valor: \033[m'))
n2 = int(input('\033[34m2° Valor: \033[m'))
opcao = 0
while opcao != 5:
    print('\033[30m=-=\033[m' * 8)
    print('''\033[33m    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos Números 
    [ 5 ] Sair \033[m''')

    opcao = int(input('\033[30m>>> Qual sua opção: \033[m'))
    if opcao == 1:
        soma = n1 + n2
        print('\033[30m>>>\033[m''\033[36m A soma de {} + {} = {}\033[m'.format(n1, n2, soma))

    elif opcao == 2:
        produto = n1 * n2
        print('\033[30m>>>\033[m''\033[36m O resultado de {} x {} = {}\033[m'.format(n1, n2, produto))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[30m>>>\033[m''\033[36m Entre {} e {} o Maior valor é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('\033[30m>> Informe os Números Novamente <<\033[m')
        n1 = int(input('\033[32m1° Valor: \033[m'))
        n2 = int(input('\033[32m2° Valor: \033[m'))

    elif opcao == 5:
        print('\033[30mFinalizando...\033[m')
    else:
        print('\033[31mOpção Inválida\033[m')
    sleep(2)
print('\033[36mFim do Programa\033[m')