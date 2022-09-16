#  Laços de repetição
 
# Para o que serve?

#   - Fazer estruturas de repetição
#   - Interadores
#   -  Repetem um trecho do código, isso tem duas condições sendo elas:
#       * enquanto uma condição avaliada for verdadeira
#       * durante uma condição pré-determinada

#   while
#       é um laço de repetição enquanto for verdadeiro ele fica execultando.

#   for
#      usado para percorrer listas
 
#   range
#       - tamanho ou parametro de medida
#       - range({quantidade de elementos}, {parametro final de quantidade}, {tamanho de numero de indentidade de quantidade})

# pratica

x = 1
while x < 10:
    print(x)
    x = x+1
    

# listas 
#  - são um conjunto de elementos.    
    
lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = ["Hello word", "!"]
lista3 = [0,"Hello","word","!",9.99,True]

for i in lista3:
    print(i)
    
for i in range(0,100,5):
    print(i)
