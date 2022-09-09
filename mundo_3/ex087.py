# 087 Mais sobre Matriz em Python
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores pares da terceira coluna
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somav = maiorv = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print()
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()
print()
print(f'A soma dos valores pares é {par}.')
for linha in range(0,3):
    somav += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somav}.')
for coluna in range(0,3):
    if coluna == 0:
        maiorv = matriz[1][coluna]
    elif matriz[1][coluna] > maiorv:
        maiorv = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorv}.')