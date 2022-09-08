# 018 Seno, Cosseno e Tangente
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an = float(input('Digite o ângulo: '))
print('O seno do ângulo {} é {:.2f}'.format(an, math.sin(math.radians(an))))
print('O cosseno do ângulo {} é {:.2f}'.format(an, math.cos(math.radians(an))))
print('A tangente do ângulo {} é {:.2f}'.format(an, math.tan(math.radians(an))))