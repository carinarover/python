# 097 Um print especial
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.

def mensagem(msg):
    tamanho = len(msg)
    print('~' * (tamanho + 6))
    print(f'   {msg}')
    print('~' * (tamanho + 6))

mensagem('Boa tarde, pessoal!')