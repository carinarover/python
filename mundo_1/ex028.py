# 028 Jogo da advinhação v. 1.0
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('--=' * 13)
print('Estou pensando em um número de 0 a 5')
print('--=' * 13)
a = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
n = randint(0, 5)

if a==n:
    print('PARABÉNS! Você venceu!')
else:
    print('O número que eu pensei foi {}, você perdeu.'.format(n))