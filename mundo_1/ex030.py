# 030 Par ou ímpar
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
r = n % 2 #resto da divisão porque resto da divisão de qualquer número par aqui será 0
if r == 0:
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))