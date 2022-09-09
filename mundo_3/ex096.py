# 096 Função que calcula área
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area():
    print('-'*30)
    print('   CONTROLE DE TERRENOS')
    print('-' * 30)
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    print(f'A área de um terreno {l}x{c} é {l*c} m².')

area()