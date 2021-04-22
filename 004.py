# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo,
# e todas as informações possíveis soble ele.

result = input('Digite algo: ')
if result.isspace() == True:
    result = 'BRANCO'

print(f'O tipo primitido de {result} é: ', type(result))
print('Só tem espaços? ', result.isspace())
print(f'{result} é um número? ', result.isnumeric())
print(f'{result} é alfabético? ', result.isalpha())
print(f'{result} é alfanumérico? ', result.isalnum())
print(f'{result} está em maiúsculas? ', result.isupper())
print(f'{result} está em minúsculas? ', result.islower())
print(f'{result} está capitalizada? ', result.istitle())