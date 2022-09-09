# 058 Jogo da Advinhação v. 2.0
# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n = randint(0, 10)
print('--=' * 13)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. Será que você consegue advidinhar qual foi? ')
print('--=' * 13)

acertou = False
palpites = 0

while not acertou:
    a = int(input('Qual número eu pensei? '))
    palpites += 1
    if a == n:
        acertou = True
    else:
        if a < n:
            print('Mais... Tente mais uma vez.')
        elif a > n:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
