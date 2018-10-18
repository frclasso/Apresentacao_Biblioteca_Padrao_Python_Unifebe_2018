# exemplo1

# Abrindo o arquivo
fo =open('foo.txt', 'r+')
str = fo.read()  # Altere esse valor, 26 primeira linha
print("Lendo o arquivo:",fo.name)
print()
print(str)

# Fechando
fo.close()


# exemplo2
# myFile = open('scores.txt', 'r')
# print("Reading...\n" + myFile.read(17))
# linhaAtual = myFile.tell()
# print(f"Posição do cursor, linha. {linhaAtual}")
# print()
# myFile.seek(0) # retorna o cursor para i inicio
# print("Reading again...\n" + myFile.read(17))
# print(f"Posição do cursor, linha. {linhaAtual}")


#exemplo3
"""O método readline () lê uma linha inteira do arquivo. """

# fo = open('foo2.txt', 'r+')
# print("Nome do arquivo: ",fo.name)
# line = fo.readline()
# print("Lendo linha: ", line) # This is 1st line
# line = fo.readline(5)
# print("Lendo linha: ", line) # This
# fo.close()

# exemplo4

"""O método readlines () lê até EOF usando o método readline( ) e retorna uma lista
contendo as linhas. """

# fo = open('foo2.txt', 'r+')
# print("Nome do arquivo: ",fo.name)
# line = fo.readlines()
# print("Lendo linhas: ", line)
# line = fo.readlines(2)
# print("Lendo linhas: ", line)
