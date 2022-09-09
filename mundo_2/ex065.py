# 065 Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from statistics import mean
lista_n = []
sn = 'S'
tentativas = 0

while sn == 'S':
    n = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    tentativas += 1
    lista_n.append(n)
print('Processo Finalizado. Você digitou {} números e a média entre eles foi {}.'.format(tentativas, mean(lista_n)))
print('O maior número foi {} e o menor número foi {}.'.format(max(lista_n), min(lista_n)))

