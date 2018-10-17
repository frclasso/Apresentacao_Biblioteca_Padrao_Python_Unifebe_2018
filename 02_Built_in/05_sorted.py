
# Ordem crescente
pointsInGame = [0,-10,15,-2,1,12]
print(sorted(pointsInGame))

# Ordem alfabetica
children =['Sue', 'Jerry','Linda']
print(sorted(children))

# Fornecendo uma chave como parâmetro
print(sorted("My favorite child is Linda".split(), key=str.upper))

# modo reverso
print(sorted(pointsInGame, reverse=True))

leaderBoard = {231:'CKL', 123:'ABC', 432:'JKC'}
print(sorted(leaderBoard, reverse=True))

students = [('alice','B', 12), ('eliza', 'A', 16), ('tony','C', 15)]
print(sorted(students, key=lambda student:student[0])) # key=nome
print(sorted(students,key=lambda student:student[1]))  # key=letra
print(sorted(students , key=lambda student:student[2])) # key=numero