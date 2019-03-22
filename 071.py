print('=' * 25)
print('BANCO 24h')
print('=' * 25)
valor = float(input('Valor do Saque R$: '))
total = valor 
cedula = 100
totcedula = 0
resto = 0
while True:
    if total >= cedula: #Se o total for maior ou igual ao valor da cedula
        total -= cedula #O total recebe ele mesmo menos o valor da cedula
        totcedula += 1 #O total de cedulas recebe ele mesmo mais 1
    else:
        if totcedula > 0: #Print se o valor das cedulas for maior que 0
            print (f'Total de {totcedula} cédulas de R${cedula}')
        #-----------------#
        if cedula == 100:
            cedula = 50
        #-----------------#
        elif cedula == 50:
            cedula = 20
        #-----------------#
        elif cedula == 20:
            cedula = 10
        #-----------------#
        elif cedula == 10:
            cedula = 5
        #-----------------#
        elif cedula == 5:
            cedula = 2
        #-----------------#
        elif cedula == 2:
            cedula = 0
        totcedula = 0
        #-----------------#
        if total == 0:
            break
print('=' * 25)
print('Obrigado por usar o Banco 24h')