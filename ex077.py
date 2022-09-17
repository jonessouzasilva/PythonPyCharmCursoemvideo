palavras = ('Aprender', 'Programar', 'Linguagem', 'Phyton',
            'Curso', 'Grátis', 'Estudar', 'Praticar',
            'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')


