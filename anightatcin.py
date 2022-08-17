cin = [["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-"]]
v_i = int(input())
v_j = int(input())
z_i = int(input())
z_j = int(input())
c_i = int(input())
c_j = int(input())
p_i = int(input())
p_j = int(input())
cracha = False
quantas_rodadas_cracha = 0
#Colocando CRACHÁ no lugar
cin[c_i][c_j] = "C"
#Colocando VOCÊ no lugar
cin[v_i][v_j] = "V"
#Colocando ZUMBI no lugar
cin[z_i][z_j] = "Z"
#Colocando PORTA no lugar
cin[p_i][p_j] = "P"
while ((cin[p_i][p_j] != "V") or (cin[v_i][v_j] != "Z")):  #enquanto você não chegar na porta ou o zumbi não chegar em vc
    # movimentação do zumbi até você
    if (v_j > z_j): #se você estiver a direta do zumbi
        z_j += 1
    elif (v_j < z_j): #se você estiver a esquerda do zumbi
        z_j -= 1
    elif (v_j == z_j): # você e o zumbi estão na mesma coluna
        if (v_i < z_i): #se voce esta acima do zumbi
            z_i -= 1
        elif (v_i > z_i): #se voce esta abaixo do zumbi
            z_i += 1
        elif (v_i == z_i): #se o zumbi chegou até voce
            cin[v_i][v_j] = "Z"
    # Sua movimentação
    if (not(cracha)): #se vc não tiver pego o cracha ainda
        #movimentação para o cracha
        if (v_j > c_j): #se você estiver a direta do cracha
            v_j -= 1
        elif (v_j < c_j): #se você estiver a esquerda do cracha
            v_j += 1
        elif (v_j == c_j): # você e o cracha estão na mesma coluna
            if (v_i < c_i): #se voce esta acima do cracha
                v_i += 1
            elif (v_i > c_i): #se voce esta abaixo do cracha
                v_i -= 1
            elif (v_i == c_i): #se voce chegou até o cracha
                cin[c_i][c_j] = "V"
                cracha = True
                quantas_rodadas_cracha += 1
    else: #vc já pegou o cracha
        #movimentação para porta
        if (v_j > p_j): #se você estiver a direta da porta
            v_j -= 1
        elif (v_j < p_j): #se você estiver a esquerda da porta
            v_j += 1
        elif (v_j == p_j): # você e a porta estão na mesma coluna
            if (v_i < p_i): #se voce esta acima da porta
                v_i += 1
            elif (v_i > p_i): #se voce esta abaixo da porta
                v_i -= 1
            elif (v_i == p_i): #se voce chegou até a porta
                cin[p_i][p_j] = "V"
    for line in cin: #printando a matriz
        print(line)
    # retorno sobre o cracha
    if(not(cracha)):
        print("Ainda não achei o crachá")
    else:
        if(quantas_rodadas_cracha == 1):
            print("Finalmente! Peguei o crachá")
        elif (quantas_rodadas_cracha > 1):
            print("Já peguei o crachá")
    # retorno sobre o zumbi
    distance = int(((v_j - z_j)**2 + (v_i - z_i)**2)**(1/2))
    if (distance >= 3):
        print("Preciso acelerar, o zumbi tá na minha cola!")
