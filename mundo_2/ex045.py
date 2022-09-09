# 045 GAME: Pedra, Papel, Tesoura
# Crie um programa que faça o programa jogar Jokenpô com você.

from random import randint
from time import sleep

jogo = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('==-== JOGO JOKENPÔ ==-==')
print('Suas opções: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA ')
print('==-==' * 5)

jogador = int(input('Digite a sua opção de jogo: '))
print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('')
print('Computador jogou {}'.format(jogo[computador]))
print('Você jogou {}'.format(jogo[jogador]))
print('')


if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada inválida. Tente novamente com um número entre 0 e 3.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    else:
        print('Jogada inválida. Tente novamente com um número entre 0 e 3.')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida. Tente novamente com um número entre 0 e 3.')
