print('Gerador de PA')
print('=-' *10)
primeiro = int(input('1° Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador < 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
