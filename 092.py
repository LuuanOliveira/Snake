from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nascimento #Ano atual do sistema, menos o ano de nascimento
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Ctps'] != 0:
    dados['Contratacao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = (dados['Contratacao'] - nascimento) + 35
print('==' * 15)
for chave, valor in dados.items():
    print(f'   - {chave} tem o valor {valor}')