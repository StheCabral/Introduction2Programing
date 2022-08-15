matchs = input().split(" ")
interferences = input().split(" ")
real_score = []
victories = 0
defeats = 0
draws = 0
lost_score = 0
for i in range (12):
    if (matchs[i] == "V"):
        if (interferences[i] == "1"):
            print("O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.")
            real_score.append(1)
            lost_score += 2
            draws += 1
        elif (interferences[i] == "0"):
            victories += 1
            real_score.append(3)
    elif (matchs[i] == "E"):
        if (interferences[i] == "1"):
            print("O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.")
            real_score.append(0)
            lost_score += 1
            defeats += 1
        elif (interferences[i] == "0"):
            real_score.append(1)
            draws += 1
    elif (matchs[i] == "D"):
        defeats += 1
        if (interferences[i] == "1"):
            print("O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!")
            real_score.append(0)
        elif (interferences[i] == "0"):
            real_score.append(0)
piece = 0
total = 0
for k in range (0, 12, 4):
    third = 0
    piece += 1
    if (k <=8):
        for j in range (4):
            index = k + j
            third += (real_score[index])
        if (third == 7):
            print(f"A pontuação na {piece}ª fatia de 4 jogos está dentro do planejado.")
        elif (third > 7):
            print(f"A pontuação na {piece}ª fatia de 4 jogos está com uma gordurinha de {(third - 7)} pontos.")
        elif (third < 7):
            print(f"A pontuação na {piece}ª fatia de 4 jogos está abaixo da planejada em {(7 - third)} pontos.")
    total += third
if (lost_score > 0):
    print(f"A maldição do sapo fez o Vascão perder {lost_score} pontos. Um número preocupante, que pode fazer diferença.")
elif ( lost_score == 0):
    print("A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.")
if (total == 21):
    print(f"Na reta final do campeonato, o Vasco garantiu um total de {total} pontos, com {victories} vitórias, {draws} empates e {defeats} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!")
elif (total < 21):
    print(f"Na reta final do campeonato, o Vasco fez somente {total} pontos, com {victories} vitórias, {draws} empates e {defeats} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.")