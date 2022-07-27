total_inputs = 0
good_jokes = 0
inputs = "none"
while (inputs != "Fim do Show!"):
    inputs = input()
    total_inputs += 1
    if (inputs == "BAZINGA!"):
        good_jokes +=1

total_jokes = (total_inputs) / 2
score = (good_jokes / total_jokes) * 100

if (score > 60):
    print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
elif (score < 40):
    print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
else:
    print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")