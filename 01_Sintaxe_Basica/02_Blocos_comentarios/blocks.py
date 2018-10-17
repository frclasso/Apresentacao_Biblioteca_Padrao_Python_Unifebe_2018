#!/usr/bin/env python3


# comentário de uma linha


"""Comentario de multiplas linhas,
   essa parte do código será ignorada
   pelo interpretador Python, sendo
   apenas texto simples/comum."""


x = 42
y = 73


if x < y:
    print('x < y: x is {}  and y is {}'.format(x, y))
elif x > y:
    print(('x > y: x is {} and y is {}'.format(x, y)))
elif x == y:
    print('x = y: x is {} and y is {}'.format(x, y))
else:
    print('Something else')

# exemplo 2
# count = 0
#
# while count < 5:
#     print(count, " is less than 5")
#     count = count + 1
# else:
#     print(count, " is not less than 5")

# exemplo 3
# no = int(input('any number: '))
#
# numbers = [11,33,55,39,55,75,37,21,23,41,13]
#
# for num in numbers:
#     if num == no:
#         print ('number found in list')
#         break
# else:
#     print('number not found in list')

