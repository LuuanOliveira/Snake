'''soma = 0
for c in range(1, 3):
    ano = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(c)))
    resultado = 2019 - ano
if resultado <= 18:
    soma += 1
    print('Temos {} menores de idade'.format(soma))
else:
    soma += 1
    print('Temos {} maiores de idade'.format(soma))'''

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 3):
    nasc = int(input('Ano de nascimento da {}° Pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Temos {} maiores de Idade'. format(maior))
print('E {} menores de Idade'.format(menor))
