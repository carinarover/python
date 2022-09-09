# 073 Tuplas com Times de Futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) os 5 primeiros
# b) os 4 últimos colocados
# c) times em ordem alfabética
# d em que posição está o time da Chapecoense.

times = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'America MG',
         'Atletico GO', 'Santos', 'Ceara', 'Internacional', 'São Paulo', 'Atletico PR', 'Cuiaba', 'Juventude', 'Gremio',
         'Bahia', 'Sport', 'Chapecoense')
print(f'Os cinco primeiros colocados no Brasileirão são: {times[0:5]}.')
print(f'Os quatro últimos colocados no Brasileirão são: {times[16:20]}.')
# ou
print(f'Os quatro últimos colocados no Brasileirão são: {times[-4:]}.')
print(f'Os times em ordem alfabética: {sorted(times)}.')
print(f'O Chapeconese está na {times.index("Chapecoense") + 1} posição.')