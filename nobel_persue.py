path = 0
step = None
nobel = 0
give_up = False
step_position = 0
bazinga_power = False

while (step != "É o fim da Estrada pra Sheldon Cooper" and step != "Ganhar o Nobel"):
    step = input()

    #verificando se ele desistiu
    if (step == "É o fim da Estrada pra Sheldon Cooper"):
        give_up = True
        bazinga_power = False

        #Considerando o ponto em que ele desistiu
        if (nobel == 0):
            print("Que potencial desperdiçado...")
        elif (nobel == 1 or nobel == 2):
            print("Tão perto, mas tão longe")
        elif (nobel == 3 or nobel == 4):
            print("Não desista Sheldon, você ainda têm muito para alcançar!")
        elif (nobel == 5):
            print("Nãoooooo, esse momento ia ser seu Sheldon")

    
    # se xingar os amigos deve repreender
    elif (step == "Tinha que ser o engenheiro sem Phd do Wolowitz" or step == "Leonard seu anão covarde" or step == "Tu é muito burro Raj"):
            print("Não xingue seus amigos Sheldon!")
            bazinga_power = False
    
    #se o próximo step for "Banzinga" o anterior será desconsiderado
    elif (step == "Bazinga"):
        if (bazinga_power):
            step_position -= 1  # desconsiderando avanço na carreira se necesário
            nobel -= 1
            bazinga_power = False

    else:
        #Começou a Trabalhar na Caltech primeiro?
        if (step == "Começou a Trabalhar na Caltech"):
            step_position +=1
            if (step_position == 1):
                bazinga_power = True
                nobel = 1
               
            else: 
                step_position -= 1

        #Trabalho sobre a String Theory segundo?
        elif (step == "Trabalho sobre a String Theory"):
            step_position +=1
            if (step_position == 2):
                bazinga_power = True
                nobel = 2
            else: 
                step_position -= 1

        #Ganhar o Chancellor de ciência terceiro?
        elif (step == "Ganhar o Chancellor de ciência"):
            step_position +=1
            if (step_position == 3):
                bazinga_power = True
                nobel = 3
            else: 
                step_position -= 1

        #Pensar na Teoria de Cooper-Hofstader quarto?
        elif (step == "Pensar na Teoria de Cooper-Hofstader"):
            step_position +=1
            if (step_position == 4):
                bazinga_power = True
                nobel = 4
            else: 
                step_position -= 1

        #Criou a Super Assimetria quinto?
        elif (step == "Criou a Super Assimetria"):
            step_position +=1
            if (step_position == 5):
                bazinga_power = True
                nobel = 5
            else: 
                step_position -= 1

        #Ganhar o Nobel sexto?
        elif (step == "Ganhar o Nobel"): 
            step_position +=1
            if (step_position == 6):
                bazinga_power = True
                nobel = 6
            else: 
                step_position -= 1
        #caso seja um step não listado
        else:
            bazinga_power = False
    #seguiu o cronograma e ganhou o notion
    if (nobel == 6):
        print("Você conseguiu Sheldon, o Nobel é seu!!!")
