from random import randint #Randomizar números inteiros
from time import sleep #Definir tempo de ação
lista = [] #Lista 
jogos = [] #Lista de jogos
quantidade = int(input('Quantos jogos devo sortear? '))#Guardando a quantidade de jgos que serão sorteados
total = 1 #Total de jogos que serão sorteados começando em 1
while total <= quantidade: #Enquanto o total for menor ou igual a quantidade
    contador = 0 #Contador começa com 0
    while True:
        numero = randint(1, 60) #Randomizando números de 1 até 60
        if numero not in lista: #Verificando se o número não está em uma lista
            lista.append(numero) #Adicionando o número caso ele não esteja na lista
            contador += 1 #Contador = contador + 1
        if contador >= 6: #Se o contador já gerou 6 números
            break #Stop (parar)
    lista.sort() #Colocando os valores da lista em ordem crescente
    jogos.append(lista[:]) #Criando uma cópia da Lista 
    lista.clear() #Limpando os dados da Lista 
    total += 1 #Total = Total + 1
print('-=' * 3, f'SORTEANDO {quantidade} JOGOS', '-=' * 3)
for i, l in enumerate(jogos): #Para cada índice com a lista em enumerate(jogos)
    print(f'Jogo {i+1}: {l}') #enumerate trata  o indice e o valor/ i=1 para começar a partir do primeiro indice
    sleep(1) #Espera 1 segundo para mostrar o print
print('-=' * 4, '< BOA SORTE >', '-=' * 4)