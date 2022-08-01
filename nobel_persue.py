

# se receber "é o fim da estrada..." antes de trabalhar na caltech deve imprimir "que potencial..."
# se ele desistir na caltech ou string theory deve imprimir "tao perto mas tao longe..."
# se estiver no chancellor ou no cooper printar "não dessitia sehldon foi..."
# se estiver na assimetria e n tiver ganho o nbel ainda "naoooooo...."
# se ele ganhar o nobel "voce conseguiu..."

path = 0
step = None
nobel = False
give_up = False
step_position = 0

while (step != "É o fim da Estrada pra Sheldon Cooper" or not(nobel)):
    step = input()
    step_position += 1


    #verificando se ele desistiu
    if (step == "É o fim da Estrada pra Sheldon Cooper"):
        give_up = True
        step_position -= 1
        bazinga_power = False
    
    # se xingar os amigos deve repreender
    elif (step == "Tinha que ser o engenheiro sem Phd do Wolowitz" or step == "Leonard seu anão covarde" or step == "Tu é muito burro Raj"):
            print("Não xingue seus amigos Sheldon!")
            step_position -= 1
            bazinga_power = False
    
    #se o próximo step for "Banzinga" o anterior será desconsiderado
    elif (step == "Bazinga"):
        step_position -= 1 #desconsiderando o passo bazinga
        if (bazinga_power):
            step_position -= 1  # desconsiderando avanço na carreira se necesário

    else:
        #Começou a Trabalhar na Caltech primeiro?
        if (step == "Começou a Trabalhar na Caltech"):
            if (step_position == 1):
                bazinga_power = True
                nobel = 1
            else: 
                step_position -= 1

        #Trabalho sobre a String Theory segundo?
        elif (step == "Trabalho sobre a String Theory"):
            if (step_position == 2):
                bazinga_power = True
                nobel = 2
            else: 
                step_position -= 1

        #Ganhar o Chancellor de ciência terceiro?
        elif (step == "Ganhar o Chancellor de ciência"):
            if (step_position == 3):
                bazinga_power = True
                nobel = 3
            else: 
                step_position -= 1

        #Pensar na Teoria de Cooper-Hofstader quarto?
        elif (step == "Pensar na Teoria de Cooper-Hofstader"):
            if (step_position == 4):
                bazinga_power = True
                nobel = 4
            else: 
                step_position -= 1

        #Criou a Super Assimetria quinto?
        elif (step == "Criou a Super Assimetria"):
            if (step_position == 5):
                bazinga_power = True
                nobel = 5
            else: 
                step_position -= 1

        #Ganhar o Nobel sexto?
        elif (step == "Ganhar o Nobel"):
            if (step_position == 6):
                bazinga_power = True
                nobel = 6
            else: 
                step_position -= 1
        #caso seja um step não listado
        else:
            step_position -= 1
            bazinga_power = False
    if (nobel == 6):
        print("Você conseguiu Sheldon, o Nobel é seu!!!")








#Começou a Trabalhar na Caltech
#Trabalho sobre a String Theory
#Ganhar o Chancellor de ciência
#Pensar na Teoria de Cooper-Hofstader
#Criou a Super Assimetria
#Ganhar o Nobel
# receber na ordem certa
#bazinga assim que avançar um feito este deve ser desconsiderado
# se n for assim que avançar ta de boa
# se receber os feitos na ordem errada deve desconsiderar
# se receber "é o fim da estrada..." antes de trabalhar na caltech deve imprimir "que potencial..."
# se ele desistir na caltech ou string theory deve imprimir "tao perto mas tao longe..."
# se estiver no chancellor ou no cooper printar "não dessitia sehldon foi..."
# se estiver na assimetria e n tiver ganho o nbel ainda "naoooooo...."
# se ele ganhar o nobel "voce conseguiu..."
