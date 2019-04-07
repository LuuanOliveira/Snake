numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1} posição ')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram: ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end='')
