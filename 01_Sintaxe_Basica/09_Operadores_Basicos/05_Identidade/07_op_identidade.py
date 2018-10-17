#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = 20
b = 20
print('Line 1', 'a=', a,'ID:', id(a),'\n', '\t', 'b=', b,'ID:', id(b))

print(a is b)

print(id(a) == id(b))
print()

b = 30
print('Line 2','a=',a,'ID:',id(a),'\n','\t', 'b=',b,'ID:',id(b))
print(a is not b)
print()

c = a
print(c is a)