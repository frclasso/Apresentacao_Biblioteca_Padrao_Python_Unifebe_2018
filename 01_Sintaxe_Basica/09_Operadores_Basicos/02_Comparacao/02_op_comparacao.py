#!/usr/bin/env python3
# -*- coding:utf-8 -*-


a = 21
b = 10

print(f'a == b: {a == b}')
print(f'a != b: {a != b}')
print(f'a < b: {a < b}')
print(f'a > b: {a > b}')

a, b = b, a  # values of a and b swapped. a becomes 10, b becomes 21

print(f'a <= b: {a <= b}')
print(f'b >= a: {b >= a}')

