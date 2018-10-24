lot_2d = [
    ['Toyota', 'Audi', 'BMW'],
    ['Lexus', 'Jeep'],
    ['Honda', 'Kia', 'Mazda']
]
# print(lot_2d)

# Acessanod via indice
#print(lot_2d[0])
# print(lot_2d[0][0])

# for x in lot_2d:
#     print(x)

for floor in lot_2d:
    for row in floor:
        print(row)

# print('-' * 40)
# lot_3d = [
#     [
#         ['Tesla', 'Fiat', 'BMW'],
#         ['Honda', 'Jeep'],
#         ['Saab', 'Kia', 'Ford']
#     ],
#     [
#         ['Subaru', 'Nissan'],
#         ['Volvo']
#     ],
#     [
#         ['Mazda', 'Chevy'],
#         ['Fusca'],
#         ['Volkswagen']
#     ]
# ]
#
# #print(lot_3d)
# # todos os carros
# for floor in lot_3d:
#     for row in floor:
#         for car in row:
#             print(car)

# Pegando apenas o primeiro carro
# for floor in lot_3d:
#     for row in floor:
#         print(row[0])
