# 044 Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3 x ou mais no cartão: 20% de juros

produto = float(input('Digite o valor do produto que comprou: R$ '))

print('Para pagamento do produto, temos as seguintes opções:'
      '\n[1] À vista dinheiro/cheque'
      '\n[2] À vista no cartão'
      '\n[3] Em até 2x no cartão'
      '\n[4] 3 x ou mais no cartão')

opcao = int(input('Selecione a opção do pagamento escolhida: '))

if opcao == 1:
    valor = produto - produto * 0.1
    print('Você escolheu a opção À VISTA EM DINHEIRO, que lhe concede um desconto de 10%. Seu valor final é R$ {:.2f}'.format(valor))
elif opcao == 2:
    valor = produto - produto * 0.05
    print('Você escolheu a opção À VISTA NO CARTÃO, que lhe concede um desconto de 5%. Seu valor final é R$ {:.2f}'.format(valor))
elif opcao == 3:
    valor = produto
    parcela = valor / 2
    print('Você escolheu a opção EM ATÉ 2X NO CARTÃO, e pagará o valor normal do produto. Seu valor final é R$ {:.2f}, sendo '
          '2 parcelas de R$ {:.2f} cada.'.format(valor, parcela))
elif opcao == 4:
    valor = produto + produto * 0.2
    vezes = int(input('Digite em quantas parcelas deseja pagar: '))
    total = valor / vezes
    print('Você escolheu a opção 3X OU MAIS NO CARTÃO, e pagará 20% de juros. Seu valor final é R$ {:.2f}, dividido em {} '
          'parcelas, com um total de R$ {:.2f} por parcela.'.format(valor, vezes, total))
else:
    print('Opção não existe, tente novamente.')