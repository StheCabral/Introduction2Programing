players_numbers_temp = input()
target = int(input())
#tratando a lista
players_numbers_temp = players_numbers_temp.replace("[", "")
players_numbers_temp = players_numbers_temp.replace("]", "")
players_numbers = [int(x) for x in players_numbers_temp.split(",")]
dic_players = {}
result = []
for i in range (len(players_numbers)):
    dic_players[i] = players_numbers[i] # {0: 1, 1: 4, 2: 6}
for key in dic_players.keys():
    for i in range (1, len(players_numbers)):
        if ((key + i) < len(players_numbers)):
            n1 = dic_players[key]
            n2 = dic_players[key+1]
            if ((dic_players[key] + dic_players[key+i]) == target):
                result = [key, key+i]
print(result)
