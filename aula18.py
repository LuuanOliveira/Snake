#=======================#
#LISTAS DENTRO DE LISTAS#
#=======================#
#teste = list()
#teste.append('Luan')
#teste.append(20)
#galera = list()
#galera.append(teste[:])#Cópia da lista teste
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)

#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][1])
#for pessoa in galera:
    #print(pessoa[0])
   # print(f'{pessoa[0]} tem {pessoa[1]} anos')

galera = []
dado = [] #Lista auxiliar para pegar dados da lista "galera"
totmaior = totmenor = 0

#=======================#
#BLOCO PARA PEGAR OS DADOS E ARMAZENAR 
for contador in range(0, 3):
    dado.append(str(input('Nome: '))) #Posição 0 na lista
    dado.append(int(input('Idade: '))) #Posição 1 na lista
    print('-' * 10)
    galera.append(dado[:]) #Cria uma cópia da lista "dado" dentro de "galera"
    dado.clear() #Limpa a lista "dado"
#print(galera)
#=======================#

#=======================#
#BLOCO PARA VERIFICAR A IDADE DA PESSOA
for pessoa in galera:
    if pessoa[1] >= 21: #Se a idade de pessoa for maior que 21, mostre:
        print(f'{pessoa[0]} é maior de idade')
        totmaior += 1 
    else:
        print(f'{pessoa[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maior de idade e {totmenor} menores')
#=======================#