# 098 Função de Contador
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
# programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até zero, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador(i, f, p):
    print('~' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)
    if p < 0: #para caso de passos negativos
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont +=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(10, 100, 5)
contador(10, 1, 1)
print('=' * 50)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)




