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
# # print("Nome do arquivo: ",fo.name)
# # line = fo.readline()
# # print("Lendo linha: ", line) # This is 1st line
#
# line = fo.readline(11) # os 5 primeiros caracteres da segunda linha
# print("Lendo linha: ", line) # This
# fo.close()


#exemplo3

"""O método readlines () lê até EOF usando o método readline( ) e retorna uma lista
contendo as linhas. """

# fo = open('foo.txt', 'r+')
# print("Nome do arquivo: ",fo.name)
# line = fo.readlines()
# print("Lendo linhas: ", line)
#
# '''exibe a posicao do cursor'''
# print(fo.tell())
# line = fo.readlines()
# print("Lendo linhas: ", line)
#
# """Retornando o cursor para o inicio do arquivo"""
# fo.seek(0)
# print(fo.tell())
# line = fo.readlines(25)  # 26 primeiro caractere da Segunda linha
# print("Lendo linhas: ", line)



