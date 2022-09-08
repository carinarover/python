# 005 Antecessor e Sucessor
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('O número digitado é {}, seu antecessor é {} e seu sucessor é {}.'.format(n, a, s))

# ou
n = int(input('Digite um número: '))
print('O número digitado é {}, seu antecessor é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))