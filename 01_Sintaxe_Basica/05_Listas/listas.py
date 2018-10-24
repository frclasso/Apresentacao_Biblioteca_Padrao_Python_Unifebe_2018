# minhaLista = ['palavras', 'a', 1, 2.3, (4,5,6), [7,8,9]]
# print(minhaLista)

cursos = ['Historia', 'Matematica', 'Fisica','Quimica', 'Economia' ]

# Indexando
# print(cursos[0])
# print(cursos[1])
# print(cursos[2])
# print(cursos[3])

# # Slincing
# print(cursos[:]) # acessa lista completa
# print(cursos[0:4]) # do primeiro ao quinto(exclusivo)
# print(cursos[:3]) # do primeiro ao terceiro(exclusivo)
# print(cursos[2:]) # a partir do terceiro elemento

# Adicionando items
# cursos.append('Artes')  # adiciona ao final da lista
# cursos.insert(0, 'Biologia') # adiciona na posição do indice especifidao
# print(cursos)
# print()

# Add items from another list
#cursos_2 = ['Fotografia', 'Musica']

# cursos.insert(0, cursos_2)
# print(cursos)
# print(cursos[0])

# comentar o bloco superior
# cursos.extend(cursos_2)
# print(cursos)


# Removing items

# # Usisng remove method
# cursos.remove('Matematica')
# print(cursos)

# # Using pop method (last object)
# cursos.pop()
# print(cursos)
#
# # Using del method
# del cursos[0] # deleta via indice o primeiro elemento
# print(cursos)
#
#
#
# numeros = [1,2,3,5,11,10,12,0,7,6,9,8,4]
# numeros.sort()
# print(numeros)
# #numeros.sort(reverse=True)
# numeros.reverse()
# print(numeros)
#

# Acessando valores via indice
# print('Indice de Fotografia: {}'.format(cursos.index('Fotografia')))
# print(cursos[5])

# copiando elementos de uma lista
# cursos3 = cursos
# print(cursos)
# print(cursos3)
# print(f'Identificador de cursos  {id(cursos)}')
# print(f'Identificador de cursos3 {id(cursos3)}')
# cursos3[0] = 'Letras'
# print(cursos3)
# print(cursos)

#
# cursos4 = cursos[:]
# print(cursos4)
# print(cursos)
# print(f'Identificador de cursos4 {id(cursos4)}')
# print(f'Identificador de cursos {id(cursos)}')
# cursos4[0] = 'Finanças'
# print(cursos4)
# print(cursos)
#
'''criando uma lista vazia'''
# listaVazia = []
# print(listaVazia)
# print(type(listaVazia))

'''Deletando a lista'''
#del cursos4
#print(cursos4)