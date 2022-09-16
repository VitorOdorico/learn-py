#   Operadores relacionais

#   igual
#       Usa-se "=="
#       Exemplo a baixo:
1 == 1

#   diferente
#       Usa-se "!="
#       Exemplo a baixo:
1 != 7

#   maior
#       Usa-se ">"
#       Exemplo a baixo:
6 > 5

#   menor
#       Usa-se "<"
#       Exemplo a baixo:
1 < 6

#   maior ou igual
#       Usa-se ">="
#       Exemplo a baixo:
15 >= 14

#   menor ou igual (divisão)
#       Usa-se "<="
#       Exemplo a baixo:
1 <= 6

# Exemplos na prática

x = 10
y = 4

soma = x + y

print(soma < y)

# Oque aconteceu aqui?
# é simples mas vou explicar foi criado suas vareáveis "x" e "y" e nelas foi definido valores, logo apos criou-se a vareável soma que recebeu os parametros de "x + y", logo após foi imprimido na tela fazendo a operação aritimética soma menor que y. e o resultado saiu no terminal, sendo falso.


# Operadores lógicos

#   AND
#       as duas condições tem que ser verdadeiras
#       Exemplo a baixo:
print(x == soma and y == soma)

#   OR
#       pelo menos uma condição sendo verdadeira ja basta
print(x == soma or y == soma)

#   NOT
#       inverte os valores
int(not 0)
int(not 1)
