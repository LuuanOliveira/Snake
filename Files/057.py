sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Digite seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))