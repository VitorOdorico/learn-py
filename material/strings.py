#       Strings

#   O que é?
#       - são objetos
#       - são dados em que se armazena uma coleção de caracteres(texto).
#       - são declaradas entre aspas ou apostrofos


#   Exemplo a baixo:

var1 = 1
# var 1 é uma vareavel do tipo numérica.
var2 = "1"
# var 2 é uma vareavel do tipo string.


#   função len
#       - serve para concatenar( contar o tamanho(numeros de caracteres))

#   exemplo a baixo:

tamanho = len("concatenar")
print(tamanho)

#   função lower e upper
#       - lower transforma a string em minusculo.
#       - upper transforma a string em maiusculo

#   exemplo a baixo:
undi =  ("upper", "lower")
undi = undi.lower()
undi = undi.upper()


#   função strip
#   - Removendo espaços no começo e no fim da string

seq = " Joao e o joao "

seq = seq.strip()

print (seq)

#   função split

#       - converte uma string em uma lista
qoq = "abcd efgh ijkl mnop qrst uvwx yz"

qoq = qoq.split()

print (qoq)

#       - converte em uma lista e remove uma letra especifica 

oqo = "o rato roeu a roupa do rei de roma"

oqo = oqo.split("r")

print(oqo)


#   função find
#       - buscar algo especifico na string

crea = "joao pedro lucas"

busca = crea.find("joao")

print (busca)

#   função replace
#       - substituir partes de uma string

substituir = "Frase alternativa"

substituir = substituir.replace("Frase substituida")

print (substituir)


#   vetor para string
#       - usa-se "[]" e o numero do vetor que será acessado.

#   exemplo a baixo:

a = "vitor"
b = "lucas"

print(a[2])

#   Mostrando como funciona na prática

