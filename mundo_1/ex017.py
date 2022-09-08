# 017 Catetos e Hipotenusa
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('Com um cateto oposto de {} e um cateto adjacente de {}, o triângulo retângulo tem \numa hipotenusa de {:.2f}.'.format(co, ca, h))

#ou
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('Com um cateto oposto de {} e um cateto adjacente de {}, o triângulo retângulo tem \numa hipotenusa de {:.2f}.'.format(co, ca, h))
