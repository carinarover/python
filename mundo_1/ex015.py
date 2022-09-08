# 015 Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0.15 por Km rodado.
km = int(input('Digite a Km que o carro percorreu: '))
d = int(input('Digite por quantos dias o carro foi alugado: '))
dia = 60 * d
preco = dia + (km * 0.15)
print('Considerando que o carro foi alugado por {} dias, e percorreu {} Km. Logo, o valor a ser pago é de R$ {:.2f}.'.format(d, km, preco))
