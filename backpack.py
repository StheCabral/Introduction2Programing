total_bags = int(input()) # quantidade de mochilas
bags_owners = input().split(" ") #lista com os donos de cada mochila
bags_sizes = [] # lista com os tamanhos das mochilas
bags_inventory = []
for i in range (total_bags):
    bag_size = int(input())
    bags_sizes.append(bag_size)
    bags_inventory.append(["Lanterna", "Omega 3 da top therm"])
total_itens = int(input())
for j in range (total_itens):
    item_name = input()
    item_place = int(input())
    if ((len(bags_inventory[item_place])) < bags_sizes[item_place]): #se o tamanho do array da mochila ainda for menor que o tamanho dela
        bags_inventory[item_place].append(item_name)
    else:
        print("Mochila cheia. Não vai dar para levar.")
# ações
action = None
possible_action = ["CHEGAMOS NO CIN!", "Tirar da mochila", "Guardar na mochila"]
while (action != "CHEGAMOS NO CIN!"):
    action = input()
    if (action not in possible_action):
        print("Ação inválida.")
    else:
        if (action != "CHEGAMOS NO CIN!"):
            item = input()
            backpack = int(input())
            if (action == "Tirar da mochila"):
                if (item not in (bags_inventory[backpack])):
                    print(f"Você não tem {item} na mochila {backpack}.")
                else:
                    bags_inventory[backpack].remove(item)
                    print(f"{item} usado com sucesso da mochila {backpack}.")
            elif (action == "Guardar na mochila"):
                if ((len(bags_inventory[backpack])) < bags_sizes[backpack]):
                    bags_inventory[backpack].append(item)
                    print(f"{item} adicionado na mochila {backpack}.")
                else:
                    print(f"Mochila {backpack} cheia!")
else:
    for k in range (total_bags):
        print(f"Mochila de {bags_owners[k]} chegou assim:")
        for t in range (len(bags_inventory[k])):
            print(bags_inventory[k][t])


