#!/usr/bin/python3

for letter in 'Python': # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

print()

# #exemplo 2
# var = 10 # Second Example
#
# while var > 0:
#     var = var -1
#     if var == 5:
#         continue
#     print('Current variable value :', var)
# print("Good bye!")
#
# #exemplo3
#
# animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')
#
# for pet in animals:
#     if pet == 'dog': continue  # NAO EXIBE 'dog'
#     #if pet == 'velociraptor': break   # Descomente essa linha
#     print(pet)
# else:
#     print("That's  all the animals")