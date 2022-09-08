# 029 Radar eletrônico
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/k, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

v = int(input('Digite a velocidade do carro: '))
print('A velocidade do carro é {} km/h.'.format(v))
m = (v - 80) * 7
if v > 80:
    print('Você ultrapassou o limite de 80km/h. Deverá pagar uma multa de R$ {}.'.format(m))
else:
    print('Você está dentro do limite de velocidade permitido de 80km/h.')