# é o restante de uma divisão retornando 1 ou 0
# com isso da para trabalhar alguns tipos de dados
#por exemplo consegue-se fazer um leitor de numero par ou impar

from statistics import _Number
from tokenize import Number



numero = float(input("de um valor"))
if (numero % 2 == 0):
    print("Seu numero é par")
elif(numero % 2 != 0):
    print("Seu numero é impar")
    