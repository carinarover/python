# 006 Dobro, Triplo, Raiz Quadrada
# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print('O número digitado é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
# :.2f arredonda para duas casas decimais