# 064 Tratando varios valores v. 1.0
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('Digite um número [999 para parar]: '))
palpites = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    palpites += 1
print('Processo finalizado com {} tentativas.'.format(palpites))

# ou
n = 0
palpites = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    palpites += 1
print('Processo finalizado com {} tentativas.'.format(palpites-1))

# ou
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))