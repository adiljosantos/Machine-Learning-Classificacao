from sklearn.naive_bayes import MultinomialNB

#  | É gordinho  |  tem perna curta  |  faz au au  |  São as variaveis da matriz

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

print(modelo.predict(elementoMisterioso1))
print(modelo.predict(elementoMisterioso2))

teste = (modelo.predict(elementoMisterioso1), modelo.predict(elementoMisterioso2))
print(teste)




