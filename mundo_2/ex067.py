# 067 Tabuada v. 3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.


while True:
    n = int(input('Digite um número para consultar sua tabuada: '))
    print('--'*10)
    if n < 0:
        break
    for c in range (0, 11):
        print(f'{n} x {c} = {n*c}')
    print('--' * 10)
print('Processo Finalizado')