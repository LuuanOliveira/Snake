matriz = [[0,0,0], [0,0,0], [0,0,0,]] #Uma lista com 3 listas
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
    print()