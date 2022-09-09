# 086 Matriz em Python
# Crie um programa que crie uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
# com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print()
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='') #:^5 para garantir que fique centralizado intependente do número de dígitos
    print() #Toda vez que quebra a coluna, ele dá um enter