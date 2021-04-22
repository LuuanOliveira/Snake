from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número, consegue adivinhar ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais .. Tente novamente')
        elif jogador > computador:
            print('Menos .. Tente novamente')
print('\033[34mAcertou\033[m você precisou de {} tentativas'.format(palpites))