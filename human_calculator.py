#Número de entradas
rounds = int(input())
score = 0

for i in range (rounds):
    type = input() #tipo de conversão
    result_int = 0
    result_str = ""
    power = 0
    length = 0

    if (type == "DEC"): # Binário para Decimal
        binary = input()
        guess = int(input())
        for element in (binary): #descobrindo quantos elementos tem no binário
            length += 1
        j = length - 1
        for element in (binary): #convertendo para decimal
            result_int +=  (int(element) * (2**j))
            j -= 1
        #Analisando a resposta de Sheldon
        if (guess == result_int):
            score += 1
        else:
            print(f"Palpite Incorreto, o valor {binary} = {result_int}")

    elif (type == "BIN"): # Decimal para binário
        decimal = int(input())
        guess = input()
        decimal_storage = decimal

        # Quantas potencias de 2 cabe nesse número decimal
        while (decimal_storage > 0):
            if (decimal_storage % 2 == 0):
                decimal_storage = decimal_storage / 2
                power += 1
            else:
                decimal_storage -= 1

        # Convertendo para binário
        decimal_storage2 = decimal
        for y in range (power, -1, -1):
                if (decimal_storage2 >= (2**y)):
                    result_str = (result_str + "1") 
                    decimal_storage2 -= (2**y)
                elif (decimal_storage2  < 2**y):
                    result_str = (result_str + "0")
  
        #Analisando a resposta de Sheldon
        if (guess == result_str):
            score += 1
        else:
            print(f"Palpite Incorreto, o valor {decimal} = {result_str}")
#Analisando resultado final do jogo
if ((score / rounds) > 0.5): #Onde fica o igual a 50%?????
    print("Bazinga! Quem realizou esses cálculos foi o computador??")
else: 
    print("Parece que realizar conversões em binário não é o seu forte")
