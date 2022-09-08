# 004 Dissecando uma variável
# Faça um programa que leai algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('É um número?', a.isnumeric())
print('É uma letra?', a.isalpha())