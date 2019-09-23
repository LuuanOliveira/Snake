def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {resultado}m²')


print(' Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA: (m) '))
comprimento = float(input('COMPRIMENTO: (m) '))
area(largura, comprimento)