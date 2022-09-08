# 033 Maior e menor valores
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

menor = a
if b < a and b > c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {} e o maior valor digitado foi {}.'.format(menor, maior))
