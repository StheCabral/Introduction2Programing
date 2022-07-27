target = int(input())
progresso = 0
score = 0

while progresso >= 0:
    progresso = int(input())
    if (progresso > 0):
        for i in range (1,(progresso + 1)):
            score += i

if (score == target):
    print("Parabéns!!! Você é o mais inteligente")
elif (score < target):
    print("Ainda falta um pouco...")
elif(score > target):
    if (score < (20*target)):
        print("Parece que o gêniozinho passou um pouco do local...")
    elif(((20 * target) <= score) and (score <= (100 * target))):
         print("Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?")
    elif(score > (100 * target)):
        print("Hum... acho que o gêniozinho não tem mesmo doutorado ein...")