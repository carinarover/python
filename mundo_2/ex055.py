# 055 Maior e menor sequência
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

lista = []
for c in range(0, 5):
    lista.append(float(input('Digite o peso da pessoa: ')))
print('O maior peso é {} Kg.'.format(max(lista)))
print('O menor peso é {} Kg.'.format(min(lista)))

# ou

maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} Kg e o menor peso lido foi de {} Kg.'.format(maior, menor))
