#Número de entradas
rounds = int(input())
length = 0
power = 0
score = 0

for i in range (rounds):
    type = input() #tipo de conversão
    result_int = 0
    result_str = ""

    if (type == "DEC"): # Binário para Decimal
        binary = input()
        for element in (binary): #descobrindo quantos elementos tem no binário
            length += 1
        j = length - 1
        for element in (binary): #convertendo para decimal
            result_int +=  (int(element) * (2**j))
            j -= 1
        #Analisando a resposta de Sheldon
        guess = input()
        if (guess != result_int):
            print(f"Palpite Incorreto, o valor {binary} = {result_int}")
        else:
            score += 1

    elif (type == "BIN"): # Decimal para binário
        decimal = int(input())
        assistant = decimal
        #if (decimal % 2 > 0): #decimal é ímpar _ _ _ 1
           # assistant -= 1

        # Quantas potencias de 2 cabe nesse número decimal
        while (assistant > 0):
            while (assistant % 2 == 0):
                assistant = assistant / 2
                power += 1
            else:
                assistant -= 1


        # Convertendo para binário
        assistant2 = decimal
        print(power)
        for y in range (power, -1, -1):
            if ((assistant2 / 2**y) >= 1):
                result_str = (result_str + "1") 
            else:
                result_str = (result_str + "0")
            assistant2 -= (assistant2 / 2 ** y)
        #Analisando a resposta de Sheldon
        guess = input()
        if (guess != result_str):
            print(f"Palpite Incorreto, o valor {decimal} = {result_str}")
        else:
            score += 1

if ((score / rounds) >= 0,5): #Onde fica o igual a 50%?????
    print("Bazinga! Quem realizou esses cálculos foi o computador??")
else: 
    print("Parece que realizar conversões em binário não é o seu forte")
