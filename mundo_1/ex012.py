# 012 Calculando Descontos
# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto: R$ '))
desconto = preco - (preco * 0.05)
print('O preço do produto com desconto de 5% ficará R$ {:.2f}.'.format(desconto))