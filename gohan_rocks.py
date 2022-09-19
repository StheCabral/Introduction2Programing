rounds = int(input())
piccolo = [int(x) for x in input().split(" ")]
gohan = [int(x) for x in input().split(" ")]
gohan_d = {}
piccolo_d = {}
gohan_win = 0
for i in range (rounds):
    piccolo_d[i] = piccolo[i]
    gohan_d[i] = gohan[i]
for key in gohan_d.keys():
    for j in range (rounds):
        if (gohan_d[key] == piccolo_d[j]):
            gohan_d[key] = -1
            gohan_win += 1
            i += 1
if (gohan_win == rounds):
    print("Dale Gohan!")
else:
    print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")

