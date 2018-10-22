#!/usr/bin/env python3

# importando o modulo random
import random

# random numbers
print(f"Numeros aleatorios entre 0 e 1: {random.random()}") # imprime um numero entre 0 e 1
print()

decider = random.randrange(2) # 0 OU 1
if decider == 0:
    print('ZERO')
else:
    print('UM')
print(f'Decider is:', decider)
print()

print("Imprime um numero no intervalo entre 1 e 7: " + str(random.randrange(1, 7)))
print()

# random sample
megaSena = random.sample(range(61), 6) # range de 0 a 60, gerando amostra  de 6 numeros
print(f"Numeros da Mega Sena: {megaSena}")
print()

# random choice
possiblePets = ['cat', 'dog', 'fish']
print(random.choice(possiblePets))
print()

# random shuffle
cards = ['Jack', 'Queen', 'Ace', 'King']
random.shuffle(cards)
print(cards)