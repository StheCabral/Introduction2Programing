#Número de entradas
rounds = int(input())

for i in range (rounds):
    type = input() #tipo de conversão
    result = 0

    if (type == "DEC"): # Binário para Decimal
        binary = input()
        for element in (binary): #descobrindo quantos elementos tem no binário
            length += 1
        j = length
        for element in (binary): #convertendo para decimal
            result +=  int(element) * (2**j)
            j -= 1
        #Analisando a resposta de Sheldon
        guess = input()
        if (guess != result):
            print(f"Palpite Incorreto, o valor {binary} = {result}")
        else:
            score += 1

    elif (type == "BIN"): # Decimal para binário
        decimal = int(input())
        assistant = decimal
        if (decimal % 2 > 0): #decimal é ímpar _ _ _ 1
            assistant -= 1

        # Quantas potencias de 2 cabe nesse número decimal
        while (assistant % 2 == 0):
            assistant = assistant / 2
            power += 1
        else:
            assistant -= 1
            while (assistant % 2 == 0):
                assistant = assistant / 2
                power += 1

        # Convertendo para binário
        assistant2 = decimal
        for k in range (power, -1, -1)
            if ((assistant2 / 2**k) >= 1):
                result += "1"
                assistant2 -= (assistant2 / 2 ** k)
            elif ((assistant2 / 2**k) < 1 ):
                result += "0"
                assistant2 -= (assistant2 / 2 ** k)
        #Analisando a resposta de Sheldon
        guess = input()
        if (guess != result):
            print(f"Palpite Incorreto, o valor {decimal} = {result}")
        else:
            score += 1

if (score / rounds >= 0,5): #Onde fica o igual a 50%?????
    print("Bazinga! Quem realizou esses cálculos foi o computador??")
else: 
    print("Parece que realizar conversões em binário não é o seu forte")


    
   





    ##############################################
        if (decimal % 2 == 0): #decimal é par _ _ _ 0

            # Quantas potencias de 2 cabe nesse número decimal
            while (assistant % 2 == 0):
                assistant = assistant / 2
                power += 1
            else:
                assistant -= 1
                while (assistant % 2 == 0):
                    assistant = assistant / 2
                    power += 1
        elif (decimal % 2 > 0): #decimal é ímpar _ _ _ 1
            assistant -= 1
            # Quantas potencias de 2 cabe nesse número decimal
            while (assistant % 2 == 0):
                assistant = assistant / 2
                power += 1
            else:
                assistant -= 1
                while (assistant % 2 == 0):
                    assistant = assistant / 2
                    power += 1

        # Convertendo para binário
        for k in range (power, -1, -1)
            if ((decimal / 2**k) > 1):
                result += "1"
                decimal -= (decimal / 2 ** k)
            elif ((decimal / 2**k) < 1 ):
                result += "0"
                decimal -= (decimal / 2 ** k)

        


    guess = input()




total_instructions = 0
i = 3
for number in (total_instructions_binary):
    total_instructions +=  int(number) * (2**i)
    i -= 1



    if (assistant % 2 > 1)
            