soma = 0 #Acumulador
cont = 0 #Contador
for c in range(1, 7):
    n1 = int(input('Digite o {}° valor: '.format(c)))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print('A soma do número par é = {}'.format(cont, soma))
