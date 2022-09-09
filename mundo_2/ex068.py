# 068 Jogo do Par ou Ímpar
# Faça um programa que jogue par ou ímpar como computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitoria = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 100)
    soma = jogador + computador
    ip = ' '
    while ip not in 'PI':
        ip = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}.')
    if ip == 'P':
        if soma % 2 == 0:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif ip == 'I':
        if soma % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você ganhou')
            vitoria += 1
print(f'GAME OVER! Você venceu {vitoria} vezes. ')
