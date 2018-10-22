# exemplo1

# Abrindo o arquivo
# fo =open('foo.txt', 'r+')
# str = fo.read()  # Altere esse valor, 26 primeira linha
# print("Lendo o arquivo:",fo.name)
# print()
# print(str)
#
# # Fechando
# fo.close()


# exemplo2

"""O método readline () lê uma linha inteira do arquivo. """

# fo = open('foo.txt', 'r+')
# print("Nome do arquivo: ",fo.name)
# line = fo.readline()
# print("Lendo linha: ", line) # This is 1st line
# line = fo.readline(5) # os 5 primeiros caracteres da primeira linha
# print("Lendo linha: ", line) # This
# fo.close()


#exemplo3

"""O método readlines () lê até EOF usando o método readline( ) e retorna uma lista
contendo as linhas. """

fo = open('foo.txt', 'r+')
print("Nome do arquivo: ",fo.name)
line = fo.readlines()
print("Lendo linhas: ", line)
print(fo.tell()) # posicao do cursor
line = fo.readlines()
print("Lendo linhas: ", line)
fo.seek(0)  # cursor volta pro inicio do arquivo
print(fo.tell())
line = fo.readlines(26)  # 26 primeiro caractere da Segunda linha
print("Lendo linhas: ", line)



