matriz = [[0,0,0], [0,0,0], [0,0,0,]] #Uma lista com 3 listas
soma_par = soma_coluna = soma_linha = 0
#Laço para adicionar os valores na matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) 
        #Adicionando valores atraves de um input na posição 'linha' e 'coluna'
#----------------------------------------------------------
print('=' * 20)
#Laço para mostrar a estrutura na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0: #Calculando a soma de todos os números pares digitados
            soma_par += matriz[linha][coluna]
    print()
print(f'A soma de todos os pares é {soma_par}')

for linha in range(0, 3): #Calculando os valores da 3 coluna
    soma_linha += matriz[linha][2]
print(f'A soma dos valores da 3° coluna é {soma_linha}')

for coluna in range(0, 3): #Pegando o maior valor da 2° Linha
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz [1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da 2° Linha é {maior}')