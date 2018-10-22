#!/usr/bin/env python3

"""O método tell () informa a posição atual dentro do arquivo; em outras palavras, o
próximo read ou write ocorrerá nesse número de bytes a partir do início do arquivo.

O método seek (offset [, from]) altera a posição atual do arquivo. O argumento
de compensação indica o número de bytes a serem movidos. O argumento from
especifica a referência posição de onde os bytes devem ser movidos."""

fo = open('scores.txt','r+')
str = fo.read()
print("Reading... ")
print(str)
print()

# Checando a posicao atual
position = fo.tell()  # exibe a posicao atual do cursor
print("Current file position: ", position)
print()

# Colocando o ponteiro no inicio
position = fo.seek(0)  # posiciona o cursor no inicio do arquivo
str = fo.read(18)  # le os primeiros 18 carcteres
print("Again... ")
print(str)

# Fechando
fo.close()