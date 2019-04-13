palavras = ('Programador', 'Developer', 'Sonho', 'Victor',
            'Luan', 'Aprender', 'Python', 'Furuto', 'Trabalhar')
for cont in palavras:
    print(f'\nNa palavra {cont.upper()} temos: ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end='')