maior = 0
menor = 0
for c in range(1, 3):
    peso = float(input('Peso da {}° Pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O mais pesado tem {}KG'.format(maior))
print('O mais leve tem {}KG'.format(menor))