# 112 Entrada de dados monetários
# Dentro do pacote utilidadesCeV que criamos no Desafio 11, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que
# seja capax de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.


from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)