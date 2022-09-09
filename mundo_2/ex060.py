# 060 Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para descobrir seu fatorial: '))
f = n
c = 1 #não pode começar com 0, pois se multiplicar qualquer coisa com 0, dará zero
while f > 0:
    print('{}'.format(f), end = '') #end para não pular de linha
    print(' x ' if f > 1 else ' = ', end = '')
    c = c * f # ou c *=c
    f -= 1
print('{}'.format(c))


# ou
from math import factorial
n = int(input('Digite um número para descobrir seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
