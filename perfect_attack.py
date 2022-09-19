players_numbers_temp = input()
target = int(input())
#tratando a lista
players_numbers_temp = players_numbers_temp.replace("[", "")
players_numbers_temp = players_numbers_temp.replace("]", "")
players_numbers = [int(x) for x in players_numbers_temp.split(",")]

for j in range (len(players_numbers)):
    for i in range (1, (len(players_numbers) - 1)):
        if ((i+j) < len(players_numbers)):
            if ((players_numbers[j] + players_numbers[j+i]) == target):
                result = [players_numbers[j], players_numbers[j+i]]
print(result)
                
