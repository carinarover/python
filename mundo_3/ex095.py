# 095 Aprimorando os dicionários
# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador

time = []
futebol = {}
n = [] #partidas

while True:
    futebol.clear()
    futebol['nome'] = str(input('Digite o nome do jogador de futebol: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    n.clear()
    for g in range(0, partidas):
        n.append(int(input(f'Quantos gols ele fez na partida {g+1}: ')))
    futebol['gols'] = n[:]
    futebol['total'] = sum(n)
    time.append(futebol.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas com F ou M: ')
    if resp == 'N':
        break
# Respostas
print('-' * 50)
print('cod    ', end='')
for i in futebol.keys():
    print(f'{i:<15}', end='') #faz cabeçalho
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>6}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código da {busca}!')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    -> Na partida {i + 1}, fez {g} gols.')
    print('-' * 40)