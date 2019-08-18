# pessoas = () Tupla
# pessoas = [] Lista
# pessoas = {'Nome': 'Luan', 'Sexo': 'M', 'Idade': '20'} #Dicionário
# print(pessoas['Nome']) #Usar [] apenas para referenciar o elemento, {} para declaração
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos') #Usar aspas duplas dentro de aspas simples
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items()) #Uma lista composta de 3 tuplas
# for key in pessoas.keys(): #Para cada chave em pessoas, faça:
    # print(key)

# for key in pessoas.values():
    # print(key)
# del pessoas['Sexo']
# pessoas['Nome'] = 'Victor' #Mutavel
# pessoas['Peso'] = 70
# for key , valor in pessoas.items(): #Similar ao enumerate   
    # print(f'{key} = {valor}')
#-------------------------------------------------------------------------------------------------------
#DICIONÁRIOS EM LISTAS#

# brasil = []
# estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1) #Adicionar o dicionario "estado1" na lista brasil
# brasil.append(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]['UF'])
# print(brasil[1]['Sigla'])
#-------------------------------------------------------------------------------------------------------

estado = {}
brasil = []
for contador in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Usar copy() para criar uma copia do dicionário sem relacionar, não é possível usar fatiamento [:]
# print(brasil)
for estad in brasil: #Cada estado é um dicionário dentro da lista
    # print(estad)
    # for chave, valor in estad.items():
        # print(f'O campo {chave} tem valor {valor}')
    for valor in estad.values():
        print(valor, end=' ')
