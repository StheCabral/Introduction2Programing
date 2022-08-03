# Recebe a quantidade de instruções através de uma string binária
total_instructions_binary = input()
# Convertendo para decimal a quantidade de instruções
total_instructions = 0
i = 3
for number in (total_instructions_binary):
    total_instructions +=  int(number) * (2**i)
    i -= 1

for i in range (total_instructions):
    object = input()

    ########################   PLANETA
    if (object == "0101"):
        beuty = False
        life = False
        water = False
        temp = False
        caracter = None
        moons = 0
        while (caracter != "End"):
            caracter = input()
            if (caracter == "Beleza"):
                beuty_binary = input()
                if (beuty_binary == "1"):
                    beuty = True
            elif (caracter == "Possibilidade de vida extraterrestre"):
                life_binary = input()
                if (life_binary == "1"):
                    life = True
            elif (caracter == "Agua aparente"):
                water_binary = input()
                if (water_binary == "1"):
                    water = True
            elif (caracter == "Temperatura adequada"):
                temp_binary = input()
                if (temp_binary == "1"):
                    temp = True
            elif (caracter == "Quantidade de luas"):
                moons_binary = input()
                moons = 0
                j = 3
                for number in (moons_binary):
                    moons +=  (int(number) * (2**j))
                    j -= 1

        if (water and temp and beuty and life):
            print(f"Achamos o planeta ideal e ainda tem {moons} lua(s)")
            print("Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?")
        elif (water and temp and beuty and not(life)):
            print("Ainda nao sabemos se o planeta e habitavel, parece nao haver vida")
        elif(water and temp and life and not(beuty)):
            print(f"O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {moons} lua(s) vamos omitir esse do relatorio!")
        else:
            print("Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo")

    ##########################    GALÁXIA
    elif (object == "1101"):
        there_is_bh = False
        planets = input()
        if (planets == "01100100"):
                planets = 100
        elif (planets == "11001000"):
                planets = 200
        elif (planets == "100101100"):
                planets = 300
        black_hole = input()
        if (black_hole == "1"):
            there_is_bh = True
        
        if (there_is_bh):
            print(f"Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de {planets} milhoes de planetas")
        else:
            print(f"Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham! Nao importa, ainda temos {planets} milhoes de planetas para observar algum deve apresentar possiblidade de vida")

    ##########################   BURACO NEGRO
    elif (object == "0000"):
        mass = input()
        if (mass == "0101"):
            mass = 5
        elif (mass == "1010"):
            mass = 10
        elif (mass == "1111"):
            mass = 15
        spin = input()
        carga = input()
        if (carga == "0000"):
            carga = "Apresenta carga inexistente ou nula"
        elif (carga == "0001"):
            carga = "Apresenta carga positiva"
        else:
            carga = "Apresenta carga negativa"
        print("Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!")
        print("De acordo com as analises, o buraco negro:")
        print(f"- Tem massa de aproximadamente {mass} milhoes massas solares")
        print(f"- Possui em media {spin} rotacao(oes) por segundo")
        print(f"- {carga}")
