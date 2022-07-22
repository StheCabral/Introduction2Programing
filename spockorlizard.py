rounds = int(input())

s_score = 0
r_score = 0
for i in range (0, rounds):
    sheldon = input()
    rajesh = input()

    if (sheldon == "lagarto"):
        if (rajesh == "spock"):
            s_score += 1
        elif (rajesh == "tesoura"):
            r_score += 1
    elif (sheldon == "spock"):
        if (rajesh == "lagarto"):
            r_score += 1
        elif (rajesh == "tesoura"):
            s_score += 1
    elif (sheldon == "tesoura"):
        if (rajesh == "spock"):
            r_score += 1
        elif (rajesh == "lagarto"):
            s_score += 1

if (s_score > r_score):
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif (r_score > s_score):
    print("ENGOLE ESSA, SHELDON!")
else:
    print("Oh não, precisamos de outra rodada.")