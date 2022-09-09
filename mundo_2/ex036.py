# 036 Aprovando empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa que deseja comprar: R$ '))
salario = float(input('Digite o seu salário: R$ '))
pagar = float(input('Digite em quantos anos deseja pagar a casa: R$ '))

p = salario * 0.3
anos = pagar * 12
valor = casa / anos

if valor <= p:
    print('Empréstimo concedido. Você pagará R$ {:.2f} por mês durante {:.0f} meses.'.format(valor, anos))
else:
    print('Empréstimo negado. O valor R$ {:.2f} ultrapassa o limite de 30% do seu salário.'.format(valor))