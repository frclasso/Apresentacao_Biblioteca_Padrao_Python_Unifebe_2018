"""Tuplas sao imutaveis, sendo as vezes chamadas de lisas somente leitura
   Permitem algumas operações semelhantes as de listas"""


# Definindo tuplas
minhaTupla = ('abcd', 786, 2.23, 'john', 70.2)

tinyTupla = (123, 'john')

print(minhaTupla)
# Indexando
print(minhaTupla[0])
print(minhaTupla[1])
print(minhaTupla[-1])
# Fatiando / Slicing
print(minhaTupla[2:])
print(minhaTupla[:5])
print(minhaTupla[2:5])
print(minhaTupla[:])

# Criando uma tupla a partir dos valores de outra tupla
novatupla = minhaTupla[0:3]
print(f'novaTupla: {novatupla}')

# Concatenando tuplas
outraTupla = minhaTupla + tinyTupla
print(f'Concatenando: {outraTupla}')

# metodo tuple
disciplinas = ['Historia', 'Matematica', 'Fisica','Quimica','Informática']
print(type(disciplinas))

disciplinasTuple = tuple(disciplinas)
print(type(disciplinasTuple))
print(disciplinasTuple)
print()

# Listas são mutáveis
list1 = ['Historia', 'Matematica', 'Fisica','Quimica','Informática']
list2 = list1
print(list1)
print(list2)

list1[0] = 'Biologia'  # Altera ambas as listas

print(list1)
print(list2)
print()

# Tuplas são imutáveis

#tuple_1 = ['Historia', 'Matematica', 'Fisica','Quimica','Informática']
#tuple_2 = tuple_1
#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Bio'  # Altera ambas as listas
#
#print(tuple_1)
#print(tuple_2)

# No entanto, uma lista pode ser alterada dentro de uma tupla
cursos = ('Historia', 'Matematica', 'Fisica','Quimica',
          'Informática',['Artes, Musica'])

print(cursos[5]) # ['Artes', 'Musica' ]
cursos[5].append('Cênicas')
print(cursos)

# Criando uma tupla vazia
tuplaVazia = ()
print(type(tuplaVazia))

# criando tupla com um unico elemento
tuplaUmElemento = 1,  # Os parenteses são opcionais, a vírgula é obrigatória
print(type(tuplaUmElemento))