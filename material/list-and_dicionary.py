# -*- coding: utf-8 -*-
#   Listas
#       Representa conjunto de dados podendo ser:
#           - numéricas [1, 2, 3, 4, 5]
#           - strings ["joao", "pedro", "lucas"]


minha_lista = ["abacaxi", "melancia", "morango"]
minha_lista2 = [1,2,3,4,5,6,7,8,9]
minha_lista3 = ["abacaxi", 2, 10.45, True, False]



# maior e menor elemento de uma lista

lista = [1,2,3,4,5,6,7,8,9]
print(max(lista))
print(min(lista))

lista_animal = [cachorro, elefante, zebra]
#aqui o max ou o min é por ordem alfabética.
print(min(lista_animal))
print(max(lista_animal))

# condicional em listas

lista_aracnidea = [aranha, escorpiao, sentopeia]
if aranha in lista_aracnidea:
    print("tem aranha na lista")
else:
    print("nao ha aranha na lista")

# adicionar um elemento na  lista
lista_animal.append('coelho, bode, ovelha')
lista.append('33, 34,62,734')


# remover um elemento da lista
# remove o vetor da lista
lista_animal.pop(1)
lista.pop(5)

# para imprimir item por item em uma lista

for item in minha_lista:
    print(item)


#   verificando o tamanho de uma lista

tamanho =  len(minha_lista)
print(tamanho)

# adicionar elementos em uma lista
minha_lista.append("jabuticaba")
print(minha_lista)

#   remover os elementos de uma lista
del minha_lista[:]
print(minha_lista)
# para remover todos elementos, ou usa um vetor para remover um elemento especifico

# como ordenar listas

lista_ordenada = [34,15,3456,568,97,34,235,213,789,0]

lista_ordenada.sort()

print(lista_ordenada)

# ordenar no mode decrescente

lista_ordenada_decrescente = [34,15,3456,568,97,34,235,213,789,0]

lista_ordenada_decrescente.sort(reverse=True)

print(lista_ordenada_decrescente)

# lista reversa

lista_ordenada_reversa = [34,15,3456,568,97,34,235,213,789,0]

lista_ordenada_reversa.reverse()

print(lista_ordenada_reversa)

# ordenar no modo alfabético

lista_ordenada_alfabetica = ["Amanda", "Bianca", "Pedro", "Fernando", "Lucas"]

lista_ordenada_alfabetica.sort()

print(lista_ordenada_alfabetica)

# ordenar no modo alfabético reverse

lista_ordenada_alfabetica = ["Amanda", "Bianca", "Pedro", "Fernando", "Lucas"]

lista_ordenada_alfabetica.sort(reverse=True)

print(lista_ordenada_alfabetica)

#   Tupla
#  len é para ler quantos elementos tem em uma tupla
tupla = (1, 2, 3, 4, 5, 6, 7)
print(len(tupla))

#   Dicionários

#       Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo:

dicionario_sites = {"Clain": "www.lojaclain.com"}
print(dicionario_sites['Clain'])
#  No dicionário acima, a chave "Clain" foi vinculado ao valor "www.lojaclain.com". Assim, para imprimir o valor chame:


# Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:

dicionario_sites = {"Clain": "www.lojaclain.com", "Youtube": "www.youtube.com.br", "Udemy": "www.udemy.com"}
for chave in dicionario_sites:
    print(dicionario_sites[chave])
