#!/usr/bin/env python3


a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky','rain')
y = 'bear'

if a and b:
    print('Expressão a AND b: True')
else:
    print('Expressão a AND b: False') # True and False = False

if a or b:
    print('Expressão a OR b: True') # True or False = True
else:
    print('Expressão a OR b: False')

# Negando valores
if not b:   # Not b(False) = True
    print("Expression 'if not b' is True")
else:
    print("Expression 'if not b' is False")

# Membership
if y in x:   # y (bear) in x (bear ...)
    print("Expression 'y in x' is True")
else:
    print("Expression 'y in x' is False")
