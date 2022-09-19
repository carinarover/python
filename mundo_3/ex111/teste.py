# 111 Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira as funções utilizadas nos
# Desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 35, 22)