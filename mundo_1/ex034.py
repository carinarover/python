# 034 Aumentos múltiplos
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$ '))
maior = salario * 0.1 + salario
menor = salario * 0.15 + salario
if salario > 1250:
    print('Seu aumento será de 10%, e seu novo salário será R$ {:.2f}'.format(maior))
else:
    print('Seu aumento será de 15%, e seu novo salário será R$ {:.2f}'.format(menor))