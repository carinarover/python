# 070 Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000
# c) Qual é o nome do produto mais barato

lista_preco = []
mais = 0
contar = menor = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$ '))
    contar += 1
    lista_preco.append(preco)
    if preco >= 1000:
        mais +=1
    if contar == 1 or preco < menor:
        menor = preco
        barato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Você deseja cadastrar mais algum produto? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('Compras finalizadas.')
print(f'O total gasto na compra foi de R$ {sum(lista_preco)}')
print(f'Foram comprados {mais} produtos que custavam mais de R$ 1000,00.')
print(f'O produto mais barato custou R$ {min(lista_preco)} e foi {barato}.')