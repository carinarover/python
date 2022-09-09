# 093 Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

futebol = {}
futebol['nome'] = str(input('Digite o nome do jogador de futebol: '))
partidas = int(input('Quantas partidas ele jogou? '))

n = []
for g in range(0, partidas):
     n.append(int(input(f'Quantos gols ele fez na partida {g+1}: ')))
     futebol['gols'] = n
futebol['total'] = sum(n)

print('-' * 50)
print(futebol)
print('-' * 50)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 50)
print(f'O jogador {futebol["nome"]} jogou {partidas} partidas.')
for g, i in enumerate(futebol['gols']):
    print(f'    -> Na partida {g+1}, fez {i} gols.')
print(f'Total de gols: {futebol["total"]}')
