#!/usr/bin/env python3

# Itertools Part 2
import itertools

'''Permutations, order matters'''

election = {1:'Pedro', 2:'Giovanna', 3:'Erick'}
# for p in itertools.permutations(election):
#     print(p)

# for p1 in itertools.permutations(election.values()):
#     print(p1)

print()


'''Combinations: Order does not matter'''
#
# colors = ["Vermelho", "Azul", "Roxo", "Laranja", "Amarelo", "Lilás"]
# for c in itertools.combinations(colors, 2): # 2 elements
#     print(c)
