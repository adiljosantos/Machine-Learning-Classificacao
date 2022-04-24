from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos

x, y = carregar_acessos()

# separamos os dados de treino e os dados de teste

treino_dados = x[:90]               # Os dados de treino serão as primeiras 90 linhas
treino_marcacoes = y[:90]           # as marcações de treino serão as primeiras 90 linhas

teste_dados = x[-9:]                # os ultimos 9 elementos serão dados para teste
teste_marcacoes = y[-9:]            # os ultimos 9 elementos serão marcações para teste


modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)       # com quem realizo o teste

# Diferença entre o que foi esperado e o resultado do sistema
diferencas = resultado - teste_marcacoes

print('Demonstrativo de acertos e erros - 0 representa o acerto e -1 representa o erro')
print(diferencas)                          # Zero corresponde a cada acerto e -1 a cada erro

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)             # Calculamos o total de acertos
total_de_elementos = len(teste_dados)       # Calculamos o total elementos testados

print("O total de acertos foi", total_de_acertos,
      "de um total de ", total_de_elementos, "elementos testados")
print("A taxa de acerto foi de ", total_de_acertos / total_de_elementos * 100, "%")

# Separamos os dados de treino e de marcação e validamos o nosso algoritmo

