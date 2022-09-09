# 059 Criando um menu de opções
# Crie um programa que leia dois valores e mostre um menu como o abaixo:
# Seu programa deverá realizar a opção solicitada em cada caso:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
print('')

opcao = 0

while opcao != 5:
    opcao = int(input('------------------------------------------------------------------ \n'
                      'Escolha a opção que deseja executar com os números digitados: \n[1] Somar \n[2] Multiplicar \n[3] Qual o '
                      'maior número \n[4] Digitar novos números \n[5] Sair do programa \n-->> SUA OPÇÃO: '))
    if opcao == 1:
        print('Você digitou os números {} e {}. O somatório entre eles é {}.'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('Você digitou os números {} e {}. A multiplicação entre eles resulta em {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Você digitou os números {} e {}. O maior deles é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Você digitou os números {} e {}. O maior deles é {}.'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    elif opcao == 5:
        print('Finalizando...')
        print('==' * 15)
    else:
        print('Opção inválida. Tente novamente')
sleep(2)
print('FIM DO JOGO!')