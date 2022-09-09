# 052 Númerosp primos
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(numero, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")