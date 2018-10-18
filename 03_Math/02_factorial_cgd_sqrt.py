#!/usr/bin/env python3

import math

# Factorial
"""Fatorial é um número natural inteiro positivo, o qual é 
representado por n! O fatorial de um número é calculado pela
multiplicação desse número por todos os seus antecessores até 
chegar ao número 1."""

# Modo tradicional


def factorialTrad(n):
    if n == 0:
        return 1
    else: return n * factorialTrad(n-1)


print(f"fatorialTrad:{factorialTrad(3)}")

# Utilizando a função math.factorial()
print(f"Fatorial utilizando math.factorial(): {math.factorial(3)}")
print()

# raiz quadrada / square root
print(f"Raiz quadrada: {math.sqrt(64)}")
print()

# Potencia pow()
print(f"Tres ao quadrado: {3 ** 2}")
print(f"Tres ao quadrado utilizando math.pow(): {math.pow(3,2)}")


"""MDC (Maximo Divisor Comum - 
GCD(GCD Greatest common denominator)"""

# Definindo uma função tradicional


def mdc(dividendo,divisor):
    if divisor == 0:
        return dividendo
    return mdc(divisor, dividendo % divisor)
print()

print(f'MDC 10 e 5 ==> {mdc(10, 5)}')
print(f'MDC 32 e 24 ==> {mdc(32, 24)}')
print(f'MDC 5 e 3 ==> {mdc(5, 3)}')
print()

# Utilizando a função math.gcd()
print(f"GCD de 10 e 5: {math.gcd(10, 5)}")
print(f"GCD de 32 e 24: {math.gcd(32, 24)}")
print(f"GCD de 5 e 3 : {math.gcd(5, 3)}")
print()


# Degrees and Radians
print(math.radians(360)) # convert degrees to radians
print(math.pi*2) # How many radians has a full circle
print(math.degrees(math.pi*2)) # convert radians to degrees

