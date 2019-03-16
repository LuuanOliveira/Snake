print('Gerador de PA')
print('=-' *10)
primeiro = int(input('1° Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer acrescentar ? '))
print('Fim, ao todo foram {} termos'.format(total))
