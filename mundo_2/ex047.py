# 047 Contagem de pares
# Crie um programa que mostre na tela todos os números pares que estão no intervalo 1 e 50

for pares in range(2, 51, 2):
    print(pares, end=' ')
print('Opção 1')

#ou
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Opção 2')