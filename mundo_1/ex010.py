# 010 Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1 = R$ 3.27
d = float(input('Digite quanto dinheiro você tem: R$ '))
print('Você pode comprar {:.2f} dólares'.format(d/3.27))