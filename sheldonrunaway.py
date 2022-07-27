total_planets = int(input())
while (total_planets < 2):
    print("Número inválido, tente novamente")
    total_planets = int(input())

previous_distance = 10

for i in range (total_planets):
    name = input()
    radius = float(input())
    mass = float(input())
    temperature = int(input())
    planet_score = (radius + mass + (temperature/288)) / 3
    distance = abs(1 - planet_score)
    if (distance < previous_distance):
        winner_name = name
        winner_score = planet_score
        previous_distance = distance

if (winner_score == 1):
    print(f"{winner_name} é perfeito!")
elif (winner_score > 1):
    print(f"{winner_name} vai ter que servir")
elif (winner_score < 1):
    print(f"{winner_name} vai dar pro gasto")