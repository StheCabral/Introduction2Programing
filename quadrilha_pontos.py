name = input()
step1 = input()
step2 = input()
step3 = input()
step4 = input()
step5 = input()

score = 0
marriage = 0
eliminated = ""


if (step1 == "Cumprimento" or step1 == "Serrote"):
    score += 100
elif (step1 == "Balancê"):
    score += 50
elif (step1 == "Passeio"):
    score += 70
elif (step1 == "Túnel" or step1 == "Despedida"):
    score = score
elif (step1 == "Casamento"):
    marriage +=1
elif(step1 != "Despedida"):
    eliminated = "yes"

if (step2 == "Cumprimento"):
    score += 10
elif (step2 == "Balancê"):
    score += 50
elif (step2 == "Passeio"):
    score += 70
elif (step2 == "Túnel"):
    score -= (10/100) * score
elif (step2 == "Serrote"):
     score += 100
elif (step2 == "Casamento"):
    marriage +=1
elif(step2 != "Despedida"):
    eliminated = "yes"

if (step3 == "Cumprimento"):
    score += 10
elif (step3 == "Balancê"):
    score += 50
elif (step3 == "Passeio"):
    score += 70
elif (step3 == "Túnel"):
    score -= (10/100) * score
elif (step3 == "Serrote"):
    score += 100
elif (step3 == "Casamento"):
    marriage +=1
elif(step3 != "Despedida"):
    eliminated = "yes"

if (step4 == "Cumprimento"):
    score += 10
elif (step4 == "Balancê"):
    score += 50
elif (step4 == "Passeio"):
    score += 70
elif (step4 == "Túnel"):
    score -= (10/100) * score
elif (step4 == "Serrote"):
    score += 100
elif (step4 == "Casamento"):
    marriage +=1
elif(step4 != "Despedida"):
    eliminated = "yes"

if (step5 == "Cumprimento"):
    score += 10
elif (step5 == "Balancê"):
    score += 50
elif (step5 == "Passeio"):
    score += 70
elif (step5 == "Túnel"):
    score -= (10/100) * score
elif (step5 == "Serrote"):
    score += 100
elif (step5 == "Despedida"):
    score += 35
elif (step5 == "Casamento"):
    marriage +=1
else:
    eliminated = "yes"


if (marriage > 0):
    score = score * 2


if (eliminated == "yes"):
    print(f"Poxa, {name}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.")
else:
    print(f"Parabéns, {name}! Bela apresentação. A pontuação foi de {score:.1f}!")