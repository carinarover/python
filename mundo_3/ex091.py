# 091 Jogo de Dados em Python
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.

from random import randint
from operator import itemgetter #para colocar em ordem de chave(0) ou valor(1)
from time import sleep

jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)
         }
ordem = []
for k, v in jogos.items():
    print(f'{k} tirou {v} no jogo de dados.')
ordem = sorted(jogos.items(), key=itemgetter(1), reverse=True) #está como lista
# print(ordem)

print('=' * 34)
print('      RANKING DOS JOGADORES       ')
for i, v in enumerate(ordem):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)