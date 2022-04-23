from sklearn.naive_bayes import MultinomialNB

#  | É gordinho  |  tem perna curta  |  faz au au  |  São as variaveis da matriz  (sendo 1 para sim e 0 para não)

porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]  # Marcamos 1 para porco e -1 para cachorro

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

elementoMisterioso1 = [[1, 1, 1]]
elementoMisterioso2 = [[1, 0, 0]]
elementoMisterioso3 = [[0, 0, 1]]

teste = (elementoMisterioso1, elementoMisterioso2, elementoMisterioso3)

marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(teste)

print(resultado)




