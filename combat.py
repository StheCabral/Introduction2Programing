#character 1 skills
my_name = "São João"
my_life = int(input())
my_attack = int(input())
my_deffense = int(input())
my_weakness = input()
#Se a fraqueza inserida não está entre as declarada ele não tem nenhuma
if (my_weakness != "fogo" and my_weakness != "gelo" and my_weakness != "eletricidade"):
    my_weakness = "nao tem"

my_resistance = input()
#Se a resistência inserida não está entre as declarada ele não tem nenhuma
if (my_resistance != "fogo" and my_resistance != "gelo" and my_resistance != "eletricidade"):
    my_resistance = "nao tem"

# enemy skills

enemy_name = input()
enemy_life = int(input())
enemy_attack = int(input())
enemy_deffense = int(input())
enemy_weakness = input()
#Se a fraqueza inserida não está entre as declarada ele não tem nenhuma
if (enemy_weakness != "fogo" and enemy_weakness != "gelo" and enemy_weakness != "eletricidade"):
    enemy_weakness = "nao tem"

enemy_resistance = input()
#Se a resistência inserida não está entre as declarada ele não tem nenhuma
if (enemy_resistance != "fogo" and enemy_resistance != "gelo" and enemy_resistance != "eletricidade"):
    enemy_resistance = "nao tem"

enemy_damage = 0 
my_damage = 0
next_round = True
game_over = ""
magic_element = "nenhum"
jump = False
game_over = "continua"

##############################################################################################################
# first round
print("Turno: 1")
action1 = input()  #recebendo a ação

#Manipulando elementos da magia para facilitar a comparação lógica
if (action1 == "Agi"):
    magic_element = "fogo"
elif (action1 == "Bufu"):
    magic_element = "gelo"
elif (action1 == "Zio"):
    magic_element = "eletricidade"
else:
    magic_element = "nenhum"

#Contabilizando o dano 
if (action1 == "Ataque Físico"):
    enemy_damage = int(my_attack - enemy_deffense)
    enemy_life -= enemy_damage
    if (enemy_life < 0):
        enemy_life = 0
    print(f"{my_name} usou {action1} e causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
else:
    if (magic_element == enemy_resistance):
        enemy_damage = int((my_attack - enemy_deffense) * (50/100))
        enemy_life -= enemy_damage
        if (enemy_life < 0):
            enemy_life = 0
        print(f"{my_name} usou {action1}, mas acertou uma resistência, portanto causou apenas {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
    elif (magic_element == enemy_weakness):
        enemy_damage = int((my_attack - enemy_deffense) * (170/100))
        next_round = False
        enemy_life -= enemy_damage
        if (enemy_life < 0):
            enemy_life = 0
        print(f"Isso! {my_name} usou {action1} e acertou a fraqueza do adversário! A magia causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
    elif (magic_element != "nenhum"):
        enemy_damage = int(my_attack - enemy_deffense)
        enemy_life -= enemy_damage
        if (enemy_life < 0):
            enemy_life = 0
        print(f"{my_name} usou {action1} e causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")

#Verificando o restante a vitalidade do atacado
if (enemy_life == 0):
    game_over = "turno1"
    next_round = False


#########################################################################################################################

#Verificando se o jogo já acabou no primeiro turno
if (game_over == "turno1"):
    print(f"Vitória! Parece que o Nahobino São João reinará nesse solstício!")
else:
    #Se o jogo não acabou no primeiro turno, verificando se o personagem está apto a jogar a próxima rodada
    if (not(next_round)):
        print("Turno: 2")
        print(f"{enemy_name} teve sua fraqueza em {enemy_weakness} acertada, portanto não poderá agir.")
        jump = True
        next_round = True
    else: 
            # Second Round
        print("Turno: 2")
        action2 = input()

        #Manipulando elementos da magia para facilitar a comparação lógica
        if (action2 == "Agi"):
            magic_element = "fogo"
        elif (action2 == "Bufu"):
            magic_element = "gelo"
        elif (action2 == "Zio"):
            magic_element = "eletricidade"
        else:
            magic_element = "nenhum"

        #Contabilizando o dano 
        if (action2 == "Ataque Físico"):
            my_damage = int(enemy_attack - my_deffense)
            my_life -= my_damage
            if (my_life < 0):
                my_life = 0
            print(f"{enemy_name} usou {action2} e causou {my_damage} de dano em {my_name} que agora tem {my_life} de vida.")
        else: 
            if (magic_element == my_resistance):
                my_damage = int((enemy_attack - my_deffense) * (50/100))
                my_life -= my_damage
                if (my_life < 0):
                    my_life = 0
                print(f"{enemy_name} usou {action2}, mas acertou uma resistência, portanto causou apenas {my_damage} de dano em {my_name} que agora tem {my_life} de vida.")
            elif (magic_element == my_weakness):
                my_damage = int((enemy_attack - my_deffense) * (170/100))
                my_life -= my_damage
                next_round = False
                if (my_life < 0):
                    my_life = 0
                print(f"Vixe! {enemy_name} usou {action2} e acertou sua fraqueza! A magia causou {my_damage} de dano em {my_name} que agora tem {my_life} de vida.")
            elif (magic_element != "nenhum"):
                my_damage = int(enemy_attack - my_deffense)
                my_life -= my_damage
                if (my_life < 0):
                    my_life = 0
                print(f"{enemy_name} usou {action2} e causou {my_damage} de dano em {my_name} que agora tem {my_life} de vida.")
    #Verificando o restante a vitalidade do atacado
    if (my_life == 0):
        game_over = "turno2"
        

##########################################################################################################################
#Verificando se o jogo já acabou no primeiro turno
if (game_over == "turno2"):
    print(f"Morremos… Parece que {enemy_name} tem mais chances de ascender ao trono da Midsommar…")
elif (game_over == "continua"):
    #Se o jogo não acabou no primeiro turno, verificando se o personagem está apto a jogar a próxima rodada
    if (not(next_round)):
        print("Turno: 3")
        print(f"{my_name} teve sua fraqueza em {my_weakness} acertada, portanto não poderá agir.")
        print(f"Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")
    else: 
            # Third Round
        print("Turno: 3")
        action3 = input()  #recebendo a ação

        #Manipulando elementos da magia para facilitar a comparação lógica
        if (action3 == "Agi"):
            magic_element = "fogo"
        elif (action3 == "Bufu"):
            magic_element = "gelo"
        elif (action3 == "Zio"):
            magic_element = "eletricidade"
        else:
            magic_element = "nenhum"

        #Contabilizando o dano 
        if (action3 == "Ataque Físico"):
            enemy_damage = int(my_attack - enemy_deffense)
            enemy_life -= enemy_damage
            if (enemy_life < 0):
                enemy_life = 0
            print(f"{my_name} usou {action3} e causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
            #Verificando o restante a vitalidade do atacado
            if (enemy_life == 0):
                print(f"Vitória! Parece que o Nahobino São João reinará nesse solstício!")
            else:
                print(f"Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")
        else:
            if (magic_element == enemy_resistance):
                enemy_damage = int((my_attack - enemy_deffense) * (50/100))
                enemy_life -= enemy_damage
                if (enemy_life < 0):
                    enemy_life = 0
                print(f"{my_name} usou {action3}, mas acertou uma resistência, portanto causou apenas {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
            elif (magic_element == enemy_weakness):
                enemy_damage = int((my_attack - enemy_deffense) * (170/100))
                enemy_life -= enemy_damage
                if (enemy_life < 0):
                    enemy_life = 0
                print(f"Isso! {my_name} usou {action3} e acertou a fraqueza do adversário! A magia causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")
            elif (magic_element != "nenhum"):
                enemy_damage = int(my_attack - enemy_deffense)
                enemy_life -= enemy_damage
                if (enemy_life < 0):
                    enemy_life = 0
                print(f"{my_name} usou {action3} e causou {enemy_damage} de dano em {enemy_name} que agora tem {enemy_life} de vida.")

            #Verificando o restante a vitalidade do atacado
            if (enemy_life == 0):
                print(f"Vitória! Parece que o Nahobino São João reinará nesse solstício!")
            else:
                print(f"Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")
