# 046 Contagem regressiva
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
# 1 segundo entre elas.

from time import sleep

for f in range(10, -1, -1):
    print(f)
    sleep(1)
print('BUM BUM BOW')
