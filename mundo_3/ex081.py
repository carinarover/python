# 081 Extraindo dados de uma lista
# Crie um programa que vai ler varios números e colocar em uma lista. Depois disso, mostre:
# a) quantos números foram digitados
# b) a lista de valores, ordenada de forma decrescente
# c) se o valor 5 for digitado e está ou não na lista

lista = []
sn = 'S'
quant = 0

while sn == 'S':
    n = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    quant += 1
    lista.append(n)
print(f'Processo Finalizado. Você digitou {quant} números.')
print(f'Os números digitados foram {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não faz parte da lista.')
