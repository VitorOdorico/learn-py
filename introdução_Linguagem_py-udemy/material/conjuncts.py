conjunto = {1, 2, 3, 4, 5, 6}
# type é para descubrir qual o tipo do dado que esta na vareavel
print(type(conjunto))

#Para unir dois conjuntos se usa o "union"

conjunto1 = {0,1,2,3,4}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)

# intercecção nos conjuntos

conjunto_intersection = conjunto1.intersection(conjunto2)
print(conjunto_intercection)


#diferença nos conjuntos

conjunto_diferenca = conjunto1.difference(conjunto2)