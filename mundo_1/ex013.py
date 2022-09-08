# 013 Reajuste Salarial
# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
s = float(input('Digite o salário do funcionário: R$ '))
n = s + (s*0.15)
print('O novo salário do funcionário, com 15% de aumento, será R$ {:.2f}.'.format(n))