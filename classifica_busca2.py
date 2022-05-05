import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from collections import Counter

df = pd.read_csv('busca_com_sim.csv')             # Data_frame

x_df = df[['home', 'busca', 'logado']]    # Passamos um array contendo as colunas
y_df = df['comprou']

xdummies_df = pd.get_dummies(x_df)        # Transformando a busca em variaveis dummies 0 ou 1
ydummies_df = y_df

x = xdummies_df.values
y = ydummies_df.values

porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino * len(y)    # Tomamos como tamanho para treino 90% do Y

tamanho_de_teste = len(y) - tamanho_de_treino         # Tomamos como tamanho do teste 10% do Y

treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]

teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]

modelo = MultinomialNB()                             # Usamos a biblioteca MultinomialNB para fazer o claculo do resultado
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
acertos = (resultado == teste_marcacoes)

total_de_acertos = sum(acertos)             # Calculamos o total de acertos
total_de_elementos = len(teste_dados)       # Calculamos o total elementos testados

print(f"A taxa de acertos do algoritmo foi: {total_de_acertos: .2f} % de um total de ",
      total_de_elementos, "elementos testados")

# Avaliando a eficácia do algoritmo que chuta tudo um unico valor
acerto_base = max(Counter(teste_marcacoes).values())     # A biblioteca collections do python chamando o Counter devolve a quantidade de acerto

taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
print(f'taxa de acerto base: {taxa_de_acerto_base: .2f} %')
