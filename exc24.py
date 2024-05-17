def desenha_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    primeira_ultima_linha = '+' + '-' * (colunas - 2) + '+'
    linha_do_meio = '|' + ' ' * (colunas - 2) + '|'
    if colunas == 1:
        print('+')
        for _ in range(linhas - 2):
            print('|')
        if linhas > 1:
            print('+')
    else:
        print(primeira_ultima_linha)
        for _ in range(linhas - 2):
            print(linha_do_meio)
        if linhas > 1:
            print(primeira_ultima_linha)
desenha_moldura(4, 5)
desenha_moldura(1, 1)
desenha_moldura(20, 20)
desenha_moldura(22, 25)