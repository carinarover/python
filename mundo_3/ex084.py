# 084 Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma lista com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

dados = []
todos = []
quant = 0
maior = menor = 0

while True:
    dados.append(str(input('Digite o nome da pessoa: ')).upper())
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(todos) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    todos.append(dados[:]) #faz copia lista
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    quant += 1
    if resp in 'N':
        break
    if 'S' != resp != 'N':
        resp = str(input('Opção não existente. Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você cadastrou {quant} pessoas, que são {todos}.') #ou sem contador e utilizar len(todos)
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in todos:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end='')
for p in todos:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
