# 108 Formatando moedas em Python
# Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# valor monetário formatado.

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',') #formata com 8 casas decimais a direita, sendo 2 após a vírgula