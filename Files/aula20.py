#def linha(): #def == definição de função(Rotina)
#    print('-' * 30)

#Programa Principal ↓
#linha()
#print('CURSO EM VIDEO')
#print('PYTHON')
#print('APRENDER')
#linha()
#-----------------------------------------------------------

#def titulo(txt): #def == definição de função(Rotina) com paramêtro
#    print('-' * 30)
#    print(txt)
#    print('-' * 30)

#Programa Principal ↓   
#titulo('CURSO EM VIDEO') #Paramêtro
#-----------------------------------------------------------

#def soma(a, b):
    #s = a + b
    #print(s)
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma de A + B = {s}')
#    print('-' * 10)

#soma(4, 5)
#soma(b=8, a=9)
#soma(a=2, b=1)
#-----------------------------------------------------------

#def contador(* num): #Asterisco significa desempacotar/ nesse caso eu posso receber 1 ou vários parametros e guardar em num
    #for valor in num:
    #    print(f'{valor} ', end='')
    #print('FIM')
#    tamanho = len(num)
#    print(f'Recebi os valores {num} o total é {tamanho}')


#contador(1, 2, 3)
#contador(5, 6, 7, 8)
#contador(0)
#-----------------------------------------------------------

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *=2
        posicao +=1


valores = [1, 2, 3, 4, 5, 6]
dobra(valores)
print(valores)