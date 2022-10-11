#       Manipulando arquivos

#           função open
#               Variavel = opne(nome, modo)

#           modos e suas funções
            
#            "r"  somente leitura
#            "w"  escrita(caso o arquivo ja existaa, ele será apagado e um novo aequivo vazio será escrito)
#            "a"  leitura e escrita(adiciona o novo conteúdo ao fim do arquivo)
#            "r+" leitura e escrita
#            "w+" escrita( o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
#            "a+" leitura e escrita(abre o arquivo para atualização)

w = open("files.txt", "w")

w.write("Esse é o meu novo arquivo")

w.close()


#           Lendo arquivos
#               read()
#                   - lê um arquivo inteiro
#               readline()
#                   - Lê uma linha
#               readlines()
#                   - Lê arquivo e o armazena em uma lista

arquivo = open("files.txt")

texto_completo = arquivo.read()

print(texto_completo)

texto_linha = arquivo.readline()

print(texto_linha)

texto_lista = arquivo.readlines()

print(texto_lista)
