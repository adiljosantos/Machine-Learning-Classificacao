from sklearn.naive_bayes import MultinomialNB

#  | É gordinho  |  tem perna curta  |  faz au au  |  São as variaveis da matriz  (sendo 1 para sim e 0 para não)

porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]  # Marcamos (1 para porco) e (-1 para cachorro)

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

elementoMisterioso1 = [1, 1, 1]           # 1º Animal a ser analisado pelo sistema
elementoMisterioso2 = [1, 0, 0]           # 2º Animal a ser analisado pelo sistema
elementoMisterioso3 = [0, 0, 1]           # 3º Animal a ser analisado pelo sistema

teste = [elementoMisterioso1, elementoMisterioso2, elementoMisterioso3]

marcacoes_teste = [-1, 1, -1]              # Resultado esperado

resultado = modelo.predict(teste)          # Resultado calculado pelo sistema

print(resultado)

diferencas = resultado - marcacoes_teste   # Diferença entre o que foi esperado e o resultado do sistema

print(diferencas)                          # Zero corresponde a cada acerto

acertos = [d for d in diferencas if d==0]

print(acertos)

total_de_acertos = len(acertos)             # Calculamos o total de acertos
total_de_elementos = len(teste)             # Calculamos o total elementos testados

print("O total de acertos foi", total_de_acertos, "de um total de ",total_de_elementos, "elementos testados")
print("A taxa de acerto foi de ", total_de_acertos / total_de_elementos * 100, "%")


