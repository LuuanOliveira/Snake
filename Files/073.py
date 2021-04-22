times = ('Atlético-PR', 'Atlético', 'Avaí', 'Bahia', 'Botafogo',
        'CSA', 'Ceará SC', 'Chapecoense', 'Corinthians', 'Cruzeiro',
        'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
        'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco Da Gama')
print('-=' * 15)
print('Lista de Times do Brasileirão: ')
for time in times:
    print(f'{time}')
print('-=' * 15)
print(f'Os 5 Primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 Ultimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-=' * 15) 
print(f'A Chapecoense está na {times.index("Chapecoense")+1}° posição')