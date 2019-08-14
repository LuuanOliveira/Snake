from time import sleep
boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media]) #Lista composta
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta in 'N':
        break
print('=' * 25)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":<8}')
print('=' * 25)
for indice, aluno in enumerate(boletim): #Indice e posição aluno com enumarate
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=' * 25)
    opcao = int(input('Exibir notas do aluno:  [999 Interrompe] '))
    if opcao == 999:
        sleep(1)
        print('Finalizando...')
        break
    if opcao <= len(boletim) - 1: #Menor que a qtd de alunos cadastrados, a partit do 1ºAluno
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}') #Opcao é o aluno, Boletim[0] é o nome do aluno, Boletim[1] são as notas 
