# 075 Lista de Preços com Tupla
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, organizando os dados de forma tabular.

listacompras = ('Carne', 72.40,
         'Leite', 3.70,
         'Arroz', 5.60,
         'Maçã', 6.78,
         'Banana', 5.79,
         'Abacaxi', 6.22,
         'Ovos', 8.99)
print('-' * 40)
print('Lista de compras')
print('-' * 40)
for item in range(0, len(listacompras)):
    if item % 2 == 0:
        print(f'{listacompras[item]:.<30}', end='')
    else:
        print(f'R$ {listacompras[item]:>5.2f}')