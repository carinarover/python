# 031 Custo da Viagem
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
# para viagens de até 200 Km e R$ 0,45 para viagens mais longas.

d = int(input('Digite a distância da viagem em Km: '))
print('A distância percorrida foi de {}.'.format(d))
if d < 200:
    print('Você pagará R$ {:.2f} pela viagem.'.format(d * 0.5))
else:
    print('Você pagará R$ {:.2f} pela viagem.'.format(d * 0.45))