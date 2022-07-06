D = int(input())
C = int(input())


tempo_de_jogo_por_dia = 90
tempo_jogo = D * tempo_de_jogo_por_dia
tempo_casa = tempo_jogo / C
ticks_casa = 1200 * tempo_casa

print(int(ticks_casa))