import csv

# Quais as caracteristicas de acesso do usuario nas páginas do site?
#  | acessou a home? | acessou como funciona? | acessou contatos? | comprou?  | São as variaveis da matriz  (sendo 1 para sim e 0 para não)
# as tres primeiras colunas são as caracteristicas que desejamos analisar sobre o comportamento do usuario, a ultima é a marcação

# separamos os dados em 2 arrays um array com os elementos do lado esquerdo contendo os valores das caracteristicas
# e um array do lado direito contendo os valores de marcarções
# chamamos o lado esquerdo de x (dados que vc quer trinar) e o lado direito y (dados que vc quer prever)

def carregar_acessos():
    x = []  # dados
    y = []  # marcacoes

    arquivo = open('acesso.csv', 'rt')
    leitor = csv.reader(arquivo)
    next(leitor)  # despresamos a primeira linha (o cabecalho do arquivo)
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
        dado = [int(acessou_home),
            int(acessou_como_funciona),
            int(acessou_contato)]
        x.append(dado)
        y.append(int(comprou))

    return x, y


