# 078 Maior e Menores valores na lista
# Faça um programa que leia 5 valores numéricos e guarde-os numa lista. No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

lista_num = []
for c in range(0, 5):
    lista_num.append(int(input('Digite um número: ')))
    maior = max(lista_num)
    menor = min(lista_num)
print(f'O maior valor digitado foi {maior} e ele está na posicao {lista_num.index(maior)}.')
print(f'O menor valor digitado foi {menor} e ele está na posicao {lista_num.index(menor)}.')

# ou
lista_num = []
maior = 0
menor = 0
for c in range(0, 5):
    lista_num.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista_num[c]
    else:
        if lista_num[c] > maior:
            maior = lista_num[c]
        if lista_num[c] < menor:
            menor = lista_num[c]
print(f'Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_num):
    if v == menor:
        print(f'{i}...', end='')
