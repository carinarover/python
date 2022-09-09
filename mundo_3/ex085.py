# 085 Listas com pares e ímpares
# Crie um programa onde um usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os
# valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

n = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort() #colocando em ordem
n[1].sort() #colocando em ordem
print(f'Você digitou os números {n}')
print(f'Os números pares digitados são {n[0]}')
print(f'Os números ímpares digitados são {n[1]}')
