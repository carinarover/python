# 099 Função que descobre o maior
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    cont = maior = 0
    print('=' * 50)
    print('Analisando os valores passados...')
    sleep(2)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(4, 5, 6, 7)
maior(3, 56, 10, 23, 34, 67, 30)