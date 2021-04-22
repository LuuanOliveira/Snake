resposta = 'S'
contador = 1
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite {}° número: '.format(contador)))
    contador += 1
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0] #[0] Para considerar apenas o 1° digito da string
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor valor foi {}'.format(maior, menor))
