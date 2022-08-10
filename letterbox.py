name = input()
total = int(input())
ranking = []

for k in range (total):
    movie = input().split(" - ") # criando uma lista [nome, nota]
    ranking.append(movie) #criando um lista [[nome, nota], [nome, nota], [nome, nota]]

for j in range (total):
    for i in range (total):
        if (i > j):
            if ranking[j][1] < ranking[i][1]:
                ranking[i], ranking[j] = ranking[j], ranking[i]
        elif (i < j):
            if ranking[j][1] > ranking[i][1]:
                ranking[i], ranking[j] = ranking[j], ranking[i]

if (name == "Bonna"):
    print("Os filmes sugeridos por Bonna são:")
elif (name == "João"):
    print("Os filmes sugeridos por João são:")
for movie in ranking:
    print(f"{movie[0]} - {movie[1]}")