# -*- coding: utf=8 -*-
# comandos condicionais


# if (se)

#  Para oque server?
#   - Realizar testes condicionais
#   - Executar um bloco até uma determinada condição for atendida
#   - Avelia se a condição é verdadeira ou não

x = 8
y = 100

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")
    

# else
#   para oque serve?
#   - se a numa condição acima não funcionar ele entra em ação e da o resultado que está programado para exibir

if x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")
    
    
# elif
#   - Caso tenha necessidade de mais do que duas condições entre o if e o else

x = 1
y = 2

if x ==y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes") 