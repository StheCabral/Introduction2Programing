rounds = int(input())
gohan = [int(x) for x in input().split(" ")]
piccolo = [int(x) for x in input().split(" ")]
gohan_win = 0
piccolo_dict = {}
gohan_dict = {}
for number in piccolo:
    if (number not in piccolo_dict.keys()):
        piccolo_dict.update({number : 1})
    else:
        piccolo_dict[number] += 1
for number in gohan:
    if (number not in gohan_dict.keys()):
        gohan_dict.update({number : 1})
    else:
        gohan_dict[number] += 1

for key in piccolo_dict.keys():
    try:
        if (piccolo_dict[key] == gohan_dict[key]):
            gohan_win += 1
    except KeyError:
        print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")

if (gohan_win == len(piccolo_dict)):
    print("Dale Gohan!")
