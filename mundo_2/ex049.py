# 049 Tabuada v.2
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para consultar sua tabuada: '))
for c in range (0, 11):
    print('{} x {} = {}'.format(n, c, n*c))