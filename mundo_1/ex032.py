# 032 Ano Bissexto
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date

ano = int(input('Que ano você gostaria de saber se é bissexto? '))

if ano == 0:
    ano = date.today().year # Se colocar zero, analisar ano atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

# todos os anos múltiplos de 4 que também não são múltiplos de 100, com exceção dos múltiplos de 400, deverão ser anos bissextos